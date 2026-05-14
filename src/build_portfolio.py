from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path("work/portfolio_build/pydeps").resolve()))

from PIL import Image, ImageOps
from pillow_heif import register_heif_opener
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

register_heif_opener()

ROOT = Path("work/portfolio_build/dropbox_unzipped")
OUT = Path("work/portfolio_build")
ASSETS = OUT / "pdf_assets"
PDF = Path("UHNW_Family_Assistant_Portfolio.pdf")

PAGE_W, PAGE_H = letter
M = 0.56 * inch

INK = colors.HexColor("#1F2528")
MUTED = colors.HexColor("#66706B")
SOFT = colors.HexColor("#F5F1EA")
CREAM = colors.HexColor("#FBFAF7")
LINE = colors.HexColor("#D8D1C5")
SAGE = colors.HexColor("#5F7569")
CLAY = colors.HexColor("#9B6F54")
GOLD = colors.HexColor("#B6955C")
CHARCOAL = colors.HexColor("#26302C")


styles = {
    "kicker": ParagraphStyle("kicker", fontName="Helvetica", fontSize=8.5, leading=11, textColor=SAGE, uppercase=True),
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=9.5, leading=13.8, textColor=INK),
    "small": ParagraphStyle("small", fontName="Helvetica", fontSize=7.2, leading=9.3, textColor=MUTED),
    "caption": ParagraphStyle("caption", fontName="Helvetica", fontSize=7.5, leading=9.2, textColor=MUTED),
    "lead": ParagraphStyle("lead", fontName="Helvetica", fontSize=11.2, leading=15.5, textColor=INK),
}


