#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path


WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
SKIP_DIRS = {".git", ".obsidian", "_skills"}
IGNORE_TARGETS = {"wikilink"}


def normalize_title(value: str) -> str:
    return value.strip().replace("\\", "/")


def page_title(path: Path, wiki_root: Path) -> str:
    rel = path.relative_to(wiki_root).as_posix()
    if rel.endswith(".md"):
        rel = rel[:-3]
    return normalize_title(rel)


def collect_pages(wiki_root: Path) -> tuple[dict[str, Path], list[Path]]:
    pages: dict[str, Path] = {}
    markdown_files: list[Path] = []
    for path in wiki_root.rglob("*.md"):
        if any(part in SKIP_DIRS or part.startswith(".git") for part in path.parts):
            continue
        markdown_files.append(path)
        rel_title = page_title(path, wiki_root)
        pages[rel_title] = path
        pages[path.stem] = path
    return pages, markdown_files


def resolve_link(target: str, current: Path, wiki_root: Path, pages: dict[str, Path]) -> bool:
    target = normalize_title(target)
    if target in pages:
        return True

    current_dir = current.parent.relative_to(wiki_root).as_posix()
    if current_dir == ".":
        current_dir = ""
    candidate = f"{current_dir}/{target}".strip("/")
    return candidate in pages


def run_lint(wiki_root: Path) -> dict:
    pages, markdown_files = collect_pages(wiki_root)
    inbound: dict[Path, set[Path]] = {path: set() for path in markdown_files}
    broken_links: list[dict] = []
    review_candidates: list[str] = []

    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        for raw_target in WIKILINK_RE.findall(text):
            if normalize_title(raw_target).lower() in IGNORE_TARGETS:
                continue
            if resolve_link(raw_target, path, wiki_root, pages):
                target_path = pages.get(normalize_title(raw_target))
                if target_path is None:
                    current_dir = path.parent.relative_to(wiki_root).as_posix()
                    candidate = f"{current_dir}/{normalize_title(raw_target)}".strip("/")
                    target_path = pages.get(candidate)
                if target_path is not None:
                    inbound[target_path].add(path)
            else:
                broken_links.append(
                    {
                        "source": path.relative_to(wiki_root).as_posix(),
                        "target": raw_target,
                    }
                )

        rel_path = path.relative_to(wiki_root).as_posix()
        if rel_path.startswith("review/") and "README" not in path.name.upper():
            review_candidates.append(rel_path)

    orphan_pages = []
    for path in markdown_files:
        rel_path = path.relative_to(wiki_root).as_posix()
        if rel_path in {"index.md", "log.md", "SCHEMA.md"}:
            continue
        if not inbound[path]:
            orphan_pages.append(rel_path)

    return {
        "wiki_root": wiki_root.as_posix(),
        "broken_links": broken_links,
        "orphan_pages": sorted(orphan_pages),
        "review_candidates": sorted(review_candidates),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint trade-system wiki structure.")
    parser.add_argument("--wiki-root", required=True, help="Path to wiki root")
    parser.add_argument("--json", action="store_true", help="Print JSON only")
    args = parser.parse_args()

    wiki_root = Path(args.wiki_root).resolve()
    result = run_lint(wiki_root)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0

    print(f"wiki_root: {result['wiki_root']}")
    print(f"broken_links: {len(result['broken_links'])}")
    for item in result["broken_links"][:20]:
        print(f"  - {item['source']} -> [[{item['target']}]]")

    print(f"orphan_pages: {len(result['orphan_pages'])}")
    for item in result["orphan_pages"][:20]:
        print(f"  - {item}")

    print(f"review_candidates: {len(result['review_candidates'])}")
    for item in result["review_candidates"][:20]:
        print(f"  - {item}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
