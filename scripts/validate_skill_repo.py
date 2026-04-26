#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "SKILL.md",
    "CHANGELOG.md",
    "MIGRATION.md",
    "LICENSE",
    ".github/workflows/ci.yml",
    ".claude/skills/mobile-logo-system/SKILL.md",
    "agents/openai.yaml",
    "references/sources.md",
    "references/live-research.md",
    "references/project-audit.md",
    "references/creative-divergence.md",
    "references/concept-quality.md",
    "references/evaluation.md",
    "references/package-spec.md",
    "references/example-requests.md",
    "references/example-responses.md",
    "references/production-resources.md",
    "references/prompt-library.md",
    "references/geometric-craft.md",
    "references/color-system.md",
    "references/typography-craft.md",
    "references/context-testing.md",
    "references/premium-craft.md",
    "scripts/install_skill.py",
    "scripts/init_logo_system_package.py",
    "scripts/render_svg_contact_sheet.py",
    "scripts/smoke_test_contact_sheet_browser.py",
    "scripts/smoke_test_contact_sheet.py",
    "scripts/smoke_test_installer.py",
    "scripts/smoke_test_package_scaffold.py",
    "assets/package-template/reviews/project-style-snapshot.md",
    "assets/package-template/reviews/concept-scorecard.md",
    "assets/package-template/reviews/reduction-checks.md",
    "assets/package-template/selected/rationale.md",
    "assets/package-template/selected/wordmark-guidance.md",
    "assets/package-template/selected/ios-icon-notes.md",
    "assets/package-template/selected/android-adaptive-notes.md",
    "assets/package-template/selected/monochrome-notes.md",
    "assets/package-template/selected/export-checklist.md",
]

MARKDOWN_GLOBS = [
    "README.md",
    "SKILL.md",
    ".claude/skills/*/SKILL.md",
    "references/*.md",
    "assets/package-template/**/*.md",
]

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
FRONTMATTER_RE = re.compile(r"^---\n(?P<body>.*?)\n---\n", re.DOTALL)
VERSION_RE = re.compile(r"^version:\s*(.+)$", re.MULTILINE)
README_VERSION_RE = re.compile(r"\*\*Current version:\s*(.+?)\*\*")
CHANGELOG_VERSION_RE = re.compile(r"^## \[(.+?)\]", re.MULTILINE)


def fail(message: str) -> None:
    raise SystemExit(f"[FAIL] {message}")


def validate_required_files() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    if missing:
        fail("Missing required files:\n" + "\n".join(missing))


def validate_skill_frontmatter() -> None:
    skill_path = ROOT / "SKILL.md"
    content = skill_path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(content)
    if not match:
        fail("SKILL.md must begin with YAML frontmatter")

    frontmatter = match.group("body")
    if "name:" not in frontmatter or "description:" not in frontmatter:
        fail("SKILL.md frontmatter must contain both name and description")
    if "version:" not in frontmatter:
        fail("SKILL.md frontmatter must contain a version field")


def validate_relative_links() -> None:
    markdown_files: list[Path] = []
    for pattern in MARKDOWN_GLOBS:
        markdown_files.extend(ROOT.glob(pattern))

    broken_links: list[str] = []
    for file_path in sorted(set(markdown_files)):
        text = file_path.read_text(encoding="utf-8")
        for lineno, line in enumerate(text.splitlines(), start=1):
            for match in LINK_RE.finditer(line):
                target = match.group(1).strip()
                if not target or "://" in target or target.startswith("#") or target.startswith("mailto:"):
                    continue
                candidate = (file_path.parent / target).resolve()
                fallback = (ROOT / target).resolve()
                if not candidate.exists() and not fallback.exists():
                    broken_links.append(
                        f"{file_path.relative_to(ROOT)}:{lineno} -> {target}"
                    )

    if broken_links:
        fail("Broken relative links found:\n" + "\n".join(broken_links))


def validate_version_consistency() -> None:
    skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    match = VERSION_RE.search(skill_text)
    if not match:
        fail("SKILL.md frontmatter does not contain a version field")
    canonical = match.group(1).strip()

    readme_text = (ROOT / "README.md").read_text(encoding="utf-8")
    rm = README_VERSION_RE.search(readme_text)
    if not rm:
        fail("README.md does not contain a **Current version: X.Y.Z** badge")
    if rm.group(1).strip() != canonical:
        fail(
            f"Version mismatch: SKILL.md says {canonical}, "
            f"README.md says {rm.group(1).strip()}"
        )

    changelog_text = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    cm = CHANGELOG_VERSION_RE.search(changelog_text)
    if not cm:
        fail("CHANGELOG.md does not contain a ## [X.Y.Z] version header")
    if cm.group(1).strip() != canonical:
        fail(
            f"Version mismatch: SKILL.md says {canonical}, "
            f"CHANGELOG.md latest entry says {cm.group(1).strip()}"
        )


