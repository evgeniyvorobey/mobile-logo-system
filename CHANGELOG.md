# Changelog

All notable changes to the mobile-logo-system skill are documented in this file.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

- **major** — breaking changes to templates, evaluation matrix, workflow phases, or output contract
- **minor** — new reference files, prompts, or capabilities without breaking existing packages
- **patch** — typos, wording fixes, link corrections

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
