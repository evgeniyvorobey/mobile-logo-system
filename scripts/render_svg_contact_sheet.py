#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
from datetime import date
from html import escape
from pathlib import Path
import sys


DEFAULT_SIZES = [1024, 180, 120, 60, 48, 29]


def parse_sizes(raw: str) -> list[int]:
    sizes: list[int] = []
    for part in raw.split(","):
        value = part.strip()
        if not value:
            continue
        try:
            size = int(value)
        except ValueError as exc:
            raise argparse.ArgumentTypeError(
                f"Invalid size {value!r}; use comma-separated integers."
            ) from exc
        if size <= 0:
            raise argparse.ArgumentTypeError("Sizes must be positive integers.")
        sizes.append(size)
    if not sizes:
        raise argparse.ArgumentTypeError("At least one size is required.")
    return sizes


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create an HTML contact sheet for SVG logo/icon review."
    )
    parser.add_argument(
        "svg_files",
        nargs="+",
        help="SVG files to include in the review sheet.",
    )
    parser.add_argument(
        "--output",
        default="svg-contact-sheet.html",
        help="HTML file to write. Default: svg-contact-sheet.html",
    )
    parser.add_argument(
        "--title",
        default="SVG Logo Contact Sheet",
        help="Title shown in the generated review sheet.",
    )
    parser.add_argument(
        "--sizes",
        type=parse_sizes,
        default=DEFAULT_SIZES,
        help="Comma-separated reduction sizes. Default: 1024,180,120,60,48,29",
    )
    return parser.parse_args()


def read_svg(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"SVG file not found: {path}")
    if not path.is_file():
        raise SystemExit(f"SVG path is not a file: {path}")
    if path.suffix.lower() != ".svg":
        raise SystemExit(f"Expected an .svg file: {path}")
    return path.read_text(encoding="utf-8")


def svg_data_uri(svg_text: str) -> str:
    encoded = base64.b64encode(svg_text.encode("utf-8")).decode("ascii")
    return f"data:image/svg+xml;base64,{encoded}"


def display_size(size: int) -> int:
    return min(size, 180)


def img_tag(uri: str, size: int, *, class_name: str = "") -> str:
    class_attr = f' class="{escape(class_name)}"' if class_name else ""
    shown = display_size(size)
    return (
        f'<img{class_attr} data-review-img="true" src="{uri}" width="{shown}" height="{shown}" '
        f'alt="SVG rendered at {size}px">'
    )


def render_reduction_strip(uri: str, sizes: list[int]) -> str:
    cells = []
    for size in sizes:
        cells.append(
            f"""
            <div class="sample">
              <div class="sample-stage checker" data-size="{size}" style="width:{display_size(size)}px;height:{display_size(size)}px">
                {img_tag(uri, size)}
              </div>
              <div class="label">{size}px</div>
            </div>
            """
        )
    return "\n".join(cells)


def render_contexts(uri: str) -> str:
    contexts = [
        ("Light", "tile-light", ""),
        ("Dark", "tile-dark", ""),
        ("Gray", "tile-gray", ""),
        ("Monochrome black", "tile-light", "mono-black"),
        ("Monochrome white", "tile-dark", "mono-white"),
        ("iOS squircle", "tile-light mask-squircle", ""),
        ("Android circle", "tile-light mask-circle", ""),
        ("Rounded square", "tile-light mask-rounded", ""),
        ("Teardrop proxy", "tile-light mask-teardrop", ""),
    ]
    parts = []
    for label, tile_class, image_class in contexts:
        parts.append(
            f"""
            <div class="context-card">
              <div class="context-stage {escape(tile_class)}">
                {img_tag(uri, 96, class_name=image_class)}
              </div>
              <div class="label">{escape(label)}</div>
            </div>
            """
        )
    return "\n".join(parts)


