# Production Resources

Use this file when the user wants real artifacts, handoff files, or a reusable output package.

## What These Resources Are For

This skill can now scaffold a reusable `logo-system/` package instead of only describing one.

Use the bundled production resources when:
- the user wants a handoff package
- the user wants files created in the project
- the work has moved past exploration into review, refinement, or export readiness
- you need a stable structure for design rationale, icon notes, and validation evidence

## Available Resources

- `scripts/init_logo_system_package.py`
  Use to scaffold a package directory with the standard structure and starter files.

- `assets/package-template/reviews/project-style-snapshot.md`
  Use to record the current product language before ideation.

- `assets/package-template/reviews/concept-scorecard.md`
  Use to compare directions with explicit pass/fail reasoning.

- `assets/package-template/reviews/reduction-checks.md`
  Use to log small-size, monochrome, and background checks.

- `assets/package-template/selected/rationale.md`
  Use for the chosen concept summary and why it won.

- `assets/package-template/selected/wordmark-guidance.md`
  Use for lockup logic, spacing, and typography rationale.

- `assets/package-template/selected/ios-icon-notes.md`
  Use for iOS icon composition and small-size rules.

- `assets/package-template/selected/android-adaptive-notes.md`
  Use for foreground/background/monochrome logic and safe-zone thinking.

- `assets/package-template/selected/monochrome-notes.md`
  Use for one-color survival and themed icon behavior.

- `assets/package-template/selected/export-checklist.md`
  Use for final pass/fail and unresolved risk notes.

## Scaffolding Command

Use:

```bash
python3 scripts/init_logo_system_package.py /path/to/logo-system --project-name "Project Name"
```

Optional flags:

```bash
python3 scripts/init_logo_system_package.py /path/to/logo-system \
  --project-name "Project Name" \
  --owner "Design Team" \
  --date "2026-04-07"
```

## Usage Rules

- If the project already has a package structure, update the existing files instead of blindly re-scaffolding.
- If the user wants only analysis, do not create files just because the resources exist.
- Mark anything not yet validated as `unverified`, `provisional`, or `concept-only`.
- Do not mark a package as shipping-ready unless reduction, monochrome, and adaptive icon checks are documented.

## Recommended Package Flow

1. Run the project audit and fill `project-style-snapshot.md`.
2. Generate directions and score them in `concept-scorecard.md`.
3. Log reduction evidence in `reduction-checks.md`.
4. Once a direction is chosen, fill the files under `selected/`.
5. Update `export-checklist.md` last so it reflects current truth.
