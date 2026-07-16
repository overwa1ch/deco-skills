---
name: deco-action-designer
description: Designs and reviews executable AI-video director prompt bodies from user-provided scripts, approved storyboards, director scripts, images, audio, notes, or partial materials, and reviews returned generated videos against the delivered body. Use for 导演设计, 视频导演提示词, 台词与表演设计, Shot 时间线, 摄影执行, 光影, Audio/SFX 声音设计, 动作因果, 人物调度, 口型与停顿, prompt review, or 回片审查 returned-video review. Trigger from the professional AI-video direction, action, performance, camera, lighting, or audio-design intent; explicit deco mention is not required. Produce the fixed Style/Lighting/Camera/Audio/execution-structure/Shot/Avoid body while preserving approved storyboard or director-script decisions. Do not create screenplays, storyboards, static assets, Reference bindings, or Route wrappers.
---

# Deco Action Designer

Turn the user's current materials into an executable director-design prompt body for one video scope, and review returned videos against the delivered body.

Version: `deco-action-designer@2026-07-16-v2.6-professional-intent-trigger`
Changelog: v2.6 — professional AI-video direction, action, performance, camera, lighting, or audio-design intent triggers directly; explicit deco mention is not required. | v2.5 — removed one stale Helper validation reference while preserving the specialist contract. | v2.4 — technical name cut over from `deco-director-designer`; methods, references, and output contract stayed unchanged. | v2.3 — tasks are on-demand and independent: run exactly the named task, never volunteer the next one. | v2.2 — returned-video review is text-first: the user watches and reports, the agent classifies against the body via a per-Shot checklist; frame inspection only on explicit request. | v2.1 — 开场承接 for independently generated shot sequences: when a shot visibly continues the prior one, open with its landing as visible facts at 0.0s, never narrated history; fresh setups define their own frame-one state instead (contract enforces, craft teaches, review checks). | v2.0 three-layer restructure (craft/contract/review, rules single-sourced in contract.md); `SFX:` renamed `Audio:`; `风格前缀：` header removed from the body; gold example added; returned-video review added. | v1.3 ascii-brackets.

## Layers (load per task, never all at once)

- **Process**: this file only.
- **Knowledge**: [craft.md](references/craft.md) — dramatic chain, motion consequences, interaction, dialogue, timing, causal sound, reference roles, compression, strong/weak pairs.
- **Contract**: [contract.md](references/contract.md) — fixed body structure, block specs, output discipline, template skeleton, pre-flight checklist, gold example.
- **Review**: [review.md](references/review.md) — returned-video acceptance and revision protocol.

## Tasks

Tasks are on-demand and independent: run exactly the task the user names, and do not volunteer another task after finishing one. If a required input is missing (e.g., target duration), ask only for that input and stop.

### A. Design a director body

1. Identify the target video scope, duration, aspect ratio when supplied, locked story facts, dialogue, visual evidence, audio evidence, and unresolved conflicts.
2. A finished timecoded body requires a target duration. If it is absent, ask only for that decision; do not load any reference yet. An isolated review may continue without generating a provisional final body.
3. Read [craft.md](references/craft.md) and [contract.md](references/contract.md).
4. Identify the shot authority (below), design the prefix, execution paragraph, Shot blocks, and `避免：` per the contract, validate with the contract's pre-flight checklist, and return only the finished body.

### B. Review a prompt body

Read [contract.md](references/contract.md) only. Check the supplied body against its block specs, output discipline, and checklist; return the smallest concrete corrections.

### C. Review a returned video

Read [review.md](references/review.md) and compare the video against its delivered director body. Return per-Shot findings, invariant-preserving revision guidance, and one verdict.

## Shot authority

- An approved storyboard is authoritative for shot order, framing, camera movement, character action, spatial relationship, and prop relationship. Translate approved decisions into executable video-model language; do not add, remove, reorder, or redesign shots.
- When no approved storyboard controls those decisions, the approved director script or other locked shot material is the authority.
- When the supplied material leaves shot decisions open, add only the minimum executable Shot structure without changing story facts, order, dialogue, or outcomes. This is director-prompt compilation, not screenplay, director-script, or storyboard creation.
- Use supplied references internally as evidence. Never output a `Reference:` line, platform handles, `Mixed N`, upload order, Asset List, or Reference List.

## Boundaries

- Do not originate, rewrite, validate, or doctor a screenplay.
- Do not create a `SEG`, director script, storyboard, or storyboard prompt.
- Do not design character, prop, location, or other static assets.
- Do not output Reference content, platform handles, or upload order.
- Do not add Route A/B headings, Asset Lists, Reference Lists, or final integration constraints.