def render_safe_zone_previews(uri: str) -> str:
    previews = [
        (
            "iOS safe zone",
            "ios-frame mask-squircle",
            "safe-zone-overlay ios-safe-zone",
            "90% optical content circle",
            "ios-safe-zone",
        ),
        (
            "Android 108dp canvas",
            "android-adaptive-frame",
            "safe-zone-overlay android-safe-zone",
            "72dp safe zone plus 64dp critical zone",
            "android-safe-zone",
        ),
        (
            "Android circle mask",
            "android-adaptive-frame mask-circle",
            "safe-zone-overlay android-safe-zone",
            "foreground must survive circular crop",
            "android-circle-frame",
        ),
        (
            "Android squircle mask",
            "android-adaptive-frame mask-squircle",
            "safe-zone-overlay android-safe-zone",
            "foreground must survive rounded-square crop",
            "android-squircle-frame",
        ),
    ]
    cards = []
    for label, frame_class, safe_class, note, test_id in previews:
        critical = (
            '<div class="safe-zone-overlay android-critical-zone" aria-hidden="true"></div>'
            if "android" in test_id
            else ""
        )
        cards.append(
            f"""
            <div class="platform-card" data-preview="{escape(test_id)}">
              <div class="platform-stage {escape(frame_class)}">
                <div class="adaptive-background-layer"></div>
                {img_tag(uri, 96, class_name="adaptive-foreground-layer")}
                <div class="{escape(safe_class)}" aria-hidden="true"></div>
                {critical}
              </div>
              <div class="label">{escape(label)}</div>
              <div class="microcopy">{escape(note)}</div>
            </div>
            """
        )
    return "\n".join(cards)


def render_layer_previews(uri: str) -> str:
    return f"""
      <div class="layer-card" data-preview="background-layer">
        <div class="layer-stage adaptive-background-only">
          <div class="adaptive-background-layer"></div>
        </div>
        <div class="label">Background layer</div>
      </div>
      <div class="layer-card" data-preview="foreground-layer">
        <div class="layer-stage checker">
          {img_tag(uri, 96, class_name="adaptive-foreground-only")}
        </div>
        <div class="label">Foreground layer</div>
      </div>
      <div class="layer-card" data-preview="combined-adaptive">
        <div class="layer-stage android-adaptive-frame mask-rounded">
          <div class="adaptive-background-layer"></div>
          {img_tag(uri, 96, class_name="adaptive-foreground-layer")}
          <div class="safe-zone-overlay android-safe-zone" aria-hidden="true"></div>
        </div>
        <div class="label">Combined adaptive proxy</div>
      </div>
    """


