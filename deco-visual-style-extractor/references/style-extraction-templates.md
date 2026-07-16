# Style Extraction Templates

Use these only when the task needs a structured artifact.

## Analysis Card

```text
Style name:
Canonical status: established / composite / no confirmed exact match
Established-style lookup:
- Candidate term:
- Source:
- Match strength:
- Rejected near-match:
Classification:
- Parent style or movement:
- Supporting established styles:
- Medium or genre:
- Descriptive modifiers, not style names:
Source samples:
Style thesis:

Stage 1 - Constraint extraction:
- What the references refuse:
- Immutable conditions:
- Single-image content to ignore:

Stage 2 - Sample purification:
- Cross-sample commonalities:
- Accidental details removed:
- Evidence strength:

Stage 3 - Style system:
- Space / composition:
- Light / atmosphere:
- Color / texture:
- Rules / constraints:

Keep:
- <rule>

Avoid:
- <rule>

Repeated choices:
- Composition:
- Camera / lens:
- Lighting:
- Color:
- Materials / texture:
- Environment / set dressing:
- Subject treatment:
- Symbols / motifs:
- Finish / rendering:

Degrees of freedom:
- Flexible:
- Fixed:

Evidence strength:
- Strong:
- Provisional:
```

If no exact established term is confirmed, use `Working description (non-canonical)` instead of `Style name`.

## Three-Stage Brief

```text
1. Constraint extraction:
   Find what is absent, rejected, muted, or non-negotiable.

2. Sample purification:
   Compare different-content samples and remove subject-specific noise.

3. System building:
   Write a reusable style guide using:
   - Space and composition
   - Light and atmosphere
   - Color and texture
   - Rules and constraints
```

## Reusable JSON Prompt

```json
{
  "classification": {
    "canonical_status": "<established | composite | no_confirmed_exact_match>",
    "parent_style": "<documented style or movement>",
    "supporting_styles": ["<documented style, genre, or aesthetic>"],
    "descriptive_modifiers": ["<visible trait, not a claimed style name>"],
    "sources": ["<reference URL or source note>"],
    "match_strength": "<strong | moderate | weak>"
  },
  "subject": "<new subject and action>",
  "scene": "<setting and concrete context>",
  "composition": "<subject position, viewing order, density, negative space>",
  "camera": "<shot size, focal length, angle, movement if video>",
  "lighting": {
    "source": "<where light comes from>",
    "target": "<what it illuminates>",
    "shadow": "<where shadows fall>",
    "ratio": "<contrast or light ratio>",
    "temperature": "<warm/cool/mixed>"
  },
  "color_palette": ["#HEX1", "#HEX2", "#HEX3"],
  "materials": "<surface qualities, grain, reflections, roughness>",
  "environment_language": "<architecture, props, cultural or brand cues>",
  "style_rules": {
    "keep": ["<stable repeated choice>"],
    "avoid": ["<excluded trait or model default>"]
  },
  "stage_notes": {
    "constraints": ["<immutable condition from stage 1>"],
    "commonalities": ["<cross-sample repeated choice from stage 2>"],
    "system_blocks": ["space_composition", "light_atmosphere", "color_texture", "rules_constraints"]
  },
  "rendering": "<finish, texture, fidelity, sharpness>",
  "constraints": "<negative constraints and quality boundaries>"
}
```

## Transfer Validation

Test the style on a new subject that does not appear in the references.

```text
New subject:
Expected style signals:
Rules that must survive:
Rules that may flex:
Likely failure modes:
Corrections if it drifts:
```

## Common Failure Modes

- Inventing a polished-sounding style name before checking established vocabularies.
- Treating a descriptive phrase, `-ism`, `-core`, or hybrid label as an established style without sources.
- Forcing one label when a combination of existing styles is more accurate.
- Calling a near-match canonical while ignoring defining features it lacks.
- Copying subject matter instead of extracting repeatable choices.
- Using one image as proof of a whole style.
- Keeping abstract adjectives without translating them into visual controls.
- Forgetting negative constraints, so the model fills defaults back in.
- Over-constraining every dimension and removing useful variation.
- Treating color as vibe instead of palette, hue distribution, contrast, and temperature.
