---
name: deco-visual-style-extractor
description: "Identify established visual styles and extract reusable style systems from reference images, moodboards, generated outputs, videos, brand materials, or craft notes. Use when the task needs to name or classify a visual style, research existing art/design/film/internet-aesthetic terms, avoid inventing unsupported style names, analyze references, create style rules, build prompt/JSON templates, define keep/avoid constraints, compare samples, or turn an aesthetic direction into a repeatable image/video generation workflow. Trigger from the professional visual-style analysis or extraction intent; explicit deco mention is not required."
---

# Deco Visual Style Extractor

Current version: `deco-visual-style-extractor@2026-07-20-v1.5-elastic-artifact-routing` (choose the smallest matching structured artifact and output only evidence-backed or task-required fields). | v1.4 every deliverable uses the matching structured template. | v1.3 professional-intent-trigger. | v1.2 deco-only-trigger superseded. | v1.1 existing-style-lookup-first.

## Core Principle

Treat style as repeated choices, not as a prompt string. Map those choices to established styles before naming anything new. Most references recombine existing movements, genres, design languages, or internet aesthetics.

## Stage 0: Existing-Style Lookup

Before assigning a style name:

1. Search existing art, design, photography, architecture, film, fashion, subculture, and internet-aesthetic vocabularies.
2. Prefer museums, archives, professional bodies, scholarship, and established aesthetic indexes. Record sources and match strength.
3. Separate the canonical style or movement from supporting styles, medium or genre, period cues, and descriptive modifiers.
4. Use a combination of established terms when no single term covers the reference.

Do not turn a descriptive phrase into a canonical style name. Coin a new name only when the user explicitly asks for naming or branding. Otherwise label unmatched wording as a non-canonical working description.

## Three-Stage Extraction Workflow

### 1. Constraint Extraction

Start by asking what the reference refuses. Identify exclusions, suppressed traits, and immutable conditions. If removing a condition would break the style, treat it as a core constraint.

Avoid describing only semantic content. A subject, prop, costume, or location is not a style rule unless it survives across unrelated samples.

### 2. Sample Purification

Use multiple same-style, different-content samples when possible. Compare them to remove accidental content and isolate repeated visual choices.

If only one sample exists, label conclusions as provisional and separate likely style rules from single-image artifacts.

### 3. System Building

Translate constraints and commonalities into a reusable style guide with four default blocks:

- Space and composition: scale, horizon, density, subject size, negative space.
- Light and atmosphere: source, direction, shadow, practical light, haze, dust, fog, snow, air clarity.
- Color and texture: palette, saturation, contrast, grain, surface finish, material age.
- Rules and constraints: keep rules, avoid rules, prompt order, negative prompt.

Validate by transfer. Apply the system to a new subject; if it only works on the original content, it is still copying rather than extracting style.

## Artifact routing

Choose the smallest artifact that directly answers the request:

- Style name or classification lookup only: `Style Lookup Result`.
- Full evidence-backed extraction: `Analysis Card`.
- Concise explanation of the extraction stages: `Three-Stage Brief`.
- Reusable generation structure: `Reusable JSON Prompt`, or the user's specified structure.
- Cross-subject portability test: `Transfer Validation`.

Do not append the other artifacts unless requested. Read `references/style-extraction-templates.md`, use the matching structure, and keep its populated fields in relative order. Preserve the selected template's exact field labels; do not translate, rename, bold, or replace them with improvised headings.

Within the selected artifact:

- Output a field only when evidence exists or the current task genuinely needs it.
- Omit empty headings, empty lists, empty JSON keys, placeholders, standalone `无` or `不适用` values, and filler inferred only to complete the template.
- Keep each fact in one owning field; do not restate the same rule across classification, stages, Keep, Avoid, and validation.
- When insufficient evidence matters, state it in `Uncertainties` instead of inventing a conclusion.
- Stay structured; do not flatten the artifact into free prose.
- Return only the selected artifact. Do not add a preface, recommendation section, search-query appendix, or another heading outside its fields.

When lookup finds no exact established term, report that as a substantive classification result, give the closest sourced terms when available, and label any unmatched wording `Working description (non-canonical)`. Never present a working description as an established style.

## Prompting Guidance

Use concrete controls before abstract descriptors:

```text
[subject and action] + [scene] + [lighting] + [camera/composition/materials] + [style micro-adjustment] + [avoid constraints]
```

Do not let words like cinematic, premium, dreamy, authentic, gritty, or editorial stand alone. Translate them into visible choices.

Likewise, do not convert a visible-choice summary into a new `-ism`, `-core`, movement, genre, or aesthetic label without documented prior usage.

## References

For every deliverable, read `references/style-extraction-templates.md` and use only the smallest matching structured template.
