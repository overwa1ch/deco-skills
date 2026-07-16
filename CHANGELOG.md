# Changelog

## 2026-07-16

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
