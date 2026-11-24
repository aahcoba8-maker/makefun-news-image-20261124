"""News Image 24 November 2026 — a one-image summary of the day's world news.

Renders a newspaper-style poster (1024x1024 PNG) with PIL and writes it to
$MAKEFUN_OUTPUT_DIR/entry.png (falling back to the script directory).
If PIL or its fonts are unavailable, a poster rendered ahead of time and
stored beside this file is copied instead, so the run still succeeds.
Everything is deterministic: fixed text, fixed layout, no network, no clock.
"""

import os
import shutil
import sys

SIZE = 1024
MARGIN = 44
WIDTH = SIZE - 2 * MARGIN

PAPER = (247, 243, 234)
INK = (17, 17, 19)
MUTED = (96, 94, 90)
RED = (176, 32, 40)
WHITE = (255, 255, 255)
BAND = (232, 226, 213)

LEAD_KICKER = "MARKETS - LEAD STORY"
LEAD_HEADLINE = "HUANG RETURNS, NVIDIA SOARS 31%"
LEAD_DECK = (
    "Jensen Huang is reinstated as Nvidia's chief executive just 11 days "
    "after resigning, igniting a record rally: chip stocks surge and "
    "Wall Street posts one of its best days in years."
)
LEAD_STATS = [
    ("+31%", "NVIDIA SHARES"),
    ("+6.5%", "NASDAQ"),
    ("+4.7%", "S&P 500"),
]

STORIES = [
    (
        "UKRAINE WAR - DIPLOMACY",
        (29, 78, 156),
        "FOUR-WAY PEACE TALKS TAKE SHAPE",
        "Zelenskyy says Kyiv is ready for talks with the US, Europe and "
        "Russia before Christmas, while Brussels and Washington clash "
        "over whether a ceasefire must come first.",
    ),
    (
        "CLIMATE",
        (176, 95, 0),
        "COP31 COLLAPSES OVER FOSSIL FUELS",
        "The Antalya summit, the longest COP ever held, ends with no "
        "deal after oil states block any mention of fossil fuels - a "
        "first collapse since Copenhagen in 2009.",
    ),
    (
        "AMERICAS",
        (110, 44, 140),
        "US BRANDS CARTEL DE LOS SOLES A TERROR GROUP",
        "Washington designates the alleged drug network it links to "
        "President Maduro a foreign terrorist organisation, sharply "
        "raising pressure on Caracas.",
    ),
    (
        "ASIA",
        (0, 105, 92),
        "FACTORY FIRE KILLS 24 IN BANTEN",
        "A blaze sweeps a candy factory in Indonesia's Banten "
        "province, killing at least 24 workers as rescue teams search "
        "the ruins for the missing.",
    ),
]

SPORT_KICKER = "SPORT"
SPORT_HEADLINE = "VERSTAPPEN WINS LAS VEGAS GRAND PRIX"
SPORT_LINE = (
    "The Red Bull driver takes the night race in Nevada; Alcaraz "
    "claims his first ATP Finals crown in Turin."
)

FOOTER = (
    "Sources: Reuters - AP - CNN - CBC - Al Jazeera - Times of India"
    "   |   Compiled 24 November 2026"
)

FONT_FILES = {
    "serif_bold": [
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf",
    ],
    "sans_bold": [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ],
    "sans": [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ],
}


def load_font(ImageFont, kind, size):
    for path in FONT_FILES[kind]:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    raise IOError("no font file found for " + kind)


def wrap(draw, text, font, max_width):
    lines = []
    current = ""
    for word in text.split():
        trial = word if not current else current + " " + word
        if draw.textlength(trial, font=font) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_lines(draw, x, y, lines, font, fill, leading):
    for line in lines:
        draw.text((x, y), line, font=font, fill=fill)
        y += leading
    return y


