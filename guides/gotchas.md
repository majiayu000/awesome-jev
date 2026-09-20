# Field notes and gotchas / 踩坑与边界

[English](#english) · [中文](#中文) · [Home](../README.md) · [Limitations taxonomy](../taxonomy/critique-limits.md)

这些条目来自公开原文或本清单维护者的核对。**不是**本仓库的独立实验室复现。链接失效时以原始页面为准。

## 中文

### 判断与表述

1. **格式对 ≠ 判断对**
   Schema 合法的 Choice / Score / Noul 仍可能自信地错。官方 [jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13.md) 与本清单[使用前注意](../README_zh.md#使用前注意)都强调这一点。

2. **「JSON 分类器」叙事**
   有人把 Jev 概括成与补全模型对立的分类器。有助于建立心智模型，但会掩盖校准、失败模式与任务边界。保留原文语气，勿写成产品承诺。
   例：[Every CEO 相关讨论](https://x.com/danshipper/status/2100251499443998766)（第三方表述）。

3. **小样本评测不能外推**
   [Every / Mike Taylor](https://every.to/also-true-for-humans/mini-vibe-check-typesafe-s-jev-judged-everything-i-ve-written-in-0-7-seconds) 报告了速度快、成本低，以及预埋缺陷 7 个中检出 6 个。这是**一次小样本实验**，不是通用准确率保证。

### 演示与复现

4. **演示赢过一次，不代表可复现**
   Pac-Man 相关演示的作者后续表示未能复现此前获胜结果。
   来源：[Ephraim Duncan](https://x.com/ephraimduncan/status/2100554620254752981)。

5. **浏览器 demo 的边界**
   Ultrafast 类演示常依赖结构化 DOM / 动作空间，不等于端到端视觉 computer-use。成功率与成本随站点变化。
   来源：[Browser Use 演示](https://x.com/gregpr07/status/2100411066966749359)；另有用户指出「正经航班 API 缺失」类吐槽，见公开讨论（如 [@awlevin](https://x.com/awlevin/status/2100427922205209012)）。

6. **开源复刻 ≠ 官方权重**
   `jevlike`、`SemIf` / OpenJev 等是独立实现或研究复刻。可读、可学，**不能**用来推断官方 Jev 的内部结构或质量。见[评测与开源实现](../README_zh.md#评测与开源实现)。

### 接入与运维

7. **网关名称与权限会变**
   Vercel / Cloudflare / OpenRouter 等页面上的模型名、计费与是否免 waitlist，以**当前**服务商文档为准，过期截图无效。

8. **首页精选也不等于已替你跑通生产**
   2026-09-20 维护者核对：两个官方 SDK 可安装导入；`jev-router` 可安装；`jev-ultrafast` 只核对 README。**没有**统一做真实 API 调用与成功率复现。
   详见：[精选核对记录](featured-review.md)。

9. **负结果同样值得收**
   如 [jev-phishing-bench](https://github.com/anisselbd/jev-phishing-bench) 包含 Jev 不及对照模型的结果。收录负结果是为了避免选择性展示。

10. **置信度阈值不能照搬博客**
    阈值必须在你自己的标注集上测；官方局限文档也提示校准问题。把「示例里的 0.8」直接写进生产是常见失误。

### 官方局限里的硬边界

11. **计数与算术留给代码**
    官方 jaggedness 写明：`jev-1.13` 不可靠计数（字符、词频、长列表），也不是计算器；应在代码里迭代并对每一项单独提问再汇总。
    来源：[Jev 1.13 jaggedness — Math and Numbers](https://docs.typesafe.ai/model-jaggedness/jev-1.13.md)。

12. **日期时间先抽取、后比较**
    模型把日期当文本读，直接问「谁更早 / 是否落在窗口内」不可靠；应把月/日/年做成 Choice 抽取，比较与运算放在代码。
    来源：[同上 — Date and time comparison](https://docs.typesafe.ai/model-jaggedness/jev-1.13.md)。

13. **无关 state 会拖累准确率**
    官方称大而无关的 state 会引入 distractor / context rot；先在代码里过滤，只送问题需要的字段。
    来源：[同上 — Large state](https://docs.typesafe.ai/model-jaggedness/jev-1.13.md)。

14. **Noul 与 Choice 没有你以为的恒等式**
    同一判断用 Noul 与 yes/no Choice 问，数值不必一致；`P` 与 `1-P(¬)` 也不保证相加为 1。不要把在一种题型上调好的阈值直接搬到另一种。
    来源：[同上 — Common-sense structural invariants](https://docs.typesafe.ai/model-jaggedness/jev-1.13.md)。

15. **Jev 不做文本生成**
    官方：不适合靠连环 Choice「拼字」；抽取应先用正则或生成模型得到候选，再让 Jev 选择。
    来源：[同上 — Generation](https://docs.typesafe.ai/model-jaggedness/jev-1.13.md)。

16. **限流与别名会动；网关 ID 也不通用**
    Models 页写明速率限制会动态调整；`jev-latest` / `jev-preview` 会随发版漂移，阈值应钉版本 ID。各网关的模型名、计费与接入条件不同，需分别核对。
    来源：[Models](https://docs.typesafe.ai/models.md)；[Vercel AI Gateway changelog](https://vercel.com/changelog/typesafe-ai-jev-now-available-on-ai-gateway)；[Cloudflare Workers AI — typesafe/jev](https://developers.cloudflare.com/ai/models/typesafe/jev/)；[OpenRouter 上线说明](https://x.com/OpenRouter/status/2100744709589316009)。

## English

### Judgment and wording

1. **Valid format ≠ correct judgment** — See official [jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13.md) and [Before using these projects](../README.md#before-using-these-projects).

2. **“JSON classifier” framing** is useful rhetoric, not a product warranty. Example discussion: [@danshipper](https://x.com/danshipper/status/2100251499443998766).

3. **Small-sample evals do not generalize** — [Every / Mike Taylor](https://every.to/also-true-for-humans/mini-vibe-check-typesafe-s-jev-judged-everything-i-ve-written-in-0-7-seconds) is one experiment (incl. 6/7 planted defects), not a universal accuracy claim.

### Demos and reproduction

4. **One demo win ≠ reproducible** — Pac-Man follow-up: [author could not reproduce an earlier win](https://x.com/ephraimduncan/status/2100554620254752981).

5. **Browser demos often use structured state**, not pure vision CU. Treat latency/cost as that run’s measurement. Launch-era demo: [Browser Use](https://x.com/gregpr07/status/2100411066966749359).

6. **Open replicas ≠ official weights** — `jevlike`, SemIf/OpenJev, etc. do not prove official model internals.

### Integration

7. **Gateway names and entitlements drift** — Re-check Vercel / Cloudflare / OpenRouter docs before citing waitlist or pricing claims.

8. **Featured cards are not a production soak test** — On 2026-09-20 maintainers installed two SDKs and the router package; browser automation was README-only. No unified live API soak. See [featured-review.md](featured-review.md).

9. **Negative results belong here** — e.g. [jev-phishing-bench](https://github.com/anisselbd/jev-phishing-bench).

10. **Do not copy confidence thresholds from blog posts** — Measure on your labeled data.

### Hard edges from official jaggedness / models

11. **Counting and arithmetic belong in code** — Official jaggedness: `jev-1.13` does not count reliably and is not a calculator; iterate in code and ask one question per item. Source: [Math and Numbers](https://docs.typesafe.ai/model-jaggedness/jev-1.13.md).

12. **Dates: extract, then compare in code** — Dates are read as text; ask for components as Choice, then compare in code. Source: [Date and time comparison](https://docs.typesafe.ai/model-jaggedness/jev-1.13.md).

13. **Irrelevant state hurts accuracy** — Large unrelated state acts as distractor / context rot; filter in code first. Source: [Large state](https://docs.typesafe.ai/model-jaggedness/jev-1.13.md).

14. **Noul and Choice are not interchangeable identities** — Same judgment as Noul vs yes/no Choice need not match; do not reuse thresholds across question types. Source: [Structural invariants](https://docs.typesafe.ai/model-jaggedness/jev-1.13.md).

15. **Jev is not for text generation** — Chaining choices to “spell” is slow and weak; extract candidates elsewhere, let Jev choose. Source: [Generation](https://docs.typesafe.ai/model-jaggedness/jev-1.13.md).

16. **Rate limits and aliases move; gateway IDs differ** — Limits adjust dynamically; pin versioned model IDs for tuned thresholds. Re-check each gateway’s model id and terms. Sources: [Models](https://docs.typesafe.ai/models.md); [Vercel AI Gateway changelog](https://vercel.com/changelog/typesafe-ai-jev-now-available-on-ai-gateway); [Cloudflare typesafe/jev](https://developers.cloudflare.com/ai/models/typesafe/jev/); [OpenRouter launch note](https://x.com/OpenRouter/status/2100744709589316009).
