# Adaptive Director Body Contract（单一真源）

Define the finished `deco-action-designer` body here. `craft.md` owns method; this file owns field selection, execution-carrier selection, formatting, and reviewable completeness.

## Core rule

First identify information that is present in the supplied material and materially controls generation. Output only the fields that carry that information.

- Do not output an empty field, placeholder, a standalone `无` or `不适用` field value, or filler written only to complete a schema.
- Give each fact one owning field. If another field already expresses it completely, omit the duplicate field or sentence.
- An omitted field is not a defect unless its missing information makes this task non-executable.
- `Audio` always carries real content because every Deco director body requires no BGM and a complete non-musical sound state. Designed silence is content; an empty audio placeholder is not.

## Canonical field order

Keep every field that is used in this relative order. There is no required-field checklist apart from the substantive `Audio` contract above.

```text
Use case:
Primary request:
Scene/background:
Subject:
Style/format:
Lighting/mood:
Color palette:
Camera:
Acting:
Continuity:
Physics:
Action:
Timing/beats:
Audio:
Text (verbatim):
Dialogue:
Constraints:
Avoid:
```

When Shot blocks are the execution carrier, place them where `Action` and `Timing/beats` would appear: after any used `Physics` field and before `Audio`. Do not add a replacement summary paragraph.

The body starts directly at its first populated field. Do not add a title, preface, `风格前缀：`, `Reference:`, platform handle, `Mixed N`, upload order, Asset List, Reference List, or Route heading.

## Choose one execution carrier

### Action only

Use `Action:` for one continuous action when exact internal timing is not needed. Do not create `Timing/beats`, `Shot 1`, or an unlabeled story summary.

### Action plus Timing/beats

Use `Action:` plus `Timing/beats:` for a single shot or continuous take whose order, synchronization, or stage change matters. Let `Action` own only participant or tool roles and the overall task identity; let the beats own every ordered step, stage change, sound trigger, and landing. Do not repeat the beat verbs or ending inside `Action`, and do not create `Shot 1` or an unlabeled story summary.

### Shot blocks

Use one or more `**Shot N [start-end s]**` blocks only when:

- the material contains multiple shots;
- an approved storyboard, director script, or other shot authority locks shot decisions; or
- the user explicitly requests Shot output.

Preserve authoritative shot count, order, framing, movement, action, space, props, dialogue, and outcomes. When shot count is genuinely open, use the fewest shots that execute the supplied process. With Shot blocks, omit global `Action:`, `Timing/beats:`, and any unlabeled execution-summary paragraph.

Every exact time range requires a user-supplied or explicitly approved target duration. Keep ranges ordered and within that duration; do not invent seconds.

## Field specs

### Use case

Include only when the evaluation purpose, test target, platform task, or downstream use changes how the model should execute the request.

### Primary request

State the requested deliverable and decisive format facts only when they are not already fully carried by another field.

### Scene/background

Describe the visible setting, background occupancy, era, or spatial context that must be generated. Omit it when a supplied image already fixes the background and no change or preservation instruction is needed.

### Subject

Name the visible people, objects, materials, or products and their initial relevant state. Do not use this field as a continuity checklist.

### Style/format

Specify visible medium, realism, image texture, capture character, period treatment, aspect ratio, or decisive format only when the task supplies or needs them. Translate abstract praise into visible controls. Do not invent a prestige style paragraph.

### Lighting/mood

Specify motivated sources, direction, subject/background exposure, atmosphere, or a story-driven light change only when light materially controls the result.

### Color palette

Specify stable palette, saturation, contrast, or material color relationships only when color is independently controlled.

### Camera

State shared framing or capture behavior: shot size, angle, lens character, depth of field, stability, movement, edit logic, or aspect ratio, but only the controls that matter. In Shot mode, keep shot-specific position, path, subject relation, and landing inside each Shot.

Use `固定机位` only when the camera has no translation or rotation; never pair it with push, pull, pan, tilt, track, or orbit.

### Acting

Use only for actual human or character performance, vocal weight, dialogue mode, restraint, theatricality, listener behavior, or lip-sync control. Object motion, hands performing a craft operation, and ordinary subject movement do not automatically require `Acting`.

### Continuity

Use only for identity, wardrobe, prop, position, state, edit, or cross-shot invariants that must survive a cut or transformation. A single continuous action with no independent invariant does not require it.

### Physics

Use only for non-default material, fluid, smoke, cloth, collision, deformation, reflection, transformation, contact, or occlusion rules. State the causal physical behavior once; do not repeat it in `Action` or `Avoid` unless the latter names a distinct visible failure.

### Action

Write the primary visible process with playable verbs, reachable targets, cause before response, and the intended landing. Keep supplied actions; do not infer gait mechanics, force, weight transfer, micro-gestures, or secondary reactions.

### Timing/beats

Use short ordered beats only when timing or synchronization matters. Each beat owns its time-specific action, change, dialogue, visible text, or sound trigger. Use counts or steps only when the source locks them or synchronization requires them.

### Shot blocks

For each Shot, include only useful visible controls: time range, framing, camera position or movement, spatial relationship, primary action, first useful response, relationship landing, locked dialogue, visible text, and decisive sound trigger. One Shot has one main story job, one primary action, and one dominant camera behavior unless the shot authority explicitly locks more.

For independently generated clips, begin a visibly continuous Shot with the prior landing as facts already true at 0.0s. A fresh setup defines its own frame-one state. Never narrate history the model cannot remember.

### Audio

Start with `无BGM。`, then design the complete non-musical sound state that matters: ambience, room tone, foley, action-triggered sound, voice acoustics, spatial behavior, transitions, and meaningful silence. If the requested result is silent, state the designed silence precisely. Put an exact causal sound in a beat or Shot when its trigger controls timing; keep the global field for the shared sound bed.

