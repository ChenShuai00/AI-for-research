"""Check catalog integrity offline; optionally verify pinned SKILL.md files online."""

from __future__ import annotations

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
import hashlib
import json
from pathlib import Path
import re
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def fetch_skill(skill: dict) -> dict:
    request = urllib.request.Request(skill["raw_url"], headers={"User-Agent": "AI-for-research-catalog"})
    with urllib.request.urlopen(request, timeout=30) as response:
        body = response.read()
        status = response.status
    text = body.decode("utf-8-sig")
    if not text.startswith("---"):
        raise ValueError("Missing YAML frontmatter")
    frontmatter = text.split("---", 2)[1]
    match = re.search(r"^name:\s*(.*?)\s*$", frontmatter, flags=re.MULTILINE)
    name = match.group(1).strip("\"'") if match else None
    if name != skill["frontmatter_name"]:
        raise ValueError(f"Name mismatch: expected {skill['frontmatter_name']!r}, got {name!r}")
    return {
        "repository": skill["repository"], "id": skill["id"], "path": skill["path"],
        "source_url": skill["raw_url"], "status": status, "frontmatter_name": name,
        "sha256_bytes": hashlib.sha256(body).hexdigest(), "bytes": len(body),
        "checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }


def offline_checks(skills: list[dict], sources: list[dict], require_evidence: bool = True, check_markdown: bool = True) -> None:
    keys = [(s["repository"], s["path"]) for s in skills]
    if len(keys) != len(set(keys)):
        raise ValueError("Duplicate repository/path")
    if len({(s["repository"], s["id"]) for s in skills}) != len(skills):
        raise ValueError("Duplicate skill IDs within a repository")
    by_repo = {s["repository"]: s for s in sources}
    counts = Counter(s["repository"] for s in skills)
    for source in sources:
        if source["selected_count"] != counts[source["repository"]]:
            raise ValueError("Incorrect selected_count")
        if not re.fullmatch(r"[0-9a-f]{40}", source["commit_sha"]):
            raise ValueError("Invalid pinned commit")
    for skill in skills:
        source = by_repo[skill["repository"]]
        for key in ("id", "name", "summary", "dependencies", "category", "path"):
            if not skill.get(key) or "\ufffd" in skill[key]:
                raise ValueError(f"Invalid {key}: {skill['id']}")
        if not skill["path"].endswith("SKILL.md") or ".." in Path(skill["path"]).parts:
            raise ValueError("Invalid skill path")
        expected_pinned = f'https://github.com/{skill["repository"]}/blob/{source["commit_sha"]}/{skill["path"]}'
        expected_raw = f'https://raw.githubusercontent.com/{skill["repository"]}/{source["commit_sha"]}/{skill["path"]}'
        if expected_pinned != skill["pinned_url"] or expected_raw != skill["raw_url"]:
            raise ValueError("Source URL does not match repository, pinned commit and path")
        if (source["stars"] < 1000) != (skill["tier"] == "emerging"):
            raise ValueError("Popularity tier inconsistent")
    catalog = ROOT / "docs" / "skills.md"
    if require_evidence:
        record_path = ROOT / "data" / "verification.json"
        if not record_path.exists():
            raise ValueError("Missing verification.json; run --online first")
        evidence = json.loads(record_path.read_text(encoding="utf-8"))
        records = evidence["skills"]
        by_key = {(r["repository"], r["path"]): r for r in records}
        if len(by_key) != len(records) or set(by_key) != set(keys):
            raise ValueError("Verification records missing, duplicated or obsolete")
        if evidence["successful"] != len(skills) or evidence["failed"] != 0 or evidence["errors"]:
            raise ValueError("Incomplete verification result")
        for skill in skills:
            record = by_key[(skill["repository"], skill["path"])]
            if (
                record.get("id") != skill["id"] or record.get("status") != 200
                or record.get("source_url") != skill["raw_url"]
                or record.get("frontmatter_name") != skill["frontmatter_name"]
                or not re.fullmatch(r"[0-9a-f]{64}", record.get("sha256_bytes", ""))
                or record.get("bytes", 0) <= 0
            ):
                raise ValueError(f"Stale or invalid verification evidence: {skill['id']}")
    if check_markdown and catalog.exists():
        text = catalog.read_text(encoding="utf-8")
        for skill in skills:
            if text.count(skill["pinned_url"]) != 1:
                raise ValueError(f"Skill missing or duplicated in Markdown: {skill['id']}")
        for line in text.splitlines():
            if line.startswith("| ") and line.count("|") != 6:
                raise ValueError(f"Malformed five-column Markdown table: {line[:90]}")
    for path in [ROOT / "README.md", *sorted((ROOT / "docs").glob("*.md"))]:
        text = path.read_text(encoding="utf-8")
        for link in re.findall(r"\]\(([^)]+)\)", text):
            if "://" not in link and not link.startswith("#"):
                target = link.split("#", 1)[0]
                if target and not (path.parent / target).exists():
                    raise ValueError(f"Broken local link in {path.name}: {link}")
    print(f"Offline checks passed: {len(skills)} skills, {len(sources)} repositories")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--online", action="store_true", help="Fetch every pinned SKILL.md; save hashes and HTTP status")
    args = parser.parse_args()
    skills = json.loads((ROOT / "data" / "skills.json").read_text(encoding="utf-8"))["skills"]
    sources = json.loads((ROOT / "data" / "sources.json").read_text(encoding="utf-8"))["repositories"]
    offline_checks(skills, sources, require_evidence=not args.online, check_markdown=not args.online)
    if args.online:
        records = []
        errors = []
        with ThreadPoolExecutor(max_workers=8) as executor:
            tasks = [(s, executor.submit(fetch_skill, s)) for s in skills]
            for skill, task in tasks:
                try:
                    records.append(task.result())
                except Exception as exc:
                    errors.append({"repository": skill["repository"], "id": skill["id"], "error": str(exc)})
        payload = {
            "checked_date": datetime.now(timezone(timedelta(hours=8))).date().isoformat(), "verification_scope": "Pinned source retrieval and metadata; no skill execution",
            "successful": len(records), "failed": len(errors), "skills": records, "errors": errors,
        }
        output = ROOT / "data" / "verification.json"
        if errors:
            output = output.with_suffix(".failed.json")
        output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Pinned source check: {len(records)}/{len(skills)} succeeded; {len(errors)} failed")
        if errors:
            print(json.dumps(errors, ensure_ascii=False, indent=2))
            raise SystemExit(1)
        offline_checks(skills, sources, check_markdown=False)


if __name__ == "__main__":
    main()
