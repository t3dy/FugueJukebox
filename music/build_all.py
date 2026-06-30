#!/usr/bin/env python3
"""
FUGUEJUKEBOX Build Pipeline — Orchestrate full generation and rendering.

Run this to generate all 500 variations (50 emblems × 10 variations)
and render them to MP3 with NES chiptune effects.
"""

import subprocess
import sys
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent


def run_stage(name: str, script: Path) -> bool:
    """Run a Python stage and return success status."""
    print(f"\n{'='*60}")
    print(f"STAGE: {name}")
    print(f"{'='*60}")

    if not script.exists():
        print(f"✗ Script not found: {script}")
        return False

    try:
        result = subprocess.run(
            [sys.executable, str(script)],
            cwd=PROJECT_ROOT,
            check=True
        )
        print(f"✓ {name} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {name} failed with exit code {e.returncode}")
        return False
    except Exception as e:
        print(f"✗ {name} error: {e}")
        return False


def main():
    print("╔═══════════════════════════════════════════════════╗")
    print("║  FUGUEJUKEBOX: Atalanta Fugiens Chiptune Remix   ║")
    print("║  50 Emblems × 10 Variations = 500 MP3s            ║")
    print("╚═══════════════════════════════════════════════════╝")

    stages = [
        ("Generate Variations (50 emblems → 500 variations)", PROJECT_ROOT / "generate_variations.py"),
        ("Render to Audio (500 variations → 500 MP3s)", PROJECT_ROOT / "render_to_audio.py"),
    ]

    results = []
    for name, script in stages:
        success = run_stage(name, script)
        results.append((name, success))
        if not success:
            print(f"\n✗ Build stopped at: {name}")
            print("\nTo resume, fix the error and run:")
            print(f"  python {script.name}")
            return 1

    # Summary
    print(f"\n{'='*60}")
    print("BUILD SUMMARY")
    print(f"{'='*60}")
    for name, success in results:
        status = "✓" if success else "✗"
        print(f"{status} {name}")

    if all(success for _, success in results):
        print(f"\n✓ All stages completed!")
        print(f"✓ Output: {PROJECT_ROOT / 'emblems'}")
        print("\nTo sample the music:")
        print("  • Open FUGUEJUKEBOX/emblems/emblem_XX/ folder")
        print("  • Play emblem_XX_variation_*.mp3 files")
        return 0
    else:
        print(f"\n✗ Build failed")
        return 1


if __name__ == '__main__':
    sys.exit(main())
