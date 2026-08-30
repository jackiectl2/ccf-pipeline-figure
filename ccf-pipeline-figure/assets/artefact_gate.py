"""Check the SHIPPED FILE, not the generator's intent.

⛔ WHY THIS IS A DIFFERENT GATE FROM THE OTHER TWO. `house_style.py` checks geometry and
figuresmith checks text fit; both read what the generator *meant* to draw. Neither opens the
exported file and asks whether it is what it claims to be. This project has already shipped
two defects of exactly that class:

  * a committed PNG whose ink ran to x=1679 of 1680 while its SVG's rightmost element ended
    at 1640 — the rasteriser had squared the canvas and cut the overflow, and the SVG was
    measurably clean the whole time;
  * a success test written as `png.exists()`, which a stale file from an earlier run
    satisfied, so the generator reported success while the raster it had just produced sat
    somewhere else under a different name.

The device is borrowed from `visio-image-rebuilder`, the one workflow out of sixteen surveyed
that inspects its own output package rather than its own render: it scans the saved `.vsdx`
for a whole embedded PNG so a pasted image cannot pass itself off as a rebuild, and
reconciles the shape count to confirm something was really constructed. See
`literature/figure-refs/production-workflows.md`, W08. What is borrowed is the idea, not the
stack — Visio is Windows-only and this runs on the exports we actually make.

⚠ THE ONE SUBTLETY, AND IT IS THE REASON A NAIVE VERSION OF THIS GATE IS USELESS.
figuresmith's `icon()` inlines Bootstrap Icons as `data:image/svg+xml` URIs, which are
vector. A check that rejects every `data:` URI would fire on every icon in every figure we
draw, and a gate that cries wolf gets switched off. So the rule is about the MIME type, not
about the URI: `image/svg+xml` is fine, `image/png` and `image/jpeg` are not.
"""
from __future__ import annotations

import re
import struct
import zlib
from pathlib import Path


class GateFailure(SystemExit):
    pass


def _fail(path: Path, what: str, detail: str) -> None:
    raise GateFailure(f"[artefact-gate] {path.name}: {what}\n    {detail}")


# --------------------------------------------------------------------------- raster geometry
def png_size(path: Path) -> tuple[int, int]:
    d = path.read_bytes()[:33]
    if d[:8] != b"\x89PNG\r\n\x1a\n":
        _fail(path, "not a PNG", "the file does not start with the PNG signature")
    return struct.unpack(">II", d[16:24])


def pdf_mediabox(path: Path) -> tuple[float, float]:
    m = re.search(rb"/MediaBox\s*\[([^\]]*)\]", path.read_bytes())
    if not m:
        _fail(path, "no MediaBox", "this does not look like a PDF page")
    b = [float(x) for x in m.group(1).split()]
    return b[2] - b[0], b[3] - b[1]


def check_exports_agree(pdf: Path, png: Path, tol: float = 0.005) -> str:
    """The vector and raster exports of one figure must have the same shape.

    ⭐ THIS IS THE CHECK THAT WOULD HAVE CAUGHT THE SHIPPED CROP, and it is stronger than
    comparing either one against the canvas. The broken PNG in this project was produced by
    `qlmanage` while its SVG was produced by the generator — two different producers, so they
    disagreed. Two exports from the same exporter cannot disagree unless something mangled
    one of them afterwards.
    """
    mw, mh = pdf_mediabox(pdf)
    w, h = png_size(png)
    if abs(mw / mh - w / h) > tol:
        _fail(png, "the two exports of one figure disagree",
              f"PDF {mw:.1f}x{mh:.1f} = {mw / mh:.4f} but PNG {w}x{h} = {w / h:.4f}. "
              f"One of them was produced or processed differently from the other.")
    return f"PDF and PNG agree at {w / h:.4f}"


