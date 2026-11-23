---
title: KI-Regeln (AGENTS.md)
layout: default
nav_order: 5
nav_exclude: true
sitemap: false
---

# AGENTS.md – Regeln für KI-Assistenten

Diese Datei gilt für alle KI-Assistenten, die in diesem Ordner arbeiten. Sie ist verbindlich; bei Widersprüchen mit anderen Dateien gewinnt sie.

## 1. Was dieses Projekt ist

Eine **Inhalts-Sammlung**, kein Programm. Das Ergebnis sind gut kuratierte Markdown-Dateien. Die Website (GitHub Pages mit `just-the-docs`) wird daraus nur erzeugt.

**Single Source of Truth für Inhalte:** `README.md` (GitHub-Ansicht), `links-de.md`, `links-en.md` und weitere `links-<sprache>.md`.
**Single Source of Truth für Marker:** `MARKERS.md` – daraus werden Legende, Issue-Formulare und Einträge abgeleitet. Alles andere ist Konfiguration oder erzeugtes Ergebnis.

## 2. Grundsatz: Vorschlag → Anmerkungen → Freigabe → Umsetzung

Der Normalablauf für neue Inhalte:

1. Der User gibt einen Link (oder eine Idee) an.
2. Die KI **prüft und schlägt vor**, wie und wo der Eintrag eingetragen wird – noch ohne Dateiänderung.
3. Der User macht Anmerkungen und sagt erst dann **„freigegeben"**.
4. Nach dieser ausdrücklichen Freigabe darf die KI **den Rest machen**: Datei schreiben, committen und pushen.

- Ohne Freigabe: **nie** Dateien ändern, committen oder pushen. Bei Unklarheit Empfehlung geben statt editieren.
- Die Freigabe gilt nur für den konkreten, besprochenen Eintrag – nicht als Dauererlaubnis für alles Weitere.
- Ändere nie stillschweigend bestehende Einträge, um sie "zu verbessern". Entferne Inhalte nur, wenn es verlangt und begründet ist (z. B. toter Link).
- Ein logischer Eintrag pro Änderung. Keine Sammel-Commits verschiedener Themen.

## 3. Vertrauensgrenze (besonders wichtig bei Gesundheitsthemen)

- **Keine medizinischen Behauptungen erfinden.** Was nicht in der verlinkten Quelle steht, wird nicht behauptet.
- Hat der User **keine Beschreibung** mitgegeben, darf die KI die Seite öffnen und **eine kurze Zusammenfassung aus deren Inhalt** schreiben – nicht mehr. Keine externen Fakten, keine Bewertung, keine Schlussfolgerungen ergänzen.
- Nicht aus dem Training "wissen", dass eine Quelle seriös ist. Link öffnen und prüfen. Wenn nicht prüfbar: neutral formulieren oder flaggen – nie behaupten.
- **Keine Heilversprechen, keine Therapieempfehlung, keine Diagnosehilfe.** Einträge verlinken auf Quellen, sie bewerten nicht deren Wahrheit.
- Umstrittene oder veraltete Quellen nur mit sichtbarem Marker (`[Outdated]`, `[Preprint]`) und neutraler Beschreibung.
- Bei Unsicherheit zu Evidenz, Einordnung oder Quelle: **dem User eine Empfehlung geben, bevor etwas geschrieben wird.**

## 4. Aufnahmekriterien

Aufnehmen, wenn die Quelle:
- thematisch passt (Long COVID, ME/CFS, Post-Viral, POTS, MCAS, hEDS, Fibromyalgie als Begleiterkrankung),
- in sich geschlossen und dauerhaft erreichbar ist (stabile URL, keine URL-Shortener),
- keine Bezahlung oder Registrierung erzwingt (sonst `[Commercial]` markieren),
- nicht rein werblich ist (Affiliate-Links ablehnen),
- eine klare Herkunft hat (Behörde, Fachgesellschaft, Wissenschaft, Selbsthilfe, Erfahrungsbericht).

Nicht aufnehmen: Heilversprechen, Verschwörungsquellen, Paywall-only-Inhalte ohne freie Zusammenfassung, reine Werbung, doppelte Links.

**Ausnahme bei doppelten Links:** Dieselbe Ressource darf in mehreren Sprachdateien stehen, wenn es dafür **jeweils eine eigene Sprachfassung** gibt. Die deutsche Version kommt nach `links-de.md`, die englische Version nach `links-en.md`. Zwei-identische Links in *derselben* Datei bleiben unerwünscht.

## 5. Eintragsformat

```
- **[Name der Quelle](https://...)** — Ein neutraler Satz zur Beschreibung. 📄 [Study]
```

- Ein Satz, kurzer Text, am Ende ein Punkt.
- **Ein Datumsmarker `[Stand: …]` wird vorerst weggelassen** (Entscheidung des Users). Nicht eigenmächtig wieder ergänzen.
- Das Icon **immer zusammen mit dem Textmarker** schreiben (z. B. `📄 [Study]`), nie nur das Emoji – sonst können Screenreader den Eintrag nicht einordnen.
- **Alle Marker stehen auf Englisch.** Die vollständige Liste mit deutscher Übersetzung steht in [`MARKERS.md`](MARKERS.md) – dort ergänzen, nicht hier kopieren.
- Mehrere Marker pro Eintrag sind erlaubt. Häufen sich bestimmte Kombinationen, kann daraus eine neue Kategorie entstehen – dann vorher mit dem User abstimmen.
- **Keine Sterne, keine Gut-schlecht-Bewertung.** Nur den Quellentyp benennen – die Leserinnen und Leser urteilen selbst.
- Sprache des Eintrags bestimmt die Datei: deutsche Quellen → `links-de.md`, englische → `links-en.md`.
- Neue Sprachdatei nur nach Absprache mit dem User anlegen; Dateiname `links-<lang>.md`. Danach die Sprachleiste in **allen** Dateien mitaktualisieren (siehe Abschnitt 6).

