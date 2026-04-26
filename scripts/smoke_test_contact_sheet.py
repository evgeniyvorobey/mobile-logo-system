#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "render_svg_contact_sheet.py"


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="mobile-logo-system-contact-") as temp:
        output = Path(temp) / "contact-sheet.html"
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                str(ROOT / "brand" / "primary-symbol.svg"),
                str(ROOT / "brand" / "small-icon.svg"),
                "--output",
                str(output),
                "--title",
                "Smoke Contact Sheet",
                "--sizes",
                "60,48,29",
            ],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        if result.returncode != 0:
            raise SystemExit(
                "[FAIL] contact sheet command failed\n"
                f"stdout:\n{result.stdout}\n"
                f"stderr:\n{result.stderr}"
            )
        if not output.exists():
            raise SystemExit(f"[FAIL] Expected contact sheet to exist: {output}")

        html = output.read_text(encoding="utf-8")
        required = [
            "Smoke Contact Sheet",
            "primary-symbol.svg",
            "small-icon.svg",
            "Reduction Review",
            "Surface And Mask Review",
            "Platform Safe Zone Review",
            "Foreground / Background Preview",
            "data:image/svg+xml;base64,",
            "data-section=\"safe-zone-review\"",
            "data-section=\"foreground-background-preview\"",
            "safe-zone-overlay",
            "android-adaptive-frame",
            "29px",
            "iOS squircle",
            "Android circle",
            "iOS safe zone",
            "Android 108dp canvas",
            "Combined adaptive proxy",
            "Monochrome black",
        ]
        missing = [marker for marker in required if marker not in html]
        if missing:
            raise SystemExit(
                "[FAIL] Contact sheet missing expected markers:\n"
                + "\n".join(missing)
            )

    print("[OK] SVG contact sheet smoke test passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
