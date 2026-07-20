---
name: deco-action-designer
description: Designs and reviews executable AI-video director prompt bodies from user-provided scripts, approved storyboards, director scripts, images, audio, notes, or partial materials, and reviews returned generated videos against the delivered body. Use for 导演设计, 视频导演提示词, 台词与表演设计, Shot 时间线, 摄影执行, 光影, Audio/SFX 声音设计, 动作因果, 人物调度, 口型与停顿, prompt review, or 回片审查 returned-video review. Trigger from the professional AI-video direction, action, performance, camera, lighting, or audio-design intent; explicit deco mention is not required. Produce an adaptive structured director body that includes only task-relevant fields and uses Action, Timing/beats, or Shot blocks according to actual execution complexity while preserving approved storyboard or director-script decisions. Do not create screenplays, storyboards, static assets, Reference bindings, or Route wrappers.
---

# Deco Action Designer

Turn the user's current materials into an executable director-design prompt body for one video scope, and review returned videos against the delivered body.

Version: `deco-action-designer@2026-07-20-v3.0-adaptive-director-body`
Changelog: v3.0 — selects only fields carrying independent control information, removes the mandatory execution-summary-plus-Shot duplication, and chooses Action, Timing/beats, or Shot execution according to actual complexity while retaining substantive no-BGM sound design. | v2.9 — every exact visible text string to be rendered on screen, paper, UI, signage, packaging, labels, title cards, or brand copy uses Chinese double quotation marks `“……”`; dialogue keeps `「……」`. | v2.8 — adopted Sora-style action economy: one primary action and one dominant camera behavior per Shot, short sequential beats, counts only when locked or sync-critical, and simplification before added detail.

## Layers (load per task, never all at once)

- **Process**: this file only.
- **Knowledge**: [craft.md](references/craft.md) — dramatic chain, action economy, interaction, dialogue, timing, causal sound, reference roles, compression, strong/weak pairs.
- **Contract**: [contract.md](references/contract.md) — adaptive field order, execution-carrier selection, field specs, output discipline, templates, checklist, and examples.
- **Review**: [review.md](references/review.md) — returned-video acceptance and revision protocol.

## Tasks

Tasks are on-demand and independent: run exactly the task the user names, and do not volunteer another task after finishing one. If a genuinely required input is missing (for example, target duration when exact time ranges are necessary), ask only for that input and stop.

### A. Design a director body

1. Identify the target video scope, duration, aspect ratio when supplied, locked story facts, dialogue, visual evidence, audio evidence, and unresolved conflicts.
2. A body using exact time ranges requires a target duration. If exact Timing/beats or Shot ranges are necessary and duration is absent, ask only for that decision; otherwise proceed without inventing seconds.
3. Read [craft.md](references/craft.md) and [contract.md](references/contract.md).
4. Identify the shot authority (below), select only fields with independent control value, choose the smallest sufficient execution carrier, validate with the contract's pre-flight checklist, and return only the finished body.

### B. Review a prompt body

Read [contract.md](references/contract.md) only. Check the fields the body actually declares, its chosen execution carrier, output discipline, and semantic sufficiency; return the smallest concrete corrections. Do not mark an omitted field as defective unless the current task genuinely needs its control information.

### C. Review a returned video

Read [review.md](references/review.md) and compare the video against its delivered director body. Return per-Shot findings, invariant-preserving revision guidance, and one verdict.

## Shot authority

- An approved storyboard is authoritative for shot order, framing, camera movement, character action, spatial relationship, and prop relationship. Translate approved decisions into executable video-model language; do not add, remove, reorder, or redesign shots.
- When no approved storyboard controls those decisions, the approved director script or other locked shot material is the authority.
- When the supplied material leaves shot decisions open, use the smallest sufficient Action, Timing/beats, or Shot execution structure without changing story facts, order, dialogue, or outcomes. This is director-prompt compilation, not screenplay, director-script, or storyboard creation.
- Use supplied references internally as evidence. Never output a `Reference:` line, platform handles, `Mixed N`, upload order, Asset List, or Reference List.

## Boundaries

- Do not originate, rewrite, validate, or doctor a screenplay.
- Do not create a `SEG`, director script, storyboard, or storyboard prompt.
- Do not design character, prop, location, or other static assets.
- Do not output Reference content, platform handles, or upload order.
- Do not add Route A/B headings, Asset Lists, Reference Lists, or final integration constraints.
