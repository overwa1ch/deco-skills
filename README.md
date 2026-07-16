# Deco Skills

Deco 是一套面向 AI 视频生产的模块化 Codex skills。每个 skill 负责一个明确的专业环节，既可以单独调用，也可以在 `deco-helper` 的协调下组合成完整工作流。

## 当前模块

| Skill | 职责 |
| --- | --- |
| `deco-helper` | 识别下一项专业工作、检查跨模块产物兼容性、完成平台引用绑定和最终提示词组装。 |
| `deco-screenplay-writer` | 故事点子、人物设计、结构大纲、节拍表、场景拆解、完整剧本与剧本诊断。 |
| `deco-storyboard-designer` | SEG 拆分、场景布局、导演脚本、分镜设计、镜头表和分镜审查。 |
| `deco-static-asset-designer` | 静态资产规划、预览、生产提示词、修订与成图审查。 |
| `deco-action-designer` | 动作、表演、摄影、光影、声音、Shot 时间线和生成视频审查。 |
| `deco-visual-style-extractor` | 从参考图、视频、情绪板和品牌材料中识别并提取可复用视觉风格系统。 |

## 安装

```bash
git clone https://github.com/overwa1ch/deco-skills.git
mkdir -p ~/.codex/skills
cp -R deco-skills/deco-* ~/.codex/skills/
```

安装后新建一个 Codex 任务，让 Codex 重新发现 skills。

只有 `deco-helper` 采用显式 Deco 触发边界：用户需要明确提到 `deco`、Deco 管线或某个 `deco-*` skill，Helper 才会介入总流程和最终组装。其余五个专业 skill 按对应专业意图正常触发，不要求用户先说 `deco`。

## 推荐协作顺序

1. `deco-screenplay-writer` 完成故事与剧本。
2. `deco-storyboard-designer` 完成 SEG、导演脚本与分镜。
3. `deco-static-asset-designer` 准备可复用静态资产。
4. `deco-action-designer` 设计动作、表演、摄影、光影和声音执行。
5. `deco-helper` 检查产物兼容性并完成最终组装。

`deco-visual-style-extractor` 可在任何需要锁定或复核视觉风格的阶段按需使用。实际顺序以当前材料和交付目标为准。

## 仓库迁移

原独立仓库已分别更名为 `overwa1ch/deco-helper-deprecated` 和 `overwa1ch/deco-helper-storyboard-deprecated`，并转为 Private，从公开列表隐藏。它们只保留历史内容，不再作为当前版本来源。本仓库是 Deco 系列唯一公开的主发布仓库。

这里的 `deco-helper/` 仍是 Deco 系列中的有效协调模块；废弃并隐藏的是原先单独发布它的旧 GitHub 仓库。

## License

[MIT](LICENSE)
