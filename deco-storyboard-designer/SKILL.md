---
name: deco-storyboard-designer
description: Convert completed scripts, locked story material, scenes, or existing shot material into SEG breakdowns, optional scene-layout SVGs, visually optimized material, processed director scripts, storyboard designs, the fixed storyboard prompt, and the fixed shot-table prompt. Use for 拆SEG, 导演脚本, 镜头脚本, 场景布局, 分镜设计, 故事板, 分镜表, Bxx, 景别, 构图, 运镜, 镜头连续性, returned-board review, or the existing copy-ready storyboard prompts. Trigger from the professional storyboard or shot-design intent; explicit deco mention is not required. Keep original screenwriting, static asset design, performance/dialogue/audio design, and final video prompt assembly outside this skill.
---

# Deco Storyboard Designer

Own the production bridge from completed story material to storyboard-ready direction and the existing fixed storyboard prompts.

Boards are test instruments first, deliverables second: a storyboard or shot table exists to prove or falsify the shot design cheaply before video generation. A finished board is the byproduct of a passed test.

Current version: `deco-storyboard-designer@2026-07-19-v1.15-short-task-separation-wording` (storyboard and shot-table short tasks now state that separate boards/tables must not be combined into one image; professional trigger and on-demand functions remain unchanged).

## Accept the user's current material

- Accept a completed screenplay, locked script, locked brief, scene excerpt, test plot, existing `SEG`, director script, shot sequence, storyboard, or any mixture.
- Do not require a particular schema, prior approval label, asset package, route choice, or fixed starting stage.
- Preserve supplied story facts. Do not expand, rewrite, doctor, or originate the screenplay; send original screenwriting work to `deco-screenplay-writer`.
- **Functions are on-demand.** Deliver exactly the product the user names — nothing before it, nothing after it. Do not pull in earlier stages, volunteer later stages, or ask sequence questions. If the named product lacks a required input, name the missing input and stop; do not produce the upstream product uninvited.

## Route the work

### SEG breakdown

For source-preserving `SEG` work, read [references/seg-breakdown-rules.md](references/seg-breakdown-rules.md). Output the pure-script breakdown and stop when the user has not yet chosen visual optimization.

### Scene-layout SVG

When the user requests spatial planning, or chooses it before director-script conversion, read [references/scene-layout-svg-rules.md](references/scene-layout-svg-rules.md). Create one simple top-down SVG per scene and stop for review. Continue only after approval or an explicit skip.

### Visual optimization

When the user wants a more shootable or storyboard-ready version, read [references/visual-optimization-rules.md](references/visual-optimization-rules.md). Preserve story content while making visible action, blocking, transitions, sound sources, and continuity anchors executable.

### Processed director script

Read [references/director-script-output-contract.md](references/director-script-output-contract.md). Apply its frame-visibility and prompt-hygiene rules to every shot block: write only what the exact crop can show, and keep off-frame continuity in validation. Write every `拍摄手法` in this order: `拍摄角度 + 景别（取景框） + 机位 + 运镜`; add focal length or optical effect only when it materially controls the image. Keep angle, crop, camera position, and camera movement distinct. Define camera movement for every shot with its start, path, subject relation, and landing. Default to a slow push-in when no stronger movement is motivated. Use `固定镜头` only when the user locks it or stillness itself is the narrative point. Use [references/ai-video-composition-rules.md](references/ai-video-composition-rules.md) only when the user explicitly requests composition-heavy output. Validate with [references/continuity-validation-rules.md](references/continuity-validation-rules.md) before delivery.

### Storyboard design or review

- For direct storyboard design, redesign, or shot-sequence revision, read [references/storyboard-design.md](references/storyboard-design.md).
- For a returned board or existing shot sequence, read [references/storyboard-review.md](references/storyboard-review.md).
- Cite concrete panels, shots, pages, or visible features when reviewing. Preserve usable choices and propose the smallest correction.
- Classify each finding as board-execution failure or shot-design failure: a faithful board that exposes a design flaw is a successful test, and its revision routes to the shot design, not to a redraw.
- Review from text: the user views the boards and reports observations; do not open board images unless explicitly asked. Offer a per-panel viewing checklist derived from the design to make the user's pass fast.

### Fixed storyboard and shot-table prompts

- For the storyboard prompt, read [templates/storyboard-prompt-template.md](templates/storyboard-prompt-template.md) and output it verbatim. There is no rough/formal grade; one fixed storyboard prompt serves every storyboard request, and `Bxx` remains only the identifier for returned boards.
- For the shot-table (分镜表) prompt, read [templates/shot-table-prompt-template.md](templates/shot-table-prompt-template.md) and output its 生成模版 block and separate 短任务提示词 verbatim, replacing only `SEGXX`.
- Storyboards and shot tables have different strengths: a storyboard gives annotated per-shot direction sketches (景别/运镜/动作); a shot table renders the model's native 分镜表 concept — the complete SEG shot sequence, numbered panels, no text, no style constraints. The choice between them belongs to the user.
- Do not modify, fill, summarize, explain, label, wrap, or append anything to either fixed prompt.
- If the requested prompt type is unclear and cannot be inferred, ask only whether the user wants the storyboard prompt or the shot-table 分镜表 prompt.

## Full-chain sequence (only on explicit request)

Run this only when the user explicitly asks for the full downstream chain; never volunteer it:

1. Produce the source-preserving `SEG` breakdown.
2. Ask whether visual optimization is wanted.
3. Create or explicitly skip scene-layout SVGs when spatial planning is requested.
4. Produce the processed director script from the selected `SEG` version.
5. Validate shot, action, spatial, prop, eyeline, screen-direction, and camera continuity internally.
6. After the director script is accepted, ask whether the user wants the storyboard prompt or the shot-table 分镜表 prompt.
7. Output the selected fixed prompt verbatim and stop for returned-board review.

For a one-product request, complete only that product. Tutorial order is not an eligibility requirement.

## Output gates (full-chain runs only)

- `WAITING_FOR_SEG_VISUAL_OPTIMIZATION_DECISION`
- `WAITING_FOR_SCENE_LAYOUT_SVG_REVIEW`
- `WAITING_FOR_DIRECTOR_SCRIPT_APPROVAL`
- `WAITING_FOR_BOARD_FORM_DECISION`
- `WAITING_FOR_RETURNED_BOARD_REVIEW`
- `READY_FOR_FIXED_STORYBOARD_PROMPT`

Gates apply only inside an explicitly requested full-chain run; a single-product request has no gates. The fixed storyboard-prompt steps override every general output convention: return only the template text.

## Boundaries

- Do not originate, rewrite, validate, or doctor a screenplay as a screenplay.
- Do not design character, group, scale, prop, scene, or other static assets.
- Do not design performance, dialogue, vocal delivery, timing performance, or audio design.
- Do not choose Route A/B or assemble a final image-to-video or text-to-video prompt.
- Keep the canonical storyboard style block and both fixed prompt templates unchanged unless the user explicitly requests an exact template edit. For an authorized edit, change only the named text surface and preserve the rest verbatim.
