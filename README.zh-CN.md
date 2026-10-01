<p align="center">
  <img src="docs/images/logo.png" alt="科研文献阅读与研究地图标志" width="128">
</p>

# 科研文献阅读与研究地图

[English](README.md) | [简体中文](README.zh-CN.md)

一个用于博士阶段论文精读、基于证据的研究综合，以及持续维护 Obsidian 文献库的 Codex skill。

![论文解析、理论梳理、方法拆解、批判性阅读和研究图谱](docs/images/overview.zh-CN.png)

## 从单次总结到持续研究综合

单篇总结解释一份来源。本工作流围绕研究问题持续积累：记录阅读覆盖、定位证据、区分报告与推断、比较文献、核查空白，并根据新证据更新研究地图。

主结构保留 **1. Motivation → 1.1 动机相关论文 → 1.2 理论基础**，以及 **2. 研究内容及其相关工作**；证据支持时尽量形成约五个有区别的方向。每个方向仍包含 **① 本方向的小 motivation 论文** 和 **② 具体研究内容**。

## 示例与输出

查看[心理学](examples/psychology/README.md)、[机器学习](examples/machine-learning/README.md)和[跨学科研究](examples/interdisciplinary/README.md)示例。这些是 illustrative/synthetic 指南，并非已完成的真实论文调研。目前没有真实执行 GIF 或 Obsidian 截图。

每个示例包含一份可导航的小型合成 vault。真实执行与 Obsidian 展示请按 [demo 录制指南](docs/demo/README.md)采集，首页没有嵌入不存在的截图。

## 核心能力

- 从构念、假设、机制与边界理解理论。
- 深入解释方法、公式、设计选择与实验。
- 在明确条件下比较支持和挑战性证据。
- 维护带范围的 Claim 节点、适配学科的证据矩阵与冲突分析。
- 主动证伪候选空白，再判断它能否成为研究机会。
- 把反馈转成定向检索，更新已有笔记。
- 将研究设想落实为假设、最小研究与失败标准。

## 安装

在 Codex 中发送：

```text
$skill-installer 请安装 https://github.com/FaFaGPT/research-literature-analyst
使用 path .，安装名称为 research-literature-analyst。
```

手动安装到 `~/.agents/skills/research-literature-analyst` 的命令见 [Windows、macOS 与 Linux 使用指南](docs/usage.md)。选择一种方式即可。使用 skill 本身无需安装依赖包。

## 使用

```text
请使用 $research-literature-analyst 调研【研究问题】。
材料：【论文链接、DOI 或本地文件】。
输出到【笔记目录或 Obsidian vault】。
保留 Motivation 和研究方向主结构，解释核心方法、实验和证据边界。
```

继续阅读时可以说：“第 2.2 部分理论不够，查找反证，更新原笔记，说明结论有哪些变化。”更多[主题调研、单篇精读和更新提示词](docs/usage.md)见使用指南。

指令和模板使用中文，默认中文输出；明确要求时使用英文。检索和 PDF 检查取决于运行环境提供的工具与来源可访问性。

## Obsidian 结构

```text
research-notes/<主题短名>/
├── 00-研究地图.md
├── 01-Papers/
├── 02-Directions/
├── 03-Concepts/
├── 04-Claims/
├── 05-Evidence/
└── 90-补读与检索记录.md
```

可作为独立 vault 打开，也可写入已有库。默认使用 Markdown、YAML 和内部链接，无需 Dataview、Templater 或 Zotero。参见[目录与链接规则](references/obsidian-format.md)。

## 证据模型

实际阅读覆盖保留 `metadata-only`、`abstract-only`、`partial-full-text`、`full-text`；附录和代码单独记录。关键判断和数值需要原文定位，论文报告、推断与研究假设分开写，缺失信息明确保留。

`reading_priority`（Tier A–D）决定阅读投入，与实际覆盖分开；核心论文全文不可得时仍可处于 abstract-only。Claim 区分 `paper-reported`、`cross-paper-synthesis`、`analyst-inference`、`research-hypothesis`；证据充分性用 strong、moderate、limited、conflicting、insufficient evidence 作定性说明。参见 [Claim、矩阵与冲突分析规则](references/evidence-synthesis.md)。

## 评测

[五类 benchmark 协议](benchmarks/README.md)覆盖精读、综合、空白核查、增量更新和 Obsidian 生成。自动检查关注结构；专家评审关注证据与结论是否一致、数值、方法理解及科研用途。

**目前没有真实论文 benchmark 结果。** 合成示例和验证脚本测试不能证明科研分析准确率。

```bash
python -m pip install -r scripts/requirements.txt
python scripts/validate_templates.py
python scripts/validate_links.py
python -m unittest discover -s scripts/tests -v
python scripts/validate_vault.py path/to/vault
```

仅运行验证时需要 Python 和 PyYAML。具体边界见[评测说明](benchmarks/README.md)。

## 仓库结构

| 位置 | 用途 |
| --- | --- |
| [SKILL.md](SKILL.md)、[agents/](agents/) | 主流程与 Codex 信息 |
| [assets/](assets/)、[references/](references/) | 模板与详细阅读规则 |
| [examples/](examples/) | 领域指南与明确标注的示例 |
| [benchmarks/](benchmarks/) | 任务、量表与结果报告 |
| [scripts/](scripts/) | 离线验证脚本和回归测试 |
| [docs/](docs/) | 使用与展示资料 |

采用 MIT 许可证，见 [LICENSE](LICENSE)。检索报告参考 [PRISMA-S](https://www.prisma-statement.org/prisma-search)，使用本 skill 不代表完成了完整系统综述。通过 Git 安装后，可在保留本地修改的前提下用 `git pull --ff-only` 更新。

[贡献指南](CONTRIBUTING.md) · [变更记录](CHANGELOG.md) · [引用信息](CITATION.cff) · [仓库设置建议](docs/repository-setup.md)