### Warn-Kästen

Wenn ein Eintrag eine klare Warnung braucht, direkt darunter schreiben:

```
> ⚠️ Diese Quelle ist veraltet – bitte nur im historischen Kontext nutzen.
```

Nur verwenden bei `⚠️ [Outdated]` oder bei Quellen mit begründeten Bedenken (z. B. nicht mehr erreichbar, umstritten – dann mit Quellenangabe). **Nicht** für `[Preprint]` oder `[Commercial]` – dafür reichen die Marker. Keine medizinische Bewertung in den Kasten schreiben, nur einen sachlichen Hinweis.

## 6. Platzierung

- Eintrag in die **passende thematische Unterkategorie** der Sprachdatei.
- Innerhalb einer Kategorie alphabetisch nach Namen, falls die Liste alphabetisch ist; sonst am Ende der Kategorie. Nicht willkürlich oben/unten mischen.
- Keine neue Kategorie ohne Absprache – die vorläufigen Kategorien stehen in den Sprachdateien.
- Mehrsprachige Quelle: **eine eigene Sprachfassung pro Sprachdatei** – deutsche Fassung nach `links-de.md`, englische Fassung nach `links-en.md`. Das ist die erlaubte Ausnahme vom Doppel-link-Verbot (siehe Abschnitt 4). Kein Kurzverweis nötig, wenn beide Fassungen vorhanden sind.
- **Einstieg der Sprachdateien:** Jede `links-<sprache>.md` beginnt nach dem Frontmatter mit dem Titel `Awesome Long COVID & ME/CFS Resources – <Sprache>`, zwei kurzen Absätzen, dem Hinweis zum Link-Einreichen, dem ⚠️- und dem ℹ️-Hinweis. Danach folgt die Sprachleiste, dann das Inhaltsverzeichnis. Es gibt keine sprachbezogenen README-Anleitungen mehr.
- **Änderungen in allen Sprachen:** Wird der Einstieg geändert, gehört dieselbe Änderung in alle `links-<sprache>.md` – übersetzt, aber mit gleicher Struktur und denselben Links. `README.md` bleibt die einzige README und verlinkt in der Tabelle nur noch auf die Links.

- Neue Sprache: erst mit dem User abstimmen, dann `links-<lang>.md` anlegen. Danach **alle** Stellen mitaktualisieren: Tabelle in `README.md`, Einstieg, Sprachleiste und Seitentitel in allen `links-*.md` sowie die Sprachliste im Issue-Formular. Sonst entstehen verwaiste Links.
- Die Website-Sprachnavigation läuft über die Seitentitel der Dateien mit Frontmatter (aktuell `links-en.md` als Startseite und `links-de.md`); `nav_exclude` hält Meta-Seiten aus der Seitenleiste. Englisch steht immer zuerst, dann Deutsch, dann weitere Sprachen.

## 7. Geschützte Bereiche – nie ohne ausdrückliche Anweisung ändern

- `README.md`: Abschnitte "Important"/"Wichtig" (Disclaimer), "Legende"
- `MARKERS.md`, `AGENTS.md`, `CONTRIBUTING.md`, `CONTRIBUTING-de.md`, `CODE_OF_CONDUCT.md`
- `_config.yml`, `.github/` (Workflows, Issue-Templates)
- `LICENSE.txt`
- Bestehende Einträge anderer Personen

## 8. Interne Links

Interne Links werden **immer als `.md` geschrieben**, z. B. `[Deutsch](links-de.md)`.
Das Plugin `jekyll-relative-links` wandelt sie beim Build automatisch in Website-Links um.
**Niemals** `.md` manuell in `.html` ändern – das zerstört die Links im GitHub-Repo und ist überflüssig.

## 9. Ablauf für einen Änderungsvorschlag

1. Scope prüfen: passt der Eintrag überhaupt hierher?
2. Quelle/Link prüfen: erreichbar, stabil, Herkunft klar?
3. Einzigartigkeit prüfen: ist die Quelle schon gelistet? (Ausnahme: eigene Sprachfassung in anderer Datei – erlaubt.)
4. Platzierung bestimmen: richtige Sprachdatei, richtige Kategorie.
5. Formulierung: Hat der User keine Beschreibung gegeben, Seite öffnen und eine **kurze Zusammenfassung aus deren Inhalt** schreiben. Sonst die Vorgabe des Users übernehmen. Kein Heilversprechen, Marker setzen – kein Datumsmarker.
6. **Vorschlag zurückgeben** – Dateien noch nicht ändern, noch nicht committen, noch nicht pushen.
7. User-Anmerkungen einarbeiten und **auf „freigegeben" warten**.
8. Erst nach Freigabe: Datei schreiben, committen und pushen. Danach kurz berichten, was passiert ist.

Im Vorschlag kurz berichten: **Entscheidung** (aufnehmen / ablehnen / nur empfehlen), **welche Dateien** betroffen wären, **welche Prüfung** gemacht wurde, **was unsicher** ist.
