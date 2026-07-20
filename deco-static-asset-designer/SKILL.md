---
name: deco-static-asset-designer
description: Plan, discuss, lock, prompt, revise, and review reusable static visual assets from any user-provided material or stage, including storyboards. Use for asset lists; Cxx, Cxx-Lxx, Gxx, CSxx, Pxx, and Sxx assets; regional_anchor; style_aesthetic; person-led Preview; production image prompts; multi-angle and multi-shot-size nine-grid scene references; and returned-asset review. Trigger from the professional static-asset or production-image intent; explicit deco mention is not required. Produce only static-asset work, not screenplays, storyboards, performance, dialogue, audio design, or final video prompts.
---

# Deco Static Asset Designer

Plan reusable static assets with the user, test their shared direction through Preview, then write or review asset prompts.

Version: `deco-static-asset-designer@2026-07-20-v2.3-structured-prompt-output`
Changelog: v2.3 — production prompts now retain the selected asset type's numbered field structure and field labels instead of flattening them into one paragraph; field definitions, field order, fixed blocks, Preview templates, and the multi-angle fixed prompt are unchanged. | v2.2 — professional static-asset or production-image intent triggers directly; explicit deco mention is not required. | v2.1 — functions are an on-demand menu: deliver exactly the named product, no sequence pressure; full chain only on explicit request. | v2.0 four-layer restructure — shared rules single-sourced in contracts.md; one asset type = one self-contained types/ file (layout contract front-loaded, exact count slots, two-layer fixed-block contract, per-type review checklist and gold example).

## Layers (load per stage, never all at once)

- **Process**: this file only.
- **Knowledge**: references/planning.md (what to lock), references/craft.md (how to write image prompts).
- **Contracts**: references/contracts.md (all shared production-prompt rules), references/review-protocol.md (shared checks and verdicts).
- **Types**: types/<asset>.md — one self-contained file per asset type: geometry contract, content slots, review checklist, gold example.

## Route from the user's actual materials

- Accept prose, scripts, tables, images, storyboards, moodboards, reference boards, partial assets, platform links, contradictory drafts, or any mixture.
- Do not require an upstream artifact, identifier system, schema, approval state, or fixed starting stage.
- Distinguish explicit visual facts, user decisions, provisional inference, and material conflicts.
- Use storyboards as evidence for visible state, props, composition, and space. Do not redesign their shot sequence.
- Credit every locked decision or usable product.
- **Functions are on-demand.** Deliver exactly the product the user names — an asset plan, a Preview prompt, one asset prompt, a returned-asset review, or a multi-angle prompt — nothing before it, nothing after it. Do not pull in earlier stages, volunteer later stages, or ask sequence questions. If the named product lacks a required input, name the missing input and stop; do not produce upstream products uninvited. The numbered workflow below runs only when the user explicitly requests a new asset system or the full chain.

## Full-chain workflow (only on explicit request)

### 1. Plan and confirm the visual asset system

Read [planning.md](references/planning.md), [regional-anchor.md](references/regional-anchor.md), and [style-aesthetic.md](references/style-aesthetic.md). Use [visual-direction-proposal.md](templates/visual-direction-proposal.md).

Propose the smallest useful asset set, one `regional_anchor` per coherent world, one compatible `style_aesthetic`, and any conflicts or open decisions. Explain each asset's reuse value. Ask the user to revise or confirm all three surfaces, then stop.

If the user already supplies all three as locked decisions, proceed to Preview. Follow `style-aesthetic.md` when complex references may benefit from the user-managed `deco-visual-style-extractor` handoff.

### 2. Produce one Preview prompt

Read [preview.md](references/preview.md) and [craft.md](references/craft.md), then use [preview-prompt.md](templates/preview-prompt.md). Return one person-led test prompt in the confirmed medium. Do not generate the image unless the user asks.

### 3. Review and lock the Preview

Read [preview.md](references/preview.md). Review the returned image or feedback, revise only the affected visual decisions or Preview prompt, and continue after the user confirms the tested direction. If the user supplies an already tested and locked Preview, proceed directly to production prompts.

### 4. Write production asset prompts

Read [contracts.md](references/contracts.md), then only the relevant types/<asset>.md file. Follow both exactly. Do not add a separate design report.

### 5. Review returned assets

Read [review-protocol.md](references/review-protocol.md), then the asset's types/<asset>.md checklist. Return the smallest actionable correction and one verdict.

### 6. Produce multi-angle scene references

After an `Sxx location_reference` image is approved, use [multi-angle.md](types/multi-angle.md) once per scene with that image as the reference. Review returned nine-grids with the checklist in the same file.

## Output

Outside copy-ready prompt steps, use concise professional language and add only useful metadata:

```text
产物类型：
使用材料：
未决事项：
```

When delivering a production asset prompt, retain the selected `types/<asset>.md` template's numbered structure and field labels, fill the applicable fields in their defined order, and add the platform-settings line from `contracts.md`. Do not flatten the template into free prose.

## Boundaries

- Do not produce scripts, `SEG` breakdowns, director scripts, storyboards, performance, dialogue, timing, or audio design.
- Do not select a video route or assemble a final image-to-video or text-to-video prompt.
- For cross-module requests, complete only the static-asset portion and name the remaining specialist product.
