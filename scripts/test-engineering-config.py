"""Negative regression checks for engineering configuration, not application tests."""
from pathlib import Path
import runpy
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
CHECK = runpy.run_path(str(ROOT / "scripts/validate-agent-config.py"))["check"]


class EngineeringConfigTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="raptora-config-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for folder in (".codex", ".agents", "docs"):
            shutil.copytree(ROOT / folder, self.root / folder)
        shutil.copy(ROOT / "AGENTS.md", self.root / "AGENTS.md")

    def test_current_configuration(self):
        CHECK(self.root)

    def test_missing_skill(self):
        (self.root / ".agents/skills/raptora-verify-code/SKILL.md").unlink()
        with self.assertRaises(ValueError):
            CHECK(self.root)

    def test_empty_skill_body(self):
        path = self.root / ".agents/skills/raptora-verify-code/SKILL.md"
        path.write_text("---\nname: raptora-verify-code\ndescription: Use when verifying code.\n---\n", encoding="utf-8")
        with self.assertRaises(ValueError):
            CHECK(self.root)

    def test_mismatched_skill_name(self):
        path = self.root / ".agents/skills/raptora-verify-code/SKILL.md"
        path.write_text(path.read_text(encoding="utf-8").replace("name: raptora-verify-code", "name: other"), encoding="utf-8")
        with self.assertRaises(ValueError):
            CHECK(self.root)

    def test_unknown_skill_metadata(self):
        path = self.root / ".agents/skills/raptora-verify-code/SKILL.md"
        path.write_text(path.read_text(encoding="utf-8").replace("---\nname:", "---\npermissions: unrestricted\nname:", 1), encoding="utf-8")
        with self.assertRaises(ValueError):
            CHECK(self.root)

    def test_invalid_plain_yaml_description(self):
        path = self.root / ".agents/skills/raptora-verify-code/SKILL.md"
        path.write_text(path.read_text(encoding="utf-8").replace(
            "description: Use when ", "description: Use when invalid: ", 1), encoding="utf-8")
        with self.assertRaises(ValueError):
            CHECK(self.root)

    def test_invalid_project_setting_types(self):
        path = self.root / ".codex/config.toml"
        original = path.read_text(encoding="utf-8")
        for before, after in (("enabled = true", "enabled = 1"),
                              ("session = 2", "session = 2.0"),
                              ("max_depth = 1", "max_depth = true")):
            with self.subTest(setting=after):
                path.write_text(original.replace(before, after), encoding="utf-8")
                with self.assertRaises(ValueError):
                    CHECK(self.root)

    def test_role_permission_override(self):
        path = self.root / ".codex/agents/architect.toml"
        path.write_text(path.read_text(encoding="utf-8") + 'sandbox_mode = "danger-full-access"\n', encoding="utf-8")
        with self.assertRaises(ValueError):
            CHECK(self.root)


if __name__ == "__main__":
    unittest.main(verbosity=2)
