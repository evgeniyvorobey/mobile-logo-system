# Package Spec

Use this file when the user wants a production-ready handoff.

## Required Deliverables

The final package should include:

1. Chosen concept summary
- concept name
- core metaphor
- emotional job
- why it won
- known risks

2. Brand mark
- primary mark
- flat master version
- monochrome version
- dark/light usage notes

3. Wordmark
- preferred lockup
- spacing relationship to the mark
- horizontal and stacked usage when relevant

4. iOS app icon guidance
- primary icon composition
- padding / optical centering notes
- what must remain visible at small size

5. Android adaptive icon guidance
- foreground layer
- background layer
- monochrome layer
- notes about safe zone discipline

6. Export checklist
- see below

## Export Checklist

Before handoff, confirm:
- master concept chosen
- flat version approved
- monochrome version approved
- iOS icon reviewed at small sizes
- Android adaptive icon split defined
- wordmark lockup reviewed
- dark/light backgrounds checked
- unresolved legal/trademark questions noted

## Suggested Folder Structure

If the skill is creating file outputs, prefer a structure like:

```text
project/
  logo-system/
    concepts/
    selected/
    exports/
    reviews/
```

For the final package:

```text
selected/
  rationale.md
  mark-flat.*
  mark-monochrome.*
  wordmark.*
  ios-icon-notes.md
  android-adaptive-notes.md
  export-checklist.md
```

## Handoff Notes

Always include:
- what is finished
- what is still conceptual
- what has been visually validated
- what still needs manual designer review

Never imply that a concept is fully shipping-ready if:
- no reduction test was done
- no monochrome check was done
- no adaptive-icon thinking was done

## Public Skill Rule

Since this skill is intended to be reusable and public:
- avoid project-specific filenames in the skill text
- keep the package pattern generic
- speak in reusable templates, not one-off repo assumptions
