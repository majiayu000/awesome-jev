# Ticket routing / 工单路由

[English](#english) · [中文](#中文) · [Live mode](#live-mode) · [Concepts](../guides/start.md)

## English

This example teaches the complete path from input to a proposed queue. It uses Python 3.10+ and only the standard library. It does not move a ticket, issue a refund, or execute model-generated commands.

Run from the repository root:

```bash
python3 examples/ticket_routing.py
python3 examples/ticket_routing.py --threshold 0.99
python3 -m unittest discover -s examples -v
```

The first command prints `mode: demo_fixture_not_a_model_result` and proposes `billing`. The second raises an **illustrative** threshold and prints `human_review`. Both read the same hand-authored synthetic fixture; neither contacts a model. Demo mode rejects `--ticket`, so it cannot pretend to classify arbitrary text using a fixed answer.

The request contains three independent questions about the same ticket: department (Choice), frustration (Score), and urgency (Noul). Only department controls the proposed queue. The code validates the Choice type, recognized options, finite confidence, probability keys, normalization, and selected maximum. These checks do not establish semantic correctness. The other answers are printed for inspection, not treated as validated action permissions.

## 中文

这个示例展示从输入、模型请求到队列建议的完整流程。只需要 Python 3.10+ 标准库，不需要安装依赖。程序不会真的移动工单、退款或执行模型生成的命令。

在仓库根目录运行上方三条命令。第一条显示 `demo_fixture_not_a_model_result` 并建议 `billing`；第二条提高**演示阈值**后转为 `human_review`；第三条运行离线测试。

两个演示命令使用同一份人工编写的数据，不调用模型。为了避免误导，离线模式禁止 `--ticket` 自定义输入。真实调用一次询问部门、情绪和紧急性；只有部门 Choice 用于建议队列。代码校验 Choice 类型、选项、有限置信度、概率键、归一化与最大值，不能因此保证语义判断正确。其余输出只展示，不用于动作授权。

## Live mode

真实调用需要 TypeSafe API 访问权限与密钥，可能产生费用。先查看[官方快速入门](https://docs.typesafe.ai/introduction/quickstart)和账户中的当前额度/计费说明。默认只发送仓库内的合成工单，不发送真实客户资料。

A live request requires a TypeSafe API key and may incur charges. The prompt below reads your key without putting its literal value in shell history. Never commit credentials. The default ticket is synthetic.

```bash
export TYPESAFE_API_KEY="$(python3 -c 'import getpass; print(getpass.getpass("TypeSafe API key: "))')"
python3 examples/ticket_routing.py --live
unset TYPESAFE_API_KEY
```

To use other **non-sensitive synthetic** text, add `--ticket "The integration returns an error."` together with `--live`. Command-line text can appear in shell history. To reproduce an evaluation, select an available pinned model with `--model`; the tutorial defaults to `jev-latest` for onboarding. Live answers can differ from the fixture and across model versions.

真实结果不保证与演示相同。自定义输入仅用于非敏感的合成数据，命令行文本可能进入历史记录。`--model` 可以指定账户中可用的固定版本；默认 `jev-latest` 便于入门，但不适合作为可复现评测的唯一版本记录。

| Situation / 情况 | Behavior / 行为 |
| --- | --- |
| Demo, no key / 离线模式 | Fixed, clearly labeled fixture; no network / 固定且显式标注的数据，无网络调用 |
| Missing key / 缺少密钥 | No request; error and review fallback / 不发送请求，报错并回退 |
| HTTP error or timeout / HTTP 错误或超时 | Error and review fallback; no automatic retries / 报错并回退，不自动重试 |
| Malformed department response / 部门响应无效 | `human_review`; exit code 2 / 退出码 2 |
| Low confidence or `other` / 低置信度或其他类别 | `human_review`; exit code 0 because abstention is expected / 合法回退，退出码 0 |
| Valid department above threshold / 符合演示规则 | Print a proposed queue only / 只打印建议，不执行 |

The HTTP call uses the official `https://api.typesafe.ai/v1/systemone` endpoint, a 20-second socket timeout, a bounded response size, and refuses redirects. It makes one attempt. A socket timeout is not a whole-process deadline. Provider error bodies, credentials, and request headers are not printed. No live API call was made while preparing this example.

`0.65` is an arbitrary teaching threshold, not a recommended production setting or a 65% accuracy claim. Build a labeled development/test split and compare error rates and abstentions before using a threshold. See [confidence](https://docs.typesafe.ai/confidence). 离线测试通过不代表真实模型达到某个准确率，也不代表生产就绪。
