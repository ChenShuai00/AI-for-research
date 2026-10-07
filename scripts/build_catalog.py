"""Render GitHub-friendly Markdown from the frozen, reviewed JSON catalog."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = [
    ("literature", "literature", "📚 文献检索与引用"),
    ("ideation", "ideation", "💡 选题与研究设计"),
    ("writing", "writing", "✍️ 写作、审稿与成果整理"),
    ("data", "data", "📊 数据整理与统计分析"),
    ("figures", "figures", "🎨 科研绘图与学术展示"),
    ("training", "training", "🧠 模型训练与微调"),
    ("evaluation", "evaluation", "🧪 评估、解释与实验记录"),
    ("compute", "compute", "⚙️ 科学计算与算力工具"),
    ("domain", "domain", "🌍 学科专用数据分析"),
    ("documents", "documents", "📄 PDF、Word、PPT 与工作簿"),
]


def cell(value: str) -> str:
    return str(value).replace("|", "&#124;").replace("\n", " ").strip()


def skill_table(skills: list[dict], by_repo: dict) -> str:
    lines = ["| Skill | 适用任务 | 来源 / 仓库 Star | 主要依赖与条件 | 核验 |", "| --- | --- | --- | --- | --- |"]
    for skill in skills:
        source = by_repo[skill["repository"]]
        name = skill["frontmatter_name"]
        lines.append(
            f'| [`{cell(name)}`]({skill["pinned_url"]}) | {cell(skill["summary"])} '
            f'| [{source["alias"]}]({source["url"]}) · ⭐ {source["stars"]:,} '
            f'| {cell(skill["dependencies"])} | {skill["verification_label"]} |'
        )
    return "\n".join(lines)


def main() -> None:
    payload = json.loads((ROOT / "data" / "skills.json").read_text(encoding="utf-8"))
    source_payload = json.loads((ROOT / "data" / "sources.json").read_text(encoding="utf-8"))
    skills = payload["skills"]
    sources = source_payload["repositories"]
    by_repo = {s["repository"]: s for s in sources}
    verification_path = ROOT / "data" / "verification.json"
    verification = json.loads(verification_path.read_text(encoding="utf-8")) if verification_path.exists() else {"skills": []}
    evidence = {(r["repository"], r["path"]): r for r in verification["skills"]}
    for skill in skills:
        record = evidence.get((skill["repository"], skill["path"]), {})
        matched = (
            record.get("status") == 200 and record.get("id") == skill["id"]
            and record.get("source_url") == skill["raw_url"]
            and record.get("frontmatter_name") == skill["frontmatter_name"]
            and re.fullmatch(r"[0-9a-f]{64}", record.get("sha256_bytes", ""))
            and record.get("bytes", 0) > 0
        )
        skill["verification_label"] = "来源已核验" if matched else "待核验"
    verified_count = sum(s["verification_label"] == "来源已核验" for s in skills)
    date = source_payload["checked_date"]
    popular = [s for s in skills if s["tier"] == "popular_source"]
    emerging = [s for s in skills if s["tier"] == "emerging"]
    counts = Counter(s["category"] for s in popular)
    catalog = [
        "# 科研 Skills 完整清单", "",
        f"核验日期：**{date}（北京时间）** · **{len(skills)} 项精选 / {len(sources)} 个来源仓库**。", "",
        "[← 返回首页](../README.md) · [筛选口径](methodology.md) · [使用指南](getting-started.md) · [源数据](../data/skills.json)", "",
        "> 每行对应一个真实的 `SKILL.md`，技能名使用上游 frontmatter；同名技能保留来源区分。名称链接固定到本次核验的提交版本。", "",
        "> Star 为整个来源仓库的累计关注度，不能解释为单项 skill 的使用量或近期增速。来源核验覆盖文件可访问性、名称和哈希；运行效果需要在自己的环境验证。", "",
        "## 导航", "",
    ]
    for key, anchor, title in CATEGORIES:
        if counts[key]:
            catalog.append(f"- [{title} · {counts[key]} 项](#{anchor})")
    catalog += [f"- [🌱 新兴学术工作流 · {len(emerging)} 项](#emerging)", "", "## 来源缩写", "",
                "| 缩写 | 来源仓库 | 本清单条数 | 类型 | 维护状态 |", "| --- | --- | --- | --- | --- |"]
    for source in sources:
        tier = "新兴候选" if source["tier"] == "emerging" else "高关注来源"
        catalog.append(f'| {source["alias"]} | [{source["repository"]}]({source["url"]}) | {source["selected_count"]} | {tier} | {source["maintenance"]} |')
    for key, anchor, title in CATEGORIES:
        group = [s for s in popular if s["category"] == key]
        if group:
            catalog += ["", f'<a id="{anchor}"></a>', "", f"## {title}", "", skill_table(group, by_repo)]
    catalog += ["", '<a id="emerging"></a>', "", "## 🌱 新兴学术工作流", "",
                "以下条目来自当前不足 1,000 Star 的新兴来源，作为方法与流程补充收录；适合试用观察。", "",
                skill_table(emerging, by_repo), "", "## 核验与更新", "",
                "完整源文件检查见 [verification.json](../data/verification.json)，每项包含固定版本 URL、HTTP 状态、技能名和 SHA256。", "",
                "原始说明见上游链接；本清单只提供中文用途摘要与导航。使用条件、许可和 API 版本以该项上游文件为准。", ""]

    featured_ids = [
        ("KD", "literature-review"), ("HF", "huggingface-papers"), ("KD", "citation-management"),
        ("OA", "zotero"), ("KD", "hypothesis-generation"), ("KD", "scientific-writing"),
        ("KD", "peer-review"), ("KD", "statistical-analysis"), ("KD", "scientific-visualization"),
        ("OA", "jupyter-notebooks"), ("HF", "huggingface-llm-trainer"), ("OR", "evaluating-llms-harness"),
    ]
    featured = [next(s for s in skills if by_repo[s["repository"]]["alias"] == alias and s["id"] == id_) for alias, id_ in featured_ids]
    readme = f'''<div align="center">

# Awesome AI for Research

**科研 Agent Skills 中文精选**

从文献、选题、数据到论文与实验，一份有来源、有版本、可继续维护的科研技能导航。

![Skills](https://img.shields.io/badge/Skills-{len(skills)}-0969da?style=flat-square)
![Sources](https://img.shields.io/badge/Source_Repos-{len(sources)}-8250df?style=flat-square)
![Checked](https://img.shields.io/badge/Checked-{date}-1a7f37?style=flat-square)
![Language](https://img.shields.io/badge/Language-中文-blue?style=flat-square)

[完整技能表](docs/skills.md) · [按任务选择](#choose) · [来源仓库](#sources) · [使用指南](docs/getting-started.md) · [贡献条目](CONTRIBUTING.md)

</div>

---

> 检索与核验日期：**{date}（北京时间）**。收录 **{len(popular)} 项高关注来源技能 + {len(emerging)} 项新兴学术工作流**。Star 来自本次 GitHub 查询；分类与推荐按科研任务整理。

## 这份清单提供什么

本仓库整理可被 AI Agent 加载的 **Skills**：以 `SKILL.md` 为入口的任务说明、参考资源和辅助脚本。适合用 Codex、Claude Code 或其他兼容宿主处理科研任务的研究者；每项兼容性与依赖见上游。[Agent Skills 标准](https://agentskills.io/home)

每个技能都在 [完整技能表](docs/skills.md) 中占一行，包含用途、来源仓库、仓库 Star、依赖和固定版本链接。当前 **{verified_count}/{len(skills)} 项**来源文件已完成读取和名称核对；本次整理没有进行技能运行效果评测。筛选规则见 [检索与核验方法](docs/methodology.md)。

<a id="choose"></a>

## 按科研任务选择

| 你正在做什么 | 去哪里找 | 高关注来源条数 |
| --- | --- | ---: |
'''
    for key, anchor, title in CATEGORIES:
        if counts[key]:
            readme += f"| {title} | [查看技能表](docs/skills.md#{anchor}) | {counts[key]} |\n"
    readme += f'''| 🌱 学术方法与复现流程的新项目 | [新兴候选](docs/skills.md#emerging) | {len(emerging)} 项另列 |

## 先从这 12 项开始

这 12 项覆盖常见研究环节。推荐依据是任务适配；每项 Star 仍对应整个仓库。

{skill_table(featured, by_repo)}

<a id="sources"></a>

## 来源仓库与关注度

按本次查询的仓库 Star 降序排列。单项技能顺序按科研流程编排。

| 来源仓库 | Star 快照 | 科研定位 | 本清单条数 | 最近推送 UTC | 状态 |
| --- | ---: | --- | ---: | --- | --- |
'''
    for source in sources:
        tier = "新兴候选" if source["tier"] == "emerging" else "高关注来源"
        readme += f'| [{source["repository"]}]({source["url"]}) | {source["stars"]:,} | {source["scope"]} | {source["selected_count"]} | {source["pushed_at"][:10]} | {tier}；{source["maintenance"]} |\n'
    readme += '''
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
'''

    source_doc = ["# 来源记录与版本快照", "", f"核验日期：**{date}（北京时间）**。", "",
                  "[← 返回首页](../README.md) · [完整技能表](skills.md) · [检索方法](methodology.md)", "",
                  "## 当前收录来源", "", "| 仓库 | Star / Fork | 许可口径 | 宿主与依赖 | 维护状态 |", "| --- | --- | --- | --- | --- |"]
    for source in sources:
        source_doc.append(f'| [{source["repository"]}]({source["url"]}) | {source["stars"]:,} / {source["forks"]:,} | {cell(source["license_note"])} | {cell(source["hosts"])} | {source["maintenance"]} |')
    source_doc += ["", "## 固定版本", "", "| 仓库 | 提交版本 | 最近推送 UTC | 核验时间 UTC | 来源 |", "| --- | --- | --- | --- | --- |"]
    for source in sources:
        source_doc.append(f'| {source["alias"]} | [`{source["commit_sha"][:12]}`]({source["url"]}/commit/{source["commit_sha"]}) | {source["pushed_at"]} | {source["checked_at"]} | [GitHub API]({source["api_url"]}) |')
    source_doc += ["", "## 本次发现的版本差异", "",
                  "- **K-Dense 更名**：当前规范仓库为 `K-Dense-AI/scientific-agent-skills`，技能位于 `skills/<name>/SKILL.md`。本次完整目录实测 177 个；旧搜索缓存中的 165/166 数字不用于当前清单。[官方 README](https://github.com/K-Dense-AI/scientific-agent-skills)",
                  "- **Orchestra 计数差异**：固定提交 README 第 20 行称 98，第 381 行仍称 87；完整目录实测 98，未截断。本清单采用目录证据。[固定版本 README](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/README.md#L381)",
                  "- **Orchestra 维护状态**：最近推送为 2026-06-16，距本次核验已超过 90 天，表中明确标出。累计关注度较高并不能证明近期维护活跃。[官方仓库](https://github.com/Orchestra-Research/AI-Research-SKILLs)",
                  "- **OpenAI 来源迁移**：`openai/skills` README 已声明 deprecated，转向 `openai/plugins`；旧库当前 27,919 Star 只记入排除记录。[弃用说明](https://github.com/openai/skills)",
                  "- **文档技能许可**：K-Dense 2.72.0 移除了 vendored `docx/pdf/pptx/xlsx`，这四项本清单直接链接 Anthropic 来源，其 frontmatter 声明 Proprietary。[K-Dense 发布说明](https://github.com/K-Dense-AI/scientific-agent-skills#whats-new-in-2720)",
                  "", "## 快照文件", "",
                  "[sources.json](../data/sources.json) 保存 Star、Fork、最近推送、版本与排除记录。[verification.json](../data/verification.json) 保存所有精选技能的固定版本访问核验。", "",
                  "目录计数包含递归发现的全部 `SKILL.md`，例如 OpenAI 插件可能包含内嵌技能，HF 也有辅助子技能；本清单的 88 行是人工精选，不等同于各库目录数之和。", ""]
    (ROOT / "docs").mkdir(exist_ok=True)
    (ROOT / "README.md").write_text(readme, encoding="utf-8")
    (ROOT / "docs" / "skills.md").write_text("\n".join(catalog), encoding="utf-8")
    (ROOT / "docs" / "sources.md").write_text("\n".join(source_doc), encoding="utf-8")
    print(f"Rendered README and 2 source-backed documents: {len(skills)} skill rows")


if __name__ == "__main__":
    main()
