"""Read-only governance environment check; no application/dependency acceptance."""
from pathlib import Path
import shutil
import subprocess
import sys


def main() -> int:
    if sys.version_info < (3, 11):
        print("FAIL: Python 3.11+ is required", file=sys.stderr)
        return 1
    root = Path(__file__).resolve().parents[1]
    if not shutil.which("git"):
        print("FAIL: Git is required", file=sys.stderr)
        return 1
    commands = (["git", "rev-parse", "--show-toplevel"],
                ["git", "diff", "--check"],
                [sys.executable, "scripts/validate-agent-config.py"],
                [sys.executable, "scripts/test-engineering-config.py"])
    for command in commands:
        result = subprocess.run(command, cwd=root, check=False)
        if result.returncode:
            return result.returncode
    print(f"PASS: governance environment; Python {sys.version.split()[0]}")
    codex = shutil.which("codex")
    if codex:
        result = subprocess.run([codex, "--version"], cwd=root, check=False)
        if result.returncode:
            print("BLOCKED: installed Codex did not report its version", file=sys.stderr)
            return result.returncode
    else:
        print("NOT RUN: Codex runtime checks; CLI absent (normal for unprivileged governance CI)")
    print("NOT RUN: dependency install, application build/tests, Windows/connected/release acceptance")
    print("Role/skill syntax and CLI version do not establish automatic Cloud loading or execution.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
