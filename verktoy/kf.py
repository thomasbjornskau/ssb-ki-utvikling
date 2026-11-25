"""Små byggeklosser for konseptfigurer etter SSBs profil (1920 x 1080).
Bare rect, line, polyline, polygon, circle, path og text. Farger og fonter som attributter."""
import math

W, H = 1920, 1080
F_TITTEL = "Roboto Condensed, Arial Narrow, Arial, sans-serif"
F_MELLOM = "Roboto, Arial, sans-serif"
F_TEKST = "Open Sans, Segoe UI, Arial, sans-serif"

C = dict(
    m5="#274247", m1="#f0f8f9", m2="#c3dcdc",
    g4="#00824d", g2="#b6e8b8", g1="#ecfeed",
    l3="#7e5ee8", l2="#d2ceff", l1="#f2f0ff", lt="#4b2fb0",
    hvit="#ffffff", gra="#5e787a", linje="#cdd3d4",
    ufyll="#f3f5f5", ustrek="#b9c5c6", rod="#dc3400",
)
STIPLET = "6 5"
FORSLAG = "8 6"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class Fig:
    def __init__(self):
        self.o = [f'<rect x="0" y="0" width="{W}" height="{H}" fill="{C["hvit"]}"/>']

    def add(self, s):
        self.o.append(s)

    def rect(self, x, y, w, h, fill, stroke="none", sw=1, rx=2, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')

    def line(self, x1, y1, x2, y2, color, sw=1, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}"{d}/>')

    def text(self, x, y, s, size=17, color=None, font=F_TEKST, weight=400, anchor="start", italic=False):
        it = ' font-style="italic"' if italic else ""
        self.add(f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{weight}" '
                 f'fill="{color or C["m5"]}" text-anchor="{anchor}"{it}>{esc(s)}</text>')

    def lines(self, x, y, rows, size=17, color=None, font=F_TEKST, weight=400, anchor="start", lh=None):
        lh = lh or round(size * 1.35)
        for i, r in enumerate(rows):
            self.text(x, y + i * lh, r, size, color, font, weight, anchor)
        return y + len(rows) * lh

    def h(self, x, y, s, size=20, color=None, anchor="start"):
        self.text(x, y, s, size, color, F_MELLOM, 700, anchor)

    def arrow(self, pts, color=None, sw=2, dash=None, hs=10):
        color = color or C["m5"]
        (x1, y1), (x2, y2) = pts[-2], pts[-1]
        L = math.hypot(x2 - x1, y2 - y1)
        ux, uy = (x2 - x1) / L, (y2 - y1) / L
        pts2 = pts[:-1] + [(x2 - ux * hs * 1.2, y2 - uy * hs * 1.2)]
        p = " ".join(f"{a:.1f},{b:.1f}" for a, b in pts2)
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<polyline points="{p}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linejoin="round"{d}/>')
        px, py = -uy, ux
        b = (x2 - ux * hs * 1.6 + px * hs * 0.75, y2 - uy * hs * 1.6 + py * hs * 0.75)
        e = (x2 - ux * hs * 1.6 - px * hs * 0.75, y2 - uy * hs * 1.6 - py * hs * 0.75)
        self.add(f'<polygon points="{x2:.1f},{y2:.1f} {b[0]:.1f},{b[1]:.1f} {e[0]:.1f},{e[1]:.1f}" fill="{color}"/>')

    def markor(self, x, y, n, r=17):
        self.add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{C["m5"]}"/>')
        self.text(x, y + 6, str(n), 17, C["hvit"], F_MELLOM, 700, "middle")

    def brikke(self, x, y, s, typ="data", size=14):
        w = len(s) * size * 0.58 + 24
        fi, st, tc, da = {
            "data": (C["g1"], C["g4"], C["g4"], None),
            "rolle": (C["l1"], C["l3"], C["lt"], None),
            "flate": (C["m1"], C["m5"], C["m5"], None),
            "uavklart": (C["hvit"], C["ustrek"], C["gra"], STIPLET),
            "forslag": (C["l1"], C["l3"], C["lt"], FORSLAG),
            "risiko": (C["hvit"], C["rod"], C["rod"], None),
            "mork": (C["m5"], C["m5"], C["hvit"], None),
        }[typ]
        hh = size + 12
        self.rect(x, y, w, hh, fi, st, 1, hh / 2, da)
        self.text(x + w / 2, y + hh / 2 + size * 0.36, s, size, tc, F_TEKST, 600, "middle")
        return w

    def svg(self):
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n'
                + "\n".join(self.o) + "\n</svg>\n")


