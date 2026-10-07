"""Refresh public GitHub metadata and SKILL.md inventories; never execute skills."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
REPOSITORIES = [
    "K-Dense-AI/scientific-agent-skills",
    "Orchestra-Research/AI-Research-SKILLs",
    "huggingface/skills",
    "anthropics/skills",
    "openai/plugins",
    "VincenzoImp/academic-research-skills",
    "jjfroehlich/agent-skills-for-academic-research",
    "openai/skills",
]


def get_json(url: str) -> dict:
    headers = {"User-Agent": "AI-for-research-catalog", "Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def inspect_repository(repository: str) -> dict:
    checked_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    api_url = f"https://api.github.com/repos/{repository}"
    metadata = get_json(api_url)
    canonical = metadata["full_name"]
    branch = metadata["default_branch"]
    commit = get_json(f"https://api.github.com/repos/{canonical}/commits/{branch}")
    sha = commit["sha"]
    tree_sha = commit["commit"]["tree"]["sha"]
    tree = get_json(f"https://api.github.com/repos/{canonical}/git/trees/{tree_sha}?recursive=1")
    if tree.get("truncated"):
        raise ValueError(f"Incomplete GitHub tree: {canonical}")
    paths = sorted(item["path"] for item in tree["tree"] if item["type"] == "blob" and item["path"].endswith("SKILL.md"))
    license_info = metadata.get("license") or {}
    return {
        "repository": canonical,
        "requested_repository": repository,
        "url": metadata["html_url"],
        "description": metadata.get("description"),
        "stars": metadata["stargazers_count"],
        "forks": metadata["forks_count"],
        "archived": metadata["archived"],
        "pushed_at": metadata["pushed_at"],
        "updated_at": metadata["updated_at"],
        "default_branch": branch,
        "commit_sha": sha,
        "tree_sha": tree_sha,
        "commit_date": commit["commit"]["committer"]["date"],
        "license_spdx": license_info.get("spdx_id"),
        "license_url": license_info.get("url"),
        "skill_files_found": len(paths),
        "skill_paths": paths,
        "checked_at": checked_at,
        "api_url": api_url,
        "tree_api_url": f"https://api.github.com/repos/{canonical}/git/trees/{tree_sha}?recursive=1",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "data" / "upstream-refresh.json")
    parser.add_argument("--repository", action="append", help="Inspect only the named owner/repo; repeat to select multiple repos")
    args = parser.parse_args()
    results = []
    errors = []
    with ThreadPoolExecutor(max_workers=4) as executor:
        tasks = [(repo, executor.submit(inspect_repository, repo)) for repo in (args.repository or REPOSITORIES)]
        for repo, task in tasks:
            try:
                result = task.result()
                results.append(result)
                print(f"{result['repository']}: {result['stars']:,} stars; {result['skill_files_found']} SKILL.md files")
            except (urllib.error.URLError, ValueError, KeyError) as exc:
                errors.append({"repository": repo, "error": str(exc)})
    if errors:
        # Leave the previous successful snapshot intact on partial failure.
        partial_path = args.output.with_suffix(".partial.json")
        partial_path.parent.mkdir(parents=True, exist_ok=True)
        partial_path.write_text(json.dumps({"repositories": results, "errors": errors}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({"errors": errors}, ensure_ascii=False, indent=2))
        raise SystemExit(1)
    payload = {"checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds"), "repositories": results}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
