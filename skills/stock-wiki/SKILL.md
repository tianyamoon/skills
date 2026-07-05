---
name: 股票wiki维护
description: 维护 `F:\wiki\trade-system` 这套中文股票知识库，覆盖入库、检索、页面维护、结构巡检、落点路由与导航修复。用于“把资讯入库”“查题材/个股/复盘”“补页面”“巡检 wiki”“修复双链”等请求。
---

# 股票wiki维护

## 定位

把 `F:\wiki\trade-system` 当成股票复盘体系的长期真源来维护，不把它当临时笔记堆放区。

这个技能服务 5 类工作：

1. `入库`
2. `检索`
3. `维护`
4. `巡检`
5. `路由`

## 先读什么

1. 判断目录落点、真源边界、页面角色时，读 `references/schema-map.md`。
2. 做入库或归档时，读 `references/ingest-rules.md`。
3. 做查询或问答时，读 `references/query-rules.md`。
4. 补题材页、个股页、复盘页、方法页时，读 `references/page-templates.md`。
5. 做结构排查、补链、巡检时，读 `references/lint-rules.md`。
6. 需要判断中文用户会怎么说、如何映射模式时，读 `references/chinese-trigger-examples.md`。
7. 需要直接跑第一轮结构巡检时，读 `references/script-usage.md` 并运行 `scripts/wiki_lint.py`。

## 硬边界

1. `reviews/` 是正式复盘真源。
2. `raw/` 是原始证据真源，不能跳过。
3. `output/` 是交付层，不反向充当事实真源。
4. `review/` 视为旧实验层，不默认写入新正式内容。
5. 页面关系以正文里的 `[[wikilink]]` 为主，不能只靠 frontmatter 的 `sources:`。
6. 涉及历史框架页时，一次只做一个小的、可确认的改动。
7. 事实不确定时显式写 `待核`，不要替用户补脑。
