# Modular AI-Video Workflow Guide

Use this guide to orient the user and identify the next useful professional product. Treat the order as a recommended production path; adapt it to what the user already has and expose only the part needed for the current step.

## Design principle: visual results are the test suite

Every text design step must yield an artifact a human can judge at a glance — shot tables and storyboards test shot designs, Previews test visual direction, returned assets test asset prompts, returned clips test director bodies. Like tests in coding, these visual results let the human spot failures intuitively and fast. The agent designs and classifies in text; the human perceives in images; no expensive generation runs without a cheaper visual test before it.

## Recommended Path

Keep `deco-helper` with the user throughout the process. A typical specialist order is `deco-screenplay-writer` → `deco-storyboard-designer` → `deco-static-asset-designer` → `deco-action-designer`, followed by Helper compatibility review, platform binding, and final assembly. Adapt to what the user already has; every specialist is an on-demand menu, and parallel work is valid when products do not share an unresolved decision.

## Skill registry（职责与功能菜单，不含方法）

Route by this registry: name a function, hand off to its owner, accept the returned product. Methods live inside each skill; this file never carries them.

### deco-screenplay-writer — 编剧
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

### deco-action-designer — 动作与导演执行
- 职责：把已批准的镜头决策编译为可执行的导演提示词正文；回片验收归它。
- 功能菜单：写导演设计正文（含逐镜独立生成的开场承接）、审查提示词正文、回片审查（文字审查；正文缺陷/生成方差/平台限制三分类）。
- 何时调用：镜头决策已在、需要变成模型面执行文本时；或回片需要验收时。

### deco-visual-style-extractor — 风格提取
- 职责：从复杂参考中识别既有视觉风格并提取可复用风格系统。
- 功能菜单：风格识别与命名（查证已有术语，不自造）、风格规则与 keep/avoid 约束、prompt/JSON 模板、样本对比。
- 何时调用：复杂参考需要系统化风格提取时；用户自管交接，结果作为普通材料返回。

### deco-helper — 新手助手与流程陪跑（本 skill）
- 职责：用户呼叫 Deco 后加载的助手身份；默认用户不了解系列，负责解释当前状态、一次推进一步并在各专业产物之间持续接力；不含专业方法。
- 功能菜单：新手接待、材料整理、流程讲解、下一步判断、能力查询（本注册表）、可复制的专业交接、跨产物兼容审查、平台参考绑定、Route A/B 最终组装与校验。

## Routing Judgment

1. Start from the user's requested outcome.
2. Credit every usable product the user already supplies, regardless of its format or production order.
3. Identify the first missing product that blocks the requested outcome.
4. Explain one next professional task, its responsible skill, required input, expected product, and completion sign.
5. Give a copy-ready next request so the user never has to translate the registry into an instruction.
6. Resume from the saved position when that product returns.

## Storyboard Decision Gate

When the available product is a director script or shot sequence and the user asks what comes next:

1. If the director script is still awaiting approval, the next task is approval or revision. Do not jump to a fixed storyboard prompt.
2. Storyboard grades no longer exist. When the board form is unresolved, hand off the storyboard-versus-shot-table 分镜表 choice to `deco-storyboard-designer`; do not pre-select it.
3. Do not infer Route A/B during next-task routing. Route A eventually needs a storyboard as model-facing control. Route B does not make a storyboard model-facing and must not be forced through storyboard production unless the user wants that validation product.

When the director script is awaiting approval, use this handoff:

```text
你现在在：导演脚本已经有了，但还没有确认它能进入分镜。
下一步只做：审查并批准或修订当前导演脚本。
为什么先做它：未批准的镜头设计继续往下做，会把问题带进故事板并增加返工。
交给：deco-storyboard-designer
你需要提供：当前导演脚本，以及你已经确认不能改的内容。
直接复制这句话：请审查这份导演脚本，指出阻塞分镜的问题；如果可用，请明确标记为已批准，如果不可用，请给出具体修订版本，并保留我锁定的内容。
完成标志：一份已批准的导演脚本，或包含明确修订要求的新版本。
完成后：把结果发回给 Deco，我继续带你下一步。
```

When the board form is unresolved, use this handoff:

```text
你现在在：镜头内容已经具备，但还没有决定用哪种图形结果来检查它。
下一步只做：在故事板和分镜表之间选择一种。故事板更适合检查单镜执行细节；分镜表更适合快速看完整序列。
为什么先做它：两种结果的用途和生成成本不同，需要按你当前最想检查的问题选择。
交给：deco-storyboard-designer
你需要提供：已批准的导演脚本或镜头材料，以及你更想检查“单镜细节”还是“整段节奏”。
直接复制这句话：请根据这份已批准的镜头材料，先判断我更适合用故事板还是分镜表；用一句话说明理由，等我确认后再给对应的固定提示词。
完成标志：你确认的故事板或分镜表选择，以及对应的固定提示词。
完成后：把结果发回给 Deco，我继续带你下一步。
```

For a new static-asset system, the specialist's recommended internal sequence is: discuss and confirm the asset plan, `regional_anchor`, and `style_aesthetic`; test one person-led Preview prompt; confirm the test direction; write production asset prompts; approve each returned `Sxx location_reference`; then derive one multi-angle, multi-shot-size nine-grid reference for each scene. `deco-visual-style-extractor` may be used as an optional user-managed style-extraction handoff. `deco-helper` only explains this sequence and accepts the returned products.

Do not send the user backward merely because their materials arrived in a different order. Parallel specialist work is valid when the products do not depend on the same unresolved decision.
