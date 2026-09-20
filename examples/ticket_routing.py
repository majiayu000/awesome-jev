"""A dependency-free Jev tutorial. Demo mode never calls an API.

API contract: https://docs.typesafe.ai/introduction/quickstart
Python 3.10+. This program prints a proposed queue; it does not act on a ticket.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
from typing import Any
from urllib import error, request

ENDPOINT = "https://api.typesafe.ai/v1/systemone"
SAMPLE = "I was charged twice for my subscription. Please check the duplicate charge."
OPTIONS = {
    "billing": "Charges, invoices, payments or subscriptions.",
    "technical": "Bugs, errors or integration failures.",
    "other": "Anything outside these categories, ambiguous or insufficient information.",
}
# Hand-authored fixture, NOT an observed model response or an accuracy claim.
DEMO = {
    "answers": {
        "department": {
            "type": "choice", "choice": "billing",
            "probabilities": {"billing": 0.90, "technical": 0.05, "other": 0.05},
            "confidence": 0.70,
        },
        "frustration": {"type": "score", "score": 0.4, "confidence": 0.6},
        "urgent": {"type": "noul", "noul": 0.2},
    }
}


def unit_interval(value: Any) -> bool:
    return type(value) in (int, float) and math.isfinite(value) and 0 <= value <= 1


def make_payload(ticket: str, model: str) -> dict[str, Any]:
    if not ticket.strip() or len(ticket) > 12000:
        raise ValueError("Ticket must contain 1-12000 characters (tutorial limit).")
    if not model.strip():
        raise ValueError("Model name must not be empty.")
    return {
        "model": model,
        "state": ticket,
        "questions": {
            "department": {
                "type": "choice",
                "instructions": "Which support team should handle the customer's message?",
                "criteria": OPTIONS.copy(),
            },
            "frustration": {
                "type": "score",
                "instructions": "How frustrated does the customer sound?",
                "criteria": ["Calm and factual", "Frustrated but civil", "Very angry"],
            },
            "urgent": {
                "type": "noul",
                "instructions": "Does the message explicitly describe a time-sensitive problem?",
            },
        },
    }


def propose_queue(response: Any, threshold: float) -> dict[str, str]:
    """Validate the consumed Choice fields; abstain on malformed/uncertain results."""
    if not unit_interval(threshold):
        raise ValueError("Threshold must be a finite number from 0 to 1.")
    fallback = {"queue": "human_review", "reason": "invalid_response"}
    if not isinstance(response, dict) or not isinstance(response.get("answers"), dict):
        return fallback
    answer = response["answers"].get("department")
    if not isinstance(answer, dict) or answer.get("type") != "choice":
        return fallback
    choice, confidence = answer.get("choice"), answer.get("confidence")
    probabilities = answer.get("probabilities")
    if not isinstance(choice, str) or choice not in OPTIONS or not unit_interval(confidence):
        return fallback
    if not isinstance(probabilities, dict) or set(probabilities) != set(OPTIONS):
        return fallback
    if not all(unit_interval(value) for value in probabilities.values()):
        return fallback
    if not math.isclose(sum(probabilities.values()), 1.0, abs_tol=0.001):
        return fallback
    if probabilities[choice] < max(probabilities.values()):
        return fallback
    if choice == "other":
        return {"queue": "human_review", "reason": "outside_supported_categories"}
    if confidence < threshold:
        return {"queue": "human_review", "reason": "below_example_threshold"}
    return {"queue": choice, "reason": "proposed_only_not_executed"}


class NoRedirect(request.HTTPRedirectHandler):
    """Do not forward an API credential through an unexpected HTTP redirect."""
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def call_api(payload: dict[str, Any], api_key: str, timeout: float = 20) -> dict[str, Any]:
    if not api_key.strip() or "\n" in api_key or "\r" in api_key:
        raise ValueError("Set a valid TYPESAFE_API_KEY in the environment.")
    if type(timeout) not in (int, float) or not math.isfinite(timeout) or timeout <= 0:
        raise ValueError("Timeout must be positive and finite.")
    req = request.Request(
        ENDPOINT, data=json.dumps(payload).encode("utf-8"), method="POST",
        headers={"Authorization": "Bearer " + api_key, "Content-Type": "application/json"},
    )
    # One bounded call, no hidden retries or automatic additional spend.
    with request.build_opener(NoRedirect()).open(req, timeout=timeout) as res:
        raw = res.read(1_000_001)
    if len(raw) > 1_000_000:
        raise ValueError("Response exceeds the tutorial's size limit.")
    result = json.loads(raw)
    if not isinstance(result, dict):
        raise ValueError("Expected a JSON object from the API.")
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live", action="store_true", help="Opt in to one potentially billable API call")
    parser.add_argument("--ticket", help="Synthetic/non-sensitive ticket; live mode only")
    parser.add_argument("--model", default="jev-latest", help="Use an available pinned model for repeatable evaluations")
    parser.add_argument("--threshold", type=float, default=0.65, help="Illustrative only, NOT a calibrated accuracy guarantee")
    args = parser.parse_args(argv)
    if not unit_interval(args.threshold):
        parser.error("--threshold must be between 0 and 1 and finite")
    if args.ticket is not None and not args.live:
        parser.error("--ticket requires --live; demo mode uses one fixed synthetic fixture")
    try:
        payload = make_payload(args.ticket if args.ticket is not None else SAMPLE, args.model)
        response = call_api(payload, os.environ.get("TYPESAFE_API_KEY", "")) if args.live else DEMO
        proposal = propose_queue(response, args.threshold)
        print(json.dumps({
            "mode": "live_api" if args.live else "demo_fixture_not_a_model_result",
            "threshold": args.threshold,
            "answers": response.get("answers"),
            "proposal": proposal,
        }, ensure_ascii=False, indent=2, allow_nan=False))
        return 0 if proposal["reason"] != "invalid_response" else 2
    except error.HTTPError as exc:
        reason = f"http_{exc.code}"
    except (error.URLError, TimeoutError, OSError):
        reason = "network_or_timeout"
    except (ValueError, UnicodeError):
        reason = "configuration_or_response_error"
    # Do not print credentials, request headers, ticket text or provider error bodies.
    print(json.dumps({"queue": "human_review", "reason": reason}), file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
