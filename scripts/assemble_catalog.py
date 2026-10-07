"""Assemble reviewed candidate records and public source evidence offline."""

from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def read(name: str) -> dict:
    return json.loads((DATA / name).read_text(encoding="utf-8-sig"))


def write(name: str, value: dict) -> None:
    (DATA / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    kd = read("k_dense_candidates.json")
    orchestra = read("orchestra_candidates.json")
    additional = read("additional_candidates.json")
    official = read("official_candidates.json")
    sources = read("official_source_snapshot.json")["repositories"]
    ks = read("k_dense_source_snapshot.json")["snapshot"]
    sources.append({
        "repository": kd["repository"], "url": f'https://github.com/{kd["repository"]}',
        "stars": ks["stars"], "forks": ks["forks"], "archived": False,
        "pushed_at": ks["pushed_at"], "default_branch": "main",
        "commit_sha": ks["commit_sha"], "license_spdx": "MIT",
        "skill_files_found": ks["total_skill_files"], "inventory_truncated": ks["tree_truncated"],
        "checked_at": ks["checked_at"], "api_url": f'https://api.github.com/repos/{kd["repository"]}',
    })
    os = read("orchestra_source_snapshot.json")
    om = os["metadata"]
    sources.append({
        "repository": os["repository"], "url": om["html_url"],
        "stars": om["stargazers_count"], "forks": om["forks_count"], "archived": om["archived"],
        "pushed_at": om["pushed_at"], "default_branch": om["default_branch"],
        "commit_sha": os["commit_sha"], "tree_sha": os["tree_sha"], "commit_date": os["commit_date"],
        "license_spdx": om["license"], "skill_files_found": os["skill_count"],
        "skill_paths": os["skill_paths"], "inventory_truncated": os["tree_truncated"],
        "checked_at": os["checked_at_utc"], "api_url": f'https://api.github.com/repos/{os["repository"]}',
    })
    extra = {r["repository"].lower(): r for r in read("additional_metadata.json")["repositories"]}
    snapshots = read("additional_source_snapshot.json")["repositories"]
    for snapshot in snapshots:
        repo = snapshot["repository"]
        metadata = extra[repo.lower()].copy()
        metadata["commit_sha"] = snapshot["commit_sha"]
        metadata["commit_verification"] = snapshot["commit_source"]
        sources.append(metadata)

    groups = [kd, orchestra] + additional["repositories"] + official["repositories"]
    skills = []
    for group in groups:
        repo = group["repository"]
        for item in group["skills"]:
            # Keep only original summaries and routing metadata, not upstream text.
            row = {key: item[key] for key in ("id", "name", "category", "summary", "path", "dependencies")}
            row["repository"] = repo
            row["frontmatter_name"] = item.get("frontmatter_name", item["name"] if repo == orchestra["repository"] else item["id"])
            if repo == orchestra["repository"]:
                row["id"] = item["name"]
            if row["id"] in {"hypothesis-generation", "experimental-design", "scientific-critical-thinking"}:
                row["category"] = "ideation"
            if row["id"] in {"academic-plotting", "data-visualization-and-figures"}:
                row["category"] = "figures"
            if row["id"] in {"weights-and-biases", "mlflow", "tensorboard"}:
                row["category"] = "evaluation"
            if row["id"] == "research-strategy-and-project-design":
                row["category"] = "ideation"
            source = next(s for s in sources if s["repository"].lower() == repo.lower())
            row["source_url"] = f'https://github.com/{repo}/blob/{source["default_branch"]}/{row["path"]}'
            row["pinned_url"] = f'https://github.com/{repo}/blob/{source["commit_sha"]}/{row["path"]}'
            row["raw_url"] = f'https://raw.githubusercontent.com/{repo}/{source["commit_sha"]}/{row["path"]}'
            row["tier"] = "emerging" if source["stars"] < 1000 else "popular_source"
            skills.append(row)

    aliases = {
        "K-Dense-AI/scientific-agent-skills": ("KD", "跨学科科研", "兼容 Agent Skills 的宿主", "MIT"),
        "Orchestra-Research/AI-Research-SKILLs": ("OR", "AI 研究工程", "Claude Code / Codex 等，按上游安装器", "MIT"),
        "huggingface/skills": ("HF", "Hugging Face 官方", "多种 Agent Skills 宿主；部分依赖 HF 账户", "Apache-2.0；检查单项条款"),
        "anthropics/skills": ("AN", "Claude 官方文档", "Claude 官方；其他宿主需适配", "混合许可；本次 4 项为专有许可"),
        "openai/plugins": ("OA", "Codex 官方插件", "Codex；部分技能需要插件与连接器", "检查各插件条款；API 未提供总许可"),
        "VincenzoImp/academic-research-skills": ("VA", "学术工作流新项目", "Agent Skills；需适配项目目录与 MCP", "MIT"),
        "jjfroehlich/agent-skills-for-academic-research": ("JA", "学术方法新项目", "Agent Skills；效果仍待评估", "MIT"),
    }
    now = datetime(2026, 10, 7, tzinfo=timezone.utc)
    for source in sources:
        alias, scope, hosts, license_note = aliases[source["repository"]]
        source.update(alias=alias, scope=scope, hosts=hosts, license_note=license_note)
        age = (now - datetime.fromisoformat(source["pushed_at"].replace("Z", "+00:00"))).days
        source["maintenance"] = "近 90 天有推送" if age <= 90 else "超过 90 天未推送"
        source["tier"] = "emerging" if source["stars"] < 1000 else "popular_source"
        source["selected_count"] = sum(s["repository"] == source["repository"] for s in skills)
        source.pop("skill_paths", None)
    sources.sort(key=lambda s: (-s["stars"], s["repository"]))
    excluded = extra["openai/skills"].copy()
    excluded["reason"] = "上游 README 明确标注 deprecated，推荐迁移至 openai/plugins；未收录技能。"
    write("sources.json", {"checked_date": "2026-10-07", "timezone": "Asia/Shanghai", "repositories": sources, "excluded_sources": [excluded]})
    write("skills.json", {"checked_date": "2026-10-07", "selection": "科研常用任务精选；仓库关注度不是单项技能热度", "skills": skills})
    print(f"Assembled {len(skills)} skills from {len(sources)} repositories")


if __name__ == "__main__":
    main()
