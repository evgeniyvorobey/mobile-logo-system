# Changelog

All notable changes to the mobile-logo-system skill are documented in this file.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

- **major** — breaking changes to templates, evaluation matrix, workflow phases, or output contract
- **minor** — new reference files, prompts, or capabilities without breaking existing packages
- **patch** — typos, wording fixes, link corrections, documentation alignment

## [2.6.0] - 2026-04-26

### Added

- `references/creative-divergence.md` — a runtime checklist for broader concept range before narrowing.
- Creative divergence hooks in `SKILL.md`, `workflow.md`, `concept-quality.md`, templates, and Codex/Claude metadata.
- `scripts/render_svg_contact_sheet.py` — dependency-free HTML contact sheets for SVG reduction, surface, monochrome, and mask review.
- `scripts/smoke_test_contact_sheet.py` and CI coverage for the contact sheet generator.
- `scripts/smoke_test_contact_sheet_browser.py` — browser visual smoke test for contact sheet rendering and SVG visibility.
- `scripts/smoke_test_package_scaffold.py` and CI coverage for handoff package scaffolding.
- Worked examples in `creative-divergence.md` showing bad pseudo-variety, strong divergence, and rejection rules.
- Validation checks that keep the prompt library aligned with the mandatory user-selection gate.

### Changed

- Prompt library examples now stop at the user-selection gate before craft pass, refinement, wordmark, or packaging work.
- Project/package templates now capture category cliches, creative stretch, and creative range snapshots.
- Contact sheets now include platform safe-zone overlays, Android adaptive icon frames, and foreground/background previews.

## [2.5.0] - 2026-04-08

### Changed

- SKILL.md compressed from 458 to 167 lines — keeps classification, tier, step order, links; details moved to references.
- Split 5 craft files into runtime checklists (~55 lines each) and full author guides (*-guide.md):
  - premium-craft.md (306 → 54), color-system.md (270 → 55), typography-craft.md (253 → 58), geometric-craft.md (248 → 53), context-testing.md (210 → 53).
- workflow.md compressed from 259 to 96 lines — removed duplication with craft files.
- Total runtime context load reduced by ~75% for hi-end runs.

### Added

- premium-craft-guide.md, color-system-guide.md, typography-craft-guide.md, geometric-craft-guide.md, context-testing-guide.md — full educational references for skill authors.

## [2.4.1] - 2026-04-08

### Fixed

- Restored SVG generation at concept stage (step 7a / Phase 5). Simple schematic-level marks are shown for each concept; full production files remain gated behind user selection.

## [2.4.0] - 2026-04-08

### Changed

- Concept stage (step 7a / Phase 5) now produces text descriptions only — SVG and production files are generated only after the user selects a direction.
- Craft files (geometric-craft.md, color-system.md, typography-craft.md, premium-craft.md, context-testing.md) are now explicitly gated to step 9 — not loaded before user selection.
- Removed example-requests.md, example-responses.md, and prompt-library.md from the Progressive Disclosure runtime list — these are authoring references, not runtime instructions.

### Added

- Hard constraints for premature SVG generation and early craft file loading.

## [2.3.0] - 2026-04-08

### Added

- Mandatory user selection gate (step 7b / Phase 6): skill now presents up to 5 mark-only concepts and waits for user choice before proceeding to refinement or packaging.
- Concept quality guidance merged into step 7a for tighter generation.
- Hard constraint: self-selecting a winner without user confirmation is explicitly prohibited.

### Changed

- Workflow Phase 5 now generates marks only — no wordmarks, lockups, or production files at concept stage.
- Workflow Phase 6 renamed to "User Selection (mandatory gate)" with explicit stop-and-ask protocol.

## [2.2.0] - 2026-04-07

### Added

- Brand identity: Construction Vesica direction — asymmetric vesica piscis from two phi-related circles.
- `brand/` directory with full deliverable set: primary symbol, monochrome symbol, small icon, horizontal lockup, construction reference variants.
- `brand/spec.md` — construction logic, color roles, typography, usage guidance for the vesica mark.

## [2.1.2] - 2026-04-07

### Fixed

- README contents now includes the `Compatibility` section for complete in-page navigation.
- README repository tree now reflects the current repo layout, including `LICENSE`
  and `.github/workflows/ci.yml`.
- `validate_skill_repo.py` now treats `LICENSE` and the CI workflow as required
  repository files to help prevent documentation and structure drift.

## [2.1.1] - 2026-04-07

### Fixed

