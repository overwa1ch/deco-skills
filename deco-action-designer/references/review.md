# Returned-Video Review（回片评审）

Use when a generated video returns for acceptance. The delivered director body is the acceptance contract; the shot authority (approved storyboard, else director script) stays the higher authority if the body itself deviated from it.

## Procedure

Text-first: the user watches the returned video and reports observations in text; review those observations against the delivered body. Do not extract or inspect frames by default — agent visual review is slow; inspect a frame only when the user explicitly asks about a named moment. To make the user's viewing fast, derive a per-Shot checklist from the body (one line per Shot: the single thing to verify).

Review Shot by Shot against each declared time range, then check cross-shot continuity. Accept partial evidence (observations covering only some Shots) and state what remains unverified.

## Per-Shot checks

1. **Duration & order:** total length and each beat inside its Shot range; cause lands before response and the response registers.
2. **Identity & continuity:** faces, wardrobe, props, positions, and states match the `Continuity:` block and supplied references across shots; the first frame matches the body's opening entry-state facts（连续镜的开场承接，或独立镜自身的起始状态）.
3. **Action fidelity:** primary action, listener response, and relationship landing occur as written; no invented performance.
4. **Visible text:** every string declared inside `“……”` renders verbatim on the specified screen, paper, UI, sign, package, label, title card, or brand surface; no undeclared text appears.
5. **Dialogue:** wording verbatim, speaker, order, delivery mode; lip sync only where the body controls it; no phantom voiceover.
6. **Camera:** shared capture language holds; per-Shot position, movement path, and landing as written; no unplanned axis breaks or movement on a `固定机位`.
7. **Audio:** `无BGM` respected; causal triggers land at their moments; spatial acoustics plausible; no phantom music, narration, or off-screen explanation.
8. **Style & world:** period, medium, texture stay in world; no modern elements, undeclared text, subtitles, or watermarks.

## Findings and revision

For every material issue: Shot number and timecode, the observed problem, its impact, and the smallest concrete revision.

Revision discipline (regeneration usually replaces the whole segment):

- Restate invariants alongside every correction: keep or add the `Continuity:` block and name what must not change.
- Change one thing per iteration; tighten `避免：` with the observed failure only when it is a real recurrence risk, not as a growing history.
- Classify each issue before editing the body: a **body defect** (the prompt under-specified or contradicted itself — fix the body), **generation variance** (the body is right — regenerate, optionally tightening `Continuity`/`避免：`), or a **platform limit** (report it; do not silently redesign the scene to hide it).

## Verdict

One verdict: **usable**, **usable with minor revisions**, or **revise and return**. Escalate story or shot-structure conflicts to the shot-authority owner (storyboard or director script) instead of redesigning shots here.
