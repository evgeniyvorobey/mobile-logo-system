# Migration Guide

## v1.0.0 to v2.0.0

This is a major upgrade. The evaluation framework, workflow, templates, and quality
expectations have all changed. This guide covers every breaking change and how to
handle it.

### Who Is Affected

- Anyone who installed the skill via `install_skill.py` before v2.0.0
- Any project that has an existing `logo-system/` handoff package scaffolded by v1
- Any project with filled-in scorecard, reduction-checks, or export-checklist files

### Upgrade Steps

#### 1. Update the skill installation

```bash
# Codex (symlink mode — already points to latest if you pull)
cd /path/to/mobile-logo-system
git pull

# Codex (copy mode — re-run installer)
python3 scripts/install_skill.py --codex --codex-mode copy --force

# Claude project (re-run installer)
python3 scripts/install_skill.py --claude-project /path/to/project --force
```

#### 2. Migrate existing scorecard files

**What changed:**
The scoring matrix expanded from 7 to 11 dimensions.

Old columns:
```
Distinctive | Small Size | Brand Fit | Monochrome | Platform Readiness | Total | Advance?
```

New columns:
```
Distinctive | Small Size | Brand Fit | Monochrome | Platform | Geometric | Color | Context | Longevity | Total | Advance?
```

**How to migrate:**
Add 4 new columns to your existing scorecard table. For directions already scored:
- **Geometric** — was the mark built on a grid? Score 1-5 retroactively, or mark as `?` and re-evaluate.
- **Color** — were color roles assigned and accessibility checked? Score or mark `?`.
- **Context** — was the mark tested on a real home screen? Score or mark `?`.
- **Longevity** — does the mark's identity live in structure or in rendering effects? Score or mark `?`.

Each direction now also requires 3 new fields:
- Construction method
- Color rationale
- Highest-risk craft weakness

If you do not have this data for existing directions, add the fields with value `not evaluated under v1` and schedule a re-evaluation.

Recalculate totals after adding the new columns.

#### 3. Migrate existing reduction-checks files

**What changed:**
Two new sections added: Context Checks and Craft Checks.

**How to migrate:**
Append these sections to your existing `reduction-checks.md`:

```markdown
## Context Checks

- iOS home screen (light wallpaper):
- iOS home screen (dark wallpaper):
- Android home screen (circular mask):
- Android home screen (rounded-square mask):
- App Store listing scale:
- Google Play listing scale:
- Settings / 29pt:
- Competitor row comparison:

## Craft Checks

- Construction grid used:
- Optical corrections applied:
- Color roles assigned:
- Grayscale hierarchy survives:
- CVD simulation passed:
- Negative space deliberate:
- Style-agnostic silhouette test:
  flat / outline / cut-out — pass or fail
```

Fill in what you can from existing work. Mark the rest as `not evaluated`.

#### 4. Migrate existing export-checklist files

**What changed:**
5 new status fields and 3 new risk fields.

**How to migrate:**
Add to the `## Package Status` section:

```markdown
- Craft pass completed:
- Context testing completed:
- Geometric construction verified:
- Color accessibility verified:
- Longevity assessment completed:
```

Add to the `## Unresolved Risks` section:

```markdown
- Craft risks (geometry, color, typography):
- Context testing gaps:
- Longevity risks (trend-dependent elements):
```

Set all new fields to `not evaluated under v1` initially.

#### 5. Migrate existing wordmark-guidance files

**What changed:**
The template was fully restructured with new sections.

**How to migrate:**
Your existing wordmark-guidance content is still valid. The new template adds
structure around it. You have two options:

**Option A (recommended):** Keep your existing file as-is and add the new sections
that are relevant to your project:

```markdown
## Weight And Size Matching

- Symbol-to-wordmark visual weight balance:
- Stroke weight correspondence:
- Cap-height to symbol height ratio:
- Size ratio justification:

## Kerning And Tracking

- Letter pairs manually adjusted:
- Tracking decision: tight / standard / loose
- Tracking justification:
- Minimum legible wordmark size (rendered height):

## Clear Space

- Clear space definition: (as function of cap-height or symbol element)

## Customizations

- Letters or features customized:
- Why each customization was made:
- Small-size survival of customizations:
```

**Option B:** Re-scaffold the package with `--force` and transfer your content
into the new template structure:

```bash
python3 scripts/init_logo_system_package.py /path/to/logo-system \
  --project-name "Your Project" --force
```

Then manually restore your filled-in content from the backup.

#### 6. Acknowledge the new workflow phase

**What changed:**
A Craft Pass phase (Phase 7.5) was inserted between Iterative Refinement and
Optional Specialized Rounds.

**What to do:**
If you have a mark that was approved under v1 without a craft pass, consider
running one before final handoff. The craft pass checks:

1. Geometric construction — is the mark on a grid? Optical corrections applied?
2. Color craft — roles assigned, contrast >= 3:1, grayscale and CVD tested?
3. Typography craft — pairing justified, kerned, lockups measured?
4. Premium craft — negative space deliberate, silhouette test passed?
5. Context validation — tested on real home screens and store listings?

This is the single biggest quality improvement in v2. Marks that passed v1
evaluation may fail v2 craft checks — this is expected and means the mark
can be improved, not that it was wrong.

#### 7. Acknowledge context testing requirement

**What changed:**
Context testing is now a mandatory step before declaring a mark production-ready.

**What to do:**
For existing marks awaiting handoff, run at minimum:
- iOS home screen test (light and dark wallpaper)
- Android home screen test (circular and rounded-square mask)
- App Store / Google Play listing scale test
- Competitor row comparison (5-7 icons from same category)

If context testing reveals problems, the mark needs revision before shipping.

#### 8. Check version in existing packages

From v2.0.0 onward, scaffolded packages include a `Skill version:` field in the
export checklist. Existing packages created under v1 will not have this field.

To retroactively mark them:

Add to the top of your `export-checklist.md`:
```markdown
Skill version: 1.0.0 (migrated to v2.0.0 on YYYY-MM-DD)
```

### What You Can Ignore

- **New reference files** (geometric-craft, color-system, typography-craft,
  context-testing, premium-craft, prompt-library): these are loaded progressively
  by the skill. You do not need to read or act on them directly. They improve
  the quality of future skill output automatically.

- **Motion consideration phase**: this is optional. If your project does not need
  animation, skip it. No migration required.

- **Prompt library**: these are ready-to-use prompts for new projects. They do not
  affect existing work.

### Quick Migration Checklist

- [ ] Skill installation updated (pull + re-install if copy mode)
- [ ] Scorecards: 4 new columns added, 3 new fields per direction added
- [ ] Reduction checks: Context Checks and Craft Checks sections added
- [ ] Export checklist: 5 new status fields and 3 new risk fields added
- [ ] Wordmark guidance: new sections added (or template re-scaffolded)
- [ ] Craft pass scheduled for any mark awaiting handoff
- [ ] Context testing scheduled for any mark awaiting handoff
- [ ] `Skill version:` field added to existing export checklists
