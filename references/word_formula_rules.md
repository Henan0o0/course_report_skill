# Word formula rules

## Draft stage

Write all formulas in LaTeX during drafting.

Use inline formulas only for short symbols or simple expressions.

Use display formulas for complex equations, derivations, objective functions, probability formulas, and loss functions.

Each display formula should appear in its own paragraph.

## Word export stage

When creating `.docx`, convert LaTeX formulas into editable Word equations when possible.

A safe method is to export Markdown with LaTeX formulas through Pandoc, because Pandoc can convert LaTeX math into Office Math Markup Language in Word documents.

If a template is supplied, use it as the reference document when exporting.

## Numbering

If formula numbering is required, use one consistent scheme.

Common choices:

- sequential numbering such as (1), (2), (3)
- section based numbering such as (3.1), (3.2)

Follow the user template if it defines a formula numbering style.

## Review checks

Before delivery, inspect the Word document.

Check that:

- formulas are visible
- formulas are not clipped
- formula symbols are not broken
- formulas are not left as raw LaTeX unless approved
- formula numbering is consistent
- variables are explained after the formula
- equations in the text match the source formulas

## Fallback

If editable Word equation export fails, tell the user. Provide a fallback that keeps the LaTeX source and, if needed, a rendered image of the formula.

Do not silently deliver a Word file with broken formulas.