def ramme(f, tittel, undertittel, etikett, panel_tittel, punkter, forklaring, bunn):
    f.text(60, 92, tittel, 46, C["m5"], F_TITTEL, 700)
    f.text(60, 136, undertittel, 24, C["gra"])
    x = 1860
    for i, e in enumerate(reversed(etikett)):
        typ = "forslag" if e == "FORSLAG" else "flate"
        w = len(e) * 17 * 0.6 + 28
        x -= w
        f.rect(x, 64, w, 34, C["l1"] if typ == "forslag" else C["hvit"], C["l3"] if typ == "forslag" else C["m5"], 1, 17,
               FORSLAG if typ == "forslag" else None)
        f.text(x + w / 2, 87, e, 17, C["lt"] if typ == "forslag" else C["m5"], F_MELLOM, 700, "middle")
        x -= 10
    f.line(60, 160, 1860, 160, C["m2"], 1)
    # panel
    f.rect(1440, 180, 420, 806, C["m1"], "none", 0, 2)
    f.rect(1440, 180, 420, 5, C["g4"], "none", 0, 0)
    f.h(1468, 232, panel_tittel, 22)
    y = 290
    for i, (hd, tx) in enumerate(punkter):
        f.markor(1484, y - 7, i + 1)
        f.h(1514, y, hd, 20)
        y = f.lines(1514, y + 28, tx, 17, C["m5"], lh=24) + 26
    # tegnforklaring og bunn
    x = 60
    for typ, tekst in forklaring:
        x = tegn(f, x, 1046, typ, tekst)
    f.text(1860, 1046, bunn, 15, C["gra"], anchor="end")


def tegn(f, x, y, typ, tekst):
    if typ == "pil":
        f.arrow([(x, y - 7), (x + 34, y - 7)], C["m5"])
        x2 = x + 44
    elif typ == "pilstiplet":
        f.arrow([(x, y - 7), (x + 34, y - 7)], C["gra"], dash=STIPLET)
        x2 = x + 44
    else:
        sty = {
            "flate": (C["m1"], C["m5"], None), "data": (C["g1"], C["g4"], None),
            "rolle": (C["l1"], C["l3"], None), "uavklart": (C["hvit"], C["ustrek"], STIPLET),
            "forslag": (C["l1"], C["l3"], FORSLAG), "utenfor": (C["ufyll"], C["ustrek"], None),
            "risiko": (C["hvit"], C["rod"], None), "mork": (C["m5"], C["m5"], None),
            "vilkar": (C["hvit"], C["g4"], None), "nei": (C["ufyll"], C["ustrek"], None),
        }[typ]
        f.rect(x, y - 19, 26, 22, sty[0], sty[1], 1, 2, sty[2])
        x2 = x + 36
    f.text(x2, y, tekst, 15, C["m5"])
    return x2 + len(tekst) * 15 * 0.56 + 34


def boks(f, x, y, w, h, tittel, linjer=(), typ="flate", size=20, tsize=16, accent=False, dash=None):
    fi, st = {"flate": (C["m1"], C["m5"]), "data": (C["g1"], C["g4"]), "rolle": (C["l1"], C["l3"]),
              "hvit": (C["hvit"], C["m5"]), "uavklart": (C["hvit"], C["ustrek"]), "utenfor": (C["ufyll"], C["ustrek"]),
              "forslag": (C["l1"], C["l3"])}[typ]
    if typ == "uavklart":
        dash = dash or STIPLET
    if typ == "forslag":
        dash = dash or FORSLAG
    f.rect(x, y, w, h, fi, st, 1, 2, dash)
    if accent:
        f.rect(x, y, w, 5, C["l3"] if typ == "rolle" else C["g4"], "none", 0, 0)
    tc = C["lt"] if typ in ("rolle", "forslag") else (C["gra"] if typ in ("uavklart", "utenfor") else C["m5"])
    yy = y + 22 + size * 0.75 + (4 if accent else 0)
    f.h(x + 18, yy, tittel, size, tc)
    f.lines(x + 18, yy + tsize * 1.7, linjer, tsize, C["m5"] if typ not in ("uavklart", "utenfor") else C["gra"], lh=round(tsize * 1.4))
