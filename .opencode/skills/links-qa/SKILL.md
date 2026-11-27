---
name: links-qa
description: >-
  Nur bei Strukturänderungen in diesem Repo laden: Contents/TOC, neue
  Überschriften und Anker, Marker, Frontmatter, Querverweise, Batch-Edits,
  neue Sprachdateien. Ergänzt die AGENTS.md um mechanische Prüfungen;
  fängt verwaiste Anker, fehlende TOC-Einträge, gelöschtes Frontmatter
  (404 trotz grünem Build) und Liquid im Markdown ab.
---

# Links-QA

Regeln und Vorschlagsweg: `AGENTS.md` (§2/§9) und `MARKERS.md`. Hier nur die Prüfhinweise, die dort nicht stehen.

## Wann laden

**Einzelner Eintrag in bestehender Rubrik → kein Skill**, sondern normaler Vorschlagsflow. Skill nur bei Strukturänderungen: Contents, neue Überschriften/Anker, Marker, Frontmatter, Querverweise, Batch-Edits, neue Sprachdateien. Keine Lesefragen, keine reinen URL-Checks.

Hinweis: `skill: deny` in review/explore/scout (OpenCode-Konfiguration) – dort ist der Skill unsichtbar; stattdessen in `build`/`general`/`plan` oder mit `@links-qa` laden.

## Reihenfolge

1. **Nie ab der ersten H2 neu bauen.** Das hat schon `permalink: /` gelöscht: 404 trotz grünem Build.

2. **Check laufen lassen**, aus dem Repo-Root und **vor dem Commit** (Vergleich gegen HEAD – danach ist die Preamble-Prüfung blind):

   ```sh
   python3 .opencode/skills/links-qa/scripts/check_links.py
   ```

   Das Skript prüft TOC↔Überschriften, Anker, Querverweise, Marker-Icons, Preamble, Platzhalter, deutsche Anführungszeichen und Liquid. Treffer einzeln auflösen oder begründet stehen lassen; zusätzlich `git diff --check` und den Diff lesen. Neue Sprachdatei: `## Contents` als TOC-Überschrift, sonst überspringt das Skript die Datei.

3. **Vom Skript nicht abgedeckt:**
   - Anker kommen vom Renderer (Kleinbuchstaben, Leerzeichen → `-`, `&`/`/` entfernt): `Arzt- und Therapeutensuche` → `#arzt--und-therapeutensuche`. Bei Umlauten/Doppelhyphen aus der gerenderten Seite nehmen; bei Umbenennung TOC-Label, Anker und Querverweise in beiden Sprachdateien mitziehen.
   - Keine neuen Überschriften mit `&` oder `&amp;`; leere DE-Rubriken dürfen auf EN verweisen, nie umgekehrt.
   - Neue H2/H3: TOCs in beiden Sprachdateien mitziehen.

4. **Skript-Befunde zum Schlussbericht ergänzen.**
