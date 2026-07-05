# 脚本使用

## `scripts/wiki_lint.py`

用于做第一轮结构巡检，当前覆盖：

1. 失效 `[[wikilink]]`
2. 无入链页面
3. `review/` 下疑似新写入页面

## 用法

```powershell
python -X utf8 F:\股票\股票复盘\skills\stock-wiki\scripts\wiki_lint.py --wiki-root F:\wiki\trade-system
```

如果只想看 JSON：

```powershell
python -X utf8 F:\股票\股票复盘\skills\stock-wiki\scripts\wiki_lint.py --wiki-root F:\wiki\trade-system --json
```

## 输出解释

- `broken_links`
  指向不存在页面的 wiki 双链。
- `orphan_pages`
  没有任何入链的页面。
- `review_candidates`
  位于 `review/` 下，疑似不该继续写入的新页面。

## 解释边界

1. 这个脚本只做结构检查，不判断市场观点对错。
2. `orphan_pages` 只是候选问题，不等于一定要修。
3. 如果页面本来就应该独立存在，需要人工判断是否保留。
