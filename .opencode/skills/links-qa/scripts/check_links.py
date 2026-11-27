#!/usr/bin/env python3
"""Mechanische Prüfung der links-*.md-Struktur. Aus dem Repo-Root aufrufen."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
FILES = sorted(ROOT.glob("links-*.md"))
ISSUES: list[str] = []


def slug(text: str) -> str:
    """Renderer-Anker: Kleinbuchstaben, Satzzeichen raus, Leerzeichen → '-'."""
    text = re.sub(r"<[^>]*>", "", text.strip().lower())
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = "".join(ch for ch in text if ch.isalnum() or ch in " -_")
    return text.replace(" ", "-")


def read_rel(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as error:
        ISSUES.append(f"{path.relative_to(ROOT).as_posix()}: Datei nicht lesbar ({error})")
        return None


def git_show(rel: str) -> str | None:
    try:
        result = subprocess.run(
            ["git", "show", f"HEAD:{rel}"], cwd=ROOT, capture_output=True, text=True,
            encoding="utf-8",
        )
    except OSError:
        return None
    return result.stdout if result.returncode == 0 else None


def before_contents(text: str) -> str:
    index = text.find("\n## Contents")
    return text if index < 0 else text[:index]


def headings_of(text: str) -> dict[str, int]:
    found: dict[str, int] = {}
    for number, line in enumerate(text.splitlines(), 1):
        match = re.match(r"^#{2,4}\s+(.+?)\s*$", line)
        if match:
            found.setdefault(slug(match.group(1)), number)
    return found


markers_text = read_rel(ROOT / "MARKERS.md") or ""
marker_icons = {
    name: icon
    for icon, name in re.findall(
        r"^\|\s*(\S+)\s*\|\s*`\[([^\]]+)\]`", markers_text, re.M
    )
}
if not marker_icons:
    ISSUES.append("MARKERS.md: Markerliste nicht lesbar")

for path in FILES:
    rel = path.relative_to(ROOT).as_posix()
    text = read_rel(path)
    if text is None:
        continue
    lines = text.splitlines()

    # Preamble / Frontmatter
    if not lines or lines[0].strip() != "---":
        ISSUES.append(f"{rel}: Frontmatter fehlt (erste Zeile ist nicht '---')")
    frontmatter_end = next(
        (i for i, line in enumerate(lines[1:], 1) if line.strip() == "---"), None
    )
    if frontmatter_end is None:
        ISSUES.append(f"{rel}: Frontmatter nicht geschlossen")
    elif rel.endswith("links-en.md"):
        frontmatter = "\n".join(lines[1:frontmatter_end])
        if not re.search(r"^permalink:\s*['\"]?/['\"]?\s*$", frontmatter, re.M):
            ISSUES.append(f"{rel}: 'permalink: /' fehlt – Startseite nicht erreichbar")
    previous = git_show(rel)
    if previous is not None and before_contents(previous) != before_contents(text):
        ISSUES.append(
            f"{rel}: Preamble vor '## Contents' geändert – Frontmatter, Titel, "
            "Intro, Hinweise und Sprachleiste prüfen"
        )

    # Querverweise stehen auch im Fließtext, nicht nur im TOC
    cross = [
        (number, match.group(1))
        for number, line in enumerate(lines, 1)
        for match in re.finditer(r"\((links-[a-z-]+\.md#[^)]+)\)", line)
    ]

    # TOC ↔ Überschriften
    toc_start = next((i for i, line in enumerate(lines) if line.strip() == "## Contents"), None)
    if toc_start is None:
        ISSUES.append(f"{rel}: '## Contents' fehlt")
    else:
        toc_end = next(
            (i for i in range(toc_start + 1, len(lines)) if lines[i].startswith("## ")),
            len(lines),
        )
        local: dict[str, int] = {}
        for number in range(toc_start + 2, toc_end + 1):
            for match in re.finditer(r"\[[^\]]+\]\((#[^)]+)\)", lines[number - 1]):
                local.setdefault(match.group(1)[1:], number)

        body_headings = {
            anchor: number
            for anchor, number in headings_of(text).items()
            if number > toc_end
        }
        for anchor, number in local.items():
            if anchor not in body_headings:
                ISSUES.append(f"{rel}:{number}: verwaister TOC-Anker #{anchor}")
        for anchor, number in body_headings.items():
            if anchor not in local:
                ISSUES.append(f"{rel}:{number}: Überschrift fehlt im TOC (#{anchor})")
            following = next((line for line in lines[number:] if line.strip()), "")
            if re.match(r"^\*(No reviewed entries yet|Noch keine|Vorschläge willkommen)", following):
                ISSUES.append(f"{rel}:{number}: leere Rubrik mit Platzhalter im TOC – prüfen")

        for number, target in cross:
            other_name, anchor = target.split("#", 1)
            other_path = ROOT / other_name
            if not other_path.exists():
                ISSUES.append(f"{rel}:{number}: Querverweis auf fehlende Datei {other_name}")
                continue
            other_text = read_rel(other_path)
            if other_text is None:
                continue
            if anchor not in headings_of(other_text):
                ISSUES.append(f"{rel}:{number}: Querverweis {target} – Anker existiert nicht")

    # Marker
    for number, line in enumerate(lines, 1):
        if not line.startswith("- **["):
            continue
        tail = line.split("** — ", 1)[-1]
        tail = re.sub(r"\[([^\]]*)\]\([^)]*\)", "", tail)  # Linktexte sind keine Marker
        mentioned = set(re.findall(r"\[([A-Z][A-Za-z -]+)\]", tail))
        if not mentioned:
            ISSUES.append(f"{rel}:{number}: Eintrag ohne Marker")
        for name in sorted(mentioned):
            if name not in marker_icons:
                ISSUES.append(f"{rel}:{number}: unbekannter Marker [{name}] (nicht in MARKERS.md)")
            elif f"{marker_icons[name]} [{name}]" not in tail:
                ISSUES.append(
                    f"{rel}:{number}: Marker [{name}] mit falschem oder fehlendem Icon "
                    f"(erwartet {marker_icons[name]})"
                )
        cleaned = tail
        for name, icon in marker_icons.items():
            cleaned = cleaned.replace(f"{icon} [{name}]", "")
        if any(icon in cleaned for icon in marker_icons.values()):
            ISSUES.append(f"{rel}:{number}: Icon ohne Textmarker")

# Liquid in irgendeiner Markdown-Datei bricht den Pages-Build
for path in ROOT.rglob("*.md"):
    rel = path.relative_to(ROOT).as_posix()
    if any(part.startswith(".") for part in Path(rel).parts):
        continue  # .git, .opencode usw. werden nicht von Jekyll gerendert
    content = read_rel(path)
    if content is None:
        continue
    for number, line in enumerate(content.splitlines(), 1):
        if "{%" in line or "{{" in line:
            ISSUES.append(f"{rel}:{number}: Liquid-Delimiter im Markdown – Build bricht")

# Deutsche Anführungszeichen
german = ROOT / "links-de.md"
german_text = read_rel(german) if german.exists() else None
if german_text is not None:
    for number, line in enumerate(german_text.splitlines(), 1):
        if line.count("„") != line.count("“"):
            ISSUES.append(f"links-de.md:{number}: Anführungszeichen nicht paarweise („ … “)")
        if '"' in line:
            ISSUES.append(f"links-de.md:{number}: gerades Anführungszeichen – Änderung vorschlagen")

if ISSUES:
    unique_issues = list(dict.fromkeys(ISSUES))
    print(f"{len(unique_issues)} Befund(e):")
    for issue in unique_issues:
        print(f" - {issue}")
    sys.exit(1)
print("OK: keine mechanischen Abweichungen gefunden.")
