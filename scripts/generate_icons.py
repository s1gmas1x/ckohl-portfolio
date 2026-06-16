#!/usr/bin/env python3

from __future__ import annotations

import json
import math
import struct
import xml.etree.ElementTree as ET
import zlib
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
SOURCE_SVG = ROOT / "src/assets/svg/logo/ck-logo-icon.svg"
PUBLIC_DIR = ROOT / "public"
PUBLIC_ICONS_DIR = PUBLIC_DIR / "icons"


@dataclass(frozen=True)
class Color:
    r: int
    g: int
    b: int
    a: int = 255


@dataclass(frozen=True)
class Matrix:
    a: float = 1.0
    b: float = 0.0
    c: float = 0.0
    d: float = 1.0
    e: float = 0.0
    f: float = 0.0

    def apply(self, x: float, y: float) -> tuple[float, float]:
        return (
            self.a * x + self.c * y + self.e,
            self.b * x + self.d * y + self.f,
        )

    def multiply(self, other: "Matrix") -> "Matrix":
        return Matrix(
            a=self.a * other.a + self.c * other.b,
            b=self.b * other.a + self.d * other.b,
            c=self.a * other.c + self.c * other.d,
            d=self.b * other.c + self.d * other.d,
            e=self.a * other.e + self.c * other.f + self.e,
            f=self.b * other.e + self.d * other.f + self.f,
        )


@dataclass
class RenderState:
    transform: Matrix
    fill: Color | None = None
    stroke: Color | None = None
    stroke_width: float = 1.0


def parse_float_list(value: str) -> list[float]:
    cleaned = value.replace(",", " ")
    return [float(part) for part in cleaned.split() if part]


def parse_transform(value: str | None) -> Matrix:
    if not value:
        return Matrix()

    matrix = Matrix()
    remainder = value.strip()
    while remainder:
        name, tail = remainder.split("(", 1)
        args_text, remainder = tail.split(")", 1)
        args = parse_float_list(args_text)
        remainder = remainder.strip()
        if name == "translate":
            tx = args[0]
            ty = args[1] if len(args) > 1 else 0.0
            matrix = matrix.multiply(Matrix(e=tx, f=ty))
        elif name == "scale":
            sx = args[0]
            sy = args[1] if len(args) > 1 else sx
            matrix = matrix.multiply(Matrix(a=sx, d=sy))
        else:
            raise ValueError(f"Unsupported transform: {name}")
    return matrix


def parse_color(value: str | None) -> Color | None:
    if not value or value == "none":
        return None
    value = value.strip()
    if value.startswith("#") and len(value) == 7:
        return Color(
            r=int(value[1:3], 16),
            g=int(value[3:5], 16),
            b=int(value[5:7], 16),
        )
    raise ValueError(f"Unsupported color: {value}")


def parse_path_data(d: str) -> list[tuple[str, list[float]]]:
    tokens: list[str] = []
    current = ""
    for char in d:
        if char.isalpha():
            if current:
                tokens.append(current)
                current = ""
            tokens.append(char)
        elif char in " ,\n\t\r":
            if current:
                tokens.append(current)
                current = ""
        elif char == "-":
            if current and current not in "+-":
                tokens.append(current)
                current = "-"
            else:
                current += char
        else:
            current += char
    if current:
        tokens.append(current)

    result: list[tuple[str, list[float]]] = []
    i = 0
    command = ""
    expected_counts = {"M": 2, "L": 2, "H": 1, "V": 1, "C": 6, "Z": 0}
    while i < len(tokens):
        token = tokens[i]
        if token.isalpha():
            command = token.upper()
            i += 1
            if command == "Z":
                result.append((command, []))
                continue
        count = expected_counts[command]
        if count == 0:
            continue
        values = [float(tokens[i + offset]) for offset in range(count)]
        i += count
        result.append((command, values))
    return result


def cubic_point(
    p0: tuple[float, float],
    p1: tuple[float, float],
    p2: tuple[float, float],
    p3: tuple[float, float],
    t: float,
) -> tuple[float, float]:
    mt = 1 - t
    x = (
        (mt ** 3) * p0[0]
        + 3 * (mt ** 2) * t * p1[0]
        + 3 * mt * (t ** 2) * p2[0]
        + (t ** 3) * p3[0]
    )
    y = (
        (mt ** 3) * p0[1]
        + 3 * (mt ** 2) * t * p1[1]
        + 3 * mt * (t ** 2) * p2[1]
        + (t ** 3) * p3[1]
    )
    return x, y


