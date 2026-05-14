from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path("work/portfolio_build/pydeps").resolve()))

from PIL import Image, ImageDraw, ImageFont
from pillow_heif import register_heif_opener


ROOT = Path("work/portfolio_build/dropbox_unzipped")
OUT = Path("work/portfolio_build")
THUMBS = OUT / "thumbs"
SHEETS = OUT / "contact_sheets"

VALID = {".heic", ".jpg", ".jpeg", ".png"}

register_heif_opener()


def safe_name(path: Path) -> str:
    rel = path.relative_to(ROOT)
    return "__".join(rel.parts).replace("/", "_")


def make_thumb(src: Path, dest: Path) -> bool:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        return True
    suffix = src.suffix.lower()
    try:
        with Image.open(src) as im:
            im.thumbnail((360, 360))
            im.convert("RGB").save(dest, "JPEG", quality=88)
        return True
    except Exception:
        return False


def sheet_for_category(category: Path, files: list[Path]) -> None:
    W, H = 1800, 2400
    margin, gap = 42, 26
    cols = 4
    cell_w = (W - margin * 2 - gap * (cols - 1)) // cols
    cell_h = 312
    rows = (H - 150 - margin) // (cell_h + gap)
    per_sheet = cols * rows
    font = ImageFont.load_default()
    title_font = ImageFont.load_default()

    for page, chunk_start in enumerate(range(0, len(files), per_sheet), 1):
        chunk = files[chunk_start : chunk_start + per_sheet]
        canvas = Image.new("RGB", (W, H), "white")
        draw = ImageDraw.Draw(canvas)
        draw.text((margin, 32), f"{category.name} - contact sheet {page}", fill=(24, 31, 37), font=title_font)
        for i, src in enumerate(chunk):
            thumb = THUMBS / f"{safe_name(src)}.jpg"
            if not make_thumb(src, thumb):
                continue
            col = i % cols
            row = i // cols
            x = margin + col * (cell_w + gap)
            y = 110 + row * (cell_h + gap)
            with Image.open(thumb) as im:
                im = im.convert("RGB")
                im.thumbnail((cell_w, 235))
                px = x + (cell_w - im.width) // 2
                canvas.paste(im, (px, y))
            label = src.name
            if len(label) > 38:
                label = label[:35] + "..."
            draw.text((x, y + 245), label, fill=(45, 50, 55), font=font)
        canvas.save(SHEETS / f"{category.name.replace(' ', '_').replace('/', '-')}_{page}.jpg", quality=92)


def main() -> None:
    SHEETS.mkdir(parents=True, exist_ok=True)
    THUMBS.mkdir(parents=True, exist_ok=True)
    for category in sorted([p for p in ROOT.iterdir() if p.is_dir()]):
        files = sorted([p for p in category.iterdir() if p.suffix.lower() in VALID], key=lambda p: p.name.lower())
        if files:
            sheet_for_category(category, files)


if __name__ == "__main__":
    main()
