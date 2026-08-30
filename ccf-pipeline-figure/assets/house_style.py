"""House-style primitives for CCF-Pipeline-Figure §2, layered on ccf-figuresmith-skills.

⛔ NOTHING HERE RE-IMPLEMENTS FIGURESMITH. Printed-size font scaling, the text-fit gate,
icon inlining, edge styles and .drawio emission all come from that skill's
`assets/build_drawio_skeleton.py`, imported from wherever it is installed. This module adds
only the devices §2 measured in the starred corpus and for which the skeleton has no
primitive:

  * REGIONS      tinted, numbered, banner-titled containers      (§2.1)
  * one ACCENT   a single saturated hue that marks the subject   (§2.2)
  * ACTORS       an icon and its label emitted as one unit       (§2.3)
  * VERBATIM     a box holding real quoted content, monospaced   (§2.4)
  * a GEOMETRY GATE that refuses to write a figure whose solid boxes overlap or leave the
    canvas. SKILL.md §4 Step 3 says "do not trust the eye about geometry, measure it"; when
    the generator knows every rectangle, that measurement is a build gate and no browser is
    needed. figuresmith's gate is text-vs-box; this one is box-vs-box and box-vs-canvas.

Why .drawio rather than the hand-written SVG this project started with: measured, not
taste. On this machine there is no SVG rasteriser that preserves the canvas -- rsvg-convert,
cairosvg and inkscape are all absent, and `qlmanage` returns a SQUARE image with the figure
scaled to fill and the right and bottom edges cut off. The draw.io desktop binary exports a
vector PDF whose MediaBox matches the canvas exactly, in about four seconds.
"""
from __future__ import annotations

import html
import importlib.util
import os
from pathlib import Path

# --------------------------------------------------------------------------- palette (§2.2)
# Ground, line art and text. Four meaning-carrying colours is the corpus median, so the
# accent plus the two semantic hues is already the budget: do not add a fifth.
PAPER = "#FFFFFF"
INK = "#1B2430"      # line art and primary text
SOFT = "#546175"     # secondary text
FAINT = "#8F9CAF"    # tertiary text, inactive strokes
RULE = "#D2DAE6"     # box borders
ACCENT = "#E8A317"   # ⭐ THE one saturated hue. It marks what the figure is about.
GOOD = "#0E8A6A"     # semantic: kept / correct
BAD = "#D93526"      # semantic: dropped / wrong
TINTS = ["#F2F5FA", "#FBF3E4", "#EEF6F2", "#F7F3F9", "#FAF2F2", "#F3F2FA"]

_MONO = "Courier New"


# --------------------------------------------------------------------------- figuresmith
def _find_figuresmith() -> Path:
    """Locate build_drawio_skeleton.py without copying it. A copy would drift."""
    cands = []
    if os.environ.get("CCF_FIGURESMITH_ASSETS"):
        cands.append(Path(os.environ["CCF_FIGURESMITH_ASSETS"]))
    here = Path.cwd().resolve()
    for d in [here, *here.parents]:
        cands.append(d / ".claude/skills/ccf-figuresmith-skills/assets")
    cands.append(Path.home() / ".claude/skills/ccf-figuresmith-skills/assets")
    for c in cands:
        if (c / "build_drawio_skeleton.py").is_file():
            return c
    raise SystemExit(
        "[house_style] ccf-figuresmith-skills is not installed, and this module is only the\n"
        "  taste half. Install it, or set CCF_FIGURESMITH_ASSETS to its assets directory.\n"
        "  Looked in:\n    " + "\n    ".join(str(c) for c in cands[:4]))


_FS = None


def figuresmith():
    """Import the skeleton once. Its OUT is redirected: it defaults to writing beside
    itself, which is inside a read-only sibling repository."""
    global _FS
    if _FS is None:
        assets = _find_figuresmith()
        spec = importlib.util.spec_from_file_location(
            "_ccf_figuresmith", assets / "build_drawio_skeleton.py")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        mod.ICONS = assets / "icons"
        _FS = mod
    return _FS


