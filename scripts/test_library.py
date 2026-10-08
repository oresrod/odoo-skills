#!/usr/bin/env python3
"""Exercise generation, relocation and failure handling in temporary directories."""

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from validate_library import validate_skill


SOURCE = Path(__file__).resolve().parents[1]


class LibraryTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="odoo-skills-test-")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / "library"
        for directory in ("common", "profiles", "scripts"):
            shutil.copytree(SOURCE / directory, self.root / directory,
                            ignore=shutil.ignore_patterns("__pycache__"))

    def run_build(self, *args):
        return subprocess.run(
            [sys.executable, "-B", str(self.root / "scripts/build_library.py"), *args],
            capture_output=True, text=True, check=False,
        )

    def test_check_is_read_only_and_generation_is_idempotent(self):
        self.assertNotEqual(self.run_build("--check").returncode, 0)
        self.assertEqual(list(self.root.glob("v*")), [])
        self.assertEqual(self.run_build().returncode, 0)
        files = [p for p in self.root.glob("v*/**/*") if p.is_file()]
        snapshot = {p: (p.read_bytes(), p.stat().st_mtime_ns) for p in files}
        self.assertEqual(self.run_build("--check").returncode, 0)
        self.assertEqual(self.run_build().returncode, 0)
        self.assertEqual(snapshot, {p: (p.read_bytes(), p.stat().st_mtime_ns) for p in files})

    def test_every_skill_can_be_relocated_alone(self):
        self.assertEqual(self.run_build().returncode, 0)
        entries = list(self.root.glob("v*/odoo-*/SKILL.md"))
        self.assertEqual(len(entries), 20)
        for entry in entries:
            with self.subTest(skill=entry.parent.name):
                isolated = self.base / "isolated" / entry.parent.name
                shutil.copytree(entry.parent, isolated)
                self.assertEqual(validate_skill(isolated), [])
                shutil.rmtree(isolated)

    def test_missing_reference_is_detected(self):
        self.assertEqual(self.run_build().returncode, 0)
        folder = self.root / "v18/odoo-v18-review"
        (folder / "references/version.md").unlink()
        self.assertTrue(validate_skill(folder))
        self.assertNotEqual(self.run_build("--check").returncode, 0)

    def test_unknown_file_is_preserved_and_reported(self):
        self.assertEqual(self.run_build().returncode, 0)
        extra = self.root / "v18/local-notes.md"
        extra.write_text("Local customization\n", encoding="utf-8")
        result = self.run_build()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("local-notes.md", result.stderr)
        self.assertEqual(extra.read_text(encoding="utf-8"), "Local customization\n")

    def test_symlink_does_not_redirect_writes(self):
        outside = self.base / "outside"
        outside.mkdir()
        sentinel = outside / "README.md"
        sentinel.write_text("Keep me\n", encoding="utf-8")
        (self.root / "v14").symlink_to(outside, target_is_directory=True)
        result = self.run_build()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(list(outside.iterdir()), [sentinel])
        self.assertEqual(sentinel.read_text(encoding="utf-8"), "Keep me\n")


if __name__ == "__main__":
    unittest.main()
