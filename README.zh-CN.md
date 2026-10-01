# 科研文献阅读与研究地图

[English](README.md) | [简体中文](README.zh-CN.md)

一个用于深入阅读科研论文、围绕研究问题持续积累 Obsidian 文献库的 Codex skill。

它把研究动机、理论基础、方法、实验证据和可能开展的研究联系起来：每篇论文有独立笔记，主题总览解释论文之间的关系。

## 能做什么

- **建立研究地图**：梳理 motivation、理论基础，并在证据支持时尽量形成五个研究方向。
- **深入阅读论文**：每篇纳入文献都有总结，对核心论文按博士研究所需的深度展开。
- **具体解释方法和实验**：覆盖假设、公式、设计理由、算法、baseline、实验数值、消融与失败情况。
- **追溯证据**：记录原文位置，区分论文报告、分析推断和研究设想。
- **根据反馈继续查阅**：把“2.2 理论不够”等反馈转成具体检索问题，更新已有笔记。
- **生成 Obsidian 笔记**：包含 Markdown、YAML 属性、内部链接、标签、Paper Card 和补读队列。

## 保留的研究结构

批判性分析和研究机会围绕以下主干展开：

```text
一个研究题目
1. Motivation
   1.1 动机相关
       论文 A：问题、为何重要、缺口、贡献、与本题目的关系
       论文 B：……
   1.2 理论基础
       来源、构念、假设、机制、适用边界
2. 研究内容及其相关工作
   2.1 可能的研究内容一
       ① 本研究方向的小 motivation 论文
       ② 具体内容
   2.2 可能的研究内容二
       ① 本研究方向的小 motivation 论文
       ② 具体内容
   ……证据允许时，尽量展开至五个有区别的方向
```

理论论文重点讲构念、机制、理论发展和边界；方法论文需要具体解释数学或操作流程，并检查实验证据。非机器学习领域按其学科方法调整，不强行套用训练集和 loss 等概念。

## 在 Codex 中安装

### 方法一：让 skill-installer 安装

在 Codex 中发送：

```text
$skill-installer 请从以下仓库安装 skill：
https://github.com/Wangmou1234/research-literature-analyst
使用仓库根目录（path .），安装名称为 research-literature-analyst。
```

### 方法二：克隆到本地 skills 目录

两种安装方式选一种即可。手动安装时，当前 Codex 官方文档列出的用户级目录为 `~/.agents/skills`；内置安装器可能采用当前环境配置的 skills 目录，不需要为覆盖不同路径而重复安装。参见 [OpenAI 官方 skill 文档](https://learn.chatgpt.com/docs/build-skills)。

**Windows / PowerShell**

```powershell
$skillRoot = Join-Path $HOME '.agents\skills'
New-Item -ItemType Directory -Path $skillRoot -Force | Out-Null
git clone https://github.com/Wangmou1234/research-literature-analyst.git (Join-Path $skillRoot 'research-literature-analyst')
```

**macOS / Linux**

```bash
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/Wangmou1234/research-literature-analyst.git "$HOME/.agents/skills/research-literature-analyst"
```

安装后可用 `$research-literature-analyst` 调用；未出现时重启 Codex。本仓库由说明和模板组成，无需安装额外依赖包。

## 使用方法

skill 指令和模板使用中文，默认也输出中文。需要英文笔记时，在请求中明确写“所有解释和笔记标题使用英文”。

### 1. 围绕一个题目开始调研

```text
请使用 $research-literature-analyst 调研【研究主题】。
我的核心科学问题是【问题】。
种子论文是【论文链接、DOI 或本地文件路径】。
输出到【笔记目录或 Obsidian vault 路径】。
保留 Motivation 和研究内容两大部分，尽量形成五个有区别的研究方向，
深入解释核心方法及其实验结果。
```

可以只提供题目或论文开始。具体问题、种子论文、研究范围和输出路径有助于聚焦；未指定 vault 时，默认在当前工作目录创建 `research-notes/<主题短名>/`。

### 2. 精读一篇论文

```text
请使用 $research-literature-analyst 精读【论文链接或本地 PDF 路径】。
解释关键公式、符号、设计理由、训练或求解过程，
以及实验证据如何支撑论文结论。
需要包含 baseline、具体数值、消融与局限。
把笔记关联到【现有研究笔记目录】中的主题。
```

### 3. 哪里不够，就继续补查

```text
请使用 $research-literature-analyst 更新【研究笔记目录】。
第 2.2 部分理论依据不够，与最接近方法的比较也不清楚。
请继续检索、查阅并更新原笔记，说明哪些结论发生变化，
还有哪些证据缺口没有解决。
```

只希望分析自己的材料时，加一句：“仅使用我提供的文件，不联网检索。”

## Obsidian 输出

```text
research-notes/<主题短名>/
├── 00-研究地图.md
├── 01-Papers/                    # 独立论文笔记
├── 02-Directions/                # 研究方向
├── 03-Concepts/                  # 可复用的理论、方法和数据节点
└── 90-补读与检索记录.md
```

可以把生成的目录作为 Obsidian vault 打开，也可以让 skill 直接写入现有 vault。已有命名约定优先，也可要求使用英文文件名。无需社区插件。

`assets/` 中是供 agent 填写的模板，不是已完成的文献笔记或可执行脚本。生成笔记时，应替换其中的 `{{...}}` 占位符。

## 证据与阅读深度

每篇论文记录实际阅读范围：`metadata-only`、`abstract-only`、`partial-full-text` 或 `full-text`；附录和代码是否查阅单独说明。

关键结论和数值应能定位到原文章节、公式、图或表。缺失信息分别标为“未报告”“未查到”“无法访问”或“不适用”。拟议实验明确标为研究设想。

联网检索和 PDF 检查取决于运行环境提供的工具，以及原始材料的可访问性。只读摘要时不能达到全文精读的细节水平；生成的研究判断仍需要研究者审阅。

## 仓库内容

| 文件 | 用途 |
| --- | --- |
| [SKILL.md](SKILL.md) | 主流程与研究框架 |
| [agents/openai.yaml](agents/openai.yaml) | Codex 展示信息与默认提示词 |
| [references/reading-depth.md](references/reading-depth.md) | 理论、方法、实验与审稿分析要求 |
| [references/search-and-update.md](references/search-and-update.md) | 检索、引用追踪和增量更新 |
| [references/obsidian-format.md](references/obsidian-format.md) | 目录、属性、命名和链接约定 |
| [assets/topic-map.md](assets/topic-map.md) | 研究地图模板 |
| [assets/paper-note.md](assets/paper-note.md) | 单篇论文模板 |
| [assets/direction-note.md](assets/direction-note.md) | 研究方向模板 |
| [assets/concept-note.md](assets/concept-note.md) | 理论、方法或数据节点模板 |
| [assets/reading-queue.md](assets/reading-queue.md) | 补读与检索记录模板 |

## 更新通过 Git 安装的 skill

进入已安装的 skill 目录，运行 `git pull --ff-only`。如果自己修改过 skill，请先检查并保留本地修改，再更新。

## 参考做法与验证状态

检索记录借鉴了 [PRISMA 2020](https://www.prisma-statement.org/prisma-2020-checklist) 和 [PRISMA-S](https://www.prisma-statement.org/prisma-search) 的报告做法，不代表每次输出都完成了完整系统综述流程。笔记格式参考 Obsidian 官方的 [内部链接](https://help.obsidian.md/links) 和 [属性说明](https://help.obsidian.md/properties)。

初始版本已通过 skill 格式、模板 YAML 和本地资源链接检查，尚未进行完整真实论文调研的效果评估。