def flatten_path(commands: list[tuple[str, list[float]]], transform: Matrix) -> tuple[list[list[tuple[float, float]]], list[list[tuple[float, float]]]]:
    polygons: list[list[tuple[float, float]]] = []
    polylines: list[list[tuple[float, float]]] = []
    current_polygon: list[tuple[float, float]] = []
    current_line: list[tuple[float, float]] = []
    cursor = (0.0, 0.0)
    start = (0.0, 0.0)

    for command, values in commands:
        if command == "M":
            if current_polygon:
                polygons.append(current_polygon)
                current_polygon = []
            if current_line:
                polylines.append(current_line)
                current_line = []
            cursor = (values[0], values[1])
            start = cursor
            transformed = transform.apply(*cursor)
            current_polygon = [transformed]
            current_line = [transformed]
        elif command == "L":
            cursor = (values[0], values[1])
            transformed = transform.apply(*cursor)
            current_polygon.append(transformed)
            current_line.append(transformed)
        elif command == "H":
            cursor = (values[0], cursor[1])
            transformed = transform.apply(*cursor)
            current_polygon.append(transformed)
            current_line.append(transformed)
        elif command == "V":
            cursor = (cursor[0], values[0])
            transformed = transform.apply(*cursor)
            current_polygon.append(transformed)
            current_line.append(transformed)
        elif command == "C":
            p0 = cursor
            p1 = (values[0], values[1])
            p2 = (values[2], values[3])
            p3 = (values[4], values[5])
            for step in range(1, 25):
                point = cubic_point(p0, p1, p2, p3, step / 24)
                transformed = transform.apply(*point)
                current_polygon.append(transformed)
                current_line.append(transformed)
            cursor = p3
        elif command == "Z":
            transformed = transform.apply(*start)
            if not current_polygon or current_polygon[-1] != transformed:
                current_polygon.append(transformed)
            polygons.append(current_polygon)
            current_polygon = []
            if current_line:
                current_line.append(transformed)
                polylines.append(current_line)
                current_line = []
            cursor = start
        else:
            raise ValueError(f"Unsupported path command: {command}")

    if current_polygon:
        polygons.append(current_polygon)
    if current_line:
        polylines.append(current_line)
    return polygons, polylines


def point_in_polygon(x: float, y: float, polygon: list[tuple[float, float]]) -> bool:
    inside = False
    n = len(polygon)
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        crosses = (y1 > y) != (y2 > y)
        if not crosses:
            continue
        intersection = (x2 - x1) * (y - y1) / (y2 - y1) + x1
        if x < intersection:
            inside = not inside
    return inside


def distance_to_segment(
    px: float,
    py: float,
    ax: float,
    ay: float,
    bx: float,
    by: float,
) -> float:
    dx = bx - ax
    dy = by - ay
    if dx == 0 and dy == 0:
        return math.hypot(px - ax, py - ay)
    t = ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)
    t = max(0.0, min(1.0, t))
    cx = ax + t * dx
    cy = ay + t * dy
    return math.hypot(px - cx, py - cy)


def point_on_polyline(x: float, y: float, points: list[tuple[float, float]], width: float) -> bool:
    threshold = width / 2
    for start, end in zip(points, points[1:]):
        if distance_to_segment(x, y, start[0], start[1], end[0], end[1]) <= threshold:
            return True
    return False


def blend(bottom: Color, top: Color) -> Color:
    alpha = top.a / 255
    inv = 1 - alpha
    return Color(
        r=round(top.r * alpha + bottom.r * inv),
        g=round(top.g * alpha + bottom.g * inv),
        b=round(top.b * alpha + bottom.b * inv),
        a=round(top.a + bottom.a * inv),
    )


