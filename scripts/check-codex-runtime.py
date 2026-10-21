"""Optional no-model CLI parser/skill-discovery smoke check. Not Cloud acceptance."""
from pathlib import Path
import json
import os
import queue
import shutil
import subprocess
import sys
import tempfile
import threading

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {"raptora-verify-code", "raptora-diagnostic-development",
            "raptora-windows-release-review", "raptora-pr-handover"}


def check() -> None:
    codex = shutil.which("codex")
    if not codex:
        raise RuntimeError("Codex CLI missing; use the approved client or document runtime checks as Not run")
    with tempfile.TemporaryDirectory(prefix="raptora-codex-smoke-") as tmp:
        home = Path(tmp)
        shutil.copy(ROOT / ".codex/config.toml", home / "config.toml")
        shutil.copytree(ROOT / ".codex/agents", home / "agents")
        env = {key: value for key, value in os.environ.items()
               if not any(part in key.upper() for part in ("TOKEN", "API_KEY", "AUTH", "SECRET"))}
        env["CODEX_HOME"] = tmp
        process = subprocess.Popen(
            [codex, "app-server", "--strict-config", "--listen", "stdio://"],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
            text=True, env=env, cwd=tmp)
        messages = queue.Queue()

        def read_lines():
            for line in process.stdout:
                messages.put(line)
            messages.put(None)

        reader = threading.Thread(target=read_lines, daemon=True)
        reader.start()

        def send(message):
            process.stdin.write(json.dumps(message) + "\n")
            process.stdin.flush()

        def request(identifier, method, params):
            import time
            send({"id": identifier, "method": method, "params": params})
            deadline = time.monotonic() + 20
            while True:
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise RuntimeError(f"Codex {method} timed out; inspect approved client compatibility")
                try:
                    line = messages.get(timeout=remaining)
                except queue.Empty:
                    raise RuntimeError(f"Codex {method} timed out; inspect approved client compatibility") from None
                if line is None:
                    raise RuntimeError("Codex app-server exited before responding; check CLI version/policy")
                data = json.loads(line)
                if data.get("id") == identifier:
                    if "result" not in data:
                        raise RuntimeError(f"Codex {method} failed; do not bypass policy or assume support")
                    return data["result"]

        try:
            request(1, "initialize", {"clientInfo": {"name": "raptora_config_check", "version": "1.0"},
                                      "capabilities": {"experimentalApi": True}})
            send({"method": "initialized"})
            config = request(2, "config/read", {"includeLayers": False, "cwd": tmp})
            agents = config["config"].get("agents", {})
            expected_settings = {"enabled": True, "max_concurrent_threads_per_session": 2, "max_depth": 1}
            if any(type(agents.get(key)) is not type(value) or agents.get(key) != value
                   for key, value in expected_settings.items()):
                raise RuntimeError("CLI did not load the expected agent settings")
            result = request(3, "skills/list", {"cwds": [str(ROOT)], "forceReload": True})
            found = set()
            for entry in result.get("data", []):
                if any(str(ROOT) in str(error) for error in entry.get("errors", [])):
                    raise RuntimeError("Project skill loader reported errors; inspect local skill metadata")
                for skill in entry.get("skills", []):
                    name = skill.get("name")
                    if name in EXPECTED and skill.get("enabled") is True:
                        expected_path = ROOT / ".agents/skills" / name / "SKILL.md"
                        if Path(skill.get("path", "")).resolve() == expected_path.resolve():
                            found.add(name)
            if found != EXPECTED:
                raise RuntimeError("CLI did not discover all four enabled project skills at expected paths")
            print("PASS: isolated CLI settings load and discovery of four enabled project skills")
            print("No model turn, native custom-role invocation, automatic Cloud loading or product acceptance claimed.")
        finally:
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()
            reader.join(timeout=2)
            process.stdin.close()
            process.stdout.close()


if __name__ == "__main__":
    try:
        check()
    except (OSError, RuntimeError, ValueError, KeyError) as error:
        print(f"BLOCKED: {error}", file=sys.stderr)
        sys.exit(1)
