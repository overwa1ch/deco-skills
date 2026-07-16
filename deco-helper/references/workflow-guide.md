# Modular AI-Video Workflow Guide

Use this guide to explain the whole process and identify the next useful professional product. Treat the order as a recommended production path; adapt it to what the user already has.

## Design principle: visual results are the test suite

Every text design step must yield an artifact a human can judge at a glance — shot tables and storyboards test shot designs, Previews test visual direction, returned assets test asset prompts, returned clips test director bodies. Like tests in coding, these visual results let the human spot failures intuitively and fast. The agent designs and classifies in text; the human perceives in images; no expensive generation runs without a cheaper visual test before it.

## Recommended Path

Typical order: `deco-screenplay-director` → `deco-storyboard-designer` → `deco-static-asset-designer` → `deco-director-designer` → `deco-helper`（绑定与组装）. Adapt to what the user already has; every specialist is an on-demand menu, and parallel work is valid when products do not share an unresolved decision.

## Skill registry（职责与功能菜单，不含方法）

Route by this registry: name a function, hand off to its owner, accept the returned product. Methods live inside each skill; this file never carries them.

### deco-screenplay-director — 编剧
- 职责：原创编剧，从点子到锁定剧本；全家族唯一允许发明剧情的 skill。
- 功能菜单：故事点子与大纲、人物设计、节拍表、场景拆解、完整剧本（概念超短片至长片/剧集）、剧本医生。
- 何时调用：故事不存在、需要改写或需要医剧本时。

### deco-storyboard-designer — 分镜与板测试
- 职责：把锁定故事材料变成经过测试的分镜设计；板子首先是分镜测试仪，其次才是交付物。
- 功能菜单：拆SEG、场景布局SVG、视觉优化、处理版导演脚本、分镜设计与修订、固定故事板提示词、固定分镜表提示词、回板审查（文字审查；板执行失败/分镜设计失败/无法判定三分类路由）。
- 何时调用：需要设计镜头、用板子验证分镜、或审查回板时。

### deco-static-asset-designer — 静态资产
- 职责：跨镜头稳定的身份锚——人物、产品、场景、世界与风格。
- 功能菜单：资产方案、regional_anchor、style_aesthetic、人物主导Preview提示词与审查、生产资产提示词（基础角色/场景角色状态/匿名群体/角色比例/道具/地点参考）、多角度九宫格、回图资产审查。
- 何时调用：任何身份需要跨镜头保持一致、或审查回图资产时。

### deco-director-designer — 导演正文
- 职责：把已批准的镜头决策编译为可执行的导演提示词正文；回片验收归它。
- 功能菜单：写导演设计正文（含逐镜独立生成的开场承接）、审查提示词正文、回片审查（文字审查；正文缺陷/生成方差/平台限制三分类）。
- 何时调用：镜头决策已在、需要变成模型面执行文本时；或回片需要验收时。

### deco-visual-style-extractor — 风格提取
- 职责：从复杂参考中识别既有视觉风格并提取可复用风格系统。
- 功能菜单：风格识别与命名（查证已有术语，不自造）、风格规则与 keep/avoid 约束、prompt/JSON 模板、样本对比。
- 何时调用：复杂参考需要系统化风格提取时；用户自管交接，结果作为普通材料返回。

### deco-helper — 总控（本 skill）
- 职责：全家族唯一做路由的 skill；不含任何专业方法。
- 功能菜单：流程讲解、下一步判断、能力查询（本注册表）、跨产物兼容审查、平台参考绑定、Route A/B 最终组装与校验。

## Routing Judgment

1. Start from the user's requested outcome.
2. Credit every usable product the user already supplies, regardless of its format or production order.
3. Identify the first missing product that blocks the requested outcome.
4. Name one next professional task and its responsible skill.
5. Resume integration when that product returns.

## Storyboard Decision Gate

When the available product is a director script or shot sequence and the user asks what comes next:

1. If the director script is still awaiting approval, the next task is approval or revision. Do not jump to a fixed storyboard prompt.
2. Storyboard grades no longer exist. When the board form is unresolved, hand off the storyboard-versus-shot-table 分镜表 choice to `deco-storyboard-designer`; do not pre-select it.
3. Do not infer Route A/B during next-task routing. Route A eventually needs a storyboard as model-facing control. Route B does not make a storyboard model-facing and must not be forced through storyboard production unless the user wants that validation product.

When the director script is awaiting approval, use this handoff:

```text
下一项专业工作：审查并批准或修订当前导演脚本
推荐 skill：deco-storyboard-designer
需要返回的产物：已批准的导演脚本，或包含明确修订要求的新版本
```

When the board form is unresolved, use this handoff:

```text
下一项专业工作：选择故事板或分镜表；故事板长于单镜执行指令（带景别/运镜/动作标注），分镜表长于序列全貌（数字标序、无文字）
推荐 skill：deco-storyboard-designer
需要返回的产物：用户选择的固定故事板提示词或固定分镜表提示词
```

For a new static-asset system, the specialist's recommended internal sequence is: discuss and confirm the asset plan, `regional_anchor`, and `style_aesthetic`; test one person-led Preview prompt; confirm the test direction; write production asset prompts; approve each returned `Sxx location_reference`; then derive one multi-angle, multi-shot-size nine-grid reference for each scene. `deco-visual-style-extractor` may be used as an optional user-managed style-extraction handoff. `deco-helper` only explains this sequence and accepts the returned products.

Do not send the user backward merely because their materials arrived in a different order. Parallel specialist work is valid when the products do not depend on the same unresolved decision.
