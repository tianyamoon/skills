---
name: 技术选股票
description: 用于技术选股和图形筛选。先用 MCP 获取个股或指数 K 线，再判断月线、周线、乖离率、强弱、量价结构和执行/证伪条件。它只回答技术证据和执行节奏，不替代产业方向、基本面和估值判断。
---

# 技术选股票

## 定位

把“图形看着强不强”的模糊讨论，压成一套先取数、再算指标、最后给执行条件的技术审查流程。

默认边界：

1. 先有数据，再有图形结论。
2. 月线和周线是资格线，日线只负责执行。
3. 技术面不能覆盖产业方向、基本面和估值纪律。
4. MCP 数据拿不到、字段不全或口径漂移时，必须写 `待核`。

## 工作流程

1. `单票技术资格审查`
2. `多个个股技术对比`
3. `月周线与乖离率复核`
4. `执行位 / 证伪位 / 支撑压力`
5. `对既有候选做技术层复核`

## 参考文件

1. 默认先读 [references/mcp-routing.md](references/mcp-routing.md)。
2. 计算前读 [references/indicator-scope.md](references/indicator-scope.md)。
3. 输出前读 [references/output-template.md](references/output-template.md)。
4. 需要稳定计算时，用 [scripts/calc_technical_metrics.py](scripts/calc_technical_metrics.py) 对 MCP K 线结果做统一计算。

## 固定顺序

`MCP取数 -> 数据口径确认 -> 月线资格 -> 周线资格 -> 月线乖离率 -> 日线执行层 -> 量价结构 -> 执行条件 -> 证伪条件`

## 输出纪律

1. 先给一句话结论。
2. 明确数据来源、日期和口径。
3. 把`事实`、`判断`、`执行`分开。
4. 结尾必须落到执行或证伪，不要只说“趋势不错”。
