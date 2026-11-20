#!/usr/bin/env python3
"""Draw the news-image-20261120 front page (1024x1024, PIL only).

Layout: newsprint masthead, one wide lead story, then a 3x2 grid of five
stories plus an 'also today' ticker cell. All text is drawn with DejaVu
fonts; pictograms are simple vector shapes, no photos, no network.
Stories were verified against Reuters / BBC / UN News / NASA on 20 Nov 2026.
"""
import math
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (18, 18, 18)
RED = (178, 34, 34)
GREY = (90, 86, 78)
PANEL = (255, 255, 255)
GOLD = (197, 141, 28)

FD = "/usr/share/fonts/truetype/dejavu/"
serif_b = lambda s: ImageFont.truetype(FD + "DejaVuSerif-Bold.ttf", s)
serif = lambda s: ImageFont.truetype(FD + "DejaVuSerif.ttf", s)
sans_b = lambda s: ImageFont.truetype(FD + "DejaVuSans-Bold.ttf", s)
sans = lambda s: ImageFont.truetype(FD + "DejaVuSans.ttf", s)
sans_i = lambda s: ImageFont.truetype(FD + "DejaVuSans.ttf", s)  # no oblique face shipped; plain sans stands in

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---- outer frame -------------------------------------------------------
d.rectangle([14, 14, W - 15, H - 15], outline=INK, width=3)
d.rectangle([20, 20, W - 21, H - 21], outline=INK, width=1)

