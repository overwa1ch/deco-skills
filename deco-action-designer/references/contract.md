# Director Body Contract（单一真源）

What the finished director-design body must be. All structure and output rules live here; `craft.md` owns method. Type conventions: English control labels, Chinese content, and the fixed Chinese `避免：` label.

## Fixed structure (in order)

1. `Style:` `Lighting:` `Camera:` — required prefix blocks.
2. `Color:` `Acting:` `Continuity:` `Physics:` — conditional, only when they materially control generation, in this order between `Camera` and `Audio`.
3. `Audio:` — required; starts with `无BGM。`.
4. One source-preserving execution-structure paragraph — unlabeled, opens with `[目标时长]秒[段落名称或场景功能]。`.
5. One or more timecoded `**Shot N [start-end s]**` blocks.
6. `避免：` — required.

The body starts directly at `Style:`. No meta headers (`风格前缀：` is retired), no `Reference:` line, platform handles, `Mixed N`, upload order, Asset List, Reference List, or Route headings.

## Block specs

### Style
Visible medium, realism level, period, production world, image texture, and explicit style exclusions. Concrete controls before prestige labels; keep `8K IMAX`, film-stock, frame-rate, or shutter language only when it supports the requested camera character. Derive from the current material — never reuse a generic style paragraph when the world, medium, era, light, or camera language differs.

### Lighting
Motivated sources, direction, color temperature or warm/cool relation when useful, subject/background exposure relation, atmosphere, and any story-driven light change. Preserve practical spatial facts such as which area stays dark or out of frame.

### Camera
The shared capture language only: lens behavior, depth of field, stability, handheld character, dominant movement logic, edit or continuous-shot logic, and the story motivation for movement. Leave focal length, position, foreground, path, and landing of each shot to the Shot blocks. Picture-edit logic lives here; sound-edit behavior (J/L-cuts) lives in `Audio`.

Use `固定机位` only for a camera with no translation or rotation; never pair it with push, pull, pan, tilt, track, or orbit. When Shots use different positions, keep `Camera:` at the shared level and leave positions to the Shots. Global and Shot-level camera rules must not contradict.

### Conditional blocks
- `Color:` decisive palette, saturation, contrast, and material colors that must stay stable.
- `Acting:` ensemble-wide performance density, vocal weight, dialogue mode, restraint, theatricality, or lip-sync rules.
- `Continuity:` identities, wardrobe, props, hand use, positions, states, and cross-shot invariants. This is the invariants block — returned-video revisions cite it.
- `Physics:` visible rules for water, smoke, cloth, impact, reflection, transformation, or occlusion transitions.

### Audio
Start with `无BGM。`, then the complete non-musical sound design: ambience, room tone, silence, foley, action-triggered sound, spatial acoustics, and sound transitions (J-cut / L-cut when supported). Dialogue wording, delivery, and voice performance stay in `Acting` or the relevant Shot; use `Audio` only for the acoustic space or edit behavior of the voice. Repeat a decisive sound again at its exact Shot moment only when the trigger changes action or editing.

### Execution-structure paragraph
One source-preserving paragraph fixing: target duration and scene function; entry state inherited from the prior moment when supplied; people, objects, and spatial relationship; the concrete dramatic process to execute; the visible ending state or handoff. Do not repeat the prefix. Do not add dialogue, turns, motives, events, or outcomes. This is the causal spine shared by all Shots.

When the delivery is a sequence of independently generated clips, judge each cut. If the shot **visibly continues the prior shot's state chain**（同一空间、同一产品状态、同一动作线）, open the paragraph with `开场承接：` followed by the prior shot's landing written as visible facts already true at 0.0s（已展开、已停在、已松开）, never as narrated history — generation models render present state at frame one; they cannot remember or depict "what just happened". If the cut starts a fresh setup（转场、时间或空间跳跃、独立插入镜）, do not import the prior landing: establish this shot's own 0.0s state and let the `Continuity:` block alone carry identity and world facts.

### Shot blocks
For every Shot, include only useful controls: exact time range within the target duration; shot size, focal character when useful, camera position; foreground, subject, background, screen direction, spatial relation when they affect readability; motivated camera movement with start, path, subject relation, and landing; primary action, follow-through, listener response, relationship landing; locked dialogue at the moment spoken with concise delivery guidance; decisive sound at its visible trigger.

One Shot carries one main story job. Preserve the shot authority exactly (storyboard, else director script, else locked material). When no approved shot structure exists, create only the minimum Shots needed, source-preserving. Only when the material leaves shot count open, use the fewest shots that can execute the process.

### 避免
Prioritize the likely failure modes of this exact generation: wrong identity, costume, prop, or hand use; wrong entrance, position, orientation, background, or spatial direction; wrong action, reaction, dialogue, sound, or duration; camera behavior that breaks the intended language; unwanted text, subtitles, watermark, face drift, style drift, or unsupported effects. Not a history of every past model failure — keep the highest-risk constraints.

## Output discipline（跨块规则，只在此处声明）

- Preserve locked dialogue wording, speaker, and order exactly.
- State each control at its owning layer: shared rules in the prefix, causal spine in the execution paragraph, moment-specific execution in Shots, likely failures in `避免：`. Do not restate unchanged information across layers.
- Budgets: one or two sentences per prefix block; one or two sentences for the execution paragraph; one compact execution paragraph per Shot plus necessary dialogue or audio triggers; four to eight grouped `避免：` clauses. Exceed only when supplied complexity requires it.
- Shot ranges are ordered, consistent with the declared duration, and never exceed it.
- ASCII square brackets for time ranges and inline annotations: `Shot 1 [0.0-5.0s]`, `角色[压低声音]：「台词」`, `[Audio触发点：……]`. No full-width parentheses in the finished body.
- Keep psychological reasoning internal; convert it into gaze, breath, posture, action, pause, voice, distance, contact, or refusal.
- Return only the finished body — no drafting structure, notes, or analysis.

