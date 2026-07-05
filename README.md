# tianyamoon/skills

这个仓库是我自定义 Codex 技能的正式真源仓库。

## 仓库内容

- `skills/`：我持续维护的自定义技能包
- `scripts/import-local-skills.ps1`：把 `C:\Users\tiany\.codex\skills` 同步到这个仓库
- `scripts/publish-to-codex.ps1`：把这个仓库里的技能发布回 `C:\Users\tiany\.codex\skills`

## 当前范围

默认跟踪 `C:\Users\tiany\.codex\skills` 下的自定义技能，并跳过 `.system`。

当前已纳入仓库的技能：

- `股票行业方法论`
- `股票行业逻辑评分`
- `股票产业趋势选股`
- `wiki原始分类路由`
- `wiki材料观点提炼`
- `股票wiki维护`
- `技术选股票`
- `wiki修链`
- `自媒体公众号写作`

## 命名说明

- 当前仓库以中文技能名为主。
- 技能显式调用时，优先使用技能本体 `name:` 对应的名称。
- 技能分组上，股票研究相关技能以 `股票...` 开头，知识库 / wiki 维护相关技能以 `wiki...` 开头。

## 推荐维护流程

1. 先在本机技能目录里创建或修改技能。
2. 运行 `powershell -ExecutionPolicy Bypass -File .\scripts\import-local-skills.ps1`。
3. 用 `git status --short` 检查变更。
4. 提交并推送到 GitHub。
5. 在另一台机器使用时，克隆本仓库后运行 `powershell -ExecutionPolicy Bypass -File .\scripts\publish-to-codex.ps1`。

## 说明

- 如果 Codex 界面没有立刻显示新技能名，通常是技能索引缓存还没刷新，不代表磁盘文件没改。
- 如果后续还要把 `C:\Users\tiany\.agents\skills` 里的某些自定义技能也纳入这个仓库，可以再补第二个来源路径和白名单规则。
