"""Fail-closed structural checks for Raptora packaging guidance.

Default mode is draft lint only. Package mode additionally requires an exact
external adoption record and an approved contract; this tool cannot grant
human ownership, security, legal or Windows acceptance approval.
No private application source or customer files are read by the default mode.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import html
import unicodedata
from html.parser import HTMLParser
from pathlib import Path

ROLES = ("maintainer", "build-engineering", "Windows/QA", "security/IP")
HEADING = re.compile(r"^## ([A-Z]{2}-\d{2}): (.+?)\s*$")
SECTION_ID = re.compile(r"^## ([A-Z]{2}-\d{2})\b")
TOP_LEVEL = re.compile(r"^# (.+?)\s*$")
SECOND_LEVEL = re.compile(r"^##(?!#)\s+")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
LINK = re.compile(r"!?\[[^\]]+\]\(([^)]+)\)")
COMMENT = re.compile(r"<!--.*?(?:-->|$)", re.DOTALL)
PLACEHOLDERS = {"todo", "tbd", "comingsoon", "[placeholder]", "placeholder"}


class ValidationError(ValueError):
    """Input cannot be considered structurally complete."""


def _read(path: Path) -> bytes:
    try:
        raw = path.read_bytes()
    except OSError as exc:
        raise ValidationError(f"missing/unreadable input: {path.name}: {exc}") from exc
    if not raw:
        raise ValidationError(f"empty input: {path.name}")
    return raw


def _utf8(raw: bytes, label: str) -> str:
    try:
        return raw.decode("utf-8-sig")
    except UnicodeError as exc:
        raise ValidationError(f"invalid UTF-8: {label}") from exc


def _approved_path(root: Path, name: str) -> Path:
    if not isinstance(name, str) or not name or Path(name).is_absolute() or "\\" in name or ":" in name or any(part in (".", "..", "") for part in name.split("/")):
        raise ValidationError("approved input must be a safe relative path")
    candidate = root
    for part in Path(name).parts:
        candidate = candidate / part
        if candidate.is_symlink():
            raise ValidationError("symlink approved input is not allowed")
    path = candidate.resolve()
    if not path.is_relative_to(root.resolve()) or not path.is_file():
        raise ValidationError(f"invalid or missing approved relative input: {name}")
    return path


def _visible_lines(source: str) -> list[str]:
    """Ignore HTML comments and fenced examples when finding required headings."""
    cleaned = COMMENT.sub("", source)
    result = []
    marker = ""
    minimum = 0
    for line in cleaned.splitlines():
        match = FENCE.match(line)
        if match:
            char = match.group(1)[0]
            length = len(match.group(1))
            if not marker:
                if char != "`" or "`" not in match.group(2):
                    marker, minimum = char, length
            elif marker == char and length >= minimum and not match.group(2).strip():
                marker, minimum = "", 0
            continue
        if not marker:
            result.append(line)
    return result


class _OutsideHTML(HTMLParser):
    """Conservatively exclude raw HTML content, including nested hidden text."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags: list[str] = []
        self.text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list) -> None:
        if tag not in {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}:
            self.tags.append(tag)

    def handle_endtag(self, tag: str) -> None:
        if tag in self.tags:
            last = len(self.tags) - 1 - self.tags[::-1].index(tag)
            self.tags = self.tags[:last]

    def handle_startendtag(self, tag: str, attrs: list) -> None:
        pass

    def handle_data(self, data: str) -> None:
        if not self.tags:
            self.text.append(data)


