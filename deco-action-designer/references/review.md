# Returned-Video Review（回片评审）

Use when a generated video returns for acceptance. The delivered director body is the acceptance contract; approved storyboard or director-script authority stays higher if the body itself deviated from it.

## Procedure

Review text-first: ask the user to watch and report observations. Do not inspect frames by default; inspect a named moment only when the user explicitly requests it.

Choose the checklist unit from the body actually delivered:

- Shot blocks present: review Shot by Shot, then check declared cross-shot invariants.
- `Timing/beats` present: review beat by beat, then check the landing.
- `Action` only: review the complete continuous action from initial state through landing.

Accept partial evidence and state what remains unverified. Do not mark an omitted field as a failure. A missing field is a body defect only when the current generation needed that control and the omission made execution ambiguous or contradictory.

## Checks to apply when declared or materially required

1. **Duration and order:** declared duration and beats fit; cause precedes response; the landing registers.
2. **Subject and scene:** visible subjects, initial states, setting, and spatial facts match the body.
3. **Action fidelity:** the primary process, useful response, and landing occur as written; no unsupported choreography appears.
4. **Continuity:** when declared or required across cuts/states, identity, wardrobe, props, positions, and states remain invariant.
5. **Physics:** when declared, contact, deformation, fluid, cloth, collision, reflection, transformation, or occlusion behaves causally.
6. **Visible text:** every string in `“……”` renders verbatim at its declared moment; no conflicting text appears.
7. **Dialogue and acting:** approved wording, speaker, order, delivery, listener behavior, and lip sync hold where controlled.
8. **Camera, style, light, and color:** only the controls actually declared in these fields or Shots are acceptance criteria; no contradiction or unplanned camera move breaks execution.
9. **Audio:** `无BGM` holds; the designed ambience, foley, silence, causal triggers, voice acoustics, and transitions occur as written.
10. **Constraints and Avoid:** positive invariants hold and the specific listed failure modes do not occur.

## Findings and revision

For every material issue, report the execution unit and time when known, the observation, its impact, and the smallest concrete revision.

- Classify it as **body defect**, **generation variance**, or **platform limit** before changing anything.
- Change one owning field or execution unit per iteration when possible.
- Add `Continuity`, `Physics`, `Constraints`, or `Avoid` only when the observed problem proves that information is independently needed.
- Tighten `Avoid` with a recurring high-risk failure, not a cumulative history.
- Preserve every unaffected field, beat, Shot, dialogue line, timing, and outcome.

## Verdict

Return one verdict: **usable**, **usable with minor revisions**, or **revise and return**. Escalate story or shot-structure conflicts to the shot-authority owner instead of redesigning them here.
