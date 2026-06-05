#!/usr/bin/env python3
"""
Export a Markdown report with LaTeX formulas to Word and check whether equations
were converted into Word equation objects.

This script uses Pandoc when available. Pandoc usually converts LaTeX math into
Office Math Markup Language in `.docx` files.

Usage:
  python export_docx_with_formulas.py input.md output.docx
  python export_docx_with_formulas.py input.md output.docx --reference-doc template.docx
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path


def count_latex_math(text: str) -> int:
    display_dollar = re.findall(r"(?<!\\)\$\$(.+?)(?<!\\)\$\$", text, flags=re.S)
    display_bracket = re.findall(r"\\\[(.+?)\\\]", text, flags=re.S)
    inline_dollar = re.findall(r"(?<!\\)\$(?!\$)(.+?)(?<!\\)\$", text, flags=re.S)
    inline_paren = re.findall(r"\\\((.+?)\\\)", text, flags=re.S)
    return len(display_dollar) + len(display_bracket) + len(inline_dollar) + len(inline_paren)


def count_omml_equations(docx_path: Path) -> int:
    with zipfile.ZipFile(docx_path) as zf:
        xml_parts = [name for name in zf.namelist() if name.startswith("word/") and name.endswith(".xml")]
        total = 0
        for name in xml_parts:
            data = zf.read(name).decode("utf-8", errors="ignore")
            total += data.count("<m:oMath")
        return total


def run_pandoc(input_md: Path, output_docx: Path, reference_doc: Path | None) -> None:
    pandoc = shutil.which("pandoc")
    if pandoc is None:
        raise RuntimeError("Pandoc was not found. Install Pandoc or use another Word export path.")

    cmd = [pandoc, str(input_md), "-o", str(output_docx)]
    if reference_doc is not None:
        cmd.extend(["--reference-doc", str(reference_doc)])

    result = subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "Pandoc export failed.")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_md")
    parser.add_argument("output_docx")
    parser.add_argument("--reference-doc", default=None)
    args = parser.parse_args()

    input_md = Path(args.input_md).expanduser().resolve()
    output_docx = Path(args.output_docx).expanduser().resolve()
    reference_doc = Path(args.reference_doc).expanduser().resolve() if args.reference_doc else None

    if not input_md.exists():
        print(f"Input Markdown file not found: {input_md}", file=sys.stderr)
        return 2

    if reference_doc is not None and not reference_doc.exists():
        print(f"Reference Word template not found: {reference_doc}", file=sys.stderr)
        return 2

    text = input_md.read_text(encoding="utf-8")
    latex_count = count_latex_math(text)

    try:
        run_pandoc(input_md, output_docx, reference_doc)
    except Exception as exc:
        print(f"Export failed: {exc}", file=sys.stderr)
        return 1

    try:
        omml_count = count_omml_equations(output_docx)
    except Exception as exc:
        print(f"Word file was created, but equation inspection failed: {exc}", file=sys.stderr)
        return 1

    print(f"LaTeX math blocks found: {latex_count}")
    print(f"Word equation objects found: {omml_count}")

    if latex_count > 0 and omml_count == 0:
        print("Warning: formulas were found in Markdown, but no Word equation objects were detected.", file=sys.stderr)
        return 3

    if latex_count > omml_count:
        print("Warning: fewer Word equation objects than source formulas were detected. Inspect the file manually.", file=sys.stderr)
        return 3

    print(f"Export completed: {output_docx}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
