# 如何选择与使用科研 Skills

[← 返回首页](../README.md) · [完整技能表](skills.md) · [来源记录](sources.md)

## 按当前任务选一组

| 研究任务 | 建议入口 | 需要先准备的材料 |
| --- | --- | --- |
| 找论文与整理文献 | `literature-review`、`paper-lookup`、`huggingface-papers` | 研究范围、关键词、时间范围与纳入标准 |
| 管理 DOI 与引用 | `citation-management`、`pyzotero`、OpenAI `Zotero` | 已有文献库、引用格式、需要修改的稿件 |
| 形成研究问题 | `hypothesis-generation`、`experimental-design`、`brainstorming-research-ideas` | 已有证据、待解释现象、资源与方法约束 |
| 清洗与统计分析 | `exploratory-data-analysis`、`statistical-analysis`、`statsmodels`、`pymc` | 原始数据、变量说明、分析单位与预设问题 |
| 画投稿图表 | `scientific-visualization`、`matplotlib`、`seaborn`、`academic-plotting` | 数据、图形目的、面板设计与期刊尺寸 |
| 写论文与改稿 | `scientific-writing`、`ml-paper-writing`、`peer-review` | 作者提供的真实结果、文献、原稿及目标期刊 |
| 做模型实验 | `peft-fine-tuning`、`huggingface-llm-trainer`、`huggingface-community-evals` | 数据划分、模型许可、硬件预算与评估方案 |
| 保存实验与汇报 | `huggingface-trackio`、`mlflow`、`scientific-slides`、`pptx` | 实验配置、指标、图表与听众需求 |

同名技能先看来源，例如 K-Dense 与 jjfroehlich 均提供 `scientific-writing`。前者位于高关注来源区，后者位于新兴区，流程与参考资源可能不同。

## 安装入口

安装由自己的 Agent 宿主与上游说明决定。表格里的名称链接固定到本次核验版本，可先阅读其 `SKILL.md`、配套资源和许可；需要最新版本时，再打开来源仓库对比变化。

| 来源 | 官方安装或使用说明 | 适用条件 |
| --- | --- | --- |
| K-Dense | [Getting Started](https://github.com/K-Dense-AI/scientific-agent-skills#-getting-started) | 支持 Agent Skills 的宿主；按任务选择所需技能 |
| Orchestra | [安装器 README](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/main/packages/ai-research-skills/README.md) | AI 实验工程工作流；GPU、框架与运行预算按具体技能配置 |
| Hugging Face | [官方技能仓库](https://github.com/huggingface/skills) | 部分操作依赖 HF 账户、令牌、Jobs 与付费算力 |
| Anthropic | [官方技能仓库](https://github.com/anthropics/skills#try-in-claude-code-claudeai-and-the-api) | Claude 的官方安装途径；文档技能逐项查看许可 |
| OpenAI | [当前插件示例库](https://github.com/openai/plugins) | 通过宿主插件机制使用；连接器依赖按各插件配置 |
| 新兴学术工作流 | [VA](https://github.com/VincenzoImp/academic-research-skills)、[JA](https://github.com/jjfroehlich/agent-skills-for-academic-research) | 先适配目录、文献服务和工作流约定，再用小任务验证 |

这里提供发现与核验记录。本次整理未安装技能；具体安装命令与路径使用上游和宿主的当前说明。

## 给 Agent 的任务描述

把问题、输入、预期输出和核验方式写清楚。以下文本可作为起点，按自己的研究替换内容。

```text
使用 literature-review 与 citation-management。
研究主题：<主题>；时间范围：<年份>；领域：<领域>。
输出：带 DOI/原文链接的文献矩阵，列出方法、样本、结论和局限。
记录：检索词、检索日期、来源与纳入/排除理由。
无法核实的文献明确标记；关键观点回到论文原文核对。
```

```text
使用 jupyter-notebooks、statistical-analysis 与 scientific-visualization。
输入：<数据路径> 和 <变量说明>；分析单位：<单位>。
问题：<预设问题>；输出：可运行 Notebook、统计表与图形生成脚本。
先检查样本、缺失、重复和变量口径，再执行分析。
报告实际运行结果、方法假设、不确定性以及输入文件版本。
```

```text
使用 scientific-writing 与 peer-review。
输入：<原稿>、<真实结果>、<已核实文献>；目标期刊：<期刊>。
根据现有证据修订论证和段落，并提供修改理由。
区分作者结果、文献证据和待验证推断，逐条检查主张与引用。
```

## 做一次小任务验证

先选一个规模可控的真实任务，例如核对 5 条参考文献、检查一张表的缺失值，或重画一幅已有图。记录使用的仓库版本、输入文件、Agent 输出和人工复核结果，再决定是否把该技能用于完整项目。

长期项目可以使用原有的 [科研工作区初始化提示词](../AI科研工作建立_prompt.md)，将文献、原始数据、处理代码和 AI 使用记录放在明确目录中。
