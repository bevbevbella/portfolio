"""Extract embedded images from the portfolio PDF into assets/, with stable
filenames keyed to the section + image slot defined in build_portfolio.py.

This gives the HTML portfolio real images to work with even though the
original Dropbox image archive lives outside the repo.
"""
from __future__ import annotations

import re
from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parent.parent
PDF_PATH = ROOT / "docs" / "UHNW_Family_Assistant_Portfolio.pdf"
OUT_DIR = ROOT / "assets" / "portfolio"

SECTION_SLUGS = [
    "cover",          # page 1: cover photo
    # page 2: profile (no images)
    "daily",          # page 3
    "nanny",          # page 4
    "meals",          # page 5
    "organization",   # page 6
    "projects",       # page 7
    "transitions",    # page 8
    "closets",        # page 9
    "gallery",        # page 10
]


def slugify(text: str) -> str:
    text = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return text or "image"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(PDF_PATH)
    section_index = 0

    for page_no, page in enumerate(doc, start=1):
        images = page.get_images(full=True)
        if not images:
            continue
        if page_no == 1:
            slug = "cover"
        else:
            slug = SECTION_SLUGS[section_index]
            section_index += 1
            if slug == "cover":
                # cover is handled by page 1; skip duplicate slot
                slug = SECTION_SLUGS[section_index]
                section_index += 1

        for slot, info in enumerate(images):
            xref = info[0]
            pix = fitz.Pixmap(doc, xref)
            if pix.n - pix.alpha > 3:
                pix = fitz.Pixmap(fitz.csRGB, pix)
            out = OUT_DIR / f"{slug}-{slot:02d}.jpg"
            if pix.alpha:
                pix.set_alpha(None)
            pix.save(out, jpg_quality=88)
            pix = None
            print(f"page {page_no:>2}  {slug:<14}  slot {slot}  ->  {out.name}")

    doc.close()


if __name__ == "__main__":
    main()