- Evaluation matrix consistency: added missing Platform and Wordmark columns to
  decision matrix in `evaluation.md`, `concept-scorecard.md`, and
  `example-responses.md`. All three files now match the full 11-dimension list.
- Scorecard template now provides both standard (7-column) and hi-end (11-column)
  table variants.
- `evaluation.md` dimensions section split into standard tier (7) and hi-end tier
  (4 additional) with numbered list for clarity.
- Windows compatibility note in README: symlink install may require Developer Mode,
  recommend `--codex-mode copy` on Windows.

## [2.1.0] - 2026-04-07

### Added

- Quality tier system: standard (default) and hi-end paths. Standard covers
  concept territories, 7-dimension evaluation, reduction and monochrome checks.
  Hi-end adds craft pass, full context testing, motion consideration, and
  11-dimension evaluation. Tier is selected automatically based on triggers
  (premium positioning, large user base, explicit request) and can be upgraded
  mid-workflow.
- Version consistency validation in `validate_skill_repo.py` — cross-checks
  version across SKILL.md, README.md, and CHANGELOG.md.
- GitHub Actions CI workflow (`.github/workflows/ci.yml`) — runs repo validation
  and installer smoke tests on push/PR to main, across Python 3.9 and 3.12.
- MIT LICENSE file.
- Compatibility section in README (Python 3.9+, Codex/Claude, macOS/Linux/Windows).

### Changed

- SKILL.md: craft pass (step 9), full context validation (step 11), and motion
  (step 13) are now gated behind hi-end tier. Success criteria split into
  "both tiers" and "hi-end additional". Hard constraint updated to reference
  tier explicitly.
- `references/workflow.md`: quality tier summary added, Phase 7.5 and Phase 10
  marked as hi-end only, Phase 11 final review split into base and hi-end checks.
- README restructured: added table of contents, consolidated duplicate install
  sections (Quick Install + Codex + Claude merged into single Installation section),
  reduced from ~340 to ~250 lines.

## [2.0.0] - 2026-04-07

### Breaking Changes

- Evaluation matrix expanded from 7 to 11 scoring dimensions. Existing scorecards
  created with v1 will be missing 4 columns: Geometric, Color, Context, Longevity.
- Workflow expanded from 10 to 11 phases. New Phase 7.5 (Craft Pass) inserted
  between Iterative Refinement and Optional Specialized Rounds. New Phase 10
  (Motion Consideration) and Phase 11 (renamed Final Review with stronger checks).
- Concept scorecard template (`concept-scorecard.md`) has 4 new columns and 3 new
  fields per direction (construction method, color rationale, highest-risk craft weakness).
- Reduction checks template (`reduction-checks.md`) has 2 new sections: Context Checks
  and Craft Checks.
- Export checklist template (`export-checklist.md`) has 5 new status fields and 3 new
  risk fields.
- Wordmark guidance template (`wordmark-guidance.md`) fully restructured with new
  sections for type classification, weight/size matching, kerning/tracking, lockup
  construction, clear space, and customizations.
- Concept quality rules now require: construction method, color rationale with roles,
  monochrome mapping, and longevity note for every direction.
- Rejection triggers expanded: 6 new triggers related to geometry, color, context,
  longevity, negative space, and tangent continuity.
- Hard constraints expanded: 7 new rules covering construction method, color roles,
  craft pass, gradient dependency, negative space, wordmark pairing, and silhouette test.
- Success criteria expanded: 5 new criteria (geometrically constructed, color-rationalized,
  context-validated, typography-crafted, premium-verified).
- Example responses (gold-standard answer format) updated to include construction method,
  color rationale, evaluation matrix, craft audit, context test results, and prioritized
  punch lists.

### Added

- `references/geometric-craft.md` — construction grids (keyline, circle, square module),
  mathematical proportions (golden ratio, root rectangles, spacing scale), optical
  corrections (overshoot, visual center, stroke compensation, corner radius progression,
  tangent discipline), pixel alignment at all target sizes, symmetry and balance,
  platform-specific grid rules for iOS and Android.
- `references/color-system.md` — color harmony models (monochromatic, analogous,
  complementary, split-complementary, triadic), color roles and area ratios, saturation
  strategy by brand positioning, WCAG contrast ratios, CVD simulation requirements,
  gradient rules (direction consistency, survival at small sizes, gradient-to-flat and
  gradient-to-monochrome mapping), color reduction strategy, category color conventions,
  platform-specific color considerations.