def validate_smoke_test_script() -> None:
    if not installer_smoke_test_expectations():
        fail("Installer smoke test expectations are not satisfied")


def installer_smoke_test_expectations() -> bool:
    installer_path = ROOT / "scripts" / "smoke_test_installer.py"
    text = installer_path.read_text(encoding="utf-8")
    required_markers = [
        "--codex",
        "--claude-project",
        "not a directory",
        "vendor_root / \".claude\"",
        "vendor_root_link / \".claude\"",
    ]
    return all(marker in text for marker in required_markers)


def validate_prompt_library_user_gate() -> None:
    prompt_path = ROOT / "references" / "prompt-library.md"
    text = prompt_path.read_text(encoding="utf-8")
    forbidden_markers = [
        "Recommend one winner",
        "Select the winner",
        "select winner",
        "Run the craft pass on the winner",
        "Score and select",
    ]
    found = [marker for marker in forbidden_markers if marker in text]
    if found:
        fail(
            "Prompt library bypasses the mandatory user-selection gate:\n"
            + "\n".join(found)
        )
    if "mandatory user-selection gate" not in text:
        fail("Prompt library must mention the mandatory user-selection gate")


def validate_contact_sheet_script() -> None:
    script_text = (ROOT / "scripts" / "render_svg_contact_sheet.py").read_text(
        encoding="utf-8"
    )
    smoke_text = (ROOT / "scripts" / "smoke_test_contact_sheet.py").read_text(
        encoding="utf-8"
    )
    required_script_markers = [
        "Reduction Review",
        "Surface And Mask Review",
        "Platform Safe Zone Review",
        "Foreground / Background Preview",
        "data:image/svg+xml;base64,",
        "data-review-img",
        "safe-zone-overlay",
        "mask-squircle",
        "android-adaptive-frame",
        "Android circle",
    ]
    required_smoke_markers = [
        "primary-symbol.svg",
        "small-icon.svg",
        "--sizes",
        "29px",
        "safe-zone-review",
        "foreground-background-preview",
    ]
    missing_script = [
        marker for marker in required_script_markers if marker not in script_text
    ]
    missing_smoke = [
        marker for marker in required_smoke_markers if marker not in smoke_text
    ]
    if missing_script or missing_smoke:
        fail(
            "Contact sheet script expectations are not satisfied:\n"
            + "\n".join(missing_script + missing_smoke)
        )


def validate_package_scaffold_smoke_test() -> None:
    smoke_text = (ROOT / "scripts" / "smoke_test_package_scaffold.py").read_text(
        encoding="utf-8"
    )
    required_markers = [
        "init_logo_system_package.py",
        "EXPECTED_DIRS",
        "PLACEHOLDER_RE",
        "Smoke Project",
        "QA Team",
        "2026-04-26",
        "Unresolved template placeholders",
        "Package scaffold smoke test passed",
    ]
    missing = [marker for marker in required_markers if marker not in smoke_text]
    if missing:
        fail(
            "Package scaffold smoke test expectations are not satisfied:\n"
            + "\n".join(missing)
        )


def validate_browser_smoke_test() -> None:
    smoke_text = (ROOT / "scripts" / "smoke_test_contact_sheet_browser.py").read_text(
        encoding="utf-8"
    )
    required_markers = [
        "playwright",
        "chromium.launch",
        "data-review-img",
        "safe-zone-review",
        "foreground-background-preview",
        "visibleImageCount",
        "safeZoneOverlays",
        "Browser contact sheet smoke test passed",
    ]
    missing = [marker for marker in required_markers if marker not in smoke_text]
    if missing:
        fail(
            "Browser contact sheet smoke test expectations are not satisfied:\n"
            + "\n".join(missing)
        )


def validate_creative_divergence_examples() -> None:
    text = (ROOT / "references" / "creative-divergence.md").read_text(
        encoding="utf-8"
    )
    required_markers = [
        "Worked Examples",
        "Bad Set: Decorative Pseudo-Difference",
        "Good Set: True Divergence",
        "Pseudo-Difference Filter",
        "same metaphor class",
        "same monochrome mapping",
    ]
    missing = [marker for marker in required_markers if marker not in text]
    if missing:
        fail(
            "Creative divergence examples are incomplete:\n"
            + "\n".join(missing)
        )


def main() -> int:
    validate_required_files()
    validate_skill_frontmatter()
    validate_relative_links()
    validate_version_consistency()
    validate_smoke_test_script()
    validate_prompt_library_user_gate()
    validate_contact_sheet_script()
    validate_package_scaffold_smoke_test()
    validate_browser_smoke_test()
    validate_creative_divergence_examples()
    print("[OK] Skill repository structure and relative links are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
