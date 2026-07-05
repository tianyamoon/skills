#!/usr/bin/env python3
"""Generate reusable templates for the industry-cycle-methodology skill."""

from __future__ import annotations

import argparse
from pathlib import Path
from textwrap import dedent


TEMPLATES = {
    "quick-stage-card": dedent(
        """\
        # [行业名称] 快速阶段卡

        ## 一句话结论

        [行业当前处于什么阶段，最重要的驱动是什么，当前最大机会或风险是什么]

        ## 当前阶段

        - 当前阶段：
        - 上一阶段：
        - 下一阶段候选：

        ## 核心证据

        ### 事实

        1. 需求：
        2. 供给：
        3. 价格：
        4. 库存：
        5. CapEx：
        6. 估值与持仓：

        ### 判断

        1. 当前更像产业验证 / 主升扩散 / 估值见顶 / 去库出清：
        2. 这个判断最依赖的变量：
        3. 当前最容易误判的点：

        ## 风险与待补点

        1. 还缺什么数据：
        2. 哪个变量一旦反向，结论就要改：

        ## 下一步

        1. 最该补的样本：
        2. 最该跟踪的变量：
        """
    ),
    "standard-industry-report": dedent(
        """\
        # [行业名称] 标准行业研究卡

        ## 一句话结论

        [行业阶段 + 主驱动 + 最大机会/风险 + 当前投资含义]

        ## 研究边界

        1. 行业定义：
        2. 环节：
        3. 区域：
        4. 时间范围：
        5. 样本范围：

        ## 样本框架

        1. 龙头：
        2. 挑战者：
        3. 上游：
        4. 下游：
        5. 失败样本：
        6. 阴影资产：

        ## 核心变量表摘要

        1. 需求变量：
        2. 供给变量：
        3. 价格变量：
        4. 库存变量：
        5. CapEx 变量：
        6. 财务质量变量：
        7. 估值与拥挤变量：

        ## 事实

        1. 需求端事实：
        2. 供给端事实：
        3. 价格与库存事实：
        4. CapEx 与融资事实：
        5. 财务事实：
        6. 市场定价事实：

        ## 判断

        1. 行业阶段判断：
        2. 资本周期判断：
        3. 估值与预期判断：
        4. 龙头与二线分化判断：
        5. 当前不是的东西：

        ## 历史映射

        1. 最相似正样本：
        2. 最相似反样本：
        3. 相似机制：
        4. 关键差异：

        ## 公司组观察

        1. 最强穿越者：
        2. 最强交易弹性：
        3. 最脆弱环节：

        ## 风险与待补点

        1. 关键数据缺口：
        2. 关键分歧：
        3. 证伪条件：

        ## 下一步

        1. 下次更新触发条件：
        2. 必跟踪变量：
        3. 必补样本：
        """
    ),
    "peer-comparison": dedent(
        """\
        # [行业名称] 公司组比较卡

        ## 比较对象

        1. 龙头：
        2. 二线：
        3. 上游：
        4. 下游：
        5. 失败样本：

        ## 比较维度

        1. 市场地位：
        2. 成本位置：
        3. CapEx 纪律：
        4. 资产负债表：
        5. 自由现金流：
        6. ROIC：
        7. 客户黏性：
        8. 当前估值与预期：

        ## 结论

        1. 最强经营质量：
        2. 最强周期穿越：
        3. 最强弹性但高风险：
        4. 最容易被证伪的公司：
        """
    ),
    "history-mapping": dedent(
        """\
        # [行业名称] 历史映射卡

        ## 当前对象

        1. 当前行业：
        2. 当前阶段候选：
        3. 当前主变量：

        ## 映射对象

        1. 成功周期样本：
        2. 失败周期样本：
        3. 旁证行业样本：

        ## 相似机制

        1. 需求机制：
        2. 供给机制：
        3. CapEx 机制：
        4. 估值扩散机制：

        ## 关键差异

        1. 技术门槛：
        2. 政策环境：
        3. 资本成本：
        4. 竞争格局：

        ## 映射结论

        1. 当前更像：
        2. 最值得警惕的历史片段：
        3. 最值得期待的结构机会：
        """
    ),
    "weekly-tracker": dedent(
        """\
        # [行业名称] 周更跟踪卡

        ## 本周一句话变化

        [本周最重要的变化及其含义]

        ## 变量更新

        1. 需求：
        2. 供给：
        3. 价格：
        4. 库存：
        5. CapEx：
        6. 估值与资金：

        ## 结论变化

        1. 阶段有没有变：
        2. 核心驱动有没有变：
        3. 风险有没有变：

        ## 本周新增分歧

        1. 市场最关注什么：
        2. 我们和市场最大的差异是什么：

        ## 下周重点

        1. 要盯的事件：
        2. 要盯的变量：
        3. 触发结论升级或降级的条件：
        """
    ),
    "multi-role-review": dedent(
        """\
        # [行业名称] 多角色审议纪要

        ## 主问题

        [最核心的争议问题]

        ## 主持人摘要

        1. 当前结论：
        2. 最大分歧：
        3. 需要裁决的变量：

        ## 角色观点

        ### 产业分析师

        1. 最强支持证据：
        2. 最弱环节：

        ### 资本周期审计员

        1. 供给扩张是否过快：
        2. 哪个时间窗最危险：

        ### 估值预期审计员

        1. 价格里已写入什么：
        2. 哪个预期最脆弱：

        ### 空头检察官

        1. 最可能错的地方：
        2. 最可能导致回撤的触发器：

        ### 风险经理

        1. 当前最不该忽视的尾部风险：
        2. 应该等待还是行动：

        ## 分歧矩阵

        1. 共识点：
        2. 核心分歧点：
        3. 需要补证的点：

        ## 综合结论

        1. 当前主结论：
        2. 当前保留意见：
        3. 下一步验证动作：
        """
    ),
    "postmortem-review": dedent(
        """\
        # [行业名称] 研究复盘卡

        ## 原始结论

        1. 当时一句话结论：
        2. 当时关键假设：
        3. 当时证伪条件：

        ## 事后结果

        1. 实际发生了什么：
        2. 哪些变量验证了：
        3. 哪些变量证伪了：

        ## 误差归因

        1. 边界定义错误：
        2. 变量选择错误：
        3. 阶段判断错误：
        4. CapEx 风险低估：
        5. 估值预期误读：
        6. 情绪噪音干扰：

        ## 方法升级

        1. 以后要新增什么变量：
        2. 哪类情况必须走多角色审议：
        3. 哪类行业必须增加失败样本：
        """
    ),
    "fund-style-research-letter": dedent(
        """\
        # [主题/行业名称] 机构式研究信

        ## 前门摘要

        - 一句话结论：
        - 当前阶段：
        - 当前不是：
        - 本期最重要变化：
        - 最大风险：

        ## Executive Summary

        1. 最重要的三个判断：
        2. 与上次相比最大的变化：
        3. 未来 90 天最值得盯的变量：

        ## 记分牌

        | 维度 | 当前状态 | 较上期变化 | 验证度 | 备注 |
        |---|---|---|---|---|
        | 需求 |  |  |  |  |
        | 供给 |  |  |  |  |
        | 价格 |  |  |  |  |
        | CapEx |  |  |  |  |
        | 财务兑现 |  |  |  |  |
        | 估值/拥挤 |  |  |  |  |

        ## 本文回答的问题

        1. 这轮行情/景气的主驱动是什么：
        2. 当前最关键的传导链条是什么：
        3. 为什么现在要看这个问题：

        ## 事实

        1. 宏观与政策事实：
        2. 行业供需事实：
        3. 价格与库存事实：
        4. CapEx 与融资事实：
        5. 财务与订单事实：
        6. 市场定价与持仓事实：

        ## 判断

        1. 阶段判断：
        2. 资本周期判断：
        3. 估值与预期判断：
        4. 龙头/二线/上游/下游分化判断：
        5. 当前最容易被误判的点：

        ## 变化

        1. 本期新增判断：
        2. 本期升级判断：
        3. 本期降级判断：
        4. 仍未解决的问题：

        ## 投资含义 / 映射含义

        1. 最强环节：
        2. 最弱环节：
        3. 最值得观察的弹性组：
        4. 历史映射或 AI 映射：

        ## 风险与证伪条件

        1. 哪个变量反向会推翻主判断：
        2. 哪个数据仍待确认：
        3. 市场当前可能交易错了什么：

        ## Appendix

        1. 关键图表：
        2. 关键来源：
        3. 待补数据：
        4. 术语与口径：
        """
    ),
    "chairman-style-year-end-letter": dedent(
        """\
        # [模块/主题名称] 年度收口信

        ## 开场摘要

        [用一段话说明这一年最重要的结果、最关键的动作、以及当前最值得继续坚持的主线。]

        ## 我们今年完成了什么

        1. 结构层：
        2. 证据层：
        3. 样本层：
        4. 总论层：

        ## 研究框架与原则

        1. 今年确认有效的方法：
        2. 今年修正的方法：
        3. 今年没有改变的底层原则：

        ## 关键结论

        1. 当前阶段判断：
        2. 当前资本周期判断：
        3. 当前最强样本/最弱样本：
        4. 当前最重要的风险边界：

        ## 本期关键动作

        1. 新增了什么：
        2. 删减或降级了什么：
        3. 为什么这样做：

        ## 仍未解决的问题

        1. 证据缺口：
        2. 高分歧问题：
        3. 需要下阶段继续跟踪的变量：

        ## 下一阶段优先级

        1. 最该补的索引/总表：
        2. 最该补的样本/图谱：
        3. 最该补的硬数据：
        4. 最该升级的方法模块：

        ## 附录

        1. 本期涉及的核心文件：
        2. 当前权威入口：
        3. 历史交接材料：
        """
    ),
    "thesis-ledger-entry": dedent(
        """\
        # Thesis Ledger Entry

        1. 研究对象：
        2. 日期：
        3. 一句话结论：
        4. 当前阶段：
        5. 核心变量：
        6. 关键假设：
        7. 证伪条件：
        8. 风险提示：
        9. 下一次检查时间：
        """
    ),
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Render reusable research templates.")
    parser.add_argument("--list", action="store_true", help="List available templates.")
    parser.add_argument("--template", choices=sorted(TEMPLATES), help="Template name.")
    parser.add_argument("--title", help="Replace the first heading with a custom title.")
    parser.add_argument("--write", help="Write the output to a file instead of stdout.")
    return parser


def render_template(template_name: str, title: str | None) -> str:
    content = TEMPLATES[template_name]
    if title:
        lines = content.splitlines()
        if lines and lines[0].startswith("# "):
            lines[0] = f"# {title}"
        content = "\n".join(lines) + "\n"
    return content


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.list:
        for name in sorted(TEMPLATES):
            print(name)
        return 0

    if not args.template:
        parser.error("either --list or --template is required")

    content = render_template(args.template, args.title)

    if args.write:
        output_path = Path(args.write)
        output_path.write_text(content, encoding="utf-8")
    else:
        print(content, end="")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
