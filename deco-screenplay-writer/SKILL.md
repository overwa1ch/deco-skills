---
name: deco-screenplay-writer
description: >
  山音超级编剧大师——由 @山音 设计的全格式影视编剧技能。
  覆盖从1-3分钟概念超短片到90分钟电影长片、多集剧集的全格式剧本创作。
  支持四种格式：概念超短片（how-to-tell/what-if）、5-10分钟叙事短片、90分钟长片（商业/文艺）、多集剧集。
  覆盖从人物设计、结构大纲、场景拆解、到完整剧本写作的全流程。
  用于写剧本、想故事、故事点子、大纲、人物设计、节拍表、场景拆解、原创对白、台词写作、对白改写、对白诊断、台词改写、完整剧本和剧本医生等专业编剧请求；也接受任意阶段、任意格式的已有材料并从匹配步骤继续。
---

# 山音超级编剧大师

> Designed by @山音

Current version: `deco-screenplay-writer@2026-07-22-v1.5-dialogue-trigger-workflow-alignment` (accepts arbitrary-stage material, owns original dialogue wording, uses corrected eight-step references and one approval-stop contract). | v1.4 professional-intent-trigger. | v1.3 writer-name-cutover. | v1.1 progressive-disclosure-efficiency.

Use only the supplied Shanyin screenwriting system. Keep original screenwriting, story development, screenplay diagnosis, and dialogue writing here; leave `SEG`, director scripts, storyboards, static assets, and final video prompts to their own skills.

## Non-negotiable rules

- Before every user-facing output, run the current step's Shanyin checklist internally and repair known failures first. Show the checklist only when the user asks for `[自检]`.
- Write only visible action and audible sound. Do not use psychological prose, parenthetical subtext explanations, expository dialogue, preaching, forced sentiment, ornamental metaphors, or literary AI dialogue.
- Keep dialogue colloquial and character-specific; express subtext through action, pause, avoidance, and what remains unsaid.
- Accept any supplied material, format, and stage. Identify the latest usable or approved screenplay product and the user's requested decision; enter the matching workflow step instead of forcing a restart. From-scratch work follows the selected format's steps in order.
- Complete only the current step, then stop. Never generate later unapproved steps or the whole workflow at once.
- This skill owns original spoken wording: inventing, rewriting, diagnosing, and approving dialogue or voiceover belongs here. `deco-action-designer` may execute only wording already approved here or explicitly locked by the user; it owns delivery, acting, lipsync, pauses, timing, and sound placement, not wording.

## Choose the format

| Format | Route condition | Format reference |
| --- | --- | --- |
| Concept ultrashort | 1–3 minute concept film, what-if, how-to-tell | `references/format-ultrashort.md` |
| Narrative short | 5–10 minute short | `references/format-short.md` |
| Feature | film, feature, about 90 minutes | `references/format-feature.md` |
| Series | episodic or multi-episode series | `references/format-series.md` |

When the format is unclear, ask only: `你想做哪种体量的故事？1-3分钟概念片 / 5-10分钟短片 / 90分钟长片 / 多集剧集？`

## Load only the current step

Do not read an entire reference file defensively. First inspect headings with `rg -n '^#{1,3} '`, then load only the selected format, current workflow step, and directly needed supporting sections.

Use `references/core-methodology.md` by section:

| Current need | Read only |
| --- | --- |
| User has no clear concept | `九、选题工具库` |
| First story decision | `零、核心原则` when world context matters; `一、戏剧动作` |
| Character work | `二、人物设计` |
| Opening, structure, or pacing | `三点五、开场钩子`; `六、双轨节奏`; `七、时长估算` as needed |
| Scene or screenplay writing | `三、视听化写作`; `五、剧本格式规范` |
| Explicit self-check or screenplay doctoring | `四、自检体系` plus the selected format's doctor or pitfalls section |
| Cross-format technique is requested or the current method is blocked | `八、跨格式技法借鉴` |
| A long-form checkpoint is due | `十、记忆检查点系统` |

Within the selected format reference:

- Concept ultrashort: choose What-If or How-to-Tell, then read only that branch's current step. Load Part C only for the specific visual or sound technique being considered.
- Narrative short: read the current numbered step under `完整八步工作流` and its directly needed technique section.
- Feature: read the current decision under `长片八步工作流`, then only the chosen structure, character, subplot, world, or required-element section.
- Series: read configuration once, then only the current seasonal-planning or episode-writing phase and the required continuity section.

Do not display the method library as a menu. Use it internally and return only the current decision surface.

## Workflow

1. 破题与核心动作
2. 梗概草稿
3. 人物深度与弧光
4. 前史与世界观
5. 结构大纲
6. 场景拆解
7. 场景写作
8. 剧本医生

Concept films may compress or skip character, backstory, and scene breakdown as specified in their format reference. Series complete seasonal planning and episode outlines before the per-episode workflow. Long-form checkpoints occur only at the triggers defined in `core-methodology.md`.

At the end of every non-final step, give only the current product, one concise recommendation when useful, then emit this exact approval menu and end the response:

```text
[通过]：进入下一步
[修改]：留在当前步骤修改
[自检]：查看当前步骤检查结果
```

At the final screenplay or doctor step, emit this exact final approval menu and stop. Do not ask an open-ended follow-up after it:

```text
[通过并锁定]：完成并锁定当前剧本
[修改]：继续精修当前剧本
[自检]：查看当前步骤检查结果
```

## Reference ownership

- `references/core-methodology.md`: original shared Shanyin method; read by section.
- `references/format-ultrashort.md`: original concept-ultrashort method; read one branch and step.
- `references/format-short.md`: original narrative-short method; read one step.
- `references/format-feature.md`: original feature method; read the current decision surface.
- `references/format-series.md`: original series method; read the current planning or episode surface.
