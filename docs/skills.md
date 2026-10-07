# 科研 Skills 完整清单

核验日期：**2026-10-07（北京时间）** · **88 项精选 / 7 个来源仓库**。

[← 返回首页](../README.md) · [筛选口径](methodology.md) · [使用指南](getting-started.md) · [源数据](../data/skills.json)

> 每行对应一个真实的 `SKILL.md`，技能名使用上游 frontmatter；同名技能保留来源区分。名称链接固定到本次核验的提交版本。

> Star 为整个来源仓库的累计关注度，不能解释为单项 skill 的使用量或近期增速。来源核验覆盖文件可访问性、名称和哈希；运行效果需要在自己的环境验证。

## 导航

- [📚 文献检索与引用 · 9 项](#literature)
- [💡 选题与研究设计 · 6 项](#ideation)
- [✍️ 写作、审稿与成果整理 · 6 项](#writing)
- [📊 数据整理与统计分析 · 14 项](#data)
- [🎨 科研绘图与学术展示 · 8 项](#figures)
- [🧠 模型训练与微调 · 9 项](#training)
- [🧪 评估、解释与实验记录 · 9 项](#evaluation)
- [⚙️ 科学计算与算力工具 · 12 项](#compute)
- [🌍 学科专用数据分析 · 3 项](#domain)
- [📄 PDF、Word、PPT 与工作簿 · 4 项](#documents)
- [🌱 新兴学术工作流 · 8 项](#emerging)

## 来源缩写

| 缩写 | 来源仓库 | 本清单条数 | 类型 | 维护状态 |
| --- | --- | --- | --- | --- |
| AN | [anthropics/skills](https://github.com/anthropics/skills) | 4 | 高关注来源 | 近 90 天有推送 |
| KD | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 34 | 高关注来源 | 近 90 天有推送 |
| OR | [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) | 25 | 高关注来源 | 超过 90 天未推送 |
| HF | [huggingface/skills](https://github.com/huggingface/skills) | 10 | 高关注来源 | 近 90 天有推送 |
| OA | [openai/plugins](https://github.com/openai/plugins) | 7 | 高关注来源 | 近 90 天有推送 |
| VA | [VincenzoImp/academic-research-skills](https://github.com/VincenzoImp/academic-research-skills) | 4 | 新兴候选 | 近 90 天有推送 |
| JA | [jjfroehlich/agent-skills-for-academic-research](https://github.com/jjfroehlich/agent-skills-for-academic-research) | 4 | 新兴候选 | 近 90 天有推送 |

<a id="literature"></a>

## 📚 文献检索与引用

| Skill | 适用任务 | 来源 / 仓库 Star | 主要依赖与条件 | 核验 |
| --- | --- | --- | --- | --- |
| [`paper-lookup`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/paper-lookup/SKILL.md) | 通过多个学术数据库查找论文、DOI、引文关系及开放获取全文，并保留查询来源。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | 联网、curl；本地脚本需 Python 3.11+；部分 API 密钥可提高额度或获取全文。 | 来源已核验 |
| [`literature-review`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/literature-review/SKILL.md) | 组织系统综述、范围综述或叙述综述的检索、筛选与证据整理流程。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | Python 3.10+、requests、联网；PDF 导出需 Pandoc/XeLaTeX；可选 AI 绘图需密钥。 | 来源已核验 |
| [`citation-management`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/citation-management/SKILL.md) | 核对参考文献元数据，检索学术记录，并把 DOI 或论文信息整理为 BibTeX。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | Python 3.9+、requests、联网；Google Scholar 路径另需 scholarly；部分 API 密钥可选。 | 来源已核验 |
| [`research-lookup`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/research-lookup/SKILL.md) | 为论文或研究简报搜集当前文献，整理支持证据、冲突发现与来源对应关系。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | Python 3.10+、parallel-web-tools、联网与 Parallel 登录或密钥；可选 Perplexity 路径需 OpenRouter 密钥。 | 来源已核验 |
| [`pyzotero`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/pyzotero/SKILL.md) | 使用 Python 查询 Zotero 文献库、整理条目和合集，并支持引文导出等自动化工作。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | Python 3.10+、pyzotero；远程私有读取或写入需 Zotero API 密钥；本地读取需开启 Zotero 本地 API。 | 来源已核验 |
| [`database-lookup`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/database-lookup/SKILL.md) | 按明确的数据库、查询条件和分页规则获取科学数据，并记录可追溯的检索证据。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | 联网及 curl 或其他 HTTP 客户端；密钥、许可与访问额度取决于目标数据库。 | 来源已核验 |
| [`huggingface-papers`](https://github.com/huggingface/skills/blob/ca0325bb20b2d0a1b2efa893670c4c72f79e707b/skills/huggingface-papers/SKILL.md) | 读取论文 Markdown 和结构化元数据，并查找关联代码、模型及数据集。 | [HF](https://github.com/huggingface/skills) · ⭐ 11,145 | HF Papers HTTP API；公开论文页面免认证；部分接口需令牌。 | 来源已核验 |
| [`Zotero`](https://github.com/openai/plugins/blob/5fd93af4cd0c623e020d0cc7e9ce178b4ac1f70f/plugins/zotero/skills/zotero/SKILL.md) | 检索本地 Zotero 文献库，导出 BibTeX 并维护论文中的引用键。 | [OA](https://github.com/openai/plugins) · ⭐ 7,335 | Zotero Desktop 本地 API；Python；导入操作按连接器配置。 | 来源已核验 |
| [`ncbi-pmc-skill`](https://github.com/openai/plugins/blob/5fd93af4cd0c623e020d0cc7e9ce178b4ac1f70f/plugins/life-science-research/skills/ncbi-pmc-skill/SKILL.md) | 查询 PMC 开放获取文章的文件可用性与元数据，整理简洁的检索结果。 | [OA](https://github.com/openai/plugins) · ⭐ 7,335 | Python 配套脚本；NCBI PMC OA 网络接口。 | 来源已核验 |

<a id="ideation"></a>

## 💡 选题与研究设计

| Skill | 适用任务 | 来源 / 仓库 Star | 主要依赖与条件 | 核验 |
| --- | --- | --- | --- | --- |
| [`scientific-critical-thinking`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scientific-critical-thinking/SKILL.md) | 分析研究设计、偏倚、混杂及统计解释，判断科学论断得到多强的证据支持。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | 核心分析指导可离线使用；可选 AI 示意图需 OpenRouter 密钥与联网。 | 来源已核验 |
| [`hypothesis-generation`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/hypothesis-generation/SKILL.md) | 把观察结果转化为可检验的假说、竞争解释、区分性预测与研究计划。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | 可选本地脚本需 Python 3.11+ 标准库；这些脚本无需联网、模型调用或密钥。 | 来源已核验 |
| [`experimental-design`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/experimental-design/SKILL.md) | 在收集数据前规划随机化、分组、区组与因子设计，使研究问题和独立实验单位一致。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | Python 3.12+、NumPy、pandas、pydoe；安装后计算可离线，无需密钥。 | 来源已核验 |
| [`autoresearch`](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/0-autoresearch-skill/SKILL.md) | 围绕实验迭代与结果综合管理研究项目，并将具体任务路由到各领域技能。 | [OR](https://github.com/Orchestra-Research/AI-Research-SKILLs) · ⭐ 13,327 | 上游未声明固定包；需具备项目读写能力的编码代理。 | 来源已核验 |
| [`brainstorming-research-ideas`](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/21-research-ideation/brainstorming-research-ideas/SKILL.md) | 使用结构化选题框架把初步兴趣转化为可讨论的研究方向与问题。 | [OR](https://github.com/Orchestra-Research/AI-Research-SKILLs) · ⭐ 13,327 | 上游声明无额外包依赖。 | 来源已核验 |
| [`creative-thinking-for-research`](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/21-research-ideation/creative-thinking-for-research/SKILL.md) | 通过类比、组合与约束重构等思考方法寻找研究问题的新角度。 | [OR](https://github.com/Orchestra-Research/AI-Research-SKILLs) · ⭐ 13,327 | 上游声明无额外包依赖。 | 来源已核验 |

<a id="writing"></a>

## ✍️ 写作、审稿与成果整理

| Skill | 适用任务 | 来源 / 仓库 Star | 主要依赖与条件 | 核验 |
| --- | --- | --- | --- | --- |
| [`scientific-writing`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scientific-writing/SKILL.md) | 起草和修订论文正文、声明与报告，并核对论断来源及文稿内部一致性。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | 核心写作指导无额外依赖；可选离线检查脚本需 Python 3.11+。 | 来源已核验 |
| [`peer-review`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/peer-review/SKILL.md) | 依据稿件证据评估研究方法、统计、可复现性和论断，生成建设性的审稿草稿。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | 可选本地脚本需 Python 3.11+ 标准库；无需联网或 API 密钥。 | 来源已核验 |
| [`research-grants`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/research-grants/SKILL.md) | 结合具体资助项目要求组织研究目标、评审要点、预算与申请书检查清单。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | 联网核验最新机构指南，或提供带日期的官方文件；可选 AI 绘图需 OpenRouter 密钥。 | 来源已核验 |
| [`ml-paper-writing`](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/20-ml-paper-writing/ml-paper-writing/SKILL.md) | 从研究材料组织机器学习论文论证，辅助引文核验与会议投稿准备。 | [OR](https://github.com/Orchestra-Research/AI-Research-SKILLs) · ⭐ 13,327 | semanticscholar、arxiv、habanero、requests；排版按需使用 LaTeX。 | 来源已核验 |
| [`huggingface-paper-publisher`](https://github.com/huggingface/skills/blob/ca0325bb20b2d0a1b2efa893670c4c72f79e707b/skills/huggingface-paper-publisher/SKILL.md) | 把 arXiv 论文页面与模型、数据集关联，整理研究成果的引用和元数据。 | [HF](https://github.com/huggingface/skills) · ⭐ 11,145 | uv 与配套 Python 脚本；写权限 HF_TOKEN。 | 来源已核验 |
| [`build-report`](https://github.com/openai/plugins/blob/5fd93af4cd0c623e020d0cc7e9ce178b4ac1f70f/plugins/data-analytics/skills/build-report/SKILL.md) | 把已完成的分析组织成带图表、来源和限制说明的可交付报告。 | [OA](https://github.com/openai/plugins) · ⭐ 7,335 | 已核验分析；宿主报告/文档输出工具；部分流程依赖连接器。 | 来源已核验 |

<a id="data"></a>

## 📊 数据整理与统计分析

| Skill | 适用任务 | 来源 / 仓库 Star | 主要依赖与条件 | 核验 |
| --- | --- | --- | --- | --- |
| [`exploratory-data-analysis`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/exploratory-data-analysis/SKILL.md) | 对本地研究数据检查缺失、异常、数据泄漏及变换敏感性，生成探索性分析记录。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | 核心离线脚本需 Python 3.11+；完整可选格式环境需 Python 3.12+、uv 及对应文件库。 | 来源已核验 |
| [`statistical-analysis`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/statistical-analysis/SKILL.md) | 根据研究问题选择统计检验，检查假设，并报告效应量、区间与结果解释。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | Python 3.12+、SciPy、statsmodels、pingouin、pandas 等；贝叶斯扩展另需 PyMC/ArviZ。 | 来源已核验 |
| [`statistical-power`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/statistical-power/SKILL.md) | 在研究规划阶段计算样本量、检验功效或最小可检测效应，并开展假设敏感性分析。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | Python 3.12+、statsmodels、SciPy、NumPy、pandas、Matplotlib；部分生存分析另需 lifelines 与 pandas<3。 | 来源已核验 |
| [`statsmodels`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/statsmodels/SKILL.md) | 拟合回归、广义线性模型和时间序列模型，并进行参数推断、诊断与模型比较。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | Python 3.10+、statsmodels；当前测试科学计算栈需 Python 3.12+；绘图另需 Matplotlib。 | 来源已核验 |
| [`pymc`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/pymc/SKILL.md) | 建立贝叶斯与层级模型，实施后验采样、预测检查及模型诊断。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | Python 3.12+、PyMC、PyTensor、ArviZ 及科学 Python 库；安装后核心分析可离线。 | 来源已核验 |
| [`polars`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/polars/SKILL.md) | 用表达式和惰性查询高效清洗、连接、聚合研究表格，处理较大的数据集。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | Python 3.10+、Polars；Excel、数据库、云存储和 GPU 功能需对应可选依赖。 | 来源已核验 |
| [`dask`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/dask/SKILL.md) | 将表格、科学数组或独立计算任务分块并行处理，扩展到超出内存或多节点的数据。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | Python 3.10+、Dask；表格需 pandas/PyArrow；分布式和云存储需对应组件。 | 来源已核验 |
| [`markitdown`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/markitdown/SKILL.md) | 把 Office、PDF 等常见研究文档转成 Markdown，便于检索、文本分析与资料整理。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | Python 3.10 至 3.14、MarkItDown、uv；本地转换可离线，OCR/云服务等路径有额外要求。 | 来源已核验 |
| [`ara-research-manager`](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/22-agent-native-research-artifact/research-manager/SKILL.md) | 在研究会话结束后记录决策、实验、失败路径与人员或代理的来源标签。 | [OR](https://github.com/Orchestra-Research/AI-Research-SKILLs) · ⭐ 13,327 | 上游声明无额外包；需研究会话记录与 ARA 工作目录。 | 来源已核验 |
| [`ray-data`](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/05-data-processing/ray-data/SKILL.md) | 通过流式与分布式处理组织机器学习数据预处理、加载和批量推理。 | [OR](https://github.com/Orchestra-Research/AI-Research-SKILLs) · ⭐ 13,327 | ray[data]、pyarrow、pandas。 | 来源已核验 |
| [`huggingface-datasets`](https://github.com/huggingface/skills/blob/ca0325bb20b2d0a1b2efa893670c4c72f79e707b/skills/huggingface-datasets/SKILL.md) | 查询数据划分、分页记录、筛选条件与 Parquet 文件，支持研究数据探索。 | [HF](https://github.com/huggingface/skills) · ⭐ 11,145 | Dataset Viewer HTTP API；受限或私有数据需 HF_TOKEN。 | 来源已核验 |
| [`jupyter-notebooks`](https://github.com/openai/plugins/blob/5fd93af4cd0c623e020d0cc7e9ce178b4ac1f70f/plugins/data-analytics/skills/jupyter-notebooks/SKILL.md) | 创建、整理和运行可复现的 Python/SQL Notebook，保留分析过程与核验记录。 | [OA](https://github.com/openai/plugins) · ⭐ 7,335 | Python/SQL 环境；nbformat、nbclient 或 Jupyter；宿主工具按工作流配置。 | 来源已核验 |
| [`analyze-data-quality`](https://github.com/openai/plugins/blob/5fd93af4cd0c623e020d0cc7e9ce178b4ac1f70f/plugins/data-analytics/skills/analyze-data-quality/SKILL.md) | 核查缺失、重复、粒度与来源冲突，判断数据是否足以支持研究结论。 | [OA](https://github.com/openai/plugins) · ⭐ 7,335 | 可读取的数据或查询结果；Python/SQL；可配合 jupyter-notebooks。 | 来源已核验 |
| [`validate-data`](https://github.com/openai/plugins/blob/5fd93af4cd0c623e020d0cc7e9ce178b4ac1f70f/plugins/data-analytics/skills/validate-data/SKILL.md) | 逐项检查方法、计算、图表和结论是否被输入证据支持。 | [OA](https://github.com/openai/plugins) · ⭐ 7,335 | 已有分析、原始来源与方法说明；与数据质量检查配合。 | 来源已核验 |

<a id="figures"></a>

## 🎨 科研绘图与学术展示

| Skill | 适用任务 | 来源 / 仓库 Star | 主要依赖与条件 | 核验 |
| --- | --- | --- | --- | --- |
| [`matplotlib`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/matplotlib/SKILL.md) | 精细控制科研图的坐标轴、注释和版式，并导出 PNG、PDF 或 SVG。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | Python 3.11+、Matplotlib、NumPy/SciPy；部分表格示例需 pandas；本地绘图无需密钥。 | 来源已核验 |
| [`seaborn`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/seaborn/SKILL.md) | 快速绘制研究数据的分布、组间比较、回归关系与热图，并明确聚合和不确定性展示方式。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | Seaborn、NumPy、pandas、Matplotlib；当前测试依赖栈需 Python 3.12+；高级分析可选 SciPy/statsmodels。 | 来源已核验 |
| [`scientific-visualization`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scientific-visualization/SKILL.md) | 设计和审查投稿用多面板科研图，检查数据表达、配色、图像元数据与导出格式。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | Python 3.11+、uv；按需使用 Matplotlib/Pillow/pypdf；Plotly 静态导出另需 Kaleido 和 Chrome。 | 来源已核验 |
| [`scientific-schematics`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scientific-schematics/SKILL.md) | 生成研究流程、系统结构或模型架构等科学示意图草稿，并进行迭代检查。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | Python 3.10+、requests、联网与 OpenRouter API 密钥；使用外部图像生成服务。 | 来源已核验 |
| [`scientific-slides`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scientific-slides/SKILL.md) | 组织组会、会议报告和答辩的演示结构，生成幻灯片并检查排版与展示节奏。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | Python 3.12+ 及文档库；生成需 OpenRouter 密钥；PPTX/Beamer 路径分别涉及 Node.js、LibreOffice 或 TeX。 | 来源已核验 |
| [`latex-posters`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/latex-posters/SKILL.md) | 把研究内容组织为可编辑的 LaTeX 学术海报，并执行 PDF 编译和印刷前检查。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | LaTeX 发行版、海报模板与 Poppler；可选 AI 图形需 Python、requests 和 OpenRouter 密钥。 | 来源已核验 |
| [`academic-plotting`](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/20-ml-paper-writing/academic-plotting/SKILL.md) | 把实验数据绘成论文图表，并为模型架构图提供单独的生成工作流。 | [OR](https://github.com/Orchestra-Research/AI-Research-SKILLs) · ⭐ 13,327 | matplotlib、seaborn、NumPy；AI 架构图另需 google-genai 与 Gemini 凭据。 | 来源已核验 |
| [`visualize-data`](https://github.com/openai/plugins/blob/5fd93af4cd0c623e020d0cc7e9ce178b4ac1f70f/plugins/data-analytics/skills/visualize-data/SKILL.md) | 选择图形与尺度，制作并审查能够清楚表达定量证据的图表。 | [OA](https://github.com/openai/plugins) · ⭐ 7,335 | 数据及变量口径；绘图库；部分输出路径依赖宿主能力。 | 来源已核验 |

<a id="training"></a>

## 🧠 模型训练与微调

| Skill | 适用任务 | 来源 / 仓库 Star | 主要依赖与条件 | 核验 |
| --- | --- | --- | --- | --- |
| [`peft-fine-tuning`](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/03-fine-tuning/peft/SKILL.md) | 使用 LoRA、QLoRA 等适配器方法开展受显存约束的大模型微调实验。 | [OR](https://github.com/Orchestra-Research/AI-Research-SKILLs) · ⭐ 13,327 | peft、transformers、PyTorch、bitsandbytes；需合适的训练硬件。 | 来源已核验 |
| [`unsloth`](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/03-fine-tuning/unsloth/SKILL.md) | 为 Unsloth 的 LoRA 与 QLoRA 微调配置、代码排错和资源优化提供参考。 | [OR](https://github.com/Orchestra-Research/AI-Research-SKILLs) · ⭐ 13,327 | unsloth、PyTorch、transformers、trl、datasets、peft。 | 来源已核验 |
| [`llama-factory`](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/03-fine-tuning/llama-factory/SKILL.md) | 通过 LLaMA-Factory 的界面或配置完成语言模型与多模态模型微调。 | [OR](https://github.com/Orchestra-Research/AI-Research-SKILLs) · ⭐ 13,327 | 上游列 llmtuner、PyTorch、transformers、datasets、peft、accelerate、gradio。 | 来源已核验 |
| [`axolotl`](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/03-fine-tuning/axolotl/SKILL.md) | 用 YAML 配置组织模型、数据与 LoRA 或偏好训练流程。 | [OR](https://github.com/Orchestra-Research/AI-Research-SKILLs) · ⭐ 13,327 | axolotl、PyTorch、transformers、datasets、peft、accelerate、deepspeed。 | 来源已核验 |
| [`fine-tuning-with-trl`](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/06-post-training/trl-fine-tuning/SKILL.md) | 在 Hugging Face 体系中开展 SFT、DPO 与奖励驱动的后训练实验。 | [OR](https://github.com/Orchestra-Research/AI-Research-SKILLs) · ⭐ 13,327 | trl、transformers、datasets、peft、accelerate、PyTorch。 | 来源已核验 |
| [`grpo-rl-training`](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/06-post-training/grpo-rl-training/SKILL.md) | 围绕自定义奖励函数配置 TRL 的 GRPO 推理与任务专用训练实验。 | [OR](https://github.com/Orchestra-Research/AI-Research-SKILLs) · ⭐ 13,327 | transformers、trl、datasets、peft、PyTorch；需训练资源与奖励定义。 | 来源已核验 |
| [`huggingface-llm-trainer`](https://github.com/huggingface/skills/blob/ca0325bb20b2d0a1b2efa893670c4c72f79e707b/skills/huggingface-llm-trainer/SKILL.md) | 规划 TRL/Unsloth 微调流程，覆盖数据检查、训练方法、算力选择和结果保存。 | [HF](https://github.com/huggingface/skills) · ⭐ 11,145 | HF Jobs、TRL/Unsloth、Trackio；Jobs 付费计划与写权限令牌。 | 来源已核验 |
| [`huggingface-vision-trainer`](https://github.com/huggingface/skills/blob/ca0325bb20b2d0a1b2efa893670c4c72f79e707b/skills/huggingface-vision-trainer/SKILL.md) | 组织检测、分类和分割实验，检查图像标注格式并生成训练工作流。 | [HF](https://github.com/huggingface/skills) · ⭐ 11,145 | HF Jobs、Transformers 与 Hub 图像数据；付费计划及写权限令牌。 | 来源已核验 |
| [`train-sentence-transformers`](https://github.com/huggingface/skills/blob/ca0325bb20b2d0a1b2efa893670c4c72f79e707b/skills/train-sentence-transformers/SKILL.md) | 训练向量检索、重排序与稀疏检索模型，配套损失选择、负例挖掘和评估器。 | [HF](https://github.com/huggingface/skills) · ⭐ 11,145 | sentence-transformers[train] >=5；多向量模型 >=6；GPU 建议；Hub 发布需写令牌。 | 来源已核验 |

<a id="evaluation"></a>

## 🧪 评估、解释与实验记录

| Skill | 适用任务 | 来源 / 仓库 Star | 主要依赖与条件 | 核验 |
| --- | --- | --- | --- | --- |
| [`ara-rigor-reviewer`](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/22-agent-native-research-artifact/rigor-reviewer/SKILL.md) | 从证据相关性、可证伪性与方法严谨性等维度审阅结构化研究材料。 | [OR](https://github.com/Orchestra-Research/AI-Research-SKILLs) · ⭐ 13,327 | 上游声明无额外包；需已通过结构校验的 ARA 材料。 | 来源已核验 |
| [`evaluating-llms-harness`](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/11-evaluation/lm-evaluation-harness/SKILL.md) | 用统一的任务与指标评估语言模型，并比较模型版本或训练阶段。 | [OR](https://github.com/Orchestra-Research/AI-Research-SKILLs) · ⭐ 13,327 | lm-eval、transformers；vLLM 为上游列出的推理后端。 | 来源已核验 |
| [`evaluating-code-models`](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/11-evaluation/bigcode-evaluation-harness/SKILL.md) | 使用 HumanEval、MBPP 等基准与 pass@k 指标比较代码生成模型。 | [OR](https://github.com/Orchestra-Research/AI-Research-SKILLs) · ⭐ 13,327 | bigcode-evaluation-harness、transformers、accelerate、datasets；执行评估需隔离环境。 | 来源已核验 |
| [`transformer-lens-interpretability`](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/04-mechanistic-interpretability/transformer-lens/SKILL.md) | 借助激活缓存、HookPoints 和激活修补分析 Transformer 的内部机制。 | [OR](https://github.com/Orchestra-Research/AI-Research-SKILLs) · ⭐ 13,327 | transformer-lens、PyTorch；需目标模型与实验资源。 | 来源已核验 |
| [`weights-and-biases`](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/13-mlops/weights-and-biases/SKILL.md) | 记录训练指标、组织超参数搜索并关联模型与数据产物。 | [OR](https://github.com/Orchestra-Research/AI-Research-SKILLs) · ⭐ 13,327 | wandb；云端同步需账户，本地记录按配置使用。 | 来源已核验 |
| [`mlflow`](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/13-mlops/mlflow/SKILL.md) | 保存实验参数、指标和模型版本，为实验复查与复现保留记录。 | [OR](https://github.com/Orchestra-Research/AI-Research-SKILLs) · ⭐ 13,327 | mlflow、sqlalchemy、boto3；后两项按存储方案配置。 | 来源已核验 |
| [`tensorboard`](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/13-mlops/tensorboard/SKILL.md) | 可视化训练曲线、模型图和性能剖析结果，辅助实验比较与调试。 | [OR](https://github.com/Orchestra-Research/AI-Research-SKILLs) · ⭐ 13,327 | tensorboard；上游另列 PyTorch 与 TensorFlow，按训练框架使用。 | 来源已核验 |
| [`huggingface-community-evals`](https://github.com/huggingface/skills/blob/ca0325bb20b2d0a1b2efa893670c4c72f79e707b/skills/huggingface-community-evals/SKILL.md) | 组织 inspect-ai 或 lighteval 基准评测，并选择本地推理后端。 | [HF](https://github.com/huggingface/skills) · ⭐ 11,145 | uv、inspect-ai/lighteval；本地 GPU 或推理服务；受限模型需令牌。 | 来源已核验 |
| [`huggingface-trackio`](https://github.com/huggingface/skills/blob/ca0325bb20b2d0a1b2efa893670c4c72f79e707b/skills/huggingface-trackio/SKILL.md) | 记录并比较训练指标，展示实验曲线，检索运行状态与诊断告警。 | [HF](https://github.com/huggingface/skills) · ⭐ 11,145 | Python trackio 或其 CLI；同步 HF Spaces 时需账户权限。 | 来源已核验 |

<a id="compute"></a>

## ⚙️ 科学计算与算力工具

| Skill | 适用任务 | 来源 / 仓库 Star | 主要依赖与条件 | 核验 |
| --- | --- | --- | --- | --- |
| [`scikit-learn`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scikit-learn/SKILL.md) | 建立分类、回归、聚类和降维流程，并规范预处理、交叉验证及模型比较。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | Python 3.11+、scikit-learn、NumPy/SciPy/joblib；示例另需 pandas/Matplotlib。 | 来源已核验 |
| [`pytorch-lightning`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/pytorch-lightning/SKILL.md) | 将研究神经网络整理为可复用的训练、评估和日志流程，并支持多设备训练配置。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | Python 3.10+、Lightning 与兼容 PyTorch；分布式训练需合适硬件，在线日志需对应服务配置。 | 来源已核验 |
| [`sympy`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/sympy/SKILL.md) | 进行符号代数、微积分、方程求解和精确数学推导，并输出 LaTeX 或计算代码。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | Python 3.9+、SymPy；数值和交互示例另需对应库，编译扩展需编译器。 | 来源已核验 |
| [`networkx`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/networkx/SKILL.md) | 分析引文、社会关系或其他研究网络的路径、中心性、聚类与社区结构。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | Python 3.12+（上游排除 3.14.1）、NetworkX；数值分析和绘图可选 NumPy/SciPy/pandas/Matplotlib。 | 来源已核验 |
| [`uncertainty-and-units`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/uncertainty-and-units/SKILL.md) | 为科学计算保留物理单位，传播测量不确定性，并检查量纲和数值数量级。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | Python 3.12+、pint、uncertainties、NumPy/SciPy；静态审查仅需标准库，工具均可离线。 | 来源已核验 |
| [`huggingface-accelerate`](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/08-distributed-training/accelerate/SKILL.md) | 为 PyTorch 训练脚本配置设备、混合精度与分布式启动。 | [OR](https://github.com/Orchestra-Research/AI-Research-SKILLs) · ⭐ 13,327 | accelerate、PyTorch、transformers；多卡实验需相应硬件。 | 来源已核验 |
| [`deepspeed`](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/08-distributed-training/deepspeed/SKILL.md) | 为大模型分布式训练配置 ZeRO、流水线并行与混合精度。 | [OR](https://github.com/Orchestra-Research/AI-Research-SKILLs) · ⭐ 13,327 | deepspeed、PyTorch、transformers、accelerate；需兼容训练环境。 | 来源已核验 |
| [`serving-llms-vllm`](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/12-inference-serving/vllm/SKILL.md) | 通过连续批处理、分页注意力与张量并行部署模型推理实验或服务。 | [OR](https://github.com/Orchestra-Research/AI-Research-SKILLs) · ⭐ 13,327 | vllm、PyTorch、transformers；需兼容加速设备。 | 来源已核验 |
| [`sglang`](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/12-inference-serving/sglang/SKILL.md) | 为模型服务配置前缀缓存、结构化输出与受约束生成。 | [OR](https://github.com/Orchestra-Research/AI-Research-SKILLs) · ⭐ 13,327 | sglang、PyTorch、transformers；需兼容推理硬件。 | 来源已核验 |
| [`llama-cpp`](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/12-inference-serving/llama-cpp/SKILL.md) | 使用 GGUF 模型在 CPU、Apple Silicon 或消费级硬件上开展本地推理。 | [OR](https://github.com/Orchestra-Research/AI-Research-SKILLs) · ⭐ 13,327 | 上游列 llama-cpp-python；需 GGUF 模型与对应编译后端。 | 来源已核验 |
| [`hf-cli`](https://github.com/huggingface/skills/blob/ca0325bb20b2d0a1b2efa893670c4c72f79e707b/skills/hf-cli/SKILL.md) | 统一管理模型、数据集与云端任务，适合获取实验输入和组织研究资产。 | [HF](https://github.com/huggingface/skills) · ⭐ 11,145 | hf CLI；写入与云任务需 HF 账户及相应权限。 | 来源已核验 |
| [`hf-mem`](https://github.com/huggingface/skills/blob/ca0325bb20b2d0a1b2efa893670c4c72f79e707b/skills/hf-mem/SKILL.md) | 读取远程权重元数据估算内存需求，帮助选择推理硬件与上下文配置。 | [HF](https://github.com/huggingface/skills) · ⭐ 11,145 | uv/uvx；受限或私有模型需 HF_TOKEN；KV cache 估算属实验功能。 | 来源已核验 |

<a id="domain"></a>

## 🌍 学科专用数据分析

| Skill | 适用任务 | 来源 / 仓库 Star | 主要依赖与条件 | 核验 |
| --- | --- | --- | --- | --- |
| [`astropy`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/astropy/SKILL.md) | 处理天文学的坐标、时间、物理量、FITS 文件与常用宇宙学计算。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | Python 3.11+、Astropy、NumPy；部分计算需 SciPy；名称解析和远程数据需联网。 | 来源已核验 |
| [`geopandas`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/geopandas/SKILL.md) | 整理和分析地理矢量数据，检查坐标参考系、空间连接及几何质量。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | 当前测试栈需 Python 3.12+、uv、GeoPandas 及 Shapely/pyproj/pyogrio 等地理库。 | 来源已核验 |
| [`pymatgen`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/pymatgen/SKILL.md) | 读取、验证和分析材料结构与计算结果，支持相图、对称性和电子结构资料处理。 | [KD](https://github.com/K-Dense-AI/scientific-agent-skills) · ⭐ 47,872 | Python 3.11+、pymatgen、uv；Materials Project 查询另需 mp-api、联网和 MP_API_KEY。 | 来源已核验 |

<a id="documents"></a>

## 📄 PDF、Word、PPT 与工作簿

| Skill | 适用任务 | 来源 / 仓库 Star | 主要依赖与条件 | 核验 |
| --- | --- | --- | --- | --- |
| [`pdf`](https://github.com/anthropics/skills/blob/683bc88e56f3e09ba94f7055977f3d3aa499f202/skills/pdf/SKILL.md) | 提取论文 PDF 的文字和表格，处理页面并对扫描文档进行 OCR。 | [AN](https://github.com/anthropics/skills) · ⭐ 180,017 | Python PDF 库；OCR/渲染命令行工具按需；专有许可见上游。 | 来源已核验 |
| [`docx`](https://github.com/anthropics/skills/blob/683bc88e56f3e09ba94f7055977f3d3aa499f202/skills/docx/SKILL.md) | 创建和编辑 Word 稿件，处理样式、批注、修订与文档内容。 | [AN](https://github.com/anthropics/skills) · ⭐ 180,017 | Node.js docx、Pandoc 等按需；专有许可见上游。 | 来源已核验 |
| [`pptx`](https://github.com/anthropics/skills/blob/683bc88e56f3e09ba94f7055977f3d3aa499f202/skills/pptx/SKILL.md) | 创建、解析和修改演示文稿，整理组会或会议汇报材料。 | [AN](https://github.com/anthropics/skills) · ⭐ 180,017 | Node.js PptxGenJS；配套渲染脚本；专有许可见上游。 | 来源已核验 |
| [`xlsx`](https://github.com/anthropics/skills/blob/683bc88e56f3e09ba94f7055977f3d3aa499f202/skills/xlsx/SKILL.md) | 清洗并编辑研究工作簿，维护公式、图表与表格输出。 | [AN](https://github.com/anthropics/skills) · ⭐ 180,017 | Python/表格工具；公式重算环境按需；专有许可见上游。 | 来源已核验 |

<a id="emerging"></a>

## 🌱 新兴学术工作流

以下条目来自当前不足 1,000 Star 的新兴来源，作为方法与流程补充收录；适合试用观察。

| Skill | 适用任务 | 来源 / 仓库 Star | 主要依赖与条件 | 核验 |
| --- | --- | --- | --- | --- |
| [`digest-paper`](https://github.com/VincenzoImp/academic-research-skills/blob/28a4f18e43ae5c086357c4a1e1412b0a96c74703/skills/digest-paper/SKILL.md) | 把单篇论文整理为全文、阅读综合、书目条目和引用关系，维护一致的文献索引。 | [VA](https://github.com/VincenzoImp/academic-research-skills) · ⭐ 3 | create-academic-research 目录约定；arxiv MCP 与至少一种书目 MCP；make check。 | 来源已核验 |
| [`explore-sota`](https://github.com/VincenzoImp/academic-research-skills/blob/28a4f18e43ae5c086357c4a1e1412b0a96c74703/skills/explore-sota/SKILL.md) | 围绕研究范围进行关键词检索、引文追踪、候选筛选和逐篇阅读。 | [VA](https://github.com/VincenzoImp/academic-research-skills) · ⭐ 3 | 同仓库 digest-paper；arxiv 与书目 MCP；SOTA 队列和索引结构。 | 来源已核验 |
| [`package-artifacts`](https://github.com/VincenzoImp/academic-research-skills/blob/28a4f18e43ae5c086357c4a1e1412b0a96c74703/skills/package-artifacts/SKILL.md) | 按论文承诺和会场要求汇集代码、数据与说明，生成校验清单并核查独立运行。 | [VA](https://github.com/VincenzoImp/academic-research-skills) · ⭐ 3 | 既有贡献目录、会场要求和论文源码；需可验证的代码/数据环境。 | 来源已核验 |
| [`manage-submission`](https://github.com/VincenzoImp/academic-research-skills/blob/28a4f18e43ae5c086357c4a1e1412b0a96c74703/skills/manage-submission/SKILL.md) | 冻结投稿版本、整理审稿关注点，并把回复与实际论文修订对应起来。 | [VA](https://github.com/VincenzoImp/academic-research-skills) · ⭐ 3 | create-academic-research 论文目录；LaTeX/make 构建；已有稿件及审稿材料。 | 来源已核验 |
| [`data-visualization-and-figures`](https://github.com/jjfroehlich/agent-skills-for-academic-research/blob/9b1b256e99055006725fe4c6b8f90d301ceef7b0/skills/data-visualization-and-figures/SKILL.md) | 审查图形类型、坐标尺度、不确定性和多面板布局，使视觉证据便于判断。 | [JA](https://github.com/jjfroehlich/agent-skills-for-academic-research) · ⭐ 1 | 输入图表、数据含义与输出要求；配套 references/checklists；未声明必需外部 API。 | 来源已核验 |
| [`grant-writing`](https://github.com/jjfroehlich/agent-skills-for-academic-research/blob/9b1b256e99055006725fe4c6b8f90d301ceef7b0/skills/grant-writing/SKILL.md) | 组织研究目标、意义、创新性、可行性与风险计划，形成面向评审的申请叙事。 | [JA](https://github.com/jjfroehlich/agent-skills-for-academic-research) · ⭐ 1 | 资助方征集说明、项目证据和约束；配套参考资料；未声明必需外部 API。 | 来源已核验 |
| [`research-strategy-and-project-design`](https://github.com/jjfroehlich/agent-skills-for-academic-research/blob/9b1b256e99055006725fe4c6b8f90d301ceef7b0/skills/research-strategy-and-project-design/SKILL.md) | 比较科研问题的知识增量与可行性，明确关键不确定性和继续、转向或停止的依据。 | [JA](https://github.com/jjfroehlich/agent-skills-for-academic-research) · ⭐ 1 | 候选问题、现有证据、资源与时间约束；配套项目选择 playbook。 | 来源已核验 |
| [`scientific-writing`](https://github.com/jjfroehlich/agent-skills-for-academic-research/blob/9b1b256e99055006725fe4c6b8f90d301ceef7b0/skills/scientific-writing/SKILL.md) | 围绕主张、证据与限制重组论文段落，改善摘要、结果、讨论和图注的表达。 | [JA](https://github.com/jjfroehlich/agent-skills-for-academic-research) · ⭐ 1 | 作者提供的科学证据和原稿；配套写作参考资料；未声明必需外部 API。 | 来源已核验 |

## 核验与更新

完整源文件检查见 [verification.json](../data/verification.json)，每项包含固定版本 URL、HTTP 状态、技能名和 SHA256。

原始说明见上游链接；本清单只提供中文用途摘要与导航。使用条件、许可和 API 版本以该项上游文件为准。