## Template skeleton

```text
Style: [可见媒介、真实度、年代、制作世界、影像质感与关键风格排除。]
Lighting: [光源、方向、色温或冷暖关系、主体与背景明暗、空气状态和剧情性光线变化。]
Camera: [全段共同的摄影质感、景深、稳定性、运镜逻辑、剪辑或连续镜头逻辑，以及镜头运动的情节动机。]
[可选：Color: 决定性的综合色彩系统。]
[可选：Acting: 全段共同的表演密度、声线、对白模式或群体表演规则。]
[可选：Continuity: 跨镜头必须保持的身份、妆造、道具、站位与状态。]
[可选：Physics: 水、烟、布料、碰撞、倒影、变形或遮挡转场等物理规则。]
Audio: 无BGM。[环境声、静默、拟音、动作触发音、空间声学和声音转场。]

[目标时长]秒[段落名称或场景功能]。[只根据已批准材料写明承接状态、人物与道具、空间关系、具体执行过程和结尾状态，不新增剧情。]

**Shot 1 [开始-结束s]**
[景别、焦段特征或镜头距离、机位、前景/主体/背景、运镜起点与落点、人物动作与反应、关系落点。]
[角色][说话方式]：「锁定台词」
[必要时：Audio触发点。]

[按需继续 Shot 2、Shot 3……]

避免：[只写本段最高风险的身份、空间、动作、声音、连续性、时长、文字和风格错误。]
```

## Pre-flight checklist

- Does every action have a playable verb and physically reachable target, with cause before response?
- Do follow-through and environment changes support the primary motion rather than compete with it?
- Does each interaction change distance, attention, access, route, control, or concealment when the story requires a turn?
- Are locked lines verbatim, naturally timed, with silence/overlap/voice mode/lip sync handled only where relevant?
- Does `Audio` open with `无BGM。` and provide a complete concise sound bed, with Shot-level repetition only at causal triggers?
- Does the prefix reflect the actual supplied world rather than a generic reusable paragraph?
- Is the body free of `风格前缀：`, `Reference:`, platform handles, and Route/Asset/Reference-List content?
- Does every Shot preserve the shot authority; are any added Shot decisions minimal and source-preserving?
- Do global and Shot-level camera rules agree; is every `固定机位` genuinely motionless?
- Do Shot ranges fit the declared duration exactly; are brackets ASCII?
- Does the execution paragraph define entry, supplied process, and ending state without adding story?
- Are conditional blocks present only when they materially control generation?
- Does the product stay inside director-design responsibility?

## Gold example（最终输出形态）

```text
Style: 写实电影质感，1985年中国北方县城供销社，自然主义表演，胶片颗粒与低饱和色调，无任何现代元素。
Lighting: 冬末上午的冷白天光从临街玻璃窗斜入，与货架上方日光灯偏绿的光混合，柜台区亮、货架深处暗，空气中有浮尘。
Camera: 中焦为主的稳定机位组，浅景深突出人物，运镜只服务注意力转移，两个镜头之间为硬切。
Continuity: 陈秀兰45岁，深蓝的确良工作外套、齐耳短发别黑色发卡；刘小根16岁，灰色学徒褂、袖口过长；搪瓷缸白底红字；两人相对位置以柜台L形转角为锚。
Audio: 无BGM。营业厅空旷的房间音，远处算盘声与街道人声垫底；搪瓷缸落地的碎裂声是全段声音焦点，碎裂后半秒静默，再进扫帚与瓷片的刮擦声。

10秒双人柜台戏。承接上一段：陈秀兰在柜台后核对账本，刘小根在L形转角外侧货架前擦拭搪瓷缸。搪瓷缸脱手落地碎裂，刘小根慌忙蹲下徒手去捡，陈秀兰放下笔绕出柜台，用鞋尖把最大的瓷片拨向墙角，递下一句话；段落结束于刘小根起身取扫帚、陈秀兰转身回柜台的状态。

**Shot 1 [0.0-4.0s]**
中景，柜台L形转角为前景，刘小根为主体，背景货架虚化。他左手扶缸右手擦拭，缸沿一滑脱手，搪瓷缸砸在水磨石地面碎裂弹开；他肩膀一缩，立即蹲下伸手去抓最近的碎片。
[Audio触发点：0.8s碎裂声，随后半秒全场静默。]

**Shot 2 [4.0-10.0s]**
中近景，机位在柜台内侧齐胸高度，陈秀兰为主体。她笔尖一顿，合上账本绕出柜台走向刘小根，两步落定，用鞋尖把最大的瓷片拨向墙角，低头看他。
陈秀兰[平静，不高]：「先扫，别用手。」
刘小根[小声]：「哎。」
她转身回柜台，背景里刘小根起身去取靠在货架边的扫帚。
[Audio触发点：9.0s扫帚落地的第一声刮擦。]

避免：陈秀兰面部与基础角色参考不一致、刘小根学徒褂消失或改样、搪瓷缸碎裂前后位置跳变、画面出现字幕或任何文字、镜头越过柜台轴线、碎裂声与画面不同步、总时长超过10秒。
```

示例演示的约定：正文直接以 `Style:` 开头；条件块只用了 `Continuity`（其余省略）；`Audio` 以 `无BGM。` 开头并给完整声床；执行段承接—过程—结尾且不加戏；因先于果（碎裂声在前，反应在后）；心理转化为可见动作（肩膀一缩、笔尖一顿）；台词逐字挂在时间点上；ASCII 方括号；`避免：` 七条按当次风险分组。