# ---- masthead ----------------------------------------------------------
d.text((W // 2, 52), "THE WORLD IN ONE DAY", font=serif_b(58),
       fill=INK, anchor="mt")
d.line([(60, 108), (W - 60, 108)], fill=INK, width=2)
d.text((W // 2, 122), "FRIDAY, 20 NOVEMBER 2026", font=sans_b(27),
       fill=RED, anchor="mt")
d.text((W // 2, 156), "Six stories that defined the day, from Shenzhen to The Hague",
       font=sans_i(20), fill=GREY, anchor="mt")
d.line([(60, 186), (W - 60, 186)], fill=INK, width=2)


def wrap(draw, text, font, width):
    """Wrap text to fit pixel width; returns list of lines."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=font) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def pictogram(kind, x, y, s=58):
    """Tiny vector icon in a square starting at (x, y)."""
    if kind == "globe":
        d.ellipse([x, y, x + s, y + s], outline=INK, width=3)
        d.ellipse([x + s // 4, y, x + 3 * s // 4, y + s], outline=INK, width=2)
        d.line([x, y + s // 2, x + s, y + s // 2], fill=INK, width=2)
        d.arc([x, y + s // 4, x + s, y + 3 * s // 4], 200, 340, fill=INK, width=2)
    elif kind == "scales":
        d.line([x + s // 2, y + 4, x + s // 2, y + s - 4], fill=INK, width=3)
        d.line([x + 6, y + 14, x + s - 6, y + 14], fill=INK, width=3)
        for cx in (x + 12, x + s - 12):
            d.line([cx, y + 14, cx, y + 30], fill=INK, width=2)
            d.polygon([(cx - 12, y + 32), (cx + 12, y + 32),
                       (cx, y + 46)], outline=INK, width=2)
        d.rectangle([x + s // 2 - 12, y + s - 6, x + s // 2 + 12, y + s - 2],
                    fill=INK)
    elif kind == "dome":
        # capitol dome: arch on a columned base
        d.arc([x + s // 4, y + 2, x + 3 * s // 4, y + s // 2], 180, 360,
              fill=INK, width=3)
        d.line([x + s // 4, y + s // 4, x + s // 4, y + s // 2], fill=INK, width=3)
        d.line([x + 3 * s // 4, y + s // 4, x + 3 * s // 4, y + s // 2],
               fill=INK, width=3)
        d.line([x + 4, y + s // 2, x + s - 4, y + s // 2], fill=INK, width=3)
        for fx in (0.18, 0.38, 0.58, 0.78):
            bx = x + int(s * fx)
            d.line([bx, y + s // 2 + 2, bx, y + s - 8], fill=INK, width=3)
        d.line([x + 4, y + s - 4, x + s - 4, y + s - 4], fill=INK, width=3)
    elif kind == "storm":
        # cyclone swirl with rain
        cx, cy = x + s // 2, y + s // 2 - 4
        d.arc([cx - 22, cy - 16, cx + 22, cy + 16], 20, 300, fill=INK, width=3)
        d.arc([cx - 12, cy - 8, cx + 12, cy + 8], 200, 120, fill=INK, width=3)
        for fx in (0.15, 0.45, 0.75):
            rx = x + int(s * fx)
            d.line([rx, y + s - 14, rx - 4, y + s - 2], fill=RED, width=3)
    elif kind == "chart":
        bars = [(0.25, 0.45), (0.5, 0.7), (0.75, 0.95)]
        for fx, fh in bars:
            bx = x + int(s * fx) - 4
            d.rectangle([bx, y + s - int(s * fh), bx + 9, y + s - 2],
                        fill=INK)
        d.line([x + 2, y + 6, x + s // 2, y + s // 3, x + s - 4, y + 2],
               fill=RED, width=3)
        d.polygon([(x + s - 4, y + 2), (x + s - 12, y + 2),
                   (x + s - 4, y + 10)], fill=RED)
    elif kind == "shield":
        pts = [(x + s // 2, y + 2), (x + s - 2, y + 10),
               (x + s - 2, y + s // 2), (x + s // 2, y + s - 2),
               (x + 2, y + s // 2), (x + 2, y + 10)]
        d.polygon(pts, outline=INK, width=3)
        d.line([x + s // 4, y + s // 2, x + s // 2 - 2, y + 2 * s // 3],
               fill=RED, width=3)
        d.line([x + s // 2 - 2, y + 2 * s // 3, x + 3 * s // 4, y + s // 3],
               fill=RED, width=3)


def panel(x, y, w, h, kicker, headline, body, icon=None):
    d.rectangle([x, y, x + w, y + h], fill=PANEL, outline=INK, width=2)
    tx = x + 16
    if icon:
        pictogram(icon, x + w - 60, y + 12, 46)
        head_w = w - 92
    else:
        head_w = w - 32
    d.text((tx, y + 12), kicker, font=sans_b(16), fill=RED)
    yy = y + 36
    for ln in wrap(d, headline, serif_b(24), head_w):
        d.text((tx, yy), ln, font=serif_b(24), fill=INK)
        yy += 29
    yy += 4
    for ln in wrap(d, body, sans(16), w - 32):
        d.text((tx, yy), ln, font=sans(16), fill=INK)
        yy += 21
        if yy > y + h - 24:
            break


# ---- lead story --------------------------------------------------------
lx, ly, lw, lh = 40, 200, W - 80, 240
d.rectangle([lx, ly, lx + lw, ly + lh], fill=PANEL, outline=INK, width=2)
pictogram("globe", lx + lw - 132, ly + 18, 104)
d.text((lx + 18, ly + 16), "SHENZHEN  •  PEACE DECLARATION", font=sans_b(18),
       fill=RED)
yy = ly + 46
for ln in wrap(d, "Trump, Xi and Putin sign a peace declaration",
               serif_b(38), lw - 180):
    d.text((lx + 18, yy), ln, font=serif_b(38), fill=INK)
    yy += 46
yy += 6
lead = ("A day after their historic trilateral, the three leaders issue a "
        "four-point declaration: \u201ca nuclear war cannot be won and must "
        "never be fought.\u201d They pledge dialogue to reduce nuclear "
        "risks \u2014 but announce no treaty and no arms-control talks.")
for ln in wrap(d, lead, sans(19), lw - 36):
    d.text((lx + 18, yy), ln, font=sans(19), fill=INK)
    yy += 25

# ---- grid: 3 columns x 2 rows -----------------------------------------
gx, gy = 40, 454
gw = (W - 80 - 2 * 16) // 3
gh = 248
gap = 16
panel(gx, gy, gw, gh, "THE HAGUE",
      "Myanmar committed genocide",
      "The ICJ rules 9\u20136 that the 2017 campaign against the Rohingya "
      "was genocide \u2014 the first state ever held responsible. "
      "Restitution and investigations ordered.", "scales")
panel(gx + gw + gap, gy, gw, gh, "WASHINGTON",
      "Senate lets Trump keep Iran war powers",
      "The Senate rejects a bid to curb the president\u2019s Iran war "
      "powers, 51\u201348. Trump says the US will \u201csee what happens\u201d "
      "after January 1.", "dome")
panel(gx + 2 * (gw + gap), gy, gw, gh, "INDIA",
      "Cyclone Akvan hits Odisha",
      "The storm makes landfall near Gopalpur after weakening. More "
      "than 300,000 people were moved to safety and 423 rescue teams "
      "deployed; no deaths reported so far.", "storm")
panel(gx, gy + gh + gap, gw, gh, "ECONOMY",
      "South Korea\u2019s exports pass $1 trillion",
      "Annual exports top $1 trillion for the first time, driven by "
      "AI chip demand \u2014 only the fourth country ever to reach the "
      "mark, after the US, China and Germany.", "chart")
panel(gx + gw + gap, gy + gh + gap, gw, gh, "CARACAS",
      "US and Venezuela sign military deal",
      "Defence chief Hegseth signs a pact in Caracas to restore "
      "military ties \u2014 joint training and intelligence sharing, ten "
      "months after Maduro\u2019s removal.", "shield")

# ---- also-today ticker cell --------------------------------------------
ax = gx + 2 * (gw + gap)
ay = gy + gh + gap
d.rectangle([ax, ay, ax + gw, ay + gh], fill=INK, outline=INK, width=2)
d.text((ax + 16, ay + 14), "ALSO TODAY", font=sans_b(17), fill=(232, 190, 90))
items = [
    "Takaichi ducks the Taiwan question at APEC, saying Japan\u2019s stance is unchanged since 1972.",
    "Voyager 1 confirmed one light-day from Earth \u2014 a radio signal now takes 24 hours.",
    "Houthi strike damages Riyadh\u2019s tallest tower; no injuries reported.",
]
yy = ay + 44
for it in items:
    for ln in wrap(d, "\u2022  " + it, sans(16), gw - 30):
        d.text((ax + 16, yy), ln, font=sans(16), fill=(245, 245, 240))
        yy += 21
    yy += 8

d.text((W // 2, H - 40), "Sources: Reuters, BBC, UN News, NASA",
       font=sans_i(15), fill=GREY, anchor="ms")

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
