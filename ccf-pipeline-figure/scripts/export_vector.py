#!/usr/bin/env python3
"""Export a reconstructed, live-text SVG; never vectorizes a raster input."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess
import unicodedata
import xml.etree.ElementTree as ET


def compact(value):
    return re.sub(r"\s+", "", unicodedata.normalize("NFC", value))


def inspect_svg(source, expected, font_names):
    raw = source.read_text(encoding="utf-8")
    if "<!DOCTYPE" in raw.upper() or "<!ENTITY" in raw.upper():
        raise ValueError("DTD/entities are not supported")
    root = ET.fromstring(raw)
    allowed = {"svg", "g", "path", "rect", "circle", "ellipse", "line",
               "polyline", "polygon", "text", "tspan", "title", "desc"}
    geometry = 0
    labels = []
    for node in root.iter():
        tag = node.tag.split("}")[-1]
        if tag not in allowed:
            raise ValueError(f"Unsupported SVG element: {tag}")
        if tag in {"path", "rect", "circle", "ellipse", "line", "polyline", "polygon"}:
            geometry += 1
        for attr, value in node.attrib.items():
            name = attr.split("}")[-1]
            if name in {"href", "style", "filter", "clip-path", "mask", "display", "visibility"} or "url(" in value.lower():
                raise ValueError(f"Unsupported/external styling: {name}")
            if name.startswith("on"):
                raise ValueError("SVG event handlers are not allowed")
            if name in {"opacity", "fill-opacity", "stroke-opacity"} and float(value) != 1:
                raise ValueError("This exporter requires fully opaque primitives")
        if tag == "text":
            label = "".join(node.itertext()).strip()
            if not label or node.get("fill") in {"none", "transparent"}:
                raise ValueError("Empty or hidden text")
            if node.get("font-family") not in font_names:
                raise ValueError("Every text element must name a registered font explicitly")
            if float(node.get("font-size", "0")) <= 0:
                raise ValueError("Text must have a positive explicit font size")
            labels.append(label)
    if not geometry or not labels:
        raise ValueError("SVG must contain both real geometry and live text")
    if Counter(map(compact, labels)) != Counter(map(compact, expected)):
        raise ValueError("SVG text does not match reviewed inventory (including repeats)")
    viewbox = [float(x) for x in root.get("viewBox", "").replace(",", " ").split()]
    if len(viewbox) != 4 or viewbox[2] <= 0 or viewbox[3] <= 0:
        raise ValueError("Expected a nonempty viewBox")
    return labels, geometry, viewbox


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("svg", type=Path)
    parser.add_argument("--pdf", required=True, type=Path)
    parser.add_argument("--width-in", required=True, type=float)
    parser.add_argument("--expected-text", required=True, type=Path)
    parser.add_argument("--font", action="append", required=True, metavar="NAME=FILE")
    args = parser.parse_args()
    if args.width_in <= 0:
        parser.error("--width-in must be positive")
    fonts = dict(item.split("=", 1) for item in args.font)
    expected = json.loads(args.expected_text.read_text(encoding="utf-8"))
    if not isinstance(expected, list) or not expected or not all(isinstance(s, str) and s.strip() for s in expected):
        parser.error("expected-text must contain a nonempty JSON list of visible strings")
    report_path = args.pdf.with_suffix(".export.json")
    text_path = args.pdf.with_suffix(".extracted.txt")
    for target in (args.pdf, report_path, text_path):
        if target.exists():
            parser.error(f"Refusing to overwrite {target}")
    labels, geometry, viewbox = inspect_svg(args.svg, expected, fonts)
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfgen import canvas
    from reportlab.graphics import renderPDF
    from svglib.svglib import svg2rlg
    from svglib.fonts import register_font
    from pypdf import PdfReader
    font_info = {}
    for name, filename in fonts.items():
        font = TTFont(name, filename)
        pdfmetrics.registerFont(font)
        # One explicit file per SVG family. Weight/style must not trigger font discovery.
        for weight in ('normal', 'bold'):
            _, exact = register_font(name, font_path=filename, weight=weight, rlgFontName=name)
            if not exact:
                raise ValueError(f"Could not bind SVG font to its explicit file: {name}")
        font_info[name] = {"path": str(Path(filename).resolve()),
                           "sha256": hashlib.sha256(Path(filename).read_bytes()).hexdigest()}
    root = ET.parse(args.svg).getroot()
    for node in root.iter():
        if node.tag.split("}")[-1] == "text":
            font = pdfmetrics.getFont(node.get("font-family"))
            missing = [c for c in "".join(node.itertext()) if not c.isspace() and ord(c) not in font.face.charToGlyph]
            if missing:
                raise ValueError(f"Font lacks glyphs: {missing}")
    drawing = svg2rlg(str(args.svg))
    if drawing is None or not drawing.width or not drawing.height:
        raise ValueError("SVG renderer produced an empty drawing")
    # ReportLab otherwise initializes graphics with an unembedded Times-Roman resource.
    drawing.initialFontName = next(iter(fonts))
    def text_fonts(node):
        found = {node.fontName} if hasattr(node, 'text') and hasattr(node, 'fontName') else set()
        for child in getattr(node, 'contents', []):
            found.update(text_fonts(child))
        return found
    used_fonts = text_fonts(drawing)
    if not used_fonts or not used_fonts.issubset(fonts):
        raise ValueError(f"Renderer substituted an undeclared font: {used_fonts - fonts.keys()}")
    width = args.width_in * 72
    height = width * viewbox[3] / viewbox[2]
    drawing.scale(width / drawing.width, height / drawing.height)
    args.pdf.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(args.pdf), pagesize=(width, height),
                        initialFontName=next(iter(fonts)), initialFontSize=10)
    pdf.setTitle(args.svg.stem + " — reconstructed vector figure")
    renderPDF.draw(drawing, pdf, 0, 0)
    pdf.showPage()
    pdf.save()
    subprocess.run(["pdftotext", "-enc", "UTF-8", str(args.pdf), str(text_path)], check=True)
    extracted = text_path.read_text(encoding="utf-8")
    flattened = compact(extracted)
    missing = {s: n for s, n in Counter(map(compact, expected)).items() if flattened.count(s) < n}
    reader = PdfReader(args.pdf)
    images = sum(len(p.images) for p in reader.pages)
    font_report = subprocess.check_output(["pdffonts", str(args.pdf)], text=True)
    font_rows = [line.split() for line in font_report.splitlines()[2:] if line.strip()]
    # Last columns: emb sub uni object ID. Font/type names contain variable spaces.
    font_checks = bool(font_rows) and all(row[-5] == "yes" and row[-3] == "yes" for row in font_rows)
    passed = not missing and images == 0 and font_checks and len(reader.pages) == 1
    report = {"text_export_passed": passed, "scientific_acceptance": "not_checked_by_exporter",
              "visual_fidelity": "requires_manual_render_review", "svg": str(args.svg.resolve()),
              "pdf": str(args.pdf.resolve()), "svg_sha256": hashlib.sha256(args.svg.read_bytes()).hexdigest(),
              "label_count": len(labels), "geometry_count": geometry, "missing_labels": missing,
              "raster_image_count": images, "fonts_embedded_with_unicode": font_checks,
              "page_points": [width, height], "fonts": font_info,
              "rendered_font_names": sorted(used_fonts), "pdffonts": font_report}
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if not passed:
        raise SystemExit("Export exists but validation FAILED; inspect report before delivery")


if __name__ == "__main__":
    main()
