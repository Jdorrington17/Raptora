"""Negative regression tests for public packaging-doc structural preflight.

These tests do NOT run the private package assembler or Windows acceptance.
"""
from pathlib import Path
import hashlib
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

    def approve_synthetic_fixture(self):
        """Pure test fixture, not real maintainer or rights-holder approval."""
        contract_path = self.path(CONTRACT)
        contract = json.loads(contract_path.read_text(encoding="utf-8"))
        contract["packagingAdoptionApproved"] = True
        contract["status"] = "approved-for-packaging"
        contract_path.write_text(json.dumps(contract), encoding="utf-8")
        manifest = {
            "contractSha256": hashlib.sha256(contract_path.read_bytes()).hexdigest(),
            "documents": {
                "PKG-DOC-01": hashlib.sha256(self.path(DOC1).read_bytes()).hexdigest(),
                "PKG-DOC-02": hashlib.sha256(self.path(DOC2).read_bytes()).hexdigest()
            },
            "reviewers": {
                "maintainer": "approved",
                "build-engineering": "approved",
                "Windows/QA": "approved",
                "security/IP": "approved"
            }
        }
        approved = REL / "synthetic-adoption.json"
        self.path(approved).write_text(json.dumps(manifest), encoding="utf-8")
        return approved, manifest

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


    def test_coming_soon_placeholder_section(self):
        path = self.path(DOC1)
        source = path.read_text(encoding="utf-8")
        start, end = source.index(WA01), source.index(WA02)
        path.write_text(source[:start] + WA01 + "\nComing soon\n\n" +
                        source[end:], encoding="utf-8")
        self.fail_validation()

    def test_synthetic_hash_bound_package_preflight(self):
        approved, _ = self.approve_synthetic_fixture()
        self.assertEqual(VALIDATE(self.root, package=True, adoption_rel=str(approved)), 19)

    def test_modified_document_refuses_package_preflight(self):
        approved, _ = self.approve_synthetic_fixture()
        self.replace(DOC1, "Obtain an approved test plan", "Obtain a reviewed test plan")
        with self.assertRaises(ValidationError):
            VALIDATE(self.root, package=True, adoption_rel=str(approved))

    def test_modified_contract_refuses_package_preflight(self):
        approved, _ = self.approve_synthetic_fixture()
        path = self.path(CONTRACT)
        contract = json.loads(path.read_text(encoding="utf-8"))
        contract["status"] = "altered-after-review"
        path.write_text(json.dumps(contract), encoding="utf-8")
        with self.assertRaises(ValidationError):
            VALIDATE(self.root, package=True, adoption_rel=str(approved))

    def test_incomplete_reviewers_refuses_package_preflight(self):
        approved, manifest = self.approve_synthetic_fixture()
        manifest["reviewers"]["security/IP"] = "pending"
        self.path(approved).write_text(json.dumps(manifest), encoding="utf-8")
        with self.assertRaises(ValidationError):
            VALIDATE(self.root, package=True, adoption_rel=str(approved))

    def set_first_body(self, body):
        path = self.path(DOC1)
        text = path.read_text(encoding="utf-8")
        start, end = text.index(WA01), text.index(WA02)
        path.write_text(text[:start] + WA01 + "\n" + body + "\n\n" + text[end:], encoding="utf-8")

    def test_formatting_only_bodies_refuse(self):
        for body in ("` `", "===", "~~TODO~~", "1. TBD", "&nbsp;\u200b", "<span></span>"):
            with self.subTest(body=body):
                self.set_first_body(body)
                self.fail_validation()

    def test_nested_heading_only_body_refuses(self):
        self.set_first_body("### Future procedure")
        self.fail_validation()

    def test_second_document_nested_heading_only_body_refuses(self):
        path = self.path(DOC2)
        text = path.read_text(encoding="utf-8")
        first = "## PU-01: Reviewed prerequisites and build identity"
        second = "## PU-02: Complete-package verification and launch"
        self.assertEqual(text.count(first), 1)
        self.assertEqual(text.count(second), 1)
        start, end = text.index(first), text.index(second)
        path.write_text(text[:start] + first + "\n### Future procedure\n\n" +
                        text[end:], encoding="utf-8")
        self.fail_validation()

    def test_reference_link_only_body_refuses(self):
        self.set_first_body("[Support][help]\n\n[help]: https://example.invalid")
        self.fail_validation()

    def test_autolink_only_body_refuses(self):
        self.set_first_body("<https://example.invalid>")
        self.fail_validation()

    def test_invalid_fence_closer_does_not_expose_headings(self):
        self.replace(DOC1, WA01, "~~~\n~~~not-a-closing-fence\n" + WA01)
        self.fail_validation()

    def test_symlink_document_inside_root_refuses(self):
        original = self.path(DOC1)
        target = self.root / "other-guide.md"
        original.rename(target)
        original.symlink_to(target)
        self.fail_validation()

    def test_absolute_document_path_inside_root_refuses(self):
        path = self.path(CONTRACT)
        contract = json.loads(path.read_text(encoding="utf-8"))
        contract["documents"][0]["path"] = str(self.path(DOC1))
        path.write_text(json.dumps(contract), encoding="utf-8")
        self.fail_validation()

    def test_missing_adoption_contract_metadata_refuses_structure(self):
        path = self.path(CONTRACT)
        original = json.loads(path.read_text(encoding="utf-8"))
        for key in ("status", "scope", "applicationValidation", "packagingAdoptionApproved", "requiredContentReviewRoles"):
            with self.subTest(key=key):
                changed = dict(original)
                del changed[key]
                path.write_text(json.dumps(changed), encoding="utf-8")
                self.fail_validation()

    def test_boolean_contract_version_refuses(self):
        path = self.path(CONTRACT)
        contract = json.loads(path.read_text(encoding="utf-8"))
        contract["formatVersion"] = True
        path.write_text(json.dumps(contract), encoding="utf-8")
        self.fail_validation()

    def test_non_object_adoption_record_has_controlled_error(self):
        approved, _ = self.approve_synthetic_fixture()
        self.path(approved).write_text("[]", encoding="utf-8")
        with self.assertRaises(ValidationError):
            VALIDATE(self.root, package=True, adoption_rel=str(approved))

    def test_multiple_placeholders_or_bare_url_body_refuses(self):
        for body in ("TODO TBD", "https://example.invalid"):
            with self.subTest(body=body):
                self.set_first_body(body)
                self.fail_validation()

    def test_out_of_root_and_traversal_document_paths_refuse(self):
        path = self.path(CONTRACT)
        contract = json.loads(path.read_text(encoding="utf-8"))
        for name in ("../outside.md", "docs/packaging/../packaging/" + DOC1.name):
            with self.subTest(name=name):
                contract["documents"][0]["path"] = name
                path.write_text(json.dumps(contract), encoding="utf-8")
                self.fail_validation()

    def test_symlink_contract_refuses(self):
        path = self.path(CONTRACT)
        target = self.root / "other-contract.json"
        path.rename(target)
        path.symlink_to(target)
        self.fail_validation()

    def test_symlink_adoption_record_refuses(self):
        approved, _ = self.approve_synthetic_fixture()
        path = self.path(approved)
        target = self.root / "other-adoption.json"
        path.rename(target)
        path.symlink_to(target)
        with self.assertRaises(ValidationError):
            VALIDATE(self.root, package=True, adoption_rel=str(approved))

    def test_missing_adoption_fields_refuse(self):
        approved, manifest = self.approve_synthetic_fixture()
        for key in ("contractSha256", "documents", "reviewers"):
            with self.subTest(key=key):
                changed = dict(manifest)
                del changed[key]
                self.path(approved).write_text(json.dumps(changed), encoding="utf-8")
                with self.assertRaises(ValidationError):
                    VALIDATE(self.root, package=True, adoption_rel=str(approved))

    def test_missing_adoption_record_refuses(self):
        self.approve_synthetic_fixture()
        with self.assertRaises(ValidationError):
            VALIDATE(self.root, package=True)

    def test_symlink_relative_link_refuses(self):
        target = self.root / "link-target.md"
        target.write_text("Public synthetic fixture.", encoding="utf-8")
        self.path(REL / "linked.md").symlink_to(target)
        with self.path(DOC1).open("a", encoding="utf-8") as stream:
            stream.write("\n[Companion](linked.md)\n")
        self.fail_validation()

    def test_malformed_required_topics_refuse(self):
        path = self.path(CONTRACT)
        contract = json.loads(path.read_text(encoding="utf-8"))
        contract["documents"][0]["requiredSections"][0]["requiredTopics"] = [None]
        path.write_text(json.dumps(contract), encoding="utf-8")
        self.fail_validation()

    def test_hidden_html_only_body_refuses(self):
        self.set_first_body('<span hidden>not visible guidance</span>')
        self.fail_validation()

    def test_indented_code_only_body_refuses(self):
        self.set_first_body('    example code, not explanatory guidance')
        self.fail_validation()

    def test_invisible_unicode_filler_only_body_refuses(self):
        for body in ('\u3164', '\uffa0', '\u115f', '\u1160'):
            with self.subTest(codepoint=ord(body)):
                self.set_first_body(body)
                self.fail_validation()

    def test_nested_hidden_html_only_body_refuses(self):
        self.set_first_body('<span hidden><span></span>hidden body</span>')
        self.fail_validation()


if __name__ == "__main__":
    unittest.main(verbosity=2)
