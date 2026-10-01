# Claim、跨论文证据矩阵与冲突分析

## Claim 是研究地图中的判断

一个 Claim 表述一个可检查、带范围的知识判断，不是某篇论文的整份摘要。优先为决定 motivation、理论关系、方法选择或方向成立与否的判断创建节点。没有真实证据时可以记录假设，但不得冒充已有结论。

创建前检查已有 Claim：同义且范围相同的判断共用 ID；实质不同的群体、任务或因果强度应拆分。细化措辞时保留修订历史；改变命题本身时创建新 ID，并链接被替代的判断。

## 元数据与状态

使用 [Claim 模板](../assets/claim-note.md)，属性保持扁平，逐项证据放正文表格。

| 属性 | 约定 |
| --- | --- |
| `claim_id` | vault 内稳定且唯一，例如 C001；不包含可变标题 |
| `claim_statement` | 有群体/情境/任务范围的具体命题 |
| `claim_type` | 下表的四种来源类型之一 |
| `current_status` | `draft` 待核查；`active` 当前地图使用；`superseded` 被新判断替代；`retired` 停用。active 不等于已证实 |
| `supporting_papers` / `challenging_papers` | 已有论文节点的引号包裹链接列表；无证据时为空 |
| `evidence_types` | 实验、观察、定性、证明、benchmark、复现等实际证据类型 |
| `population_context_task` / `boundary_conditions` | 群体/任务/情境与成立边界，未知明确写未确定 |
| `evidence_locations` | 论文节点及章节、表格、公式等定位列表，与正文证据行对应 |
| `evidence_sufficiency` | 下述五类定性判断之一，正文说明理由 |
| `unresolved_conflict` | 尚未解决的分歧；无已知冲突不能写成已证明一致 |
| `linked_concepts` / `linked_directions` | 相关概念和方向的链接列表 |

| `claim_type` | 含义 |
| --- | --- |
| `paper-reported` | paper-reported claim：忠实转述一篇论文报告，原文强度与范围不扩大 |
| `cross-paper-synthesis` | cross-paper synthesis：比较多篇论文后得到的综合，给出逐篇依据 |
| `analyst-inference` | analyst inference：分析者解释，说明推理前提、替代解释与未验证部分 |
| `research-hypothesis` | research hypothesis：待验证命题，写出反驳条件 |

## 证据充分性

以下标签是有理由的定性概括，不是概率、分数或机械分档：

- `strong evidence`：在声明范围内，直接且方法可信的证据形成一致支持，重要反证得到实质处理。
- `moderate evidence`：有直接证据，但独立验证、方法或适用范围仍有限。
- `limited evidence`：少量、间接或受较大限制的证据，仅能支持较窄判断。
- `conflicting evidence`：可相关地比较的支持与挑战仍有重要分歧；列出分歧而非用平均数抹平。
- `insufficient evidence`：缺少足以作当前判断的直接材料；包括未阅读、关键来源不可得或只有未检验假设。

选择标签时说明证据直接性、研究设计、独立性、范围和访问限制。不可按论文数投票；同一数据、样本或研究的不同版本不算独立支持。综述总结和它引用的原研究也不能重复计票。统计不显著不自动证明无效，应结合效应和不确定性。

## 跨论文证据矩阵

用 [矩阵模板](../assets/evidence-matrix.md) 选择适合当前问题的列。可以嵌在方向页；跨多个方向复用时保存到 `05-Evidence/`。一个矩阵围绕具体 Claim 或同一可比问题，不围绕“我读过的所有论文”。

共同保留 Paper、Claim relation、Evidence location。关系使用 `supports`、`challenges`、`qualifies`、`context-only` 或 `not-comparable`；后两类不作为直接支持/反对票数。

- 社会科学：Design、Sample/Population、Construct/IV、DV、Effect、Uncertainty、Context/Boundary。
- 机器学习：Dataset/version、Split、Method、Baseline、Metric、Result/uncertainty、Compute/implementation、Limitation。
- 理论：Core construct、Assumption、Mechanism/proposition、Scope、Extension/challenge。
- 混合学科：按证据类型分表，用共同 Claim 连接；不能把主观量表、模型准确率和数学定理拼成同一种效果。

同一论文有不同样本、设置或主张时可以多行，每行标清单位。没有可比条件时保留行并解释不兼容点，不强制合并排序或进行未经设计的 meta-analysis。

表后必须回答：哪些证据最直接？反对证据是什么？结果是否依赖某种边界条件？为什么综合判断比逐篇摘要多提供了信息？还有什么来源能改变结论？

## Conflict Analysis

先确认双方是否真的回答同一个命题，再诊断分歧。按学科检查以下可能来源；不适用项可省略，未报告项与相同条件不能混淆。

- population、sample、task、context；样本重叠、选择偏差与人群边界。
- construct definition、operationalization、intervention；是否同名异义或测量了不同对象。
- design、statistical power、效应和不确定性；不能仅凭样本量推断检验功效。
- dataset/version、split、metric、baseline、compute、implementation；比较预算与实现是否公平。
- theoretical assumption、时间、模型/软件/论文版本变化。

社会科学尤其检查 boundary conditions；ML 尤其检查数据划分、算力、实现与对照公平性。

| Observed disagreement | Possible source | Evidence | Current interpretation | Remaining uncertainty |
| --- | --- | --- | --- | --- |
| 双方具体哪里不同 | 候选原因，标注推断 | 两侧原文位置或缺失信息 | 当前可支持的解释 | 还需什么证据来区分解释 |

不同条件仅是解释线索，不自动证明某个 moderator 或机制。无法区分替代解释时保留冲突，不能为了得到统一故事选择性舍弃论文。

## 从证据到方向，以及更新

方向中的六步链必须逐步连接：Existing evidence（Claim/矩阵）→ Unresolved issue（有范围的缺口）→ Candidate mechanism（理论依据与替代机制）→ Research hypothesis（可证伪）→ Minimal viable study（最小能区分解释的研究）→ Failure criterion（什么结果会使方向暂时不成立）。

科学失败标准应指向效应、机制或解释，而非“实验效果不好”。数据不可得、资源超限等停止条件另列；它们不证明假设为假。具体阈值只有在研究依据充分时预先设定，不能为了填表编数字。

新证据出现后更新相关矩阵、Claim 的类型/充分性/边界、方向与主题摘要，保留修改前后的判断和原因。已解决的冲突标注解决依据；被反例否定的 gap 要修改状态和拟议方案，不能只在补读队列加一条待办。
