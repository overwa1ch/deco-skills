# Scene Layout SVG Rules

Use after a screenplay is locked/approved and before converting it into a processed director script.

## Purpose

Create one simple topdown spatial check per screenplay scene before director-script camera and blocking decisions.

## Gate

- Ask first: `要不要先给每个场景画一张极简俯视布局 SVG？`
- If the user agrees, create one SVG per screenplay scene.
- After creating the SVGs, stop at `WAITING_FOR_SCENE_LAYOUT_SVG_REVIEW`.
- Continue to `SEG`, visual optimization, or processed director script only after the user approves the SVGs or skips the gate.

## Output

Create local `.svg` files, one per scene, with clear names such as:

```text
<project-or-title>-scene-01-layout.svg
<project-or-title>-scene-02-layout.svg
```

If the scene count is small and the user asks for one file, a single multi-panel SVG is acceptable, but default to one SVG per scene.

## Drawing Rules

Use simple geometric shapes only:

- Room or location boundary.
- Major doors, windows, entrances, exits, or partitions.
- Main furniture or large spatial anchors.
- Main character positions at the scene's starting state.
- Scene label and short labels for characters / key spatial anchors.

Default to static layout only.

Keep out:

- movement arrows or blocking paths unless requested
- camera positions, camera-side zones, focal lengths, shot numbers, coverage diagrams, frame boundaries
- storyboard panels, `Bxx`, standalone video-generation timestamp prompts, video prompts
- small prop ledgers, decorative objects, texture, lighting design, style concepts
- minor items that do not affect spatial understanding

## Content Selection

For each scene, include:

- The minimum space needed to understand where characters start.
- The minimum furniture/partition layout needed to explain interaction.
- Key fixed obstacles that affect later blocking.

Leave dramatically important small props to the screenplay/director script when they do not affect spatial layout.

## Review Criteria

Before stopping for review, check:

- Scene count: one SVG exists for each screenplay scene.
- Layout clarity: the viewer can tell where characters are and what major spatial areas exist.
- Simplicity: no clutter, no small prop overload, no camera/shot/storyboard content.
- Source fidelity: locations and character positions match the screenplay.
- Technical validity: each SVG parses as valid XML.

## Review Prompt

After creating the SVGs, tell the user:

```text
场景俯视布局 SVG 已画完，请先审查空间和人物位置是否对。通过后我再继续转 processed director script。
```
