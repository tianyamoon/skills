---
name: industry-cycle-methodology
description: 股票行业周期方法论，行业周期方法论-股票。通用行业周期分析与股票研究技能，用于构建、复用和应用第一性原理与顶级机构方法论，支持股票视角的行业阶段判断、资本周期分析、估值与预期校验、历史复盘、AI与跨行业映射，以及把研究结果组织成顶级基金风格的最终输出。用于“股票”“股票行业周期”“股票周期研究”“股票方法论”“行业周期方法论-股票”“周期方法论-股票”等请求，或需要明确区分“过程层”和“结果层”时使用。
---

# Industry Cycle Methodology

把本技能明确分成两层：

1. `过程层`
   - 解决“研究怎么做”。
   - 产出的是内部研究生产物，如变量表、阶段判断、比较卡、复盘卡、审议纪要。
2. `结果层`
   - 解决“研究做完后，最终怎么输出给读者”。
   - 产出的是最终可阅读成果，如机构式研究信、季度信、年终收口信、正式总结稿。

不要把两层混写。

1. `结果层`不能替代`过程层`。
   - 没有变量、证据、验证链，最终成稿只会像漂亮结论。
2. `过程层`也不等于`结果层`。
   - 研究卡、变量表、审议纪要通常服务作者，不自动等于读者友好的正式输出。

## 先判任务属于哪一层

优先先做这一步。

1. 任务是在判断行业阶段、供需、CapEx、估值、映射、证伪条件。
   - 走`过程层`。
2. 任务是在整理正式汇报、阶段总结、对外可读长文、交接信、年度总述。
   - 走`结果层`。
3. 任务既要研究，又要形成正式成稿。
   - 先走`过程层`，再走`结果层`。

## 过程层

把`过程层`当成研究生产系统，而不是写稿系统。

### 默认阅读顺序

1. 先读 [references/methodology-baseline.md](references/methodology-baseline.md)
   - 用于校准总公式、六个镜头、五类周期、默认分析顺序。
2. 再读 [references/research-workflow.md](references/research-workflow.md)
   - 用于定义边界、建样本框架、建变量表、收集证据、做阶段判断。
3. 再读 [references/module-routing.md](references/module-routing.md)
   - 用于判断本次任务需要哪些模块组合，不要把所有模块机械堆上去。

### 按需补读

1. 任务涉及方法论外部校准、机构镜头借鉴。
   - 读 [references/institutional-methodology-corpus.md](references/institutional-methodology-corpus.md)
2. 任务涉及高分歧、热门题材、多空交叉审计。
   - 读 [references/multi-role-review.md](references/multi-role-review.md)
3. 任务涉及复盘、台账、方法升级、研究质量验证。
   - 读 [references/evaluation-and-review.md](references/evaluation-and-review.md)

### 过程层产物

优先把过程层产物理解成“内部研究对象”。

1. `quick-stage-card`
2. `standard-industry-report`
3. `peer-comparison`
4. `history-mapping`
5. `weekly-tracker`
6. `multi-role-review`
7. `postmortem-review`
8. `thesis-ledger-entry`

读取 [references/output-templates.md](references/output-templates.md) 查看模板定位。

### 过程层最低要求

至少保留以下链条：

1. `事实`
2. `变量`
3. `传导`
4. `验证`
5. `映射`

如果这个链条表达不清，就不要急着进入`结果层`包装。

## 结果层

把`结果层`当成读者路径设计系统，而不是研究过程回放系统。

### 默认阅读顺序

1. 先读 [references/top-fund-organization.md](references/top-fund-organization.md)
   - 用于学习顶级基金如何组织最终可读成果。
2. 再读 [references/output-templates.md](references/output-templates.md)
   - 用于选模板，并区分过程产物、桥接产物、结果产物。
3. 需要直接起草模板时，运行 [scripts/render_template.py](scripts/render_template.py)

### 结果层原则

1. 先优化读者路径，不要照搬作者研究路径。
2. 先给一句话结论、阶段定位、记分牌、关键变化。
3. 再展开事实、判断、动作、风险、附录。
4. 让附录承担“仓库功能”，不要让正文被原始资料淹没。
5. 把“本期变化”单独拎出来，保证连续跟踪的可读性。

### 结果层产物

优先使用以下模板：

1. `fund-style-research-letter`
   - 适合主题总论、阶段总结、机构式研究信。
2. `chairman-style-year-end-letter`
   - 适合年度收口、模块总述、交接信、方法升级总结。

## 桥接层

有些模板天然介于两层之间，可以先服务研究，再被升级成正式结果。

1. `standard-industry-report`
   - 默认视为`桥接层`
   - 先作为研究主骨架，再决定是否改写成基金风格成稿。

## 模板调用

运行：

```powershell
python -X utf8 C:\Users\tiany\.codex\skills\industry-cycle-methodology\scripts\render_template.py --list
python -X utf8 C:\Users\tiany\.codex\skills\industry-cycle-methodology\scripts\render_template.py --template fund-style-research-letter
python -X utf8 C:\Users\tiany\.codex\skills\industry-cycle-methodology\scripts\render_template.py --template chairman-style-year-end-letter
```

## 推荐串联方式

### 纯研究任务

1. 读取 `methodology-baseline`
2. 读取 `research-workflow`
3. 按需读取 `module-routing`
4. 产出一个或多个`过程层`模板

### 研究加正式成稿

1. 先完成`过程层`
2. 确认关键变量、证据链、证伪条件已经成型
3. 再读取 `top-fund-organization`
4. 用`结果层`模板重组内容

### 年度收口或阶段交接

1. 用`过程层`先汇总今年完成的结构、样本、证据、结论、缺口
2. 用`evaluation-and-review`整理复盘与未解问题
3. 再改写为 `chairman-style-year-end-letter`

## 禁止动作

1. 不要用`结果层`漂亮结构掩盖过程证据缺口。
2. 不要把研究顺序原样端给读者。
3. 不要因为要追求正式输出，就删掉`待补`、`待核`、`证伪条件`。
4. 不要把顶级基金组织方式误解成“多写套话”。