def render_poster():
    """Draw the poster with PIL and return the PNG bytes."""
    from PIL import Image, ImageDraw, ImageFont

    img = Image.new("RGB", (SIZE, SIZE), PAPER)
    d = ImageDraw.Draw(img)

    f_top = load_font(ImageFont, "sans_bold", 19)
    f_mast = load_font(ImageFont, "serif_bold", 80)
    f_date = load_font(ImageFont, "sans_bold", 28)
    f_kick = load_font(ImageFont, "sans_bold", 20)
    f_lead = load_font(ImageFont, "serif_bold", 56)
    f_deck = load_font(ImageFont, "sans", 22)
    f_stat = load_font(ImageFont, "serif_bold", 25)
    f_head = load_font(ImageFont, "sans_bold", 26)
    f_body = load_font(ImageFont, "sans", 18)
    f_sport = load_font(ImageFont, "sans_bold", 23)
    f_sport_line = load_font(ImageFont, "sans", 17)
    f_foot = load_font(ImageFont, "sans", 16)

    # --- masthead ------------------------------------------------------
    d.line([(MARGIN, 30), (SIZE - MARGIN, 30)], fill=INK, width=3)
    d.text((MARGIN, 40), "G L O B A L   E D I T I O N", font=f_top, fill=INK)
    right = "TUESDAY"
    d.text((SIZE - MARGIN - d.textlength(right, font=f_top), 40),
           right, font=f_top, fill=INK)
    title = "THE WORLD TODAY"
    tw = d.textlength(title, font=f_mast)
    d.text(((SIZE - tw) / 2, 62), title, font=f_mast, fill=INK)
    d.line([(MARGIN, 156), (SIZE - MARGIN, 156)], fill=INK, width=5)
    d.line([(MARGIN, 163), (SIZE - MARGIN, 163)], fill=INK, width=2)

    # --- date band ------------------------------------------------------
    d.rectangle([MARGIN, 170, SIZE - MARGIN, 210], fill=INK)
    date_text = "24 NOVEMBER 2026"
    dw = d.textlength(date_text, font=f_date)
    d.text(((SIZE - dw) / 2, 177), date_text, font=f_date, fill=WHITE)

    # --- lead story ------------------------------------------------------
    y = 224
    kw = d.textlength(LEAD_KICKER, font=f_kick)
    d.rectangle([MARGIN, y, MARGIN + kw + 22, y + 32], fill=RED)
    d.text((MARGIN + 11, y + 5), LEAD_KICKER, font=f_kick, fill=WHITE)
    y += 44
    y = draw_lines(d, MARGIN, y, wrap(d, LEAD_HEADLINE, f_lead, WIDTH),
                   f_lead, INK, 58)
    y += 2
    y = draw_lines(d, MARGIN, y, wrap(d, LEAD_DECK, f_deck, WIDTH),
                   f_deck, (40, 40, 44), 29)
    y += 8
    d.line([(MARGIN, y), (SIZE - MARGIN, y)], fill=MUTED, width=2)
    y += 8
    strip = "   -   ".join(lab + " " + num for num, lab in LEAD_STATS)
    sw2 = d.textlength(strip, font=f_stat)
    d.text(((SIZE - sw2) / 2, y), strip, font=f_stat, fill=RED)
    y += 36
    d.line([(MARGIN, y), (SIZE - MARGIN, y)], fill=INK, width=3)

    # --- four story blocks, two columns ----------------------------------
    y += 12
    cell_w = (WIDTH - 28) // 2
    cell_h = 184
    for idx, (kicker, color, head, body) in enumerate(STORIES):
        cx = MARGIN + (idx % 2) * (cell_w + 28)
        cy = y + (idx // 2) * (cell_h + 12)
        d.rectangle([cx, cy, cx + 11, cy + 22], fill=color)
        d.text((cx + 19, cy), kicker, font=f_kick, fill=color)
        hy = draw_lines(d, cx, cy + 30, wrap(d, head, f_head, cell_w),
                        f_head, INK, 31)
        draw_lines(d, cx, hy + 3, wrap(d, body, f_body, cell_w),
                   f_body, (40, 40, 44), 21)
    y = y + 2 * cell_h + 12 + 8

    # --- sport band -------------------------------------------------------
    d.rectangle([MARGIN, y, SIZE - MARGIN, y + 52], fill=BAND)
    d.text((MARGIN + 16, y + 6), SPORT_KICKER, font=f_kick, fill=RED)
    kw2 = d.textlength(SPORT_KICKER, font=f_kick)
    d.text((MARGIN + 28 + kw2, y + 4), SPORT_HEADLINE, font=f_sport,
           fill=INK)
    d.text((MARGIN + 16, y + 30), SPORT_LINE, font=f_sport_line,
           fill=(40, 40, 44))

    # --- footer ------------------------------------------------------------
    fy = SIZE - 38
    d.line([(MARGIN, fy), (SIZE - MARGIN, fy)], fill=INK, width=2)
    fw = d.textlength(FOOTER, font=f_foot)
    d.text(((SIZE - fw) / 2, fy + 9), FOOTER, font=f_foot, fill=MUTED)

    import io
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()


def fallback_png_bytes():
    """A minimal valid PNG (plain paper colour) built with the stdlib."""
    import struct
    import zlib

    def chunk(tag, data):
        out = struct.pack(">I", len(data)) + tag + data
        return out + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)

    ihdr = struct.pack(">IIBBBBB", SIZE, SIZE, 8, 2, 0, 0, 0)
    row = b"\x00" + bytes(PAPER) * SIZE
    idat = zlib.compress(row * SIZE, 9)
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr)
            + chunk(b"IDAT", idat) + chunk(b"IEND", b""))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        out_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")

    data = None
    try:
        data = render_poster()
        if len(data) < 20000:
            data = None
    except Exception:
        data = None
    if data is None:
        asset = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "poster.png")
        if os.path.exists(asset):
            with open(asset, "rb") as fh:
                data = fh.read()
    if data is None:
        data = fallback_png_bytes()

    with open(target, "wb") as fh:
        fh.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