### Text (verbatim)

Use only when the model must render exact visible text. Enclose every exact string in Chinese double quotation marks `“……”`. Put time-bound text in the relevant beat or Shot instead of repeating it here.

### Dialogue

Use only when actual spoken content exists. Preserve approved wording, speaker, order, voice mode, and delivery. Keep dialogue in `「……」`. Put time-bound dialogue in the relevant beat or Shot instead of repeating it here.

### Constraints

Include only positive invariants explicitly required by the material and not already owned by another field. Do not convert every descriptive fact into a constraint.

### Avoid

Include only likely, observable failure modes specific to this generation. Omit the field when no independent high-risk failure is present. Do not build a generic history of model failures or repeat positive rules in negative form.

## Output discipline

- Preserve locked story facts, dialogue, speaker, order, and outcomes exactly.
- Preserve supplied shot authority; compile it into executable model language without redesigning it.
- Keep psychological reasoning internal; convert it into gaze, breath, posture, action, pause, voice, distance, contact, or refusal only when supported.
- Keep each fact at one layer. Global fields own shared controls; Action, beats, or Shots own execution; `Constraints` owns unique positive invariants; `Avoid` owns distinct high-risk failures.
- Do not emit both a global execution summary and a detailed execution carrier.
- Use ASCII square brackets for time ranges and inline annotations: `Shot 1 [0.0-5.0s]`, `角色[压低声音]：「台词」`, `[Audio trigger: ...]`.
- Return only the finished body, without notes or analysis.

## Adaptive skeletons

### Continuous action

```text
[Only populated fields before execution, in canonical order.]
Action: [One continuous visible process and landing.]
Audio: 无BGM。[Complete non-musical sound state.]
[Only populated Text, Dialogue, Constraints, or Avoid fields, in canonical order.]
```

### Single shot with precise beats

```text
[Only populated fields before execution, in canonical order.]
Action: [Concise whole process.]
Timing/beats:
- [0.0-1.0s] [First meaningful stage.]
- [1.0-3.2s] [Second meaningful stage.]
- [3.2-4.0s] [Landing.]
Audio: 无BGM。[Complete non-musical sound state.]
[Only populated Text, Dialogue, Constraints, or Avoid fields, in canonical order.]
```

### Multiple or authoritative shots

```text
[Only populated global fields through Physics, in canonical order.]

**Shot 1 [start-end s]**
[Only this Shot's executable visible and audible controls.]

**Shot 2 [start-end s]**
[Only this Shot's executable visible and audible controls.]

Audio: 无BGM。[Shared non-musical sound state not already owned by a Shot trigger.]
[Only populated Text, Dialogue, Constraints, or Avoid fields, in canonical order.]
```

## Gold example: 4-second clay test

```text
Use case: AI视频模型的手部与软质材料物理连续性测试。
Primary request: 生成一条写实的4秒竖屏手作视频。
Scene/background: 简洁的浅灰白桌面，安静室内，没有其他工具或杂物。
Subject: 一双结构自然稳定的成人手；一个手掌大小的白色黏土半身像，开场时已有完整脸部、头颈、肩膀和多层衣褶，后脑没有头发。
Style/format: 9:16竖屏写实手机手作教程质感，连续实拍感，无定格动画或跳帧。
Lighting/mood: 柔和均匀的中性顶光，白色黏土纹理清楚。
Camera: 固定俯斜微距近景，主体居中，全程无变焦、摇移或切镜。
Physics: 黏土只在手指实际接触并施压的位置变形，附加块逐步与后脑融合，不自行融化、增殖或瞬间变形。
Action: 一只手全程只负责托稳半身像，另一只手是唯一塑形执行者，只处理后脑的附加黏土。
Timing/beats:
- [0.0-1.0s] 独立小块黏土被贴稳在后脑。
- [1.0-3.2s] 指腹沿上缘和两侧接缝按压、推开并向下抹合。
- [3.2-4.0s] 手指离开，完成状态稳定展示。
Audio: 无BGM。只有轻微室内底噪和指腹摩擦柔软黏土的近距离声音，无旁白。
Constraints: 始终只有一个半身像和一块附加黏土；既有脸部、衣褶、肩膀和整体比例保持不变。
Avoid: 多指或缺指，手指穿透黏土，手与雕像粘连，雕像重置或复制，新增工具，字幕、水印或任何文字。
```

The example intentionally has no `Acting`, `Continuity`, `Color palette`, story summary, or `Shot 1`; `Action` owns hand roles and the overall landing, `Timing/beats` owns step detail, and physics, invariants, and failure modes each have one owner.

## Pre-flight checklist

- Does every emitted field carry unique task-specific control information?
- Are empty fields, placeholders, filler, and redundant restatements absent?
- Is the execution carrier the smallest sufficient one: Action, Action plus Timing/beats, or Shots?
- If Shots are used, are global Action, Timing/beats, and an unlabeled execution summary absent?
- If exact time ranges are used, do they fit the approved duration?
- Are cause, action, response, and landing executable and source-preserving?
- Are `Acting`, `Continuity`, and `Physics` present only for their actual professional purposes?
- Does `Audio` start with `无BGM。` and describe a substantive complete sound state?
- Are exact visible strings in `“……”` and dialogue in `「……」`, only when they exist?
- Do `Constraints` and `Avoid` contain unique information, and is `Avoid` omitted when there is no independent high-risk failure?
- Is the body free of `Reference:`, platform handles, and Route/Asset/Reference-List content?
- Does the product stay inside director-design responsibility?