def render_document(title: str, svg_paths: list[Path], sizes: list[int]) -> str:
    sections = []
    for path in svg_paths:
        svg_text = read_svg(path)
        uri = svg_data_uri(svg_text)
        sections.append(
            f"""
            <section class="mark-section">
              <h2>{escape(path.name)}</h2>
              <p class="path">{escape(str(path))}</p>

              <h3>Reduction Review</h3>
              <div class="reduction-grid" data-section="reduction-review">
                {render_reduction_strip(uri, sizes)}
              </div>

              <h3>Surface And Mask Review</h3>
              <div class="context-grid" data-section="surface-mask-review">
                {render_contexts(uri)}
              </div>

              <h3>Platform Safe Zone Review</h3>
              <div class="platform-grid" data-section="safe-zone-review">
                {render_safe_zone_previews(uri)}
              </div>

              <h3>Foreground / Background Preview</h3>
              <div class="layer-grid" data-section="foreground-background-preview">
                {render_layer_previews(uri)}
              </div>
            </section>
            """
        )

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)}</title>
  <style>
    :root {{
      --ink: #24242a;
      --muted: #686872;
      --line: #d9d9df;
      --paper: #fbfbfd;
      --panel: #ffffff;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      padding: 32px;
      color: var(--ink);
      background: var(--paper);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      line-height: 1.45;
    }}
    header, .mark-section {{
      max-width: 1180px;
      margin: 0 auto 28px;
    }}
    header {{
      border-bottom: 1px solid var(--line);
      padding-bottom: 18px;
    }}
    h1, h2, h3 {{ margin: 0; }}
    h1 {{ font-size: 30px; }}
    h2 {{ font-size: 22px; margin-bottom: 4px; }}
    h3 {{ font-size: 15px; margin: 24px 0 12px; }}
    .meta, .path, .label, .microcopy, .notes {{ color: var(--muted); font-size: 12px; }}
    .mark-section {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 20px;
    }}
    .reduction-grid, .context-grid, .platform-grid, .layer-grid {{
      display: flex;
      flex-wrap: wrap;
      align-items: flex-end;
      gap: 14px;
    }}
    .sample, .context-card, .platform-card, .layer-card {{
      display: grid;
      justify-items: center;
      gap: 8px;
      max-width: 138px;
    }}
    .sample-stage, .context-stage, .platform-stage, .layer-stage {{
      position: relative;
      display: grid;
      place-items: center;
      border: 1px solid var(--line);
      overflow: hidden;
    }}
    .sample-stage {{ min-width: 29px; min-height: 29px; }}
    .context-stage {{ width: 96px; height: 96px; }}
    .platform-stage, .layer-stage {{ width: 108px; height: 108px; }}
    .checker {{
      background:
        linear-gradient(45deg, #ececf1 25%, transparent 25%),
        linear-gradient(-45deg, #ececf1 25%, transparent 25%),
        linear-gradient(45deg, transparent 75%, #ececf1 75%),
        linear-gradient(-45deg, transparent 75%, #ececf1 75%);
      background-color: #fff;
      background-position: 0 0, 0 8px, 8px -8px, -8px 0;
      background-size: 16px 16px;
    }}
    .tile-light {{ background: #ffffff; }}
    .tile-dark {{ background: #18181d; }}
    .tile-gray {{ background: #777981; }}
    .mask-squircle {{ border-radius: 22%; }}
    .mask-circle {{ border-radius: 50%; }}
    .mask-rounded {{ border-radius: 16px; }}
    .mask-teardrop {{ border-radius: 50% 50% 50% 12%; }}
    .ios-frame {{
      background:
        linear-gradient(145deg, #ffffff 0%, #f5f5f8 45%, #e3e5ec 100%);
      box-shadow: inset 0 0 0 1px rgba(0,0,0,0.06);
    }}
    .android-adaptive-frame {{
      background: #e9eef5;
      border-radius: 24px;
      box-shadow: inset 0 0 0 1px rgba(0,0,0,0.07);
    }}
    .adaptive-background-layer {{
      position: absolute;
      inset: 0;
      background:
        radial-gradient(circle at 36% 28%, #ffffff 0 10%, transparent 11%),
        linear-gradient(145deg, #f4dfd2 0%, #c67a52 100%);
    }}
    .adaptive-foreground-layer {{
      position: relative;
      z-index: 2;
      width: 72px;
      height: 72px;
    }}
    .adaptive-foreground-only {{
      width: 80px;
      height: 80px;
    }}
    .safe-zone-overlay {{
      position: absolute;
      z-index: 3;
      pointer-events: none;
      border: 1.5px dashed rgba(36, 36, 42, 0.64);
      background: rgba(255, 255, 255, 0.08);
    }}
    .ios-safe-zone {{
      width: 90%;
      height: 90%;
      border-radius: 50%;
    }}
    .android-safe-zone {{
      width: 72px;
      height: 72px;
      border-radius: 14px;
    }}
    .android-critical-zone {{
      width: 64px;
      height: 64px;
      border-radius: 12px;
      border-style: solid;
      border-color: rgba(44, 44, 52, 0.34);
    }}
    .adaptive-background-only {{
      background:
        radial-gradient(circle at 36% 28%, #ffffff 0 10%, transparent 11%),
        linear-gradient(145deg, #f4dfd2 0%, #c67a52 100%);
    }}
    .platform-stage.mask-circle, .layer-stage.mask-circle {{ border-radius: 50%; }}
    .platform-stage.mask-squircle, .layer-stage.mask-squircle {{ border-radius: 22%; }}
    .platform-stage.mask-rounded, .layer-stage.mask-rounded {{ border-radius: 16px; }}
    .platform-stage.mask-teardrop, .layer-stage.mask-teardrop {{ border-radius: 50% 50% 50% 12%; }}
    .mono-black {{ filter: grayscale(1) brightness(0); }}
    .mono-white {{ filter: grayscale(1) brightness(0) invert(1); }}
    .notes {{
      max-width: 760px;
      margin-top: 24px;
      padding-top: 14px;
      border-top: 1px solid var(--line);
    }}
  </style>
</head>
<body>
  <header>
    <h1>{escape(title)}</h1>
    <p class="meta">Generated {date.today().isoformat()} by render_svg_contact_sheet.py</p>
    <p class="notes">Use this sheet to inspect silhouette memory, detail collapse,
    monochrome behavior, safe-zone discipline, adaptive icon framing, and basic
    mask fit. It is review evidence, not an automatic shipping verdict.</p>
  </header>
  {''.join(sections)}
</body>
</html>
"""


def main() -> int:
    args = parse_args()
    svg_paths = [Path(path).expanduser().resolve() for path in args.svg_files]
    output = Path(args.output).expanduser().resolve()

    html = render_document(args.title, svg_paths, args.sizes)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(html, encoding="utf-8")
    print(f"[OK] Wrote SVG contact sheet to {output}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BrokenPipeError:
        sys.exit(1)
