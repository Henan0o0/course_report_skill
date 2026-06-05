---
name: course-report-production
version: 0.2.0
description: Assist with course reports from requirements to outline, drafting, figures, citations, Word export, and final review. Use this skill when the user needs a course report, reading report, literature review, experiment report, project report, seminar report, or a Word report with equations.
---

# Course report production skill

Use this skill when the user asks for help with a course report, reading report, literature review, seminar report, experiment report, project report, final course paper, or report revision.

The skill helps produce reports that follow the assignment, match the user's style, use real sources, handle figures responsibly, and export to Word with readable formulas.

## Core rules

1. Follow the assignment before any default choice.
2. Do not invent papers, data, results, screenshots, formulas, teacher requirements, page numbers, or citation details.
3. If the user provides previous reports, learn only writing style. Do not reuse old facts, data, figures, conclusions, or references unless the user confirms they apply to the new report.
4. If the user provides a template, follow it first. If no template exists, use the default template in `templates/default_course_report_template.md`.
5. If the final output is Word, formulas must be exported as editable Word equations when possible. Do not leave important formulas as plain text.
6. AI generated images may be used only as concept diagrams, process diagrams, architecture sketches, or visual aids. They must not be presented as real experimental results, real screenshots, or figures copied from papers.
7. Ask only for missing information that affects report direction, factual correctness, academic honesty, or required format. If a safe default exists, use it and state the default briefly.

## Intake workflow

Start by collecting or inferring the following information. If the user has already provided an item, do not ask again.

### Step 1. Task requirements

Confirm the course topic, report type, language, length, grading points, required materials, submission form, and any teacher instructions.

If the user only gives a broad topic, produce a compact intake form and request the minimum missing details.

### Step 2. Template

Ask whether the user has a template.

If yes, ask the user to upload the template and follow it.

If no, use the default template. For Chinese reports, the default sections are title, abstract, keywords, introduction, related work, method, experimental results, conclusion, and references. For English reports, use title, abstract, introduction, related work, method, experimental results, conclusion, and references.

If the report has no experiments, replace experimental results with analysis and discussion.

### Step 3. Previous reports for style

Ask whether the user wants to provide previous reports as style references.

If previous reports are provided, first extract a style profile using `templates/style_profile_template.md`.

The style profile should capture tone, sentence length, paragraph length, section transition patterns, technical wording, figure caption style, formula explanation style, and summary style.

Do not copy source text from previous reports. Use the style profile as a guide for new wording and organization.

### Step 4. Source materials

Confirm which materials will be used.

Possible materials include course slides, papers, textbooks, code, experiment logs, datasets, teacher notes, draft text, and user supplied references.

If source materials are missing, the agent may generate an outline with placeholders, but must mark facts, data, formulas, and citations that need user confirmation.

### Step 5. Section plan

Confirm the section plan with the user.

Default plan:

1. Abstract
2. Introduction
3. Related work
4. Method
5. Experimental results
6. Conclusion
7. References

Adjust the section plan by report type.

For a reading report, use introduction, paper background, core method, key results, strengths, limitations, course connection, and conclusion.

For a literature review, use problem definition, review scope, theme grouping, method comparison, limitations, future work, and conclusion.

For an experiment report, use objective, theory, setup, procedure, results, analysis, error sources, and conclusion.

For a project report, use problem, method, implementation, evaluation, results, discussion, limitations, and conclusion.

### Step 6. Figure plan

Confirm each figure before drafting.

For every figure, record figure type, target section, source, caption, and whether it must be generated, drawn from data, or inserted from user files.

Allowed figure sources:

1. User uploaded image
2. User supplied data plot
3. Redrawn method diagram with citation
4. AI generated concept diagram
5. Placeholder for later replacement

Rules:

1. AI generated figures cannot be used as experimental results.
2. Paper figures must be cited if used or redrawn.
3. Experimental plots must come from user data or real experiment outputs.
4. Every figure needs a caption and a reference in the main text.

### Step 7. Formula plan

Ask whether the report contains formulas.

If formulas are needed, confirm formula source, notation, numbering style, and Word export requirement.

During drafting, keep formulas in LaTeX source form. Use inline formulas only for short symbols and simple expressions. Use display formulas for complex expressions, loss functions, probability expressions, optimization objectives, and derivations.

During Word export, use the instructions in `references/word_formula_rules.md` and the script in `scripts/export_docx_with_formulas.py` when available.

### Step 8. Citation format

Confirm the citation style.

Supported defaults:

1. GB/T 7714 for Chinese course reports
2. IEEE for English engineering reports
3. APA when the course asks for social science style
4. User supplied style if the teacher requires it

Use `references/citation_rules.md` for citation behavior.

Do not create references that the user did not provide or that cannot be checked. If a source is needed but missing, insert a clear placeholder.

### Step 9. Outline generation

After steps 1 to 8, generate an outline for user confirmation.

The outline must include title options, section structure, paragraph goals, planned figures, planned formulas, planned citations, required user inputs, and default choices already made.

Do not write the full report before the user confirms the outline, unless the user explicitly asks to skip confirmation.

### Step 10. Drafting

After outline confirmation, draft section by section.

For each section, keep the argument clear. State the problem, method, evidence, analysis, and limitation where relevant.

Keep terminology consistent. Once an abbreviation is defined, use the same abbreviation later.

Use the style profile if one exists.

### Step 11. Word export

If the user asks for Word output, create a `.docx` file.

Before delivery, inspect the Word file. Check headings, tables, figures, captions, references, and formulas.

For formulas, verify that display equations are readable and, when possible, stored as Word equation objects. If equation conversion fails, report the issue and include the LaTeX source near the formula or provide a fallback version approved by the user.

### Step 12. Final review

Run the checklist in `checklists/final_review.md` before final delivery.

If there are missing facts, missing data, broken formulas, unresolved citations, or placeholder text, tell the user clearly.

## Default response patterns

### When starting a new report

Ask for missing task requirements, template availability, previous style reports, source materials, figure plan, formula needs, and citation style in one compact message.

### When the user provides many files

First classify files by role. Possible roles are template, previous report for style, source paper, course slide, dataset, figure, draft, and grading requirement.

Then extract constraints and produce a report brief.

### When the user asks to proceed directly

Use defaults. Generate an outline with assumptions and placeholders. Do not stop unless a missing detail creates a factual or academic honesty risk.

### When creating Word output

Use display equations for complex formulas. Export formulas as editable Word equations when possible. Inspect the final document before providing the file.
