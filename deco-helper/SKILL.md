---
name: deco-helper
description: >
  Invoke only when the user explicitly mentions deco (the deco pipeline or a deco-* skill by name); never trigger on generic AI-video, workflow, or prompt keywords alone. Guides the complete modular AI-video workflow, identifies the next professional task from the user's current materials, reviews cross-module artifact compatibility, binds platform references in Route A or Route B, and assembles final video prompts from approved specialist products. Use for AI 视频完整流程, 下一步判断, 产物审查与组合, platform reference binding, Route A/B selection, or final prompt packaging. Do not use for writing scripts, designing storyboards, designing static assets, or authoring director-design content; those are specialist products supplied to this skill.
---

# Deco Helper

Guide the modular workflow and assemble approved professional products into the final prompt. Keep specialist knowledge outside this skill.

Version: `deco-helper@2026-07-16-v3.1-single-source-assembly`
Changelog: v3.1 — SKILL.md slimmed to process only; all assembly invariants single-sourced into artifact-compatibility.md (absorbed there: director-body no-edit list, identity-name positive examples, full one-asset-one-name rule). | v3.0 — workflow guide carries the family skill registry; helper knows menus, never methods. | v2.10 — single-identity naming in Route B Shot citations.

## Responsibilities

- Explain the recommended end-to-end workflow.
- Answer capability questions: which skill owns what and which on-demand functions it offers (skill registry in the workflow guide).
- Identify the next missing professional product.
- Review whether supplied products can be combined.
- Bind grammatically referable screen-object identity names to platform references.
- Assemble Route A or Route B while preserving approved director execution; Route B may relocate the trailing `避免` clauses into `Constraints` as defined below.

This skill contains no screenplay, storyboard, static-asset, director-design, performance, dialogue, camera, lighting, or audio method. It knows every sibling's responsibility and on-demand function menu (the registry), but it does not read, invoke, or embed sibling skill files.

## Load only the current task

1. Inventory the target scope, available products, platform bindings, requested route, and content type. Accept any format or natural-language description.
2. For an overall-process, next-task, or capability request（哪个skill负责什么、有哪些功能）, read [references/workflow-guide.md](references/workflow-guide.md). If the requested outcome visibly lacks a required professional product, return the handoff below and stop. Do not read compatibility rules or route templates. Do not infer Route A/B or choose between the storyboard and shot-table 分镜表 prompt when the user has not chosen it.
3. When the required product types are present and the user wants review or final assembly, read [references/artifact-compatibility.md](references/artifact-compatibility.md).
4. If compatibility review finds a blocking missing or incompatible product, return the same handoff and stop. Do not load a route template.
5. For final assembly, select Route A or B, bind confirmed platform references with referable screen-object identity names, and read only the selected template in `templates/`.
6. Fill the selected template. For a file-backed Route B output, run `python3 scripts/validate_route_b_prompt.py [prompt-file]` and correct every reported error. Return only the finished prompt. Any unresolved required binding blocks assembly.

Use this exact missing-product handoff:

```text
下一项专业工作：[需要完成的工作]
推荐 skill：[对应 deco-* 技术名]
需要返回的产物：[简短说明]
```

Accept specialist products as free professional text. Optional metadata may help distinguish revisions, but missing labels never invalidate otherwise usable material.

## Route selection

- **Route A:** the uploaded storyboard is the model-facing control for shot order, camera movement, character action, spatial relationships, and prop relationships; a selected Preview may add visual direction.
- **Route B:** the Director Designer body is the model-facing execution control, supported by platform-bound static references; the storyboard is not model-facing.

## Assembly rules (single source)

Binding grammar, identity naming, director-body preservation, and constraint selection are single-sourced in [references/artifact-compatibility.md](references/artifact-compatibility.md); this file and the templates cite it instead of restating it. Follow it exactly during review and assembly.

## Boundaries

- Do not author or revise any specialist product.
- Do not infer missing professional content or turn tutorial order into an eligibility rule.
- When the board form is unresolved, hand off the storyboard-versus-shot-table choice defined in the workflow guide; never pre-select it.
- Do not require a fixed input schema or expose internal identifiers.
- Do not insert platform bindings or `Reference:` into the Director Designer body.