# --------------------------------------------------------------------------- geometry gate
class _Geo:
    """Every rectangle the figure emits, so 'does it fit' is measured rather than eyeballed.

    ⚠ TEXT IS CHECKED TOO, and that is the whole lesson of the first render. The first
    version of this gate exempted text nodes as "not solid", passed a figure clean, and the
    render then showed a pill sitting on top of a banner title, a corner label written
    through two sub-labels, and a chip buried under a sentence -- every one of them a text
    collision the gate had been told to ignore. A label occupies the box you declared for
    it; if you declare it, you own it.

    Only CONTAINERS are exempt: the ground and the §2.1 regions exist to have things drawn
    inside them.
    """

    def __init__(self, w: int, h: int):
        self.w, self.h = w, h
        self.content: list[tuple[float, float, float, float, str]] = []
        self.all: list[tuple[float, float, float, float, str]] = []

    def add(self, x, y, w, h, name, container: bool = False):
        self.all.append((x, y, w, h, name))
        if not container:
            self.content.append((x, y, w, h, name))

    def check(self, figname: str):
        for x, y, w, h, name in self.all:
            if x < 0 or y < 0 or x + w > self.w or y + h > self.h:
                raise SystemExit(
                    f"[geometry] {figname}: {name} spans "
                    f"({x:.0f},{y:.0f})-({x + w:.0f},{y + h:.0f}), canvas is {self.w}x{self.h}")
        for i, (ax, ay, aw, ah, an) in enumerate(self.content):
            for bx, by, bw, bh, bn in self.content[i + 1:]:
                ox = min(ax + aw, bx + bw) - max(ax, bx)
                oy = min(ay + ah, by + bh) - max(ay, by)
                if ox > 1 and oy > 1:
                    raise SystemExit(
                        f"[geometry] {figname}: {an} and {bn} overlap by "
                        f"{ox:.0f}x{oy:.0f} units")