- `references/typography-craft.md` — type classification for logo work (6 families),
  symbol-type pairing principles (contrast vs harmony), weight matching, size ratios,
  optical kerning (5 pair types), tracking strategy, lockup construction (horizontal,
  stacked, icon-only, wordmark-only), clear space definition, case strategy,
  wordmark customization rules.
- `references/context-testing.md` — 10 mandatory mockup contexts (iOS home screen,
  Android home screen, App Store listing, Google Play listing, notification bar, settings,
  spotlight, app switcher, splash screen, share sheet), competition proximity testing
  (competitor row, category wall, confusion test), environmental testing (wallpaper
  variation, device size variation, dynamic color/theming).
- `references/premium-craft.md` — negative space as design tool (counterform identity,
  figure-ground ambiguity, trapped space, breathing room), material language (lighting
  direction, subtle depth, edge treatment, surface texture), internal complexity vs
  external simplicity, restraint principles (color count, focal point, gradient restraint,
  detail budget), craftsmanship signals (stroke terminals, corner radius progression,
  weight distribution, tangent continuity G1/G2, path cleanliness), longevity assessment
  (trend resistance, style-agnostic silhouette test, 5-year durability), anti-patterns.
- `references/prompt-library.md` — 8 ready-to-use prompts: premium app from scratch,
  redesign generic icon, productivity tool, health/wellness, children's educational app,
  production audit, Android-first monochrome, brand refresh with equity preservation.
- Craft Pass phase in the workflow (Phase 7.5) covering geometric, color, typography,
  premium, and context validation sub-passes.
- Motion Consideration phase (Phase 10) for animation-ready mark design.
- Context Validation step (Step 11 in SKILL.md) as a mandatory pre-production gate.
- Craft Audit Gate in evaluation — 5 checks that must pass before a direction can
  advance from selection to refinement.
- `version` field in SKILL.md frontmatter.
- `CHANGELOG.md` and `MIGRATION.md` for version tracking and upgrade guidance.
- Bilingual prompt instructions (Codex `$` and Claude `/` syntax documented).

### Changed

- `references/evaluation.md` — scoring dimensions 7 to 11, expanded decision matrix,
  added craft audit gate, 6 new rejection triggers.
- `references/concept-quality.md` — added geometric construction discipline, color
  craft discipline, expanded improvement loop, added craft gate.
- `references/workflow.md` — added Phase 7.5 (Craft Pass), Phase 10 (Motion
  Consideration), strengthened Phase 11 (Final Review).
- `references/example-requests.md` — expanded from 4 to 6 examples, each with
  detailed expected behavior including craft pass and context testing.
- `references/example-responses.md` — Example 1 now includes construction method,
  color rationale, evaluation matrix with scores, craft-aware improvement moves.
  Example 3 now includes craft audit, context test results, prioritized punch list.
- `agents/openai.yaml` — default_prompt updated to mention geometric construction,
  evaluation matrix, and craft pass.
- SKILL.md steps reordered: concept quality (step 8) now precedes craft pass (step 9).
- README streamlined from 547 to 313 lines: prompts extracted to prompt-library.md,
  repository tree annotated with descriptions, scripts section completed.

## [1.0.0] - 2026-04-07

### Added

- Initial skill implementation with SKILL.md as canonical entrypoint.
- 11 reference files: sources, live-research, project-audit, concept-quality,
  evaluation, package-spec, production-resources, workflow, round-types,
  example-requests, example-responses.
- Package templates: project-style-snapshot, concept-scorecard, reduction-checks,
  rationale, wordmark-guidance, ios-icon-notes, android-adaptive-notes,
  monochrome-notes, export-checklist.
- `install_skill.py` — installer for Codex (link/copy) and Claude (vendor + wrapper).
- `init_logo_system_package.py` — handoff package scaffolder.
- `validate_skill_repo.py` — repo structure and link validator.
- `smoke_test_installer.py` — installer smoke tests.
- `agents/openai.yaml` — Codex UI metadata.
- `.claude/skills/mobile-logo-system/SKILL.md` — Claude-compatible wrapper.
- Bilingual policy (reply in user's language).
- Output contract (Mode, Platform scope, Assumptions, Known facts, Recommendations,
  Next actions).
- 7-dimension evaluation matrix (Distinctiveness, Small-size, Brand fit, Platform
  readiness, Premium feel, Monochrome survival, Wordmark compatibility).
- 10-phase workflow (Discovery through Final Review).
- Progressive disclosure of reference files.
