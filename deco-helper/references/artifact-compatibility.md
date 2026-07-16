# Artifact Compatibility and Assembly Rules

Single source for cross-product compatibility review and final-assembly rules; SKILL.md and the templates cite this file instead of restating it. Review only whether the supplied products can be assembled for the user's requested route; assemble by the rules below. Preserve specialist content.

## Shared checks

- Confirm one current video scope or `SEG` label.
- Confirm one content type for the fixed tone line.
- Confirm that names for the same character, prop, place, and scope are unambiguous across products.
- Confirm that platform handles point to the user-intended references and every binding has a declared role.
- Confirm that the director-design product belongs to the current scope.
- Confirm that it contains `Style`, `Lighting`, `Camera`, `Audio: 无BGM。` (legacy bodies may use `SFX: 无BGM。`; both pass), one source-preserving execution paragraph, ordered timecoded Shots, and `避免`.
- Confirm that the director-design product contains no `Reference:` line, platform handle, `Reference List`, or `Asset List`.
- Confirm that Shot ranges fit the declared duration and unresolved issues do not block generation.

If names differ but identity is clear, normalize only the model-facing display label and keep a temporary mapping. If identity is unclear, request one binding decision.

## Route A checks

- A storyboard platform reference is present and covers the current scope.
- Necessary static references are bound by visible names and platform handles.
- The optional Preview image is included only when supplied and selected.
- The outer `Reference List` names the storyboard as the model-facing controller of shot order, camera movement, character action, spatial relationships, and prop relationships.
- The complete director-design product can be pasted unchanged.

## Route B checks

- Every model-facing reference has a quoted referable screen-object identity name, a platform handle, an asset form, and a role.
- Every entry maps to an actual approved finished file and confirmed platform handle. A multi-view, nine-grid, or multi-state board remains one asset; its panels, states, crops, details, and uses are not separate inventory entries unless separate finished assets and handles actually exist.
- The actual static references collectively cover every identity and structure that the current SEG cannot safely infer from text alone. Bind a multi-state board once and reuse its exact quoted identity name for every state or detail shown inside it; exclude unrelated inventory. If required coverage is absent, request a static-asset product instead of inventing an identity name or handle.
- Every asset in the outer `Asset List` uses `“[referable screen-object identity]” = @[confirmed platform handle] - [asset form and use]` and is cited by that exact same quoted identity inside each relevant timecoded Shot sentence where it is visible or controlling. A `Continuity`-only or summary-only citation fails. The quoted identity must grammatically denote the person, place, vehicle, or prop being controlled, such as `“车主”`, `“黑色内饰车辆”`, `“破旧长柄竞品”`, or `“AUTOWOEL前挡遮阳伞”`; asset-form labels such as `“人物三视图”` and `“场景九宫格”` fail. The raw handle stays in `Asset List`, and no separate `Asset Use:` or asset-summary block is present.
- The storyboard is absent from the model-facing outer `Asset List`.
- The director-design product contains enough timing, action, dialogue, camera, lighting, and audio detail for execution.
- The director sentence order and execution content can be preserved while minimal visible-name asset citations are inserted at the states they control; the trailing `避免：` clauses can be extracted once and moved into `Constraints` without content loss.

When director-design content is insufficient or internally contradictory, request a revised `deco-director-designer` product. Do not repair it during integration.

## Outer reference binding rule

Use only confirmed platform bindings that resolve to actual approved finished assets. Route A writes them in `Reference List`; Route B writes them in `Asset List` as `“[referable screen-object identity]” = @[confirmed platform handle] - [asset form and use]`. The equality binding makes the exact quoted identity name the Prompt-facing reference. The identity name must be usable in a natural execution sentence; keep asset format and role after the hyphen. Do not expose internal IDs, provisional references, invented derivative asset names, or invented semantic handles. Positional handles such as `@图片1` must follow the actual upload order for that SEG and remain in `Asset List`; Prompt cites the bound quoted identity name instead of repeating the positional handle.

Never add, replace, or rewrite a `Reference:` line inside the director-design body.

## Director-body preservation

Route A pastes the complete Director Designer body unchanged. Route B preserves the Director sentence order and execution content; the only permitted edits are inserting the minimal quoted-identity citation into the exact `Continuity`, execution, or Shot sentence each asset controls, and extracting the single trailing `避免：` line once into `Constraints` as `禁止出现：`. Never summarize, repair, retime, split, or duplicate director execution or audio design.

## One asset, one name

After binding, every mention of a bound asset anywhere in Prompt or Constraints uses its exact quoted identity name. Replace near-synonym aliases such as `人物`, `产品`, `商品`, `折叠体`, `对比产品`, `自家产品` with the bound name. Keep each product part to one canonical part name (once `软包端` and `外露硬端` are chosen, variants like `软包圆头` or `硬尖` are errors). Do not name an asset that is not bound in the current SEG; rewrite cross-SEG comparisons into results directly visible in this SEG. Image-form labels such as `人物三视图参考` and genre or technique words such as `产品演示` or `纸就产品` are not asset names and are exempt. `scripts/validate_route_b_prompt.py` reports generic alias tokens as errors.

## Final format check

- Route B contains no separate `影片调性` line; its film tone comes from the preserved Director `Style:` block.
- All template placeholders are replaced.
- The outer reference list matches the selected route and contains only confirmed bindings.
- The Route B asset-name set equals the actual approved asset inventory for that SEG; a reference board appears once regardless of how many internal panels or states are used.
- In Route B, Director sentence order, timings, actions, camera, acting, lighting, audio, dialogue, and outcomes match the approved product; differences are limited to inline citations using the exact quoted identity names bound in `Asset List`. Every listed identity appears in the timecoded Shot execution where it is used; `Continuity` alone does not count. No asset-form label is used as an identity citation, raw handles do not appear inside Prompt, no `Asset Use:` or asset-summary block exists, and the original `避免：` clauses appear once under `Constraints` as `禁止出现：`.
- Director bodies containing `Voiceover`, `Dialogue`, or other approved speech include `画面中不得生成文字、字幕或对白气泡。`
- If the director-design body contains approved voiceover or off-screen speech, use `不得添加导演正文之外的旁白、画外解说。`; otherwise use `无旁白、无画外解说。`. No separate no-BGM constraint is added outside the director-design `Audio` block (legacy bodies: `SFX`).