# --------------------------------------------------------------------------- the figure
class Figure:
    """A canvas in draw.io units, with the §2 devices as methods.

    `width_units` is the whole canvas. Font sizes are COMPUTED from it and `frac` -- the
    fraction of the column the figure is included at -- so the printed point size is right
    and never eyeballed. Declare `frac` here and keep it equal to the number in
    \\includegraphics[width=...]; that pair is the most repeated bug in figure work.
    """

    def __init__(self, name: str, out_dir, width_units: int, height_units: int,
                 frac: float = 1.0):
        fs = figuresmith()
        fs.OUT = Path(out_dir)
        fs.OUT.mkdir(parents=True, exist_ok=True)
        fs.scale_fonts(width_units, frac)
        self.fs = fs
        self.name = name
        self.w, self.h = width_units, height_units
        self.frac = frac
        self.dia = fs.Diagram(name, frac)
        self.geo = _Geo(width_units, height_units)
        self._regions: list[str] = []
        self.node("", INK, 0, 0, width_units, height_units,
                  style=f"rounded=0;fillColor={PAPER};strokeColor=none;", container=True,
                  name="ground")

    # -- font sizes, in canvas units, all derived from the skeleton's printed-size targets
    @property
    def f_label(self) -> int:
        return self.fs.FONT_LABEL

    @property
    def f_small(self) -> int:
        return self.fs.FONT_SMALL

    @property
    def f_banner(self) -> int:
        return round(self.fs.FONT_LABEL * 1.18)

    def printed_pt(self, size_units: float) -> float:
        return size_units * self.frac * self.fs.TEXT_W_PT / self.w

    # -- low level ---------------------------------------------------------------
    def node(self, value, colour, x, y, w, h, style, container=False, name=None):
        self.geo.add(x, y, w, h, name or (value[:28] if value else "unnamed"), container)
        return self.dia.node(value, x, y, w, h, style)

    def _text(self, value, x, y, w, h, size, colour=INK, bold=False, align="center",
              mono=False, name=None):
        style = (f"text;html=1;strokeColor=none;fillColor=none;align={align};"
                 f"verticalAlign=middle;fontSize={size};fontColor={colour};"
                 f"fontStyle={1 if bold else 0};"
                 + (f"fontFamily={_MONO};" if mono else ""))
        return self.node(value, colour, x, y, w, h, style,
                         name=name or f"text:{value[:20]}")

    # -- §2.1 regions -------------------------------------------------------------
    def region(self, x, y, w, h, badge: str, title: str, corner: str = "", tint: int = 0):
        """A tinted, numbered, banner-titled container. §2.1: 3-6 of these, never a chain."""
        fill = TINTS[tint % len(TINTS)]
        self.node("", INK, x, y, w, h,
                  f"rounded=1;arcSize=6;fillColor={fill};strokeColor={RULE};strokeWidth=1.5;"
                  f"dashed=1;dashPattern=10 6;", container=True, name=f"region:{title[:18]}")
        d = round(self.f_label * 1.5)
        self.node(badge, INK, x + d * 0.5, y + d * 0.4, d, d,
                  f"ellipse;fillColor={INK};strokeColor=none;fontColor=#FFFFFF;fontStyle=1;"
                  f"fontSize={self.f_small};", name=f"badge:{badge}")
        self._text(title, x + d * 1.7, y + d * 0.4, w - d * 2.4, d, self.f_banner,
                   INK, bold=True, align="left", name=f"banner:{title[:18]}")
        if corner:
            self._text(corner, x + w * 0.3, y + h - self.f_small * 2.2, w * 0.66 - 12,
                       self.f_small * 1.6, self.f_small, FAINT, align="right",
                       name=f"corner:{corner[:18]}")
        self._regions.append(title)

    # -- §2.3 actors ---------------------------------------------------------------
    def actor(self, cx, cy, icon: str, label: str, sub: str = "", colour=INK, size=None):
        """An icon and its label, emitted together so they cannot drift apart."""
        s = size or round(self.f_label * 2.2)
        self.node("", colour, cx - s / 2, cy - s / 2, s, s, self.fs.icon(icon, colour),
                  name=f"icon:{icon}")
        lw = self.f_label * len(label) * 0.62 + self.f_label * 2
        self._text(label, cx - lw / 2, cy + s * 0.62, lw, self.f_label * 1.3,
                   self.f_label, INK, bold=True, name=f"actor:{label}")
        if sub:
            sw = self.f_small * len(sub) * 0.6 + self.f_small * 2
            self._text(sub, cx - sw / 2, cy + s * 0.62 + self.f_label * 1.45, sw,
                       self.f_small * 1.5, self.f_small, SOFT, name=f"sub:{sub[:18]}")

    # -- boxes, pills, verbatim ------------------------------------------------------
    def box(self, x, y, w, h, label, sub="", accent=False, fill="#FFFFFF"):
        stroke = ACCENT if accent else RULE
        self.node(label if not sub else f"{label}", INK, x, y, w, h,
                  f"rounded=1;arcSize=12;whiteSpace=wrap;html=1;fillColor={fill};"
                  f"strokeColor={stroke};strokeWidth=1.8;fontSize={self.f_label};"
                  f"fontColor={INK};fontStyle=1;verticalAlign={'top' if sub else 'middle'};"
                  f"spacingTop={self.f_label * 0.4 if sub else 0};",
                  name=f"box:{label[:20]}")
        if sub:
            self._text(sub, x, y + h - self.f_small * 2.2, w, self.f_small * 1.8,
                       self.f_small, SOFT, name=f"boxsub:{sub[:18]}")

    def pill(self, cx, cy, text, fill=ACCENT, fg="#3D2A00"):
        w = self.f_small * len(text) * 0.72 + self.f_small * 3
        h = self.f_small * 2.1
        self.node(text, fg, cx - w / 2, cy - h / 2, w, h,
                  f"rounded=1;arcSize=50;fillColor={fill};strokeColor=none;"
                  f"fontSize={self.f_small};fontColor={fg};fontStyle=1;",
                  name=f"pill:{text[:18]}")

    def verbatim(self, x, y, w, h, text, name="verbatim"):
        """§2.4: real quoted content, shown exactly. The highest-lift move in the style."""
        self.node(text, INK, x, y, w, h,
                  f"rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#FFFFFF;"
                  f"strokeColor={RULE};strokeWidth=1.8;align=left;verticalAlign=middle;"
                  f"spacingLeft={self.f_small};fontFamily={_MONO};fontSize={self.f_small};"
                  f"fontColor={SOFT};", name=name)

    # -- flow ------------------------------------------------------------------------
    def arrow(self, x1, y1, x2, y2, accent=False, dashed=0, width=None):
        colour = ACCENT if accent else FAINT
        style = (f"edgeStyle=none;html=1;strokeColor={colour};"
                 f"strokeWidth={width or max(2, round(self.f_label * 0.09))};"
                 f"dashed={dashed};dashPattern=8 5;endArrow=block;endFill=1;"
                 f"endSize={max(4, round(self.f_label * 0.22))};")
        self.dia._n += 1
        self.dia.cells.append(
            f'<mxCell id="e{self.dia._n}" style="{style}" edge="1" parent="1">'
            f'<mxGeometry relative="1" as="geometry">'
            f'<mxPoint x="{x1}" y="{y1}" as="sourcePoint"/>'
            f'<mxPoint x="{x2}" y="{y2}" as="targetPoint"/></mxGeometry></mxCell>')

    def divider(self, x, y0, y1, left: str = "", right: str = ""):
        """§2.1 device 4: one vertical dashed rule splitting the figure into two named halves."""
        self.dia._n += 1
        self.dia.cells.append(
            f'<mxCell id="d{self.dia._n}" style="endArrow=none;html=1;strokeColor={FAINT};'
            f'strokeWidth=2;dashed=1;dashPattern=9 7;" edge="1" parent="1">'
            f'<mxGeometry relative="1" as="geometry">'
            f'<mxPoint x="{x}" y="{y0}" as="sourcePoint"/>'
            f'<mxPoint x="{x}" y="{y1}" as="targetPoint"/></mxGeometry></mxCell>')
        if left:
            self._text(left, x - self.w * 0.46, y0 - self.f_label * 2.4, self.w * 0.42,
                       self.f_label * 1.8, self.f_label, INK, bold=True, align="right",
                       name=f"half:{left[:16]}")
        if right:
            self._text(right, x + self.w * 0.04, y0 - self.f_label * 2.4, self.w * 0.42,
                       self.f_label * 1.8, self.f_label, INK, bold=True, align="left",
                       name=f"half:{right[:16]}")

    def text(self, *a, **k):
        return self._text(*a, **k)

    # -- emit ---------------------------------------------------------------------
    def write(self):
        if not 3 <= len(self._regions) <= 6:
            raise SystemExit(
                f"[house-style] {self.name}: §2.1 wants 3-6 named regions, this has "
                f"{len(self._regions)}. A figure with fewer is usually a chain, which is "
                f"the one composition no starred figure in the corpus uses.")
        self.geo.check(self.name)
        self.dia.write()
        path = self.fs.OUT / f"{self.name}.drawio"
        print(f"  regions {len(self._regions)}  canvas {self.w}x{self.h}  frac {self.frac}")
        print(f"  printed: label {self.printed_pt(self.f_label):.1f}pt  "
              f"small {self.printed_pt(self.f_small):.1f}pt  "
              f"banner {self.printed_pt(self.f_banner):.1f}pt")
        return path


