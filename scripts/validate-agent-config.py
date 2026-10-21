"""Validate Raptora's deliberately small Codex 0.163.0 configuration subset.

Python 3.11+, standard library only. This is a repository policy check, not
an upstream schema replacement or proof of runtime role loading.
"""
from pathlib import Path
import sys
import tomllib

ROLES = {"architect", "developer", "security-reviewer", "qa-engineer", "windows-deployment"}
DOCS = ("AGENTS.md", "docs/AGENT_ARCHITECTURE.md", "docs/AGENT_WORKFLOW.md",
        "docs/AGENT_USAGE.md", "docs/AGENT_VALIDATION.md")


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
    for doc in DOCS:
        if not (root / doc).is_file() or not (root / doc).read_text(encoding="utf-8").strip():
            raise ValueError(f"Missing or empty documentation: {doc}")


if __name__ == "__main__":
    try:
        check(Path(__file__).resolve().parents[1])
    except (OSError, ValueError, tomllib.TOMLDecodeError) as error:
        print(f"Agent configuration validation failed: {error}", file=sys.stderr)
        sys.exit(1)
    print("PASS: project configuration, five role definitions and required guidance")
    print("Policy/TOML validation only; no Cloud custom-role or application acceptance claimed.")
