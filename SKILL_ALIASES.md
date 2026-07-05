# Skill Aliases

This file defines the recommended Chinese calling names for custom skills in this repository.

## Rule

- Native explicit invocation should still use `$english-skill-slug`.
- Chinese names below are recommended human-facing aliases for discussion, routing, and documentation.
- If a future agent/router layer supports alias mapping, these names should be the first-choice Chinese aliases.

## Alias Table

| Skill slug | Recommended Chinese alias | Short alias | What it is for |
|---|---|---|---|
| `股票行业方法论` | `股票行业方法论` | `行业周期方法论-股票` | General industry-cycle research framework, including process layer and results layer |
| `股票行业逻辑评分` | `股票行业逻辑评分` | `行业逻辑评分器-股票` | Score the rigor of an industry thesis, sector note, or research draft |
| `industry-trend-stock-picker` | `股票产业趋势选股` | `产业趋势选股票` | Pick directions first, then select stocks within the winning direction |
| `wiki原始分类路由` | `wiki原始分类路由` | `分类路由` | Decide where raw materials should be filed before they enter the knowledge base |
| `wiki材料观点提炼` | `wiki材料观点提炼` | `观点提炼` | Convert raw source material into reusable thesis, catalyst, and verification points |
| `stock-wiki` | `股票wiki维护` | `股票wiki` | Maintain and route content inside `F:\wiki\trade-system` |
| `technical-stock-picker` | `股票技术选股` | `技术选股票` | Technical review for trend, deviation, support, pressure, and execution conditions |
| `wiki-link-repair` | `wiki修链` | `双链修复` | Repair broken links, missing backlinks, and isolated knowledge pages |
| `zmt-gzh-zy` | `自媒体公众号写作` | `公众号写作` | Turn research and review assets into publishable public-facing articles |

## Recommended explicit usage

Use these stable forms when you want zero ambiguity:

- `$industry-cycle-methodology`
- `$industry-logic-scorer`
- `$industry-trend-stock-picker`
- `$raw-taxonomy-router`
- `$source-to-thesis-extractor`
- `$stock-wiki`
- `$technical-stock-picker`
- `$wiki-link-repair`
- `$zmt-gzh-zy`

## Recommended human phrasing

These are good natural-language ways to ask for the same skills:

- `用行业周期方法论看一下这个研究框架`
- `用逻辑评分器给这篇 AI 产业链 memo 打个分`
- `用产业趋势选股排一下下周主攻方向`
- `用原始分类路由判断这份材料该进哪个 raw`
- `用材料观点提炼把这篇研报压成 thesis`
- `用股票wiki 把这条资讯入库`
- `用技术选股看这票月周线和执行位`
- `用 wiki修链 修一下这批孤点页`
- `用公众号写作把这份复盘改成发布稿`

## Non-recommended aliases

Avoid aliases that are too broad or easy to conflict:

- `研究`
- `写作`
- `wiki`
- `选股`
- `技术`
- `分类`

They are too ambiguous to serve as durable calling names.