def check_trim_is_only_margin(path: Path, canvas_w: float, canvas_h: float,
                              max_frac: float = 0.05) -> str:
    """The export may be smaller than the canvas, but only by whitespace.

    ⚠ THIS IS DELIBERATELY NOT AN EQUALITY. `draw.io -x --crop` trims the outer margin by
    design, so a correct export of a 1400x1096 canvas comes back at 1400x1075 — 2% shorter,
    all of it empty. An equality check fires on every correct figure, and a gate that cries
    wolf is a gate that gets switched off.

    What the tolerance is really separating: a few per cent means margin, a sixth means the
    rasteriser scaled the drawing up and cut the overflow — which is what happened here once,
    at 17%.
    """
    if path.suffix.lower() == ".pdf":
        ew, eh = pdf_mediabox(path)
    else:
        ew, eh = png_size(path)
    want, got = canvas_w / canvas_h, ew / eh
    # express the disagreement as the fraction of canvas height that went missing
    lost = abs(1 - (canvas_w / got) / canvas_h)
    if lost > max_frac:
        _fail(path, "the export is not the canvas, and not by a margin",
              f"canvas {canvas_w:g}x{canvas_h:g} = {want:.4f}, export = {got:.4f}; "
              f"{lost * 100:.1f}% of the height is unaccounted for, over the {max_frac:.0%} "
              f"allowed for a trimmed margin. Check whether content was cut.")
    return f"{lost * 100:.1f}% trimmed (margin only, {max_frac:.0%} allowed)"


def check_ink_inside(path: Path, margin_px: int = 2) -> str:
    """No ink on the outermost rows or columns.

    Content touching the very edge is what a crop looks like from the inside. A figure drawn
    with any margin at all should never reach the frame.
    """
    try:
        from PIL import Image
    except ImportError:
        return "SKIPPED — Pillow is not installed, so the ink box was not measured"
    im = Image.open(path).convert("RGB")
    w, h = im.size
    px = im.load()
    # ⚠ NOT `!= (255,255,255)`. That was the first version, and it failed a correct figure:
    # draw.io antialiases the ground rectangle's own boundary to (254,254,254), one value off
    # white and invisible, on the outermost column of every figure this generator makes. A
    # check that fires on every correct input is worse than no check. INK_MAX is set well
    # below any real content and well above antialiasing; the crop this gate exists to catch
    # had black text and coloured fills sitting on the frame.
    INK_MAX = 240
    def dark(x, y): return min(px[x, y]) < INK_MAX
    def col(x): return any(dark(x, y) for y in range(0, h, 3))
    def row(y): return any(dark(x, y) for x in range(0, w, 3))
    touching = []
    for x in range(margin_px):
        if col(x) or col(w - 1 - x):
            touching.append("left/right")
            break
    for y in range(margin_px):
        if row(y) or row(h - 1 - y):
            touching.append("top/bottom")
            break
    if touching:
        _fail(path, "ink reaches the frame",
              f"content touches the {' and '.join(touching)} edge, which is what a crop "
              f"looks like from inside the file. Measure the source too before concluding.")
    return "no ink on the outer rows or columns"


# --------------------------------------------------------------------------- embedded rasters
_BAD_MIME = re.compile(rb"data:image/(?!svg\+xml)([a-z]+)", re.I)


def check_no_embedded_raster(path: Path) -> str:
    """Refuse a 'vector' artefact that is really a picture of one.

    ⚠ `data:image/svg+xml` is allowed and expected — that is how icons are inlined. Anything
    else in a data URI is a bitmap wearing a vector's clothes.
    """
    raw = path.read_bytes()
    suffix = path.suffix.lower()

    bad = {m.group(1).decode(errors="replace").lower() for m in _BAD_MIME.finditer(raw)}
    if bad:
        _fail(path, "a raster is embedded in a vector file",
              f"found data URIs of type {sorted(bad)}. `image/svg+xml` is fine (that is how "
              f"icons are inlined); a bitmap is not — it means something was pasted rather "
              f"than drawn.")

    if suffix == ".svg":
        n = len(re.findall(rb"<image\b", raw))
        if n:
            _fail(path, "a raster is embedded in an SVG",
                  f"{n} <image> element(s). Asking a model to 'output SVG' produces exactly "
                  f"this when it traces nothing and wraps a bitmap instead.")
        return "no <image> elements and no bitmap data URIs"

    if suffix == ".pdf":
        n = len(re.findall(rb"/Subtype\s*/Image", raw))
        if n:
            _fail(path, "a raster is embedded in a PDF",
                  f"{n} image XObject(s). A diagram exported as vector should contain none.")
        return "no image XObjects"

    return "no bitmap data URIs"


