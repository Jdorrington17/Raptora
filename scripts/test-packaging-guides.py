"""Negative regression tests for public packaging-doc structural preflight.

These tests do NOT run the private package assembler or Windows acceptance.
"""
from pathlib import Path
import json
import runpy
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
MODULE = runpy.run_path(str(ROOT / "scripts/validate-packaging-guides.py"))
VALIDATE = MODULE["validate"]
ValidationError = MODULE["ValidationError"]
REL = Path("docs/packaging")
DOC1 = REL / "WINDOWS_ACCEPTANCE_AND_LIMITATIONS.md"
DOC2 = REL / "PACKAGE_USE_BUILD_AND_RECOVERY.md"
CONTRACT = REL / "required-sections.json"
WA01 = "## WA-01: Authorisation and isolation"
WA02 = "## WA-02: Recoverable baseline and backups"


class PackagingGuideTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="raptora-packaging-docs-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copytree(ROOT / REL, self.root / REL)

    def path(self, name):
        return self.root / name

    def replace(self, file, old, new):
        path = self.path(file)
        s = path.read_text(encoding="utf-8")
        self.assertEqual(s.count(old), 1, f"expected one fixture target: {old}")
        path.write_text(s.replace(old, new), encoding="utf-8")

    def fail_validation(self):
        with self.assertRaises(ValidationError):
            VALIDATE(self.root)

    def test_draft_docs_validate(self):
        self.assertEqual(VALIDATE(self.root), 19)

    def test_missing_first_document(self):
        self.path(DOC1).unlink()
        self.fail_validation()

    def test_missing_second_document(self):
        self.path(DOC2).unlink()
        self.fail_validation()

    def test_unreadable_document_path(self):
        self.path(DOC1).unlink()
        self.path(DOC1).mkdir()
        self.fail_validation()

    def test_empty_document(self):
        self.path(DOC2).write_bytes(b"")
        self.fail_validation()

    def test_whitespace_only_document(self):
        self.path(DOC1).write_text(" \n\t\n", encoding="utf-8")
        self.fail_validation()

    def test_invalid_utf8(self):
        self.path(DOC2).write_bytes(b"\xff\xfe\xfd")
        self.fail_validation()

    def test_missing_mandatory_heading(self):
        self.replace(DOC1, WA01, "")
        self.fail_validation()

    def test_renamed_mandatory_heading(self):
        self.replace(DOC1, WA01, "## WA-01: Different content")
        self.fail_validation()

    def test_duplicate_required_heading(self):
        self.replace(DOC1, WA01, WA01 + "\nUseful text.\n" + WA01)
        self.fail_validation()

    def test_out_of_order_sections(self):
        self.replace(DOC1, WA01, "## WA-XX: Authorisation and isolation")
        self.fail_validation()

    def test_empty_section_body(self):
        path = self.path(DOC1)
        text = path.read_text(encoding="utf-8")
        start, end = text.index(WA01), text.index(WA02)
        path.write_text(text[:start] + WA01 + "\n\n" + text[end:], encoding="utf-8")
        self.fail_validation()

    def test_placeholder_only_section_body(self):
        path = self.path(DOC1)
        text = path.read_text(encoding="utf-8")
        start, end = text.index(WA01), text.index(WA02)
        path.write_text(text[:start] + WA01 + "\nTODO\n\n" + text[end:], encoding="utf-8")
        self.fail_validation()

    def test_fenced_only_heading(self):
        self.replace(DOC1, WA01, "~~~markdown\n" + WA01 + "\n~~~")
        self.fail_validation()

    def test_commented_only_heading(self):
        self.replace(DOC1, WA01, "<!--\n" + WA01 + "\n-->")
        self.fail_validation()

    def test_invalid_relative_link(self):
        path = self.path(DOC1)
        with path.open("a", encoding="utf-8") as f:
            f.write("\n[Invalid companion](MISSING_COMPANION.md)\n")
        self.fail_validation()

    def test_missing_contract(self):
        self.path(CONTRACT).unlink()
        self.fail_validation()

    def test_malformed_contract(self):
        self.path(CONTRACT).write_text("{not-json", encoding="utf-8")
        self.fail_validation()

    def test_unsupported_contract_version(self):
        path = self.path(CONTRACT)
        data = json.loads(path.read_text(encoding="utf-8"))
        data["formatVersion"] = 999
        path.write_text(json.dumps(data), encoding="utf-8")
        self.fail_validation()

    def test_duplicate_contract_section_ids(self):
        path = self.path(CONTRACT)
        data = json.loads(path.read_text(encoding="utf-8"))
        data["documents"][0]["requiredSections"][1]["id"] = "WA-01"
        path.write_text(json.dumps(data), encoding="utf-8")
        self.fail_validation()

    def test_package_mode_rejects_unapproved_draft(self):
        with self.assertRaises(ValidationError):
            VALIDATE(self.root, package=True)

    def test_broken_title(self):
        self.replace(DOC2, "# Raptora package use, build, maintenance and recovery",
                     "# Missing the correct title")
        self.fail_validation()


if __name__ == "__main__":
    unittest.main(verbosity=2)
