# Changelog

## 2026-07-20

- `deco-helper` 升级为 V3.8，包含 V3.7–V3.8 累积更新：保留各专业产物的模板结构；兼容旧 V2 固定导演正文与新 V3 弹性正文；用语义充分性检查代替固定字段组合检查；Route B 可在 `Subject`、`Action`、`Timing/beats` 或 Shot 中绑定资产，无 Avoid 时省略空限制。
- `deco-static-asset-designer` 升级为 V2.3：六类生产资产提示词保留编号、字段名、层级和字段顺序；Preview、视觉方向、九宫格固定提示词和资产几何定义保持不变。
- `deco-action-designer` 升级为 V3.0：字段只在承担独立控制信息时出现；单一连续动作、精确单镜和多镜头分别使用 `Action`、`Action + Timing/beats` 或 Shot；删除剧情总述与 Shot 的重复层；继续提供完整无BGM声音设计。
- `deco-visual-style-extractor` 升级为 V1.5，包含 V1.4–V1.5 累积更新：交付物使用匹配的结构化模板；按请求选择 Style Lookup、Analysis Card、Three-Stage Brief、Reusable JSON Prompt 或 Transfer Validation；模板内部省略空字段和无证据字段。
- Screenplay Writer V1.4 与 Storyboard Designer V1.15 保持不变。Helper Route A、Static Asset 固定提示词、Storyboard canonical style、固定故事板提示词和固定分镜表提示词通过冻结面校验。
- 六项 skill 通过结构校验、fresh-process 前向测试、Route A/B 兼容检查、live/repository 树一致性和公开发布安全检查。

## 2026-07-19

- `deco-helper` 升级为 V3.6：明确承担 Deco 系列的用法与跨模块制作经验层；新增“剧本初稿 → 故事板草稿测试 → 静态资产 → 资产支持的分镜表复核 → 动作设计 → 最终组装”推荐路线，同时保留用户独立调用任一专业功能的选择。
- 场景多角度参考默认先使用九宫格；九格无法保持场景身份、拓扑、家具、设备或风格一致时，推荐降低信息密度并改用 `2×2` 四宫格。
- `deco-storyboard-designer` 升级为 V1.15：按用户授权，只修改故事板和分镜表固定短任务的分图措辞，分别明确故事板之间、分镜表之间不要拼成一张图；canonical 故事板样式和其余模板内容不变。
- `deco-action-designer` 升级为 V2.9，包含 V2.7–V2.9 累积更新：删除会诱发多余动作编排的 connected-motion-consequences / follow-through 规则；采用单一主动作、单一主导摄影行为和按需顺序节拍的动作经济；画面中需要逐字生成的文字统一使用中文双引号“……”，对白继续使用「……」。
- Screenplay Writer V1.4、Static Asset Designer V2.2、Visual Style Extractor V1.3 保持不变；六项 skill 通过结构校验、边界扫描和公开发布安全检查。

## 2026-07-16

- `deco-helper` 升级为 V3.5：身份提示词改用第一人称，Deco 以“我是 Deco”介绍自己，不再把内部第二人称指令原样展示给用户。
- `deco-helper` 升级为 V3.4：身份层收口为一段用户确认的精简提示词，列出五个专业 skill 及其核心功能。
- 明确 Deco 不能调用或代替专业 skill；需要专业工作时，只推荐对应 skill 并提供由用户复制执行的调用请求。
- `deco-helper` 升级为 V3.3 助手身份：用户说“deco”后，默认按零基础用户接待，从目标或现有材料开始，一次推进一个步骤。
- 新增固定新手引导循环与可复制的专业交接格式；交接会说明当前状态、下一步、所需材料、预期产物和完成标准。
- 修正 Helper 内残留的旧技术名，统一使用 `deco-screenplay-writer` 与 `deco-action-designer`；Route A/B 组装结构未改。
- 将两个退役独立仓库更名为 `deco-helper-deprecated` 与 `deco-helper-storyboard-deprecated`，并转为 Private；`deco-skills` 保持公开。
- 修正触发边界：只有 `deco-helper` 要求用户明确呼叫 Deco；编剧、故事板、静态资产、动作设计和视觉风格五个专业 skill 按各自专业意图正常触发。
- 专业 skill 版本更新为 Screenplay Writer V1.4、Storyboard Designer V1.14、Static Asset Designer V2.2、Action Designer V2.6、Visual Style Extractor V1.3。
- 建立 `overwa1ch/deco-skills`，作为 Deco 系列唯一的主发布仓库。
- 首次统一发布六个当前模块：`deco-helper`、`deco-screenplay-writer`、`deco-storyboard-designer`、`deco-static-asset-designer`、`deco-action-designer`、`deco-visual-style-extractor`。
- 正式采用 `deco-screenplay-writer` 和 `deco-action-designer` 两个新技术名。
- 宣布原独立仓库 `overwa1ch/deco-helper` 与 `overwa1ch/deco-helper-storyboard` 退役。
- 六个 skill 均通过 Codex skill 结构校验和公开发布安全扫描。