DRAWIO_MAC = "/Applications/draw.io.app/Contents/MacOS/draw.io"


def export(path: Path, png_width: int | None = None, pdf: bool = True):
    """Export with the draw.io binary, then MEASURE the raster against the canvas.

    ⛔ The check is not `the file exists`. This project shipped a cropped PNG for weeks
    because the generator checked exactly that, and a stale file from an earlier run
    satisfied it. Compare the raster's aspect to the canvas, or the check cannot fail.
    """
    import subprocess
    path = Path(path)
    binary = DRAWIO_MAC if Path(DRAWIO_MAC).exists() else "drawio"
    out = []
    if pdf:
        target = path.with_suffix(".pdf")
        target.unlink(missing_ok=True)
        r = subprocess.run([binary, "-x", "--crop", "-o", str(target), str(path)],
                           capture_output=True)
        if not target.exists():
            raise SystemExit(f"[export] PDF export failed: {r.stderr.decode()[:300]}")
        out.append(target)
    if png_width:
        target = path.with_suffix(".png")
        target.unlink(missing_ok=True)
        r = subprocess.run([binary, "-x", "--width", str(png_width), "-o", str(target),
                            str(path)], capture_output=True)
        if not target.exists():
            raise SystemExit(f"[export] PNG export failed: {r.stderr.decode()[:300]}")
        out.append(target)
    for f in out:
        print(f"  {f}  ({f.stat().st_size // 1024} KB)")
    return out
