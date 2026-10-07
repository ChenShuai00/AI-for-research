<div align="center">

# Awesome AI for Research

**科研 Agent Skills 中文精选**

从文献、选题、数据到论文与实验，一份有来源、有版本、可继续维护的科研技能导航。

![Skills](https://img.shields.io/badge/Skills-88-0969da?style=flat-square)
![Sources](https://img.shields.io/badge/Source_Repos-7-8250df?style=flat-square)
![Checked](https://img.shields.io/badge/Checked-2026-10-07-1a7f37?style=flat-square)
![Language](https://img.shields.io/badge/Language-中文-blue?style=flat-square)

[完整技能表](docs/skills.md) · [按任务选择](#choose) · [来源仓库](#sources) · [使用指南](docs/getting-started.md) · [贡献条目](CONTRIBUTING.md)

</div>

---

> 检索与核验日期：**2026-10-07（北京时间）**。收录 **80 项高关注来源技能 + 8 项新兴学术工作流**。Star 来自本次 GitHub 查询；分类与推荐按科研任务整理。

## 这份清单提供什么

本仓库整理可被 AI Agent 加载的 **Skills**：以 `SKILL.md` 为入口的任务说明、参考资源和辅助脚本。适合用 Codex、Claude Code 或其他兼容宿主处理科研任务的研究者；每项兼容性与依赖见上游。[Agent Skills 标准](https://agentskills.io/home)

每个技能都在 [完整技能表](docs/skills.md) 中占一行，包含用途、来源仓库、仓库 Star、依赖和固定版本链接。当前 **88/88 项**来源文件已完成读取和名称核对；本次整理没有进行技能运行效果评测。筛选规则见 [检索与核验方法](docs/methodology.md)。

<a id="choose"></a>

## 按科研任务选择

| 你正在做什么 | 去哪里找 | 高关注来源条数 |
| --- | --- | ---: |
| 📚 文献检索与引用 | [查看技能表](docs/skills.md#literature) | 9 |
| 💡 选题与研究设计 | [查看技能表](docs/skills.md#ideation) | 6 |
| ✍️ 写作、审稿与成果整理 | [查看技能表](docs/skills.md#writing) | 6 |
| 📊 数据整理与统计分析 | [查看技能表](docs/skills.md#data) | 14 |
| 🎨 科研绘图与学术展示 | [查看技能表](docs/skills.md#figures) | 8 |
| 🧠 模型训练与微调 | [查看技能表](docs/skills.md#training) | 9 |
| 🧪 评估、解释与实验记录 | [查看技能表](docs/skills.md#evaluation) | 9 |
| ⚙️ 科学计算与算力工具 | [查看技能表](docs/skills.md#compute) | 12 |
| 🌍 学科专用数据分析 | [查看技能表](docs/skills.md#domain) | 3 |
| 📄 PDF、Word、PPT 与工作簿 | [查看技能表](docs/skills.md#documents) | 4 |
| 🌱 学术方法与复现流程的新项目 | [新兴候选](docs/skills.md#emerging) | 8 项另列 |

## 先从这 12 项开始

这 12 项覆盖常见研究环节。推荐依据是任务适配；每项 Star 仍对应整个仓库。

| Skill | 适用任务 | 来源 / 仓库 Star | 主要依赖与条件 | 核验 |
| --- | --- | --- | --- | --- |
| [`literature-review`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/literature-review/SKILL.md) | 组织系统综述、范围综述或叙述综述的检索、筛选与证据整理流程。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | Python 3.10+、requests、联网；PDF 导出需 Pandoc/XeLaTeX；可选 AI 绘图需密钥。 | 来源已核验 |
| [`huggingface-papers`](https://github.com/huggingface/skills/blob/ca0325bb20b2d0a1b2efa893670c4c72f79e707b/skills/huggingface-papers/SKILL.md) | 读取论文 Markdown 和结构化元数据，并查找关联代码、模型及数据集。 | [HF](https://github.com/huggingface/skills) · ⭐ 11,145 | HF Papers HTTP API；公开论文页面免认证；部分接口需令牌。 | 来源已核验 |
| [`citation-management`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/citation-management/SKILL.md) | 核对参考文献元数据，检索学术记录，并把 DOI 或论文信息整理为 BibTeX。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | Python 3.9+、requests、联网；Google Scholar 路径另需 scholarly；部分 API 密钥可选。 | 来源已核验 |
| [`Zotero`](https://github.com/openai/plugins/blob/5fd93af4cd0c623e020d0cc7e9ce178b4ac1f70f/plugins/zotero/skills/zotero/SKILL.md) | 检索本地 Zotero 文献库，导出 BibTeX 并维护论文中的引用键。 | [OA](https://github.com/openai/plugins) · ⭐ 7,335 | Zotero Desktop 本地 API；Python；导入操作按连接器配置。 | 来源已核验 |
| [`hypothesis-generation`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/hypothesis-generation/SKILL.md) | 把观察结果转化为可检验的假说、竞争解释、区分性预测与研究计划。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | 可选本地脚本需 Python 3.11+ 标准库；这些脚本无需联网、模型调用或密钥。 | 来源已核验 |
| [`scientific-writing`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scientific-writing/SKILL.md) | 起草和修订论文正文、声明与报告，并核对论断来源及文稿内部一致性。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | 核心写作指导无额外依赖；可选离线检查脚本需 Python 3.11+。 | 来源已核验 |
| [`peer-review`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/peer-review/SKILL.md) | 依据稿件证据评估研究方法、统计、可复现性和论断，生成建设性的审稿草稿。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | 可选本地脚本需 Python 3.11+ 标准库；无需联网或 API 密钥。 | 来源已核验 |
| [`statistical-analysis`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/statistical-analysis/SKILL.md) | 根据研究问题选择统计检验，检查假设，并报告效应量、区间与结果解释。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | Python 3.12+、SciPy、statsmodels、pingouin、pandas 等；贝叶斯扩展另需 PyMC/ArviZ。 | 来源已核验 |
| [`scientific-visualization`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scientific-visualization/SKILL.md) | 设计和审查投稿用多面板科研图，检查数据表达、配色、图像元数据与导出格式。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | Python 3.11+、uv；按需使用 Matplotlib/Pillow/pypdf；Plotly 静态导出另需 Kaleido 和 Chrome。 | 来源已核验 |
| [`jupyter-notebooks`](https://github.com/openai/plugins/blob/5fd93af4cd0c623e020d0cc7e9ce178b4ac1f70f/plugins/data-analytics/skills/jupyter-notebooks/SKILL.md) | 创建、整理和运行可复现的 Python/SQL Notebook，保留分析过程与核验记录。 | [OA](https://github.com/openai/plugins) · ⭐ 7,335 | Python/SQL 环境；nbformat、nbclient 或 Jupyter；宿主工具按工作流配置。 | 来源已核验 |
| [`huggingface-llm-trainer`](https://github.com/huggingface/skills/blob/ca0325bb20b2d0a1b2efa893670c4c72f79e707b/skills/huggingface-llm-trainer/SKILL.md) | 规划 TRL/Unsloth 微调流程，覆盖数据检查、训练方法、算力选择和结果保存。 | [HF](https://github.com/huggingface/skills) · ⭐ 11,145 | HF Jobs、TRL/Unsloth、Trackio；Jobs 付费计划与写权限令牌。 | 来源已核验 |
| [`evaluating-llms-harness`](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/11-evaluation/lm-evaluation-harness/SKILL.md) | 用统一的任务与指标评估语言模型，并比较模型版本或训练阶段。 | [OR](https://github.com/Orchestra-Research/AI-Research-SKILLs) · ⭐ 13,327 | lm-eval、transformers；vLLM 为上游列出的推理后端。 | 来源已核验 |

<a id="sources"></a>

## 来源仓库与关注度

按本次查询的仓库 Star 降序排列。单项技能顺序按科研流程编排。

| 来源仓库 | Star 快照 | 科研定位 | 本清单条数 | 最近推送 UTC | 状态 |
| --- | ---: | --- | ---: | --- | --- |
| [anthropics/skills](https://github.com/anthropics/skills) | 180,017 | Claude 官方文档 | 4 | 2026-10-05 | 高关注来源；近 90 天有推送 |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 47,872 | 跨学科科研 | 34 | 2026-10-05 | 高关注来源；近 90 天有推送 |
| [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) | 13,327 | AI 研究工程 | 25 | 2026-06-16 | 高关注来源；超过 90 天未推送 |
| [huggingface/skills](https://github.com/huggingface/skills) | 11,145 | Hugging Face 官方 | 10 | 2026-10-01 | 高关注来源；近 90 天有推送 |
| [openai/plugins](https://github.com/openai/plugins) | 7,335 | Codex 官方插件 | 7 | 2026-09-28 | 高关注来源；近 90 天有推送 |
| [VincenzoImp/academic-research-skills](https://github.com/VincenzoImp/academic-research-skills) | 3 | 学术工作流新项目 | 4 | 2026-08-25 | 新兴候选；近 90 天有推送 |
| [jjfroehlich/agent-skills-for-academic-research](https://github.com/jjfroehlich/agent-skills-for-academic-research) | 1 | 学术方法新项目 | 4 | 2026-08-28 | 新兴候选；近 90 天有推送 |

K-Dense 已从 `claude-scientific-skills` 更名为 `scientific-agent-skills`。Orchestra 的实际目录有 98 个技能，部分 README 说明仍写 87。`openai/skills` 已标注弃用，官方来源改收 `openai/plugins`。上述变化与固定提交均记录在 [来源记录](docs/sources.md)。

## 典型使用路径

| 场景 | 可组合的技能 | 给 Agent 的任务示例 |
| --- | --- | --- |
| 初步了解研究方向 | `literature-review` → `citation-management` → `hypothesis-generation` | “检索这个主题的代表性研究，核对 DOI，整理共识、分歧和可检验的问题。” |
| 做可复现的定量分析 | `analyze-data-quality` → `jupyter-notebooks` → `statistical-analysis` → `scientific-visualization` | “先检查样本、缺失和变量口径，再保留可运行分析与绘图代码。” |
| 完成稿件与组会材料 | `scientific-writing` → `peer-review` → `scientific-slides` / `pptx` | “根据提供的结果修订稿件，逐条核对主张与证据，再制作组会汇报。” |
| 开展语言模型实验 | `huggingface-datasets` → `peft-fine-tuning` → `huggingface-community-evals` → `huggingface-trackio` | “检查数据划分，规划微调与评估，记录参数、指标和结果文件。” |

## 仓库结构

```text
AI-for-research/
├── README.md                     # GitHub 风格首页与精选入口
├── CONTRIBUTING.md               # 收录与更新规则
├── CHANGELOG.md                   # 版本记录
├── docs/
│   ├── skills.md                  # 每个 skill 一行的完整表格
│   ├── sources.md                 # 固定提交、维护状态与来源
│   ├── methodology.md             # 热门口径、检索方法与核验边界
│   └── getting-started.md         # 选择与使用指南
├── data/
│   ├── skills.json                # 中文精选条目
│   ├── sources.json               # 仓库热度与版本快照
│   ├── verification.json          # 文件访问、名称与哈希核验
│   ├── *_candidates.json          # 各来源的精选输入
│   └── *_source_snapshot.json     # 检索与版本证据
├── scripts/
│   ├── assemble_catalog.py        # 整合来源输入，离线运行
│   ├── build_catalog.py           # 从 JSON 生成 Markdown
│   ├── verify_catalog.py          # 检查表格与固定版本来源
│   └── refresh_sources.py         # 查询上游新快照，供人工比较
└── .github/ISSUE_TEMPLATE/        # 推荐技能与失效链接反馈
```

## 本地更新

需要 Python 3.10+；脚本只使用标准库。维护条目后，可离线重新生成并检查：

```bash
python scripts/build_catalog.py
python scripts/verify_catalog.py
```

变更来源或提交版本时，先执行 `python scripts/verify_catalog.py --online`，再生成并离线检查 Markdown。查询新的上游元数据：`python scripts/refresh_sources.py`，结果写入独立的 `data/upstream-refresh.json`，由维护者比较后再更新精选条目。GitHub 公共 API 有配额限制，脚本支持 `GITHUB_TOKEN` 环境变量；失败时保留原快照。

## 贡献与许可

欢迎按 [贡献规则](CONTRIBUTING.md) 推荐新技能、修复路径或补充依赖。所有上游技能保留各自许可；尤其 Anthropic 文档技能为专有许可可见源码，使用与再分发需查看各目录的 `LICENSE.txt`。[Anthropic 官方说明](https://github.com/anthropics/skills)

原有 [科研工作区初始化提示词](AI科研工作建立_prompt.md) 保留，可配合本清单建立研究目录。
