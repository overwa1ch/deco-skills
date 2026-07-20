#!/usr/bin/env python3
"""Validate Route B asset bindings and adaptive execution citations."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys


SEGMENT_HEADING = re.compile(r"(?m)^SEG\d+\s*$")
SECTIONS = re.compile(
    r"Asset List:\s*\n(?P<assets>.*?)\n\s*\nPrompt:\s*\n(?P<prompt>.*)"
    r"\n\s*\nConstraints:\s*\n(?P<constraints>.*)\Z",
    re.DOTALL,
)
ASSET_BINDING = re.compile(r"^“([^”]+)”\s*=\s*(@[^@\s]\S*)\s+-\s+(.+)$")
INVALID_IDENTITY_NAMES = {
    "人物三视图",
    "场景九宫格",
    "对比产品",
    "自家产品",
    "人物参考资产",
    "场景参考资产",
    "对比产品参考资产",
    "自家产品参考资产",
}
ASSET_FORM_SUFFIX = re.compile(
    r"(?:三视图|九宫格|参考图|参考资产|素材图|资产图|人物图|场景图|产品图)$"
)
SHOT_HEADING = re.compile(r"(?m)^\*{0,2}Shot\s+\d+.*$")
FIELD_HEADING = re.compile(
    r"(?m)^(?P<label>"
    r"Use case|Primary request|Scene/background|Subject|Style/format|"
    r"Lighting/mood|Color palette|Camera|Acting|Continuity|Physics|"
    r"Action|Timing/beats|Audio|Text \(verbatim\)|Dialogue|Constraints|Avoid|"
    r"Style|Lighting|Color|SFX"
    r"):\s*"
)
EXECUTION_FIELDS = {"Subject", "Action", "Timing/beats"}
AVOID_HEADING = re.compile(r"(?m)^(?:Avoid:\s*|避免：\s*)")
EMPTY_AVOID_CONSTRAINT = re.compile(r"(?m)^禁止出现：\s*$")
# One asset, one name: generic alias tokens must not denote a bound asset in
# Prompt or Constraints; only the exact quoted identity name may. Longest first
# so 对比产品 does not additionally report 产品.
GENERIC_ALIAS_TOKENS = ("对比产品", "自家产品", "折叠体", "商品", "人物", "产品")
ALIAS_EXEMPT_TERMS = ("产品演示", "产品反转", "纸就产品", "成品资产")


def execution_scope(prompt: str) -> tuple[str, list[str]]:
    """Return the Subject/Action/Timing or Shot text that may carry assets."""
    markers: list[tuple[int, int, str, str]] = []
    for match in FIELD_HEADING.finditer(prompt):
        markers.append((match.start(), match.end(), "field", match.group("label")))
    for match in SHOT_HEADING.finditer(prompt):
        markers.append((match.start(), match.end(), "shot", "Shot"))
    markers.sort(key=lambda item: item[0])

    chunks: list[str] = []
    carriers: list[str] = []
    for index, (start, _end, kind, label) in enumerate(markers):
        end = markers[index + 1][0] if index + 1 < len(markers) else len(prompt)
        if kind == "shot" or label in EXECUTION_FIELDS:
            chunks.append(prompt[start:end])
            carriers.append(label)
    return "\n".join(chunks), carriers


def split_segments(text: str) -> list[tuple[str, str]]:
    matches = list(SEGMENT_HEADING.finditer(text))
    if not matches:
        return []
    segments: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[match.end() : end].strip()
        body = re.sub(r"\n---\s*\Z", "", body).strip()
        segments.append((match.group().strip(), body))
    return segments


def validate(text: str) -> tuple[list[str], int, int]:
    errors: list[str] = []
    binding_count = 0
    citation_count = 0

    if "Asset Use:" in text:
        errors.append("Route B must not contain an Asset Use section")
    if "影片调性" in text:
        errors.append("Route B must not contain a separate 影片调性 line")

    segments = split_segments(text)
    if not segments:
        return ["no SEGXX block found"], 0, 0

    for heading, body in segments:
        section_match = SECTIONS.search(body)
        if not section_match:
            errors.append(f"{heading}: expected Asset List / Prompt / Constraints sections")
            continue

        asset_text = section_match.group("assets").strip()
        prompt = section_match.group("prompt")
        carrier_text, carriers = execution_scope(prompt)
        if not carriers:
            errors.append(
                f"{heading}: Prompt has no Subject, Action, Timing/beats, or Shot execution carrier"
            )
        if AVOID_HEADING.search(prompt):
            errors.append(
                f"{heading}: Prompt retains Avoid/避免; move its content to outer Constraints"
            )
        if EMPTY_AVOID_CONSTRAINT.search(section_match.group("constraints")):
            errors.append(f"{heading}: empty 禁止出现 line must be omitted")
        asset_lines = [line.strip() for line in asset_text.splitlines() if line.strip()]
        names: list[str] = []
        handles: list[str] = []

        for line_number, line in enumerate(asset_lines, start=1):
            binding = ASSET_BINDING.fullmatch(line)
            if not binding:
                errors.append(
                    f"{heading} Asset List line {line_number}: expected "
                    "“referable object name” = @handle - asset form and use"
                )
                continue
            name, handle, _description = binding.groups()
            names.append(name)
            handles.append(handle)
            binding_count += 1

            if name in INVALID_IDENTITY_NAMES or ASSET_FORM_SUFFIX.search(name):
                errors.append(
                    f"{heading}: “{name}” describes an asset form or role, not a referable screen object"
                )

        if len(names) != len(set(names)):
            errors.append(f"{heading}: duplicate quoted identity name in Asset List")
        if len(handles) != len(set(handles)):
            errors.append(f"{heading}: duplicate platform handle in Asset List")

        for name in names:
            citation = f"“{name}”"
            count = prompt.count(citation)
            if count == 0:
                errors.append(f"{heading}: Prompt does not cite {citation}")
            else:
                citation_count += count
            if citation not in carrier_text:
                errors.append(
                    f"{heading}: Subject/Action/Timing/Shot execution does not cite {citation}; "
                    "Continuity-only or summary-only citation is insufficient"
                )

        for handle in handles:
            handle_in_prompt = re.search(
                rf"(?<![\w@]){re.escape(handle)}(?![\w])", prompt
            )
            if handle_in_prompt:
                errors.append(
                    f"{heading}: raw handle {handle} appears in Prompt; cite its bound quoted identity name"
                )

        alias_scope = prompt + "\n" + section_match.group("constraints")
        masked = re.sub(r"“[^”]*”", "", alias_scope)
        for term in ALIAS_EXEMPT_TERMS:
            masked = masked.replace(term, "")
        for token in GENERIC_ALIAS_TOKENS:
            if token in masked:
                errors.append(
                    f"{heading}: generic alias “{token}” appears outside a quoted identity; "
                    "use the exact bound identity name for the asset"
                )
                masked = masked.replace(token, "")

    return errors, binding_count, citation_count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prompt_file", type=Path)
    args = parser.parse_args()
    text = args.prompt_file.read_text(encoding="utf-8")
    errors, bindings, citations = validate(text)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(
        f"PASS: {bindings} Asset List bindings and {citations} exact quoted Prompt citations"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
