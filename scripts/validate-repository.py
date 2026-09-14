\
#!/usr/bin/env python3
"""Organization-wide mechanical repository policy checks."""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote

TEXT_EXTENSIONS = {
    ".md", ".markdown", ".yaml", ".yml", ".json", ".toml", ".sh", ".bash",
    ".py", ".go", ".rs", ".tf", ".tfvars", ".js", ".mjs", ".cjs", ".ts",
    ".tsx", ".jsx", ".c", ".h", ".cc", ".cpp", ".hpp",
}
TEXT_NAMES = {
    "Dockerfile", "Taskfile.yml", "Taskfile.yaml", ".gitignore",
    ".editorconfig",
}
EXCLUDED_PARTS = {
    ".git", ".org-standards", "node_modules", "vendor", "third_party",
    "__pycache__", ".venv", "venv", "dist", "build", "old",
}
LOCAL_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
USES_RE = re.compile(r"^\s*uses:\s*([^\s#]+)")
FULL_SHA_RE = re.compile(r"^[0-9a-f]{40}$")
SECRET_PATTERNS = [
    ("private key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b")),
    ("AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
]


class Reporter:
    def __init__(self) -> None:
        self.errors = 0
        self.warnings = 0

    @staticmethod
    def _escape(message: str) -> str:
        return message.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")

    def error(self, path: Path, line: int, message: str) -> None:
        self.errors += 1
        print(f"::error file={path},line={line}::{self._escape(message)}")

    def warning(self, path: Path, line: int, message: str) -> None:
        self.warnings += 1
        print(f"::warning file={path},line={line}::{self._escape(message)}")


def is_excluded(path: Path) -> bool:
    return any(part in EXCLUDED_PARTS for part in path.parts)


def is_text_candidate(path: Path) -> bool:
    return path.suffix.lower() in TEXT_EXTENSIONS or path.name in TEXT_NAMES


def iter_files(root: Path):
    for path in sorted(root.rglob("*")):
        if path.is_file() and not is_excluded(path.relative_to(root)):
            yield path


def check_text_hygiene(root: Path, reporter: Reporter) -> None:
    for path in iter_files(root):
        rel = path.relative_to(root)
        if not is_text_candidate(path):
            continue
        try:
            raw = path.read_bytes()
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            reporter.error(rel, 1, "tracked text/config file is not UTF-8")
            continue

        lines = text.splitlines()
        for index, line in enumerate(lines, 1):
            if line.rstrip(" \t") != line:
                reporter.error(rel, index, "trailing whitespace")
            if path.suffix.lower() in {".md", ".markdown", ".yaml", ".yml", ".json"} and "\t" in line:
                reporter.error(rel, index, "tab character in indentation-sensitive text")

            for label, pattern in SECRET_PATTERNS:
                if pattern.search(line):
                    reporter.error(rel, index, f"possible committed {label}")

        if raw and not raw.endswith(b"\n"):
            reporter.error(rel, max(1, len(lines)), "file must end with a newline")


def resolve_local_link(source: Path, target: str) -> Path | None:
    target = target.strip()
    if not target or target.startswith("#"):
        return None
    if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target):
        return None
    target = target.split("#", 1)[0].split("?", 1)[0]
    if not target:
        return None
    return (source.parent / unquote(target)).resolve()


def check_markdown(root: Path, reporter: Reporter, enforce_numbered_docs: bool) -> None:
    root_resolved = root.resolve()

    for path in iter_files(root):
        if path.suffix.lower() not in {".md", ".markdown"}:
            continue

        rel = path.relative_to(root)
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()

        if enforce_numbered_docs and rel.parts and rel.parts[0] == "docs":
            if path.name.lower() != "readme.md" and not re.match(r"^\d{2}_[a-z0-9][a-z0-9_-]*\.md$", path.name):
                reporter.error(
                    rel,
                    1,
                    "canonical docs filename must match NN_topic_slug.md",
                )

        h1_lines = [i for i, line in enumerate(lines, 1) if re.match(r"^#\s+\S", line)]
        if not h1_lines:
            reporter.warning(rel, 1, "Markdown document has no level-1 heading")
        elif len(h1_lines) > 1:
            reporter.error(rel, h1_lines[1], "Markdown document must not contain multiple level-1 headings")

        for line_no, line in enumerate(lines, 1):
            for match in LOCAL_LINK_RE.finditer(line):
                destination = match.group(1).strip().strip("<>")
                resolved = resolve_local_link(path, destination)
                if resolved is None:
                    continue
                try:
                    resolved.relative_to(root_resolved)
                except ValueError:
                    reporter.error(rel, line_no, f"local link escapes repository root: {destination}")
                    continue
                if not resolved.exists():
                    reporter.error(rel, line_no, f"broken local link: {destination}")


def check_workflows(root: Path, reporter: Reporter) -> None:
    workflow_dir = root / ".github" / "workflows"
    if not workflow_dir.exists():
        return

    for path in sorted(list(workflow_dir.glob("*.yml")) + list(workflow_dir.glob("*.yaml"))):
        rel = path.relative_to(root)
        lines = path.read_text(encoding="utf-8").splitlines()

        if not any(re.match(r"^permissions:\s*(?:#.*)?$", line) for line in lines):
            reporter.error(rel, 1, "workflow must declare explicit top-level permissions")

        for line_no, line in enumerate(lines, 1):
            if re.match(r"^\s*pull_request_target\s*:", line):
                reporter.error(rel, line_no, "pull_request_target is prohibited by organization policy")

            match = USES_RE.match(line)
            if not match:
                continue

            value = match.group(1).strip("'\"")
            if value.startswith("./") or value.startswith("docker://"):
                continue
            if "@" not in value:
                reporter.error(rel, line_no, f"action/workflow reference is not pinned: {value}")
                continue

            target, ref = value.rsplit("@", 1)
            if FULL_SHA_RE.fullmatch(ref):
                continue

            if target.lower().startswith("homel-dev/"):
                reporter.warning(
                    rel,
                    line_no,
                    f"organization-owned workflow/action uses mutable ref @{ref}; pin to reviewed SHA when stable",
                )
            else:
                reporter.error(
                    rel,
                    line_no,
                    f"third-party action/workflow must use a full commit SHA, got @{ref}",
                )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--enforce-numbered-docs", action="store_true")
    args = parser.parse_args()

    root = args.root.resolve()
    reporter = Reporter()

    check_text_hygiene(root, reporter)
    check_markdown(root, reporter, args.enforce_numbered_docs)
    check_workflows(root, reporter)

    print(
        f"repository-policy: errors={reporter.errors} warnings={reporter.warnings}"
    )
    return 1 if reporter.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
