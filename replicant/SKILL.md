---
name: replicant
description: Identify and remove likely signs of AI-generated writing using the Wikipedia “Signs of AI writing” field guide. Use when asked to humanize text, edit away AI tone, review drafts for AI tells, or rewrite content to sound specific, natural, and human-written without changing core meaning.
triggers: ["humanize", "humanize this", "remove ai tone", "ai tone", "ai tells", "rewrite this", "sounds like ai", "too ai", "edit this", "clean this up", "de-ai", "make this sound human", "ai writing", "ai generated", "robot writing", "sounds robotic", "polish this", "review this draft"]
---

# Replicant

Rewrite text so it keeps the original meaning but drops common AI tells.

## Workflow

1. Run a quick scan for likely AI signals (see `references/signs-of-ai-writing.md`).
2. Mark only high-confidence issues; do not over-edit clean prose.
3. Rewrite for specificity, plain language, and natural rhythm.
4. Preserve facts, intent, and tone target from the user.
5. Return:
   - Edited text
   - Short bullet list of what changed

## Editing rules

- Replace vague, grand claims with concrete facts.
- Cut “importance theater” (e.g., *pivotal moment*, *underscores significance*, *lasting legacy*) unless evidence clearly supports it.
- Remove generic “broader trend” filler when it adds no information.
- Reduce over-attribution lists (“featured in X, Y, Z media outlets”) unless those citations are the point.
- Convert superficial analysis into direct statements tied to evidence.
- Prefer simple syntax over repetitive transition-heavy flow.
- Remove repetitive framing patterns and stock AI phrasing.
- Keep the author’s voice when present; do not flatten personality.

## Output style

- Default: provide full revised text.
- If text is long (>700 words), include a compact before/after sample for the most problematic paragraph.
- If confidence is low, say so and explain why the text may be human-written.

## Guardrails

- Do not fabricate sources or facts.
- Do not change claims that require domain verification; flag them instead.
- Do not claim certainty that text is AI-generated.
- Treat this as probabilistic style editing, not forensic proof.

## References

- Core detection/editing cues: `references/signs-of-ai-writing.md`
