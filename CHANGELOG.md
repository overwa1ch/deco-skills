# Changelog

## 2026-07-16

- 修正触发边界：只有 `deco-helper` 要求用户明确呼叫 Deco；编剧、故事板、静态资产、动作设计和视觉风格五个专业 skill 按各自专业意图正常触发。
- 专业 skill 版本更新为 Screenplay Writer V1.4、Storyboard Designer V1.14、Static Asset Designer V2.2、Action Designer V2.6、Visual Style Extractor V1.3。
- 建立 `overwa1ch/deco-skills`，作为 Deco 系列唯一的主发布仓库。
- 首次统一发布六个当前模块：`deco-helper`、`deco-screenplay-writer`、`deco-storyboard-designer`、`deco-static-asset-designer`、`deco-action-designer`、`deco-visual-style-extractor`。
- 正式采用 `deco-screenplay-writer` 和 `deco-action-designer` 两个新技术名。
- 宣布原独立仓库 `overwa1ch/deco-helper` 与 `overwa1ch/deco-helper-storyboard` 退役。
- 六个 skill 均通过 Codex skill 结构校验和公开发布安全扫描。