def _substantive_body(body: str) -> bool:
    # Raw HTML and indented code alone are not explanatory Markdown prose.
    parser = _OutsideHTML()
    parser.feed(body)
    parser.close()
    body = "".join(parser.text)
    lines = []
    for line in body.splitlines():
        if line.startswith(("    ", "\t")):
            continue
        if re.match(r"^\s{0,3}(?:#{1,6}(?:\s|$)|\[[^\]]+\]:)", line):
            continue
        line = re.sub(r"<[^>]*>", "", line)
        line = html.unescape(line)
        # Hangul fillers render blank despite having Unicode letter categories.
        line = "".join(c for c in line if unicodedata.category(c) != "Cf" and c not in "\u115f\u1160\u3164\uffa0")
        line = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", line)
        line = re.sub(r"\[[^\]]*\]\([^)]+\)", "", line)
        line = re.sub(r"^\s*[-*+]\s*\[[ xX]\]\s*", "", line)
        line = re.sub(r"^\s*(?:[-*+]|\d+[.)])\s+", "", line)
        line = re.sub(r"\[[^\]]*\](?:\[[^\]]*\])?", "", line)
        line = re.sub(r"https?://\S+", "", line)
        normalized = "".join(c for c in line.lower() if c.isalnum())
        words = re.findall(r"\w+", line.lower())
        if normalized and normalized not in PLACEHOLDERS and not (words and all(word in PLACEHOLDERS for word in words)):
            lines.append(normalized)
    return bool(lines)


def _links_resolve(root: Path, path: Path, source: str) -> None:
    for target in LINK.findall(source):
        url = target.strip().split(" ", 1)[0].strip("<>").split("#", 1)[0]
        if not url or re.match(r"^[a-z][a-z0-9+.-]*:", url, re.I) or url.startswith("//"):
            continue
        dest = (path.parent / url).resolve()
        if not dest.is_relative_to(root.resolve()) or not dest.exists():
            raise ValidationError(f"broken/out-of-scope relative link in {path.name}: {url}")
        candidate = path.parent / url
        if any(p.is_symlink() for p in (candidate, *candidate.parents)):
            raise ValidationError(f"symlink relative link in {path.name}")


def _check_document(root: Path, doc: dict, source: str, path: Path) -> int:
    lines = _visible_lines(source)
    titles = [m.group(1) for line in lines if (m := TOP_LEVEL.match(line))]
    if titles != [doc["requiredTitle"]]:
        raise ValidationError(f"{doc['id']}: missing/duplicated/incorrect document title")
    actual = [m.group(0) for line in lines if (m := HEADING.match(line))]
    expected = [f"## {s['id']}: {s['heading']}" for s in doc["requiredSections"]]
    if actual != expected:
        raise ValidationError(f"{doc['id']}: required section IDs, titles or order differ")
    all_l2 = [(idx, line) for idx, line in enumerate(lines) if SECOND_LEVEL.match(line)]
    if [line for _, line in all_l2] != expected:
        raise ValidationError(f"{doc['id']}: unexpected, missing, duplicated or renamed level-two heading")
    ids = [m.group(1) for line in lines if (m := SECTION_ID.match(line))]
    if len(ids) != len(set(ids)):
        raise ValidationError(f"{doc['id']}: repeated required section ID")
    for index, (start, _) in enumerate(all_l2):
        end = all_l2[index + 1][0] if index + 1 < len(all_l2) else len(lines)
        if not _substantive_body("\n".join(lines[start + 1:end])):
            raise ValidationError(f"{doc['id']}: empty/placeholder-only body: {expected[index]}")
    _links_resolve(root, path, source)
    return len(expected)


