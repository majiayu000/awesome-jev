"""Offline tests of request construction and application logic, NOT model quality."""
import copy
import io
import unittest
from contextlib import redirect_stderr, redirect_stdout
from unittest.mock import patch, MagicMock
from urllib.error import HTTPError, URLError
import ticket_routing as demo


class RoutingTests(unittest.TestCase):
    def setUp(self):
        self.response = copy.deepcopy(demo.DEMO)
        self.answer = self.response["answers"]["department"]

    def test_payload_has_three_independent_question_types(self):
        payload = demo.make_payload("A ticket", "jev-latest")
        self.assertEqual(payload["state"], "A ticket")
        self.assertEqual({q["type"] for q in payload["questions"].values()}, {"choice", "score", "noul"})
        self.assertIn("other", payload["questions"]["department"]["criteria"])

    def test_input_bounds(self):
        for text in ("", "  ", "x" * 12001):
            with self.subTest(text_length=len(text)), self.assertRaises(ValueError):
                demo.make_payload(text, "jev-latest")

    def test_demo_proposes_billing(self):
        self.assertEqual(demo.propose_queue(self.response, 0.65)["queue"], "billing")

    def test_high_threshold_abstains(self):
        self.assertEqual(demo.propose_queue(self.response, 0.99)["queue"], "human_review")

    def test_other_abstains(self):
        self.answer.update(choice="other", probabilities={"billing": 0.05, "technical": 0.05, "other": 0.9})
        self.assertEqual(demo.propose_queue(self.response, 0.1)["reason"], "outside_supported_categories")

    def test_malformed_responses_abstain(self):
        for response in (None, [], {}, {"answers": []}, {"answers": {"department": "billing"}}):
            with self.subTest(response=response):
                self.assertEqual(demo.propose_queue(response, 0.65)["reason"], "invalid_response")

    def test_unknown_choice_abstains(self):
        for choice in ("refund_money", [], None):
            self.answer["choice"] = choice
            self.assertEqual(demo.propose_queue(self.response, 0.65)["queue"], "human_review")

    def test_invalid_confidence_abstains(self):
        for value in (None, True, "0.9", float("nan"), float("inf"), -1, 2):
            with self.subTest(value=value):
                self.answer["confidence"] = value
                self.assertEqual(demo.propose_queue(self.response, 0.65)["queue"], "human_review")

    def test_invalid_distribution_abstains(self):
        for probabilities in ({}, {"billing": 1}, {"billing": 0.9, "technical": 0.9, "other": 0.9},
                              {"billing": True, "technical": 0, "other": 0},
                              {"billing": float("nan"), "technical": 0, "other": 0}):
            self.answer["probabilities"] = probabilities
            self.assertEqual(demo.propose_queue(self.response, 0.65)["reason"], "invalid_response")

    def test_choice_must_match_distribution_maximum(self):
        self.answer["choice"] = "technical"
        self.assertEqual(demo.propose_queue(self.response, 0.65)["reason"], "invalid_response")

    def test_wrong_answer_type_abstains(self):
        self.answer["type"] = "noul"
        self.assertEqual(demo.propose_queue(self.response, 0.65)["reason"], "invalid_response")

    def test_invalid_thresholds_rejected(self):
        for value in (-0.1, 1.1, float("nan"), True):
            with self.assertRaises(ValueError):
                demo.propose_queue(self.response, value)

    def test_demo_never_calls_api(self):
        with patch.object(demo, "call_api") as api, redirect_stdout(io.StringIO()) as output:
            self.assertEqual(demo.main([]), 0)
            api.assert_not_called()
            self.assertIn("demo_fixture_not_a_model_result", output.getvalue())

    def test_demo_rejects_custom_ticket(self):
        with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            demo.main(["--ticket", "Do not pretend this was classified"])

    def test_live_missing_key_fails_without_network(self):
        with patch.dict(demo.os.environ, {}, clear=True), redirect_stderr(io.StringIO()), patch.object(demo.request, "build_opener") as opener:
            self.assertEqual(demo.main(["--live"]), 2)
            opener.assert_not_called()

    def test_http_error_does_not_leak_provider_body(self):
        exc = HTTPError(demo.ENDPOINT, 401, "secret-provider-message", {}, None)
        with patch.object(demo, "call_api", side_effect=exc), redirect_stderr(io.StringIO()) as output:
            self.assertEqual(demo.main(["--live"]), 2)
            self.assertIn("http_401", output.getvalue())
            self.assertNotIn("secret-provider-message", output.getvalue())

    def test_network_error_abstains(self):
        with patch.object(demo, "call_api", side_effect=URLError("private-detail")), redirect_stderr(io.StringIO()) as output:
            self.assertEqual(demo.main(["--live"]), 2)
            self.assertIn("network_or_timeout", output.getvalue())
            self.assertNotIn("private-detail", output.getvalue())

    def test_transport_uses_fixed_endpoint_and_bounded_timeout(self):
        opener = MagicMock()
        opener.open.return_value.__enter__.return_value.read.return_value = b'{"answers":{}}'
        with patch.object(demo.request, "build_opener", return_value=opener):
            self.assertEqual(demo.call_api(demo.make_payload("test", "jev-latest"), "test-key"), {"answers": {}})
        args, kwargs = opener.open.call_args
        self.assertEqual(args[0].full_url, demo.ENDPOINT)
        self.assertEqual(args[0].method, "POST")
        self.assertEqual(kwargs["timeout"], 20)
        self.assertEqual(args[0].get_header("Authorization"), "Bearer test-key")

    def test_redirects_are_refused(self):
        self.assertIsNone(demo.NoRedirect().redirect_request(None, None, 302, "", {}, "https://example.org"))


if __name__ == "__main__":
    unittest.main()
