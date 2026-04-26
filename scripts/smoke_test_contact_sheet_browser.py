#!/usr/bin/env python3
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RENDER_SCRIPT = ROOT / "scripts" / "render_svg_contact_sheet.py"


BROWSER_CHECK_JS = r"""
const { chromium } = require("playwright");

const pageUrl = process.argv[2];
const screenshotPath = process.argv[3];

(async () => {
  const browser = await chromium.launch({ headless: true });
  let ok = false;
  try {
    const page = await browser.newPage({
      viewport: { width: 1280, height: 1400 },
      deviceScaleFactor: 1
    });
    await page.goto(pageUrl, { waitUntil: "load" });
    await page.waitForSelector('[data-section="reduction-review"]', { timeout: 10000 });
    await page.waitForFunction(() => {
      const images = Array.from(document.querySelectorAll('img[data-review-img="true"]'));
      return images.length > 0 && images.every((img) => img.complete && img.naturalWidth > 0 && img.naturalHeight > 0);
    }, null, { timeout: 10000 });

    const report = await page.evaluate(() => {
      const requiredSections = [
        "reduction-review",
        "surface-mask-review",
        "safe-zone-review",
        "foreground-background-preview"
      ];
      const sectionStatus = Object.fromEntries(
        requiredSections.map((section) => [
          section,
          Boolean(document.querySelector(`[data-section="${section}"]`))
        ])
      );
      const images = Array.from(document.querySelectorAll('img[data-review-img="true"]'));
      const visibleImages = images.filter((img) => {
        const rect = img.getBoundingClientRect();
        const style = window.getComputedStyle(img);
        return (
          img.complete &&
          img.naturalWidth > 0 &&
          img.naturalHeight > 0 &&
          rect.width > 0 &&
          rect.height > 0 &&
          style.display !== "none" &&
          style.visibility !== "hidden"
        );
      });
      const text = document.body.innerText;
      return {
        title: document.title,
        sectionStatus,
        imageCount: images.length,
        visibleImageCount: visibleImages.length,
        safeZoneOverlays: document.querySelectorAll(".safe-zone-overlay").length,
        adaptiveFrames: document.querySelectorAll(".android-adaptive-frame").length,
        layerPreviewCards: document.querySelectorAll(
          '[data-preview="background-layer"], [data-preview="foreground-layer"], [data-preview="combined-adaptive"]'
        ).length,
        hasIosSafeZoneText: text.includes("iOS safe zone"),
        hasAndroidFrameText: text.includes("Android 108dp canvas"),
        hasCombinedPreviewText: text.includes("Combined adaptive proxy")
      };
    });

    await page.screenshot({ path: screenshotPath, fullPage: true });

    const allSectionsPresent = Object.values(report.sectionStatus).every(Boolean);
    ok =
      report.title === "Browser Smoke Contact Sheet" &&
      allSectionsPresent &&
      report.imageCount >= 20 &&
      report.visibleImageCount === report.imageCount &&
      report.safeZoneOverlays >= 6 &&
      report.adaptiveFrames >= 6 &&
      report.layerPreviewCards >= 3 &&
      report.hasIosSafeZoneText &&
      report.hasAndroidFrameText &&
      report.hasCombinedPreviewText;

    console.log(JSON.stringify(report, null, 2));
    if (!ok) {
      console.error("[FAIL] Browser contact sheet checks did not pass.");
      process.exitCode = 1;
    }
  } finally {
    await browser.close();
  }
})();
"""


def run_contact_sheet(output: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(RENDER_SCRIPT),
            str(ROOT / "brand" / "primary-symbol.svg"),
            str(ROOT / "brand" / "small-icon.svg"),
            "--output",
            str(output),
            "--title",
            "Browser Smoke Contact Sheet",
            "--sizes",
            "60,48,29",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )


def main() -> int:
    if shutil.which("npx") is None:
        raise SystemExit(
            "[FAIL] npx is required for the browser smoke test. "
            "Install Node.js/npm, then retry."
        )
    if shutil.which("npm") is None:
        raise SystemExit(
            "[FAIL] npm is required for the browser smoke test. "
            "Install Node.js/npm, then retry."
        )

    with tempfile.TemporaryDirectory(prefix="mobile-logo-system-browser-") as temp:
        temp_dir = Path(temp)
        html_path = temp_dir / "contact-sheet.html"
        js_path = temp_dir / "browser_check.js"
        screenshot_path = temp_dir / "contact-sheet.png"

        result = run_contact_sheet(html_path)
        if result.returncode != 0:
            raise SystemExit(
                "[FAIL] contact sheet command failed\n"
                f"stdout:\n{result.stdout}\n"
                f"stderr:\n{result.stderr}"
            )
        js_path.write_text(BROWSER_CHECK_JS, encoding="utf-8")

        (temp_dir / "package.json").write_text(
            '{"private":true,"type":"commonjs"}\n',
            encoding="utf-8",
        )
        install_result = subprocess.run(
            [
                "npm",
                "install",
                "--silent",
                "--no-audit",
                "--no-fund",
                "playwright",
            ],
            cwd=temp_dir,
            text=True,
            capture_output=True,
        )
        if install_result.returncode != 0:
            raise SystemExit(
                "[FAIL] failed to install temporary Playwright package\n"
                f"stdout:\n{install_result.stdout}\n"
                f"stderr:\n{install_result.stderr}"
            )

        browser_result = subprocess.run(
            [
                "node",
                str(js_path),
                html_path.as_uri(),
                str(screenshot_path),
            ],
            cwd=temp_dir,
            text=True,
            capture_output=True,
        )
        combined_output = browser_result.stdout + browser_result.stderr
        if browser_result.returncode != 0 and (
            "Executable doesn't exist" in combined_output or "Please run" in combined_output
        ):
            browser_install_result = subprocess.run(
                ["npx", "playwright", "install", "chromium"],
                cwd=temp_dir,
                text=True,
                capture_output=True,
            )
            if browser_install_result.returncode == 0:
                browser_result = subprocess.run(
                    [
                        "node",
                        str(js_path),
                        html_path.as_uri(),
                        str(screenshot_path),
                    ],
                    cwd=temp_dir,
                    text=True,
                    capture_output=True,
                )
                combined_output = browser_result.stdout + browser_result.stderr

        if browser_result.returncode != 0:
            hint = ""
            if "Executable doesn't exist" in combined_output or "Please run" in combined_output:
                hint = (
                    "\nHint: install the Chromium browser for Playwright with "
                    "`npx playwright install chromium`."
                )
            raise SystemExit(
                "[FAIL] browser contact sheet smoke test failed\n"
                f"stdout:\n{browser_result.stdout}\n"
                f"stderr:\n{browser_result.stderr}"
                f"{hint}"
            )
        if not screenshot_path.exists():
            raise SystemExit("[FAIL] Browser smoke test did not create a screenshot")

    print("[OK] Browser contact sheet smoke test passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