def render_svg_rgba(svg_path: Path, size: int, supersample: int = 4) -> bytes:
    tree = ET.parse(svg_path)
    root = tree.getroot()
    view_box = [float(part) for part in root.attrib["viewBox"].split()]
    _, _, vb_width, vb_height = view_box
    scale = size / vb_width

    shapes: list[tuple[str, object, RenderState]] = []

    def walk(node: ET.Element, state: RenderState) -> None:
        tag = node.tag.split("}")[-1]
        next_state = RenderState(
            transform=state.transform.multiply(parse_transform(node.attrib.get("transform"))),
            fill=parse_color(node.attrib.get("fill", None)) if "fill" in node.attrib else state.fill,
            stroke=parse_color(node.attrib.get("stroke", None)) if "stroke" in node.attrib else state.stroke,
            stroke_width=float(node.attrib.get("stroke-width", state.stroke_width)),
        )

        if tag == "rect":
            shapes.append(("rect", dict(node.attrib), next_state))
        elif tag == "circle":
            shapes.append(("circle", dict(node.attrib), next_state))
        elif tag == "path":
            shapes.append(("path", node.attrib["d"], next_state))

        for child in node:
            walk(child, next_state)

    walk(root, RenderState(transform=Matrix()))

    prepared_shapes: list[tuple[str, object, Color | None, Color | None, float]] = []
    for shape_type, payload, state in shapes:
        if shape_type == "rect":
            rect = payload
            x0 = float(rect["x"]) if "x" in rect else 0.0
            y0 = float(rect["y"]) if "y" in rect else 0.0
            width = float(rect["width"])
            height = float(rect["height"])
            p0 = state.transform.apply(x0, y0)
            p1 = state.transform.apply(x0 + width, y0 + height)
            left, right = sorted((p0[0], p1[0]))
            top, bottom = sorted((p0[1], p1[1]))
            prepared_shapes.append(("rect", (left, top, right, bottom), state.fill, None, 0.0))
        elif shape_type == "circle":
            circle = payload
            cx, cy = state.transform.apply(float(circle["cx"]), float(circle["cy"]))
            radius = float(circle["r"]) * state.transform.a
            prepared_shapes.append(("circle", (cx, cy, radius), state.fill, None, 0.0))
        elif shape_type == "path":
            polygons, polylines = flatten_path(parse_path_data(payload), state.transform)
            prepared_shapes.append(
                (
                    "path",
                    (polygons, polylines),
                    state.fill,
                    state.stroke,
                    state.stroke_width * state.transform.a,
                )
            )

    pixels = bytearray(size * size * 4)

    def set_pixel(px: int, py: int, color: Color) -> None:
        if not (0 <= px < size and 0 <= py < size):
            return
        offset = (py * size + px) * 4
        pixels[offset] = color.r
        pixels[offset + 1] = color.g
        pixels[offset + 2] = color.b
        pixels[offset + 3] = color.a

    for shape_type, payload, fill, stroke, stroke_width in prepared_shapes:
        if shape_type == "rect" and fill:
            left, top, right, bottom = payload
            x_start = max(0, int(math.floor(left * scale)))
            x_end = min(size, int(math.ceil(right * scale)))
            y_start = max(0, int(math.floor(top * scale)))
            y_end = min(size, int(math.ceil(bottom * scale)))
            for py in range(y_start, y_end):
                for px in range(x_start, x_end):
                    set_pixel(px, py, fill)
        elif shape_type == "circle" and fill:
            cx, cy, radius = payload
            x_start = max(0, int(math.floor((cx - radius) * scale)))
            x_end = min(size, int(math.ceil((cx + radius) * scale)))
            y_start = max(0, int(math.floor((cy - radius) * scale)))
            y_end = min(size, int(math.ceil((cy + radius) * scale)))
            for py in range(y_start, y_end):
                for px in range(x_start, x_end):
                    x = (px + 0.5) / scale
                    y = (py + 0.5) / scale
                    if math.hypot(x - cx, y - cy) <= radius:
                        set_pixel(px, py, fill)
        elif shape_type == "path":
            polygons, polylines = payload
            if fill:
                for polygon in polygons:
                    xs = [point[0] for point in polygon]
                    ys = [point[1] for point in polygon]
                    x_start = max(0, int(math.floor(min(xs) * scale)))
                    x_end = min(size, int(math.ceil(max(xs) * scale)))
                    y_start = max(0, int(math.floor(min(ys) * scale)))
                    y_end = min(size, int(math.ceil(max(ys) * scale)))
                    for py in range(y_start, y_end):
                        for px in range(x_start, x_end):
                            x = (px + 0.5) / scale
                            y = (py + 0.5) / scale
                            if point_in_polygon(x, y, polygon):
                                set_pixel(px, py, fill)
            if stroke:
                for line in polylines:
                    xs = [point[0] for point in line]
                    ys = [point[1] for point in line]
                    padding = stroke_width / 2
                    x_start = max(0, int(math.floor((min(xs) - padding) * scale)))
                    x_end = min(size, int(math.ceil((max(xs) + padding) * scale)))
                    y_start = max(0, int(math.floor((min(ys) - padding) * scale)))
                    y_end = min(size, int(math.ceil((max(ys) + padding) * scale)))
                    for py in range(y_start, y_end):
                        for px in range(x_start, x_end):
                            x = (px + 0.5) / scale
                            y = (py + 0.5) / scale
                            if point_on_polyline(x, y, line, stroke_width):
                                set_pixel(px, py, stroke)

    return bytes(pixels)


