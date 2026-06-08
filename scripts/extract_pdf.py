#!/usr/bin/env python3
"""Extract the AII source PDF into structured website content."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CONTENT_OUT = PROJECT_ROOT / "src" / "content" / "pdf-pages.json"
SOURCE_OUT = PROJECT_ROOT / "assets" / "source" / "AII.pdf"
THUMB_DIR = PROJECT_ROOT / "assets" / "img"

SECTION_RANGES = [
    (1, 3, "start", "Start Here"),
    (4, 10, "activities", "Activities"),
    (11, 14, "about", "About the Institute"),
    (15, 21, "active-inference", "Active Inference"),
    (22, 44, "institute", "Institute Foundation"),
    (45, 57, "structure", "People and Structure"),
    (58, 85, "programs", "Programs and Support"),
    (86, 166, "institute-projects", "Institute Projects"),
    (167, 199, "ecosystem", "Ecosystem and Domains"),
    (200, 204, "project-process", "Project Process"),
    (205, 211, "get-involved", "Get Involved"),
]

THUMBNAIL_PAGES = [1, 4, 12, 22, 58, 87, 121, 167, 205]


def require_tool(name: str) -> str:
    path = shutil.which(name)
    if not path:
        raise SystemExit(f"Required tool not found: {name}")
    return path


def run(args: list[str]) -> str:
    completed = subprocess.run(args, check=True, capture_output=True, text=True)
    return completed.stdout


def pdf_page_count(pdf: Path) -> int:
    info = run([require_tool("pdfinfo"), str(pdf)])
    for line in info.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":", 1)[1].strip())
    raise RuntimeError("Could not determine PDF page count")


def clean_text(text: str) -> str:
    text = text.replace("\u200b", "").replace("\u2060", "").replace("\ufeff", "")
    text = re.sub(r"[\ue000-\uf8ff]", "", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.strip()


def section_for_page(number: int) -> tuple[str, str]:
    for start, end, section_id, label in SECTION_RANGES:
        if start <= number <= end:
            return section_id, label
    return "source", "Source"


def title_for_page(text: str, number: int) -> str:
    for line in text.splitlines():
        candidate = line.strip(" -\t")
        if candidate:
            return candidate[:120]
    return f"Source page {number:03d}"


def summary_for_text(text: str) -> str:
    compact = re.sub(r"\s+", " ", text).strip()
    if not compact:
        return "Blank or spacer page in the source PDF."
    return compact[:280] + ("..." if len(compact) > 280 else "")


def extract_pages(pdf: Path) -> dict:
    tmp_text = PROJECT_ROOT / ".cache" / "AII.txt"
    tmp_text.parent.mkdir(parents=True, exist_ok=True)
    run([require_tool("pdftotext"), "-layout", str(pdf), str(tmp_text)])
    raw_pages = tmp_text.read_text(encoding="utf-8", errors="replace").split("\f")
    total_pages = pdf_page_count(pdf)

    pages = []
    for number in range(1, total_pages + 1):
        raw = raw_pages[number - 1] if number - 1 < len(raw_pages) else ""
        text = clean_text(raw)
        section_id, section_label = section_for_page(number)
        pages.append(
            {
                "number": number,
                "slug": f"page-{number:03d}",
                "title": title_for_page(text, number),
                "section": section_id,
                "sectionLabel": section_label,
                "summary": summary_for_text(text),
                "text": text,
            }
        )

    sections = []
    for start, end, section_id, label in SECTION_RANGES:
        sections.append({"id": section_id, "label": label, "start": start, "end": end})

    return {
        "source": {
            "title": "Active Inference Institute source PDF",
            "file": "assets/source/AII.pdf",
            "reportedPages": total_pages,
            "extractedPages": len(pages),
        },
        "sections": sections,
        "pages": pages,
    }


def render_thumbnails(pdf: Path) -> None:
    require_tool("pdftoppm")
    THUMB_DIR.mkdir(parents=True, exist_ok=True)
    for number in THUMBNAIL_PAGES:
        prefix = THUMB_DIR / f"source-page-{number:03d}"
        run(["pdftoppm", "-png", "-singlefile", "-f", str(number), "-l", str(number), "-r", "120", str(pdf), str(prefix)])


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: scripts/extract_pdf.py /path/to/AII.pdf", file=sys.stderr)
        return 2
    pdf = Path(sys.argv[1]).expanduser().resolve()
    if not pdf.exists():
        print(f"PDF not found: {pdf}", file=sys.stderr)
        return 2

    data = extract_pages(pdf)
    CONTENT_OUT.parent.mkdir(parents=True, exist_ok=True)
    CONTENT_OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    SOURCE_OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(pdf, SOURCE_OUT)
    render_thumbnails(pdf)
    print(f"Wrote {CONTENT_OUT} with {len(data['pages'])} pages")
    print(f"Copied source PDF to {SOURCE_OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