sections = [
    {
        "title": "Daily Household Support",
        "folder": "DAILY TASKS",
        "copy": "Consistent, attentive support across multiple residences: resetting rooms, stocking essentials, preparing guest-ready spaces, managing errands, and noticing the small details that keep a private household calm, ready, and well cared for.",
        "skills": ["Household resets", "Stocking & readiness", "Errands", "Property detail care"],
        "images": [
            ("Elmwood .HEIC", "Room styling and daily reset"),
            ("Farm (10).HEIC", "Fresh florals and tabletop care"),
            ("Farm (15).HEIC", "Beverage drawer restock"),
            ("Farm (5).HEIC", "Refrigerator readiness"),
            ("Farm  (9).HEIC", "Snack and pantry support"),
            ("Lake Move-In .HEIC", "Bedroom setup and move-in support"),
        ],
    },
    {
        "title": "Nanny & Child-Focused Support",
        "folder": "NANNY TASKS",
        "copy": "Warm, steady family support with a practical eye for schedules, activities, transport, child spaces, pet care, and the emotional tone of the home. The work is nurturing, organized, and discreet.",
        "skills": ["Child activities", "School/airport logistics", "Play spaces", "Pet care"],
        "images": [
            ("Fam Pick Up .heic", "Family transport logistics"),
            ("L Activities  (3).HEIC", "Playroom organization"),
            ("L Activities  (8).HEIC", "Prepared activity gifts"),
            ("L Activities  (5).HEIC", "Care for child interests"),
            ("Cat Care .JPG", "Pet-care readiness"),
            ("L Activities  (12).HEIC", "Family room setup"),
        ],
    },
    {
        "title": "Meal Prep & Cooking",
        "folder": "MEAL PREP - COOKING",
        "copy": "Simple, reliable meal preparation with attention to presentation, preferences, timing, and household rhythm. Meals are prepared to feel approachable, clean, and ready for family life rather than overworked.",
        "skills": ["Daily meals", "Light cooking", "Presentation", "Preference awareness"],
        "images": [
            ("Breakfast .JPG", "Breakfast setup"),
            ("Caesar Wrap  (1).HEIC", "Prepared wrap plate"),
            ("Soup .HEIC", "Soup and grilled toast"),
            ("Salad .HEIC", "Family-style salad plates"),
            ("Pasta .HEIC", "Comfort meal prep"),
            ("Muffins .HEIC", "Homemade baked goods"),
        ],
    },
    {
        "title": "Household Organization",
        "folder": "ORGANIZATION",
        "copy": "Practical systems that make daily life easier: grouped categories, visible inventory, guest-ready storage, tidy utility areas, and organized spaces that can be maintained by the household team over time.",
        "skills": ["Pantry systems", "Fridge restock", "Garage/utility zones", "Linen & laundry care"],
        "images": [
            ("Fridge Organization  (1).jpg", "Beverage and fridge organization"),
            ("Farm Kitchen Organization .JPG", "Kitchen drawer system"),
            ("Laundry Organization .jpg", "Laundry cabinet reset"),
            ("Farm Garage Organization .JPG", "Garage storage zones"),
            ("Farm Office Org .JPG", "Office and supply organization"),
            ("Linen Organization .HEIC", "Linen storage"),
        ],
    },
    {
        "title": "Special Projects",
        "folder": "SPECIAL PROJECTS",
        "copy": "One-off projects handled with ownership: seasonal decor, craft-room resets, garden harvesting, new-pet setup, household requests, and hands-on property support from planning through final presentation.",
        "skills": ["Seasonal decor", "Project ownership", "Hands-on setup", "Follow-through"],
        "images": [
            ("Farm Halloween Deco .JPG", "Seasonal decor plan"),
            ("Farm Christmas Deco .JPG", "Holiday home setup"),
            ("Mitchell Craft Room (Final Product).JPG", "Craft room final result"),
            ("Lake J Wood Request (Final Product).JPG", "Outdoor request completed"),
            ("Garden Harvest .HEIC", "Garden harvest sorting"),
            ("Farm New Cats .HEIC", "New pet setup"),
        ],
    },
    {
        "title": "Household Transitions & Relocation",
        "folder": "TRANSITION - HOUSEHOLD RELOCATION",
        "copy": "Support through household moves and seasonal transitions: packing, vehicle loading, unpacking, staging essentials, organizing storage, and helping each property feel functional quickly.",
        "skills": ["Packing & transport", "Move-in setup", "Storage staging", "Seasonal transitions"],
        "images": [
            ("Farm Deco Storage .HEIC", "Seasonal storage staging"),
            ("Lake To Mitchell .HEIC", "Vehicle load planning"),
            ("Lake Move-In .HEIC", "Move-in bedroom setup"),
            ("Mitchell Move-In  (4).heic", "Kitchen essentials placed"),
            ("Mitchell Move-In  (5).heic", "Item sorting and staging"),
            ("Warehouse Transport .HEIC", "Transport coordination"),
        ],
    },
    {
        "title": "Closet Organization",
        "folder": "CLOSET ORGANIZATION",
        "copy": "Closet support focused on order, visibility, and ease of use: clothing sorted by category, folded consistently, staged for access, and maintained with a quiet, high-service standard.",
        "skills": ["Wardrobe sorting", "Folding systems", "Children's closets", "Move-in organization"],
        "images": [
            ("A Clothes .heic", "Wardrobe sorting"),
            ("A Clothes  (7).HEIC", "Folded clothing system"),
            ("C Clothes .heic", "Closet organization"),
            ("C Clothes  (14).HEIC", "Drawers and garments"),
            ("L Clothes .heic", "Child closet setup"),
            ("M Clothes .heic", "Adult closet support"),
        ],
    },
    {
        "title": "Property & Lifestyle Gallery",
        "folder": "PHOTO GALLERY",
        "copy": "A visual sense of the environments supported: private residences, farm and lake properties, family animals, outdoor spaces, and the lifestyle context that requires discretion, flexibility, and steady judgment.",
        "skills": ["Multi-property awareness", "Lifestyle support", "Animal care", "Discretion"],
        "images": [
            ("Lake .jpg", "Lake property context"),
            ("Farm .heic", "Farm property support"),
            ("Elmwood .HEIC", "Residence care"),
            ("Animal .jpg", "Animal care"),
            ("Animal  (1).HEIC", "Pet companionship"),
            ("Mitchell  (3).HEIC", "Private residence environment"),
        ],
    },
]


def find_image(folder: str, name: str) -> Path:
    p = ROOT / folder / name
    if p.exists():
        return p
    matches = list((ROOT / folder).glob(name))
    if matches:
        return matches[0]
    def norm(s: str) -> str:
        return " ".join(s.lower().split())
    wanted = norm(name)
    for candidate in (ROOT / folder).iterdir():
        if candidate.is_file() and norm(candidate.name) == wanted:
            return candidate
    raise FileNotFoundError(f"{folder}/{name}")


def prepare_image(path: Path, key: str, size=(1600, 1600)) -> Path:
    ASSETS.mkdir(parents=True, exist_ok=True)
    dest = ASSETS / f"{key}.jpg"
    if dest.exists():
        return dest
    with Image.open(path) as im:
        im = ImageOps.exif_transpose(im).convert("RGB")
        im.thumbnail(size, Image.Resampling.LANCZOS)
        im.save(dest, "JPEG", quality=88, optimize=True)
    return dest


