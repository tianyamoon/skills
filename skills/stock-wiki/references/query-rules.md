# 检索规则

## 查询顺序

1. 先查 `reviews/`
2. 再查 `topics/`、`entities/stocks/`、`cycles/`
3. 再查 `concepts/`、`strategies/`、`tactics/`、`sop/`
4. 需要证据时回到 `raw/`
5. 最后才参考 `output/`

## 中文问法映射

- “这个题材最近怎么演化” -> `topics/` + `reviews/` + `cycles/`
- “这只股票挂了哪些概念” -> `entities/stocks/` + `topics/`
- “某天复盘怎么写的” -> `reviews/`
- “这条消息从哪里来的” -> `raw/`
- “这个打法以前怎么定义过” -> `strategies/` / `tactics/` / `sop/`

## 回答结构

优先用这 4 层组织：

1. `结论`
2. `证据`
3. `关联页面`
4. `缺口 / 待核`

## 注意

1. 不把单一 raw 材料直接说成正式结论。
2. 不把 `output/` 当主证据。
3. 用户问的是“有没有”，先给结论，再展开。
