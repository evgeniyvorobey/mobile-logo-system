---
name: mobile-logo-system
description: Create, review, refine, and package mobile-first logo systems for iOS and Android. Use when you want a project-first app icon and logo workflow directly in Claude with /mobile-logo-system.
argument-hint: "[task / brand / icon request]"
disable-model-invocation: true
---

# Mobile Logo System

Use the repository's canonical mobile logo system skill for this request.

When invoked:

1. Read `${CLAUDE_SKILL_DIR}/../../../SKILL.md` first. That file is the canonical skill entrypoint and contains the core workflow.
2. Read supporting files only as needed:
   - `${CLAUDE_SKILL_DIR}/../../../references/project-audit.md`
   - `${CLAUDE_SKILL_DIR}/../../../references/live-research.md`
   - `${CLAUDE_SKILL_DIR}/../../../references/sources.md`
   - `${CLAUDE_SKILL_DIR}/../../../references/concept-quality.md`
   - `${CLAUDE_SKILL_DIR}/../../../references/evaluation.md`
   - `${CLAUDE_SKILL_DIR}/../../../references/package-spec.md`
   - `${CLAUDE_SKILL_DIR}/../../../references/production-resources.md`
   - `${CLAUDE_SKILL_DIR}/../../../references/example-responses.md`
3. If the task requires real handoff files, use `${CLAUDE_SKILL_DIR}/../../../scripts/init_logo_system_package.py`.
4. Apply the canonical workflow to the current request.

Invocation payload:

$ARGUMENTS

If no arguments were passed after `/mobile-logo-system`, use the most recent user request from the conversation as the task input.

Return the result as a normal skill response, following the structure defined by the canonical skill.
