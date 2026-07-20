# Director Design Craft

How to design the drama, motion, interaction, dialogue, timing, and sound of one executable AI-video prompt. Apply only the sections the current task needs. What the finished body must look like lives in `contract.md`.

## 1. Build The Dramatic Chain

Resolve these questions internally before writing cues:

1. What does each performer want in the current beat?
2. What blocks that action now?
3. What is the playable tactic?
4. What triggers the first visible change?
5. Who initiates, who responds, and what relationship state lands at the end?

Keep the chain continuous across the whole requested scope. Each unit needs only its current causal link; do not repeat the full analysis in every line.

## 2. Choose And Keep The Execution Unit Executable

- Use one `Action` for a continuous process, add `Timing/beats` only when sequence or synchronization matters, and use Shot blocks only for multiple or authoritative shots. Do not turn a single continuous take into `Shot 1` merely to satisfy a format.
- Preserve every approved action, but identify one primary action and one dominant camera behavior for each execution unit unless the shot authority explicitly locks more. Keep supplied continuous background processes low-weight instead of turning them into additional choreography.
- Use plain visible nouns and verbs. State only the path, direction, timing, or landing needed to make the approved action unambiguous; do not infer gait mechanics, force, weight transfer, micro-gestures, or secondary body reactions.
- Use short sequential beats only when their order or timing matters. A short execution unit should not exceed one or two source-supported primary beats; continuous background state does not create another beat.
- Use counts or steps only when the source locks them or exact synchronization requires them. Never invent a step count to make ordinary movement sound more precise.
- If a prompt or returned video becomes chaotic, first simplify the camera behavior, action, or background, then add back one constraint at a time.

## 3. Stage Interaction As Relationship Change

For two or more performers, establish only the spatial facts that affect the interaction:

- initial relation: distance, gaze, orientation, visibility, occlusion, access, or route;
- trigger: sound, look, line, prop, approach, interruption, or unexpected movement;
- initiative: one performer acts with a readable tactic;
- response: another performer changes attention, position, action, or refusal;
- landing: someone changes another person's route, distance, control, access, or emotional cover.

Use observation, concealment, approach, pursuit, withdrawal, interception, yielding, blocking, passing, shared prop contact, or deliberate stillness when supported by the material. Avoid stand-and-deliver dialogue when the relationship should be changing.

In group scenes, give the primary action full clarity and compress the group into one shared low-weight response unless an individual response changes the story.

## 4. Design Dialogue For Action

- Preserve locked wording, speaker, and order exactly.
- Check that each line fits the available duration with room for breath, pause, interruption, and listener response.
- Attach dialogue to an action, withheld action, or change of tactic. Do not decorate every line with a gesture.
- Give the speaker at most one action or state that changes delivery.
- Give the listener at most the first useful response unless later reactions create a new beat.
- Control lip movement only when sync, deliberate silence, closed-mouth listening, overlap, or off-screen delivery matters.
- Propose new wording only when the user requests dialogue writing or revision. Mark proposed lines clearly until approved.
- Preserve supported voiceover, off-screen speech, phone/radio speech, overlap, and silence when the task includes them; report technical conflicts instead of silently converting the mode.

## 5. Use Timing Without False Precision

When reliable timing exists and materially affects execution:

- keep ranges ordered, continuous when the task requires continuity, and non-overlapping unless overlap is intentional;
- budget spoken words, breath, action preparation, contact, reaction, and settling time;
- place the cause before the response and allow the response to register;
- shorten the action or flag a duration conflict when the beat cannot fit.

When exact timing is unnecessary, keep the order inside `Action` with relative timing such as `先`, `随即`, `停半拍`, `被打断后`, and `落稳后`. A timecoded body requires a user-supplied or explicitly approved target duration; ask for it instead of inventing seconds.

## 6. Place Sound At Causal Points

Use sound when it changes action timing, attention, space, or relationship:

- an approaching sound triggers a look or concealment;
- a contact sound confirms impact, placement, release, or breakage;
- a sound stops with the performer and makes the stop legible;
- a door, object, device, or voice reveals new information;
- a brief sound accent lands a relationship or emotional turn.

Write one complete non-musical sound bed for the scope: ambience, room tone, necessary routine foley, action-triggered sound, spatial acoustics, transitions, and meaningful silence. Keep the global bed concise; move a sound into its beat or Shot only when the exact trigger changes action or editing.

## 7. Assign Reference Roles

Use each supplied reference for the evidence it can reliably carry:

- character images: identity and visible state;
- storyboards or shot material: existing spatial and camera decisions;
- action video: mechanics, weight, rhythm, and contact;
- audio: delivery, cadence, voice continuity, and sound timing;
- scripts and notes: story authority, dialogue, intention, and constraints.

The user may override this allocation. When references conflict, preserve the declared authority and record the unresolved execution risk briefly.

## 8. Compress For Execution

For each chosen execution unit, write:

1. the dominant action;
2. the trigger or first response when it changes execution;
3. the relationship landing when it is not already visible in the action;
4. exact dialogue at the moment it is spoken;
5. the key sound only when it times or lands the beat.

One or two sentences per unit is usually enough. Merge the ending state into the last action instead of adding a repeated summary. Do not add an unlabeled story paragraph beside Action, beats, or Shots.

## 9. Strong/Weak Pairs

- Weak: 她很伤心地站在那里，气氛压抑，情绪拉满。
- Strong: 她背对柜台站定，手指反复摩挲围裙边，听到脚步声呼吸停半拍，没有回头。
- Weak: 镜头炫酷地运动，电影感十足。
- Strong: 机位从柜台端头齐胸高度起，随她的移动向左缓慢横移，在她停步时同步落定，浅景深让背景货架虚化。
- Weak: 上一镜里他刚展开伞，被外露的尖端吓了一跳。
- Strong: 开场承接：伞已完全展开停在前挡附近，外露尖端已经露出，右手已停在尖端旁。

The strong version converts psychology into gaze, breath, posture, and action, and gives camera movement a start, path, motivation, and landing; the weak version stacks judgments the model cannot execute. Entry states follow the same rule: write states the model can render at frame one, not events it must remember — and carry the prior shot's landing only when the two shots are visibly continuous; a fresh setup defines its own frame-one state instead.