def cropped_image(path: Path, key: str, w: float, h: float) -> Path:
    ASSETS.mkdir(parents=True, exist_ok=True)
    path_key = str(path).replace("/", "_").replace(" ", "_").replace("(", "").replace(")", "")
    dest = ASSETS / f"{key}_{path_key}_{int(w)}x{int(h)}.jpg"
    if dest.exists():
        return dest
    ratio = w / h
    with Image.open(path) as im:
        im = ImageOps.exif_transpose(im).convert("RGB")
        iw, ih = im.size
        if iw / ih > ratio:
            new_w = int(ih * ratio)
            left = (iw - new_w) // 2
            im = im.crop((left, 0, left + new_w, ih))
        else:
            new_h = int(iw / ratio)
            top = (ih - new_h) // 2
            im = im.crop((0, top, iw, top + new_h))
        im = im.resize((int(w * 2), int(h * 2)), Image.Resampling.LANCZOS)
        im.save(dest, "JPEG", quality=88, optimize=True)
    return dest


def para(c: canvas.Canvas, text: str, style: ParagraphStyle, x: float, y_top: float, w: float) -> float:
    p = Paragraph(text, style)
    _, h = p.wrap(w, PAGE_H)
    p.drawOn(c, x, y_top - h)
    return h


def draw_wrapped(c: canvas.Canvas, text: str, x: float, y: float, max_w: float, font="Helvetica", size=8, leading=10, color=MUTED):
    c.setFont(font, size)
    c.setFillColor(color)
    words = text.split()
    line = ""
    lines = []
    for word in words:
        test = (line + " " + word).strip()
        if stringWidth(test, font, size) <= max_w:
            line = test
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    for i, ln in enumerate(lines[:2]):
        c.drawString(x, y - i * leading, ln)


def image_card(c: canvas.Canvas, img: Path, x: float, y: float, w: float, h: float, caption: str, key: str):
    c.setFillColor(colors.white)
    c.roundRect(x, y, w, h, 5, fill=1, stroke=0)
    c.setStrokeColor(LINE)
    c.roundRect(x, y, w, h, 5, fill=0, stroke=1)
    pad = 6
    cap_h = 25
    crop = cropped_image(img, key, w - pad * 2, h - cap_h - pad * 2)
    c.drawImage(str(crop), x + pad, y + cap_h + pad, w - pad * 2, h - cap_h - pad * 2)
    draw_wrapped(c, caption, x + pad, y + 15, w - pad * 2, size=7.2, leading=8.5)


def page_header(c: canvas.Canvas, section_no: str, title: str):
    c.setFillColor(CREAM)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    c.setStrokeColor(LINE)
    c.line(M, PAGE_H - 0.54 * inch, PAGE_W - M, PAGE_H - 0.54 * inch)
    c.setFont("Helvetica", 7.8)
    c.setFillColor(SAGE)
    c.drawString(M, PAGE_H - 0.39 * inch, section_no)
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(INK)
    c.drawString(M, PAGE_H - 0.9 * inch, title)


def cover(c: canvas.Canvas):
    bg = find_image("PHOTO GALLERY", "Lake .jpg")
    crop = cropped_image(bg, "cover_lake", PAGE_W, PAGE_H)
    c.drawImage(str(crop), 0, 0, PAGE_W, PAGE_H)
    c.setFillColor(colors.Color(0, 0, 0, alpha=0.38))
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont("Helvetica", 10)
    c.drawString(M, PAGE_H - 1.1 * inch, "PRIVATE FAMILY SERVICE PORTFOLIO")
    c.setFont("Helvetica-Bold", 34)
    c.drawString(M, PAGE_H - 1.82 * inch, "UHNW Family")
    c.drawString(M, PAGE_H - 2.32 * inch, "Assistant")
    c.setStrokeColor(colors.white)
    c.setLineWidth(0.8)
    c.line(M, PAGE_H - 2.62 * inch, M + 2.45 * inch, PAGE_H - 2.62 * inch)
    c.setFont("Helvetica", 13)
    c.drawString(M, PAGE_H - 2.98 * inch, "Household operations, childcare support, organization,")
    c.drawString(M, PAGE_H - 3.22 * inch, "meal preparation, relocation assistance, and special projects.")
    c.setFont("Helvetica", 8.5)
    c.drawString(M, 0.68 * inch, "Prepared as a visual portfolio for future UHNW/private family roles")
    c.showPage()