def validate(root: Path, contract_rel: str = "docs/packaging/required-sections.json",
             *, package: bool = False, adoption_rel: str | None = None) -> int:
    root = root.resolve()
    contract_path = _approved_path(root, contract_rel)
    contract_raw = _read(contract_path)
    try:
        contract = json.loads(_utf8(contract_raw, "contract"))
    except (json.JSONDecodeError, UnicodeError) as exc:
        raise ValidationError("invalid content contract JSON") from exc
    if not isinstance(contract, dict) or type(contract.get("formatVersion")) is not int or contract.get("formatVersion") != 1:
        raise ValidationError("unsupported/malformed content contract")
    if (contract.get("status") not in ("draft-for-review", "approved-for-packaging")
            or contract.get("scope") != "documentation-completeness-only"
            or contract.get("applicationValidation") is not False
            or type(contract.get("packagingAdoptionApproved")) is not bool
            or contract.get("requiredContentReviewRoles") != list(ROLES)):
        raise ValidationError("missing/malformed adoption contract metadata")
    if contract.get("contractId") != "RAPTORA-PACKAGING-DOCS-1":
        raise ValidationError("unexpected content contract identity")
    docs = contract.get("documents")
    if not isinstance(docs, list) or not all(isinstance(x, dict) for x in docs) or [x.get("id") for x in docs] != [
        "PKG-DOC-01", "PKG-DOC-02"
    ]:
        raise ValidationError("both required document records must be present and ordered")
    for d in docs:
        if any(not isinstance(d.get(key), str) or not d[key].strip() for key in ("path", "requiredTitle", "genericDestinationRole")):
            raise ValidationError("malformed document identity/path/destination metadata")
        sections = d.get("requiredSections")
        if not isinstance(sections, list) or not sections:
            raise ValidationError(f"{d['id']}: no mandatory section contract")
        ids = [x.get("id") for x in sections if isinstance(x, dict)]
        if len(ids) != len(sections) or any(not isinstance(i, str) or not re.fullmatch(r"[A-Z]{2}-\d{2}", i) for i in ids) or len(ids) != len(set(ids)):
            raise ValidationError(f"{d['id']}: malformed or duplicate contract section IDs")
        if any(not isinstance(x.get("heading"), str) or not x["heading"].strip()
               or not isinstance(x.get("requiredTopics"), list)
               or not x["requiredTopics"] or any(not isinstance(topic, str) or not topic.strip() for topic in x["requiredTopics"]) for x in sections):
            raise ValidationError(f"{d['id']}: malformed mandatory heading/topics")
    hashes = {}
    count = 0
    for doc in docs:
        path = _approved_path(root, doc["path"])
        raw = _read(path)
        count += _check_document(root, doc, _utf8(raw, doc["id"]), path)
        hashes[doc["id"]] = hashlib.sha256(raw).hexdigest()
    if package:
        if contract.get("packagingAdoptionApproved") is not True:
            raise ValidationError("packaging adoption is not approved by the contract")
        if contract.get("status") != "approved-for-packaging":
            raise ValidationError("packaging contract is still a draft")
        if not adoption_rel:
            raise ValidationError("exact reviewed adoption manifest required")
        approval_path = _approved_path(root, adoption_rel)
        try:
            approved = json.loads(_utf8(_read(approval_path), "adoption manifest"))
        except json.JSONDecodeError as exc:
            raise ValidationError("invalid adoption manifest JSON") from exc
        if not isinstance(approved, dict):
            raise ValidationError("adoption manifest must be an object")
        if approved.get("contractSha256") != hashlib.sha256(contract_raw).hexdigest():
            raise ValidationError("contract hash is not the approved version")
        if approved.get("documents") != hashes:
            raise ValidationError("document bytes do not match approved SHA-256 values")
        if approved.get("reviewers") != {role: "approved" for role in ROLES}:
            raise ValidationError("exact-content reviewer decisions incomplete")
        # These machine-readable flags are an additional guard, not evidence
        # of authorised human signatures; maintain that approval externally.
    return count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--contract", default="docs/packaging/required-sections.json")
    parser.add_argument("--package", action="store_true", help="also enforce reviewed adoption identity")
    parser.add_argument("--adoption-manifest", help="relative path to separately approved hash/role record")
    args = parser.parse_args()
    try:
        count = validate(args.root, args.contract, package=args.package, adoption_rel=args.adoption_manifest)
    except (ValidationError, KeyError, TypeError) as exc:
        print(f"FAIL: packaging guidance validation: {exc}", file=sys.stderr)
        return 1
    mode = "structural and adoption-record preflight" if args.package else "draft structure only"
    print(f"PASS: {count} required sections; {mode}")
    if not args.package:
        print("NOT RUN: private packager enforcement, owner sign-off, Windows and release acceptance")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
