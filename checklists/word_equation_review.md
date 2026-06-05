# Word equation review checklist

Use this checklist for `.docx` output with formulas.

## Source check

- Every formula has a LaTeX source
- Complex formulas are display formulas
- Formula labels and references are consistent

## Export check

- LaTeX math has been converted to Word equation objects when possible
- Raw LaTeX is not visible in the final Word file unless accepted by the user
- Formula symbols are readable
- Fractions, summations, integrals, matrices, Greek letters, and subscripts render correctly

## Layout check

- Display formulas are on separate lines
- Formula numbering is aligned consistently
- No formula is clipped by margins
- Line breaks do not split important formula parts

## Fallback check

- Any failed conversion is reported
- LaTeX source is preserved
- User is told which formulas need manual check