def profile(c: canvas.Canvas):
    c.setFillColor(CREAM)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    c.setFillColor(SOFT)
    c.rect(0, PAGE_H - 2.9 * inch, PAGE_W, 2.9 * inch, fill=1, stroke=0)
    c.setFont("Helvetica", 9)
    c.setFillColor(SAGE)
    c.drawString(M, PAGE_H - 0.75 * inch, "PORTFOLIO OVERVIEW")
    c.setFont("Helvetica-Bold", 26)
    c.setFillColor(INK)
    c.drawString(M, PAGE_H - 1.34 * inch, "Warm, discreet support")
    c.drawString(M, PAGE_H - 1.76 * inch, "for private family life.")
    intro = (
        "This portfolio presents a visual record of hands-on household support across private residences. "
        "The work reflects a service style built on discretion, care, initiative, and steady follow-through: "
        "keeping spaces ready, children supported, kitchens stocked, closets ordered, projects moving, and transitions handled with calm attention."
    )
    para(c, intro, styles["lead"], M, PAGE_H - 3.45 * inch, PAGE_W - 2 * M)

    cols = [
        ("HOUSEHOLD OPERATIONS", "Daily resets, errands, restocking, readiness checks, and small details that make a property feel cared for."),
        ("FAMILY SUPPORT", "A warm presence for children, pets, activities, transport, and the shifting practical needs of family life."),
        ("ORDER & SYSTEMS", "Closets, pantries, utility spaces, and storage areas organized for visibility, access, and maintenance."),
        ("PROJECT OWNERSHIP", "Seasonal decor, move-ins, special requests, garden harvests, and hands-on household projects carried through."),
    ]
    card_w = (PAGE_W - 2 * M - 18) / 2
    y = PAGE_H - 5.15 * inch
    for i, (head, body) in enumerate(cols):
        x = M + (i % 2) * (card_w + 18)
        yy = y - (i // 2) * 1.25 * inch
        c.setFillColor(colors.white)
        c.roundRect(x, yy - 0.84 * inch, card_w, 0.95 * inch, 6, fill=1, stroke=0)
        c.setStrokeColor(LINE)
        c.roundRect(x, yy - 0.84 * inch, card_w, 0.95 * inch, 6, fill=0, stroke=1)
        c.setFont("Helvetica-Bold", 8.5)
        c.setFillColor(CLAY)
        c.drawString(x + 12, yy - 16, head)
        para(c, body, styles["small"], x + 12, yy - 31, card_w - 24)
    c.setFont("Helvetica", 8)
    c.setFillColor(MUTED)
    c.drawString(M, 0.62 * inch, "Note: Contact information can be added when ready.")
    c.showPage()


def section_page(c: canvas.Canvas, sec: dict, idx: int):
    page_header(c, f"{idx:02d}", sec["title"])
    left_w = 2.05 * inch
    copy_h = para(c, sec["copy"], styles["body"], M, PAGE_H - 1.28 * inch, left_w)
    c.setFillColor(SAGE)
    c.setFont("Helvetica-Bold", 8)
    signal_top = min(PAGE_H - 2.72 * inch, PAGE_H - 1.28 * inch - copy_h - 0.28 * inch)
    c.drawString(M, signal_top, "SERVICE SIGNALS")
    y = signal_top - 0.26 * inch
    for skill in sec["skills"]:
        c.setFillColor(SOFT)
        c.roundRect(M, y - 14, left_w, 18, 9, fill=1, stroke=0)
        c.setFillColor(CHARCOAL)
        c.setFont("Helvetica", 7.5)
        c.drawString(M + 8, y - 8, skill)
        y -= 25

    grid_x = M + left_w + 0.28 * inch
    grid_w = PAGE_W - M - grid_x
    top = PAGE_H - 1.24 * inch
    gap = 10
    big_h = 2.52 * inch
    small_h = 1.88 * inch
    col_w = (grid_w - gap) / 2
    imgs = [(find_image(sec["folder"], n), cap) for n, cap in sec["images"]]
    image_card(c, imgs[0][0], grid_x, top - big_h, col_w, big_h, imgs[0][1], f"s{idx}_0")
    image_card(c, imgs[1][0], grid_x + col_w + gap, top - big_h, col_w, big_h, imgs[1][1], f"s{idx}_1")
    y2 = top - big_h - gap - small_h
    for j in range(4):
        x = grid_x + (j % 2) * (col_w + gap)
        yy = y2 - (j // 2) * (small_h + gap)
        image_card(c, imgs[j + 2][0], x, yy, col_w, small_h, imgs[j + 2][1], f"s{idx}_{j+2}")
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 7)
    c.drawRightString(PAGE_W - M, 0.45 * inch, "UHNW Family Assistant Portfolio")
    c.showPage()


def main():
    c = canvas.Canvas(str(PDF), pagesize=letter)
    c.setTitle("UHNW Family Assistant Portfolio")
    cover(c)
    profile(c)
    for i, sec in enumerate(sections, 1):
        section_page(c, sec, i)
    c.save()
    print(PDF.resolve())


if __name__ == "__main__":
    main()