# --------------------------------------------------------------------------- content is real
def check_element_count(path: Path, at_least: int) -> str:
    """A file that exists is not a file with anything in it.

    The `.drawio` case reconciles the cell count the way W08 reconciles the Visio shape
    count: the generator knows how many nodes it emitted, so a file with fewer is a file
    that lost something.
    """
    raw = path.read_bytes()
    suffix = path.suffix.lower()
    if suffix == ".drawio":
        n = len(re.findall(rb"<mxCell\b", raw))
        kind = "mxCell"
    elif suffix == ".svg":
        n = len(re.findall(rb"<(rect|path|circle|line|text|polygon|ellipse)\b", raw))
        kind = "drawing element"
    elif suffix == ".pdf":
        n = _pdf_text_ops(raw)
        kind = "text-showing operator"
    else:
        return f"SKIPPED — no element rule for {suffix}"
    if n < at_least:
        _fail(path, "the artefact is emptier than the generator claims",
              f"{n} {kind}(s), expected at least {at_least}.")
    return f"{n} {kind}(s), at least {at_least} required"


def _pdf_text_ops(raw: bytes) -> int:
    """Count text-showing operators, decompressing streams where necessary."""
    n = len(re.findall(rb"\bTj\b|\bTJ\b", raw))
    for m in re.finditer(rb"stream\r?\n(.*?)endstream", raw, re.S):
        try:
            n += len(re.findall(rb"\bTj\b|\bTJ\b", zlib.decompress(m.group(1))))
        except Exception:
            continue
    return n


# --------------------------------------------------------------------------- staleness
def check_is_fresh(path: Path, newer_than: Path) -> str:
    """The artefact must be newer than the source that claims to have produced it.

    ⛔ This is the `png.exists()` bug as a rule. A check that a file exists is satisfied by
    a file from last week; a check that it is newer than its generator is not.
    """
    if not path.exists():
        _fail(path, "the artefact was not written", f"{path} does not exist")
    if path.stat().st_mtime < newer_than.stat().st_mtime:
        _fail(path, "the artefact is stale",
              f"{path.name} is older than {newer_than.name}. It is left over from an "
              f"earlier run; the current run did not write it.")
    return f"newer than {newer_than.name}"


# --------------------------------------------------------------------------- the whole gate
def gate(canvas_w: float, canvas_h: float, *, drawio: Path | None = None,
         pdf: Path | None = None, png: Path | None = None, svg: Path | None = None,
         min_elements: int = 0, source: Path | None = None, verbose: bool = True) -> None:
    """Run every applicable check. Raises SystemExit on the first failure."""
    checks: list[tuple[Path, str, str]] = []
    for f in (drawio, pdf, png, svg):
        if f is None:
            continue
        f = Path(f)
        if source is not None:
            checks.append((f, "fresh", check_is_fresh(f, Path(source))))
        if f.suffix.lower() in (".svg", ".pdf", ".drawio"):
            checks.append((f, "no embedded raster", check_no_embedded_raster(f)))
        if min_elements and f.suffix.lower() in (".drawio", ".svg", ".pdf"):
            checks.append((f, "content", check_element_count(f, min_elements)))
        if f.suffix.lower() in (".png", ".pdf"):
            checks.append((f, "vs canvas", check_trim_is_only_margin(f, canvas_w, canvas_h)))
        if f.suffix.lower() == ".png":
            checks.append((f, "ink box", check_ink_inside(f)))
    if pdf is not None and png is not None:
        checks.append((Path(png), "exports agree", check_exports_agree(Path(pdf), Path(png))))
    if verbose:
        for f, name, detail in checks:
            print(f"  [artefact-gate] {f.name:34s} {name:20s} {detail}")
