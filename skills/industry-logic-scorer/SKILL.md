---
name: industry-logic-scorer
description: 行业逻辑评分器-股票。Scores current industry-thesis or sector research for first-principles rigor, cycle positioning, supply-demand transmission, capital-cycle discipline, valuation awareness, and falsifiability in stock research. Use when Codex needs to review an industry report, strategy note, AI chain memo, bridge-layer research card, results-layer draft, or any stock/market/industry thesis, assign a weighted score, identify blind spots, and propose concrete补证 actions. Trigger on “股票行业逻辑评分”“行业逻辑评分器-股票”“研究打分”“赛道逻辑打分”“股票研究评分”.
---

# Industry Logic Scorer

## Overview

Use this skill to audit whether a piece of industry research is actually investable research, or just fluent narrative.

Default mindset:

1. Separate `research quality` from `conclusion direction`.
2. Score the chain, not the writing style.
3. Prefer finding the weakest link over praising what is already obvious.

## Core Principle

Treat top-tier research as an `audit sequence`:

`stage -> variables -> transmission -> capital cycle -> economics -> valuation -> falsification -> monitoring`

If the research cannot be rebuilt through that sequence, it is not ready for a strong conclusion.

## Workflow

### Step 1: Define the object being scored

Identify:

1. What the document is trying to answer.
2. Whether it is an industry thesis, company thesis, bridge-layer card, or formal summary.
3. What time horizon it is using.
4. What it is explicitly *not* answering.

If the document has no clear scope, mention that before scoring details.

### Step 2: Rebuild the thesis chain

Rewrite the argument in this order:

1. `Facts`
2. `Variables`
3. `Transmission`
4. `Capital cycle`
5. `Economics`
6. `Valuation / expectations`
7. `Verification / falsification`

If you cannot rebuild the chain, that gap is itself a finding.

### Step 3: Score the 10 dimensions

Use this weight set:

| Dimension | Weight |
|---|---:|
| Problem definition and scope | 8 |
| Structural force and macro backdrop | 7 |
| Core variable decomposition | 15 |
| Transmission-chain completeness | 12 |
| Supply / CapEx / capital-cycle audit | 12 |
| Wallet share / profit pool / business economics | 12 |
| Stage positioning and historical mapping | 10 |
| Valuation / expectations / crowding | 12 |
| Evidence quality and falsifiability | 7 |
| Risks, monitoring points, and next verification step | 5 |

### Step 4: Apply hard ceilings

Apply these caps even if the prose is strong:

1. No stage judgment: cap total at `75`.
2. No valuation, expectations, or crowding discussion: cap total at `72`.
3. Heavy-CapEx thesis with no supply or CapEx audit: cap total at `68`.
4. No dates, sources, or unit discipline: cap total at `60`.
5. No disconfirming evidence or main risks: cap total at `78`.

State the ceiling explicitly when used.

### Step 5: Diagnose the real deficiency

Do not stop at "needs more data." Say which category is missing:

1. `Missing stage`
2. `Missing variables`
3. `Missing transmission`
4. `Missing supply / CapEx audit`
5. `Missing economics`
6. `Missing valuation`
7. `Missing evidence discipline`
8. `Missing falsification`
9. `Missing monitoring plan`

### Step 6: Prioritize repairs

Always rank fixes by expected value, not by completeness theater.

Default repair order:

1. Add stage judgment.
2. Add the small set of dominant variables.
3. Add the transmission chain.
4. Add supply / CapEx / capital-cycle audit.
5. Add valuation / expectations / crowding.
6. Add falsification conditions and monitoring points.

## Scoring Guidance

### What high-scoring work looks like

High-scoring research usually:

1. Starts by saying where we are in the cycle.
2. Distinguishes demand from supply and funding conditions.
3. Knows which layer captures revenue versus profit.
4. Audits CapEx and return on capital before extrapolating growth.
5. Separates "industry logic is right" from "stock is worth buying here."
6. Lists what would prove the thesis wrong.

### What weak work looks like

Weak research usually:

1. Starts from a conclusion and backfills stories.
2. Lists catalysts without ranking variables.
3. Confuses theme heat with industrial validation.
4. Talks about TAM but not profit pool.
5. Ignores valuation and crowding.
6. Offers no maintenance plan after publication.

## Output Format

Use this structure unless the user asks otherwise:

1. `One-line verdict`
2. `Total score + grade`
3. `Score table by dimension`
4. `Top 3 strengths`
5. `Top 3 weaknesses`
6. `Hard-ceiling items`
7. `Most urgent evidence to add`
8. `What would most likely break the thesis`
9. `What would raise the score by the next 5-10 points`

## Tone and Discipline

1. Be direct, but do not confuse harshness with rigor.
2. Separate facts from judgment.
3. If evidence is missing, say `待补`, `待核`, or `待确认` rather than guessing.
4. If the thesis is good but the stock is expensive, say so explicitly.
5. If the thesis is bad but the writing is smooth, do not reward presentation quality.

## Recommended Language

Use phrases like:

1. `结论方向可能对，但估值链缺失，当前只能给中等分。`
2. `主变量已识别，但供给反应和资本开支反噬没有审计，结论不宜上收。`
3. `叙事强于审计，建议先补阶段判断和证伪条件。`
4. `更像桥接层研究骨架，不足以直接进入结果层正式结论。`

## Do Not

1. Do not reward a document for using many buzzwords.
2. Do not let good formatting hide a weak variable chain.
3. Do not treat stock-price strength as basic-fundamental proof.
4. Do not score a heavy-industry thesis without checking CapEx, supply, and cash flow.
5. Do not turn the review into a rewrite unless the user asks for that.