def resize_rgba(source: bytes, source_size: int, target_size: int) -> bytes:
    if source_size == target_size:
        return source

    output = bytearray(target_size * target_size * 4)
    scale = source_size / target_size

    def get_pixel(ix: int, iy: int) -> tuple[int, int, int, int]:
        offset = (iy * source_size + ix) * 4
        return (
            source[offset],
            source[offset + 1],
            source[offset + 2],
            source[offset + 3],
        )

    for y in range(target_size):
        sy = (y + 0.5) * scale - 0.5
        y0 = max(0, min(source_size - 1, int(math.floor(sy))))
        y1 = min(source_size - 1, y0 + 1)
        wy = sy - y0
        for x in range(target_size):
            sx = (x + 0.5) * scale - 0.5
            x0 = max(0, min(source_size - 1, int(math.floor(sx))))
            x1 = min(source_size - 1, x0 + 1)
            wx = sx - x0

            p00 = get_pixel(x0, y0)
            p10 = get_pixel(x1, y0)
            p01 = get_pixel(x0, y1)
            p11 = get_pixel(x1, y1)

            channels = []
            for index in range(4):
                top = p00[index] * (1 - wx) + p10[index] * wx
                bottom = p01[index] * (1 - wx) + p11[index] * wx
                channels.append(round(top * (1 - wy) + bottom * wy))

            offset = (y * target_size + x) * 4
            output[offset:offset + 4] = bytes(channels)

    return bytes(output)


def png_chunk(chunk_type: bytes, data: bytes) -> bytes:
    return (
        struct.pack(">I", len(data))
        + chunk_type
        + data
        + struct.pack(">I", zlib.crc32(chunk_type + data) & 0xFFFFFFFF)
    )


def png_bytes(width: int, height: int, rgba: bytes) -> bytes:
    stride = width * 4
    raw = bytearray()
    for y in range(height):
        raw.append(0)
        start = y * stride
        raw.extend(rgba[start:start + stride])

    header = struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0)
    return b"".join(
        [
            b"\x89PNG\r\n\x1a\n",
            png_chunk(b"IHDR", header),
            png_chunk(b"IDAT", zlib.compress(bytes(raw), 9)),
            png_chunk(b"IEND", b""),
        ]
    )


def ico_bytes(png_images: Iterable[tuple[int, bytes]]) -> bytes:
    images = list(png_images)
    header = struct.pack("<HHH", 0, 1, len(images))
    offset = 6 + 16 * len(images)
    entries = bytearray()
    data = bytearray()
    for size, png in images:
        width_byte = 0 if size >= 256 else size
        height_byte = 0 if size >= 256 else size
        entries.extend(
            struct.pack(
                "<BBBBHHII",
                width_byte,
                height_byte,
                0,
                0,
                1,
                32,
                len(png),
                offset,
            )
        )
        data.extend(png)
        offset += len(png)
    return header + bytes(entries) + bytes(data)


def write_binary(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def write_text(path: Path, data: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(data, encoding="utf-8")


def main() -> None:
    PUBLIC_DIR.mkdir(exist_ok=True)
    PUBLIC_ICONS_DIR.mkdir(exist_ok=True)

    svg_text = SOURCE_SVG.read_text(encoding="utf-8")
    write_text(PUBLIC_DIR / "favicon.svg", svg_text)

    sizes = {
        "favicon-16x16.png": 16,
        "favicon-32x32.png": 32,
        "favicon-48x48.png": 48,
        "favicon-96x96.png": 96,
        "favicon-128x128.png": 128,
        "apple-touch-icon.png": 180,
        "android-chrome-192x192.png": 192,
        "android-chrome-512x512.png": 512,
        "mstile-150x150.png": 150,
    }

    base_size = 512
    base_rgba = render_svg_rgba(SOURCE_SVG, base_size, supersample=1)

    rendered: dict[int, bytes] = {}
    for filename, size in sizes.items():
        rgba = resize_rgba(base_rgba, base_size, size)
        png = png_bytes(size, size, rgba)
        rendered[size] = png
        write_binary(PUBLIC_DIR / filename, png)

    compatibility_icons = {
        "favicon-16x16.png": rendered[16],
        "favicon-32x32.png": rendered[32],
        "favicon-96x96.png": rendered[96],
        "favicon-128x128.png": rendered[128],
    }
    for filename, png in compatibility_icons.items():
        write_binary(PUBLIC_ICONS_DIR / filename, png)

    favicon_ico = ico_bytes(
        [
            (16, rendered[16]),
            (32, rendered[32]),
            (48, rendered[48]),
        ]
    )
    write_binary(PUBLIC_DIR / "favicon.ico", favicon_ico)

    manifest = {
        "name": "CKohl Portfolio",
        "short_name": "CKohl",
        "description": "Chad Kohl portfolio site",
        "display": "standalone",
        "background_color": "#111820",
        "theme_color": "#111820",
        "icons": [
            {
                "src": "/android-chrome-192x192.png",
                "sizes": "192x192",
                "type": "image/png",
                "purpose": "any maskable",
            },
            {
                "src": "/android-chrome-512x512.png",
                "sizes": "512x512",
                "type": "image/png",
                "purpose": "any maskable",
            },
        ],
    }
    write_text(PUBLIC_DIR / "site.webmanifest", json.dumps(manifest, indent=2) + "\n")


if __name__ == "__main__":
    main()
