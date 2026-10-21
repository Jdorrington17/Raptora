"""Validate Raptora's deliberately small Codex 0.163.0 configuration subset.

Python 3.11+, standard library only. This is a repository policy check, not
an upstream schema replacement or proof of runtime role loading.
"""
from pathlib import Path
import re
import sys
import tomllib

ROLES = {"architect", "developer", "security-reviewer", "qa-engineer", "windows-deployment"}
SKILLS = {"raptora-verify-code", "raptora-diagnostic-development",
          "raptora-windows-release-review", "raptora-pr-handover"}
DOCS = ("AGENTS.md", "docs/AGENT_ARCHITECTURE.md", "docs/AGENT_WORKFLOW.md",
        "docs/AGENT_USAGE.md", "docs/AGENT_VALIDATION.md", "docs/AGENT_SKILLS.md",
        "docs/CODEX_ENVIRONMENT.md", "docs/CODEX_CONFIGURATION_REGISTER.md",
        "docs/AGENT_RECOVERY.md", "docs/SOURCE_ACTIVATION_PLAN.md",
        "docs/PRIVATE_MIGRATION_AUDIT.md")


def check(root: Path) -> None:
    config_dir = root / ".codex"
    project = tomllib.loads((config_dir / "config.toml").read_text(encoding="utf-8"))
    agents = project.get("agents", {})
    if not isinstance(agents, dict) or any(
        type(agents.get(key)) is not expected_type
        for key, expected_type in (("enabled", bool),
                                   ("max_concurrent_threads_per_session", int),
                                   ("max_depth", int))
    ):
        raise ValueError("Agent settings require a boolean enabled flag and integer concurrency/depth")
    if project != {"agents": {"enabled": True, "max_concurrent_threads_per_session": 2, "max_depth": 1}}:
        raise ValueError("Project settings must preserve the reviewed agent-only configuration and concurrency budget")
    # Recursive scan also catches accidental nested roles that Codex would discover.
    paths = sorted((config_dir / "agents").rglob("*.toml"))
    if {p.relative_to(config_dir / "agents").as_posix() for p in paths} != {f"{name}.toml" for name in ROLES}:
        raise ValueError("Expected exactly the five reviewed role files, with no nested or duplicate definitions")
    for path in paths:
        if path.is_symlink():
            raise ValueError(f"Role file must not be a symlink: {path.name}")
        role = tomllib.loads(path.read_text(encoding="utf-8"))
        if set(role) != {"name", "description", "developer_instructions"}:
            raise ValueError(f"Unexpected role fields or missing metadata: {path.name}")
        if role["name"] != path.stem:
            raise ValueError(f"Role name must match file: {path.name}")
        for key in ("description", "developer_instructions"):
            if not isinstance(role[key], str) or not role[key].strip():
                raise ValueError(f"Missing nonempty {key}: {path.name}")
    skills_dir = root / ".agents/skills"
    skill_paths = sorted(skills_dir.rglob("SKILL.md"))
    if {p.relative_to(skills_dir).as_posix() for p in skill_paths} != {
        f"{name}/SKILL.md" for name in SKILLS
    }:
        raise ValueError("Expected exactly four reviewed project skill files")
    for path in skill_paths:
        if path.is_symlink():
            raise ValueError("Skill files must not be symlinks")
        content = path.read_text(encoding="utf-8")
        sections = content.split("---\n", 2)
        if len(sections) != 3 or sections[0] or not sections[2].strip():
            raise ValueError(f"Skill needs frontmatter and a nonempty body: {path.parent.name}")
        # Intentional plain-scalar subset; upstream discovery validates actual YAML.
        fields = {}
        for line in sections[1].splitlines():
            match = re.fullmatch(r"(name|description): ([^\r\n]+)", line)
            if not match or match[1] in fields:
                raise ValueError(f"Unexpected/duplicate skill metadata: {path.parent.name}")
            if ": " in match[2] or " #" in match[2] or "\t" in match[2]:
                raise ValueError(f"Skill metadata must use an unambiguous plain YAML scalar: {path.parent.name}")
            fields[match[1]] = match[2]
        if set(fields) != {"name", "description"} or fields["name"] != path.parent.name:
            raise ValueError(f"Missing or mismatched skill metadata: {path.parent.name}")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", fields["name"]) or len(fields["name"]) > 64:
            raise ValueError("Invalid skill name")
        if not fields["description"].startswith("Use when ") or len(fields["description"]) > 1024:
            raise ValueError("Invalid skill description")
    for doc in DOCS:
        if not (root / doc).is_file() or not (root / doc).read_text(encoding="utf-8").strip():
            raise ValueError(f"Missing or empty documentation: {doc}")


if __name__ == "__main__":
    try:
        check(Path(__file__).resolve().parents[1])
    except (OSError, ValueError, tomllib.TOMLDecodeError) as error:
        print(f"Agent configuration validation failed: {error}", file=sys.stderr)
        sys.exit(1)
    print("PASS: project configuration, five roles, four skills and required guidance")
    print("Policy/TOML validation only; no Cloud custom-role or application acceptance claimed.")
