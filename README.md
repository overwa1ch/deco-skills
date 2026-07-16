# Deco Skills

Deco 是一套面向 AI 视频生产的模块化 Codex skills。用户说“deco”后，`deco-helper` 会加载 Deco 助手身份，整理材料、判断下一步并组装最终视频提示词。它知道每个专业 skill 的用途，但不能替用户调用；专业工作必须由用户明确调用对应 skill。

## 当前模块

| Skill | 职责 |
| --- | --- |
| `deco-helper` | Deco 助手身份；整理材料、判断下一步并组装最终视频提示词。 |
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

只有 `deco-helper` 采用显式 Deco 触发边界：用户明确说 `deco`、提到 Deco 系列 / 管线或点名某个 `deco-*` skill 时，Helper 才会加载助手身份。它会说明五个专业 skill 的用途；需要专业工作时，它只推荐 skill 并给出可复制的调用请求，由用户明确调用。其余五个专业 skill 按对应专业意图正常触发，不要求用户先说 `deco`。

## 新手使用方式

直接说“deco”，然后描述想做的视频，或上传任意已有材料。Helper 会整理信息、判断下一步，并给出对应 skill 名称和可以直接复制的调用请求；用户复制请求并明确调用该 skill，再把产物带回 Deco。

## 典型专业顺序

1. `deco-screenplay-writer` 完成故事与剧本。
2. `deco-storyboard-designer` 完成 SEG、导演脚本与分镜。
3. `deco-static-asset-designer` 准备可复用静态资产。
4. `deco-action-designer` 设计动作、表演、摄影、光影和声音执行。
5. `deco-helper` 检查产物兼容性并完成最终组装。

`deco-helper` 从开始到结束持续陪同；上面的顺序只是常见路径。`deco-visual-style-extractor` 可在任何需要锁定或复核视觉风格的阶段按需使用。实际顺序以当前材料和交付目标为准。

## 仓库迁移

原独立仓库已分别更名为 `overwa1ch/deco-helper-deprecated` 和 `overwa1ch/deco-helper-storyboard-deprecated`，并转为 Private，从公开列表隐藏。它们只保留历史内容，不再作为当前版本来源。本仓库是 Deco 系列唯一公开的主发布仓库。

这里的 `deco-helper/` 仍是 Deco 系列中的有效协调模块；废弃并隐藏的是原先单独发布它的旧 GitHub 仓库。

## License

[MIT](LICENSE)
