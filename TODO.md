---
title: ToDo
layout: default
nav_order: 7
---

# ToDo – Stand nach Veröffentlichung

Ziel: Awesome-Liste zu ME/CFS, Post-COVID/Long COVID und verwandten Erkrankungen.
Veröffentlicht als GitHub-Repo `awesome-long-covid-mecfs`, mehrsprachig, Sprache als Hauptkategorie.

**Live:** https://github.com/awesome-long-covid-mecfs/awesome-long-covid-mecfs · https://awesome-long-covid-mecfs.github.io/awesome-long-covid-mecfs/
**Kurz-URL:** https://awesome-long-covid-mecfs.github.io/ → Weiterleitung auf die Projektseite (eigenes Repo `awesome-long-covid-mecfs.github.io`)

## Fundament

- [x] Repo-Namen final auf GitHub geprüft – `awesome-long-covid-mecfs` angelegt und gepusht
- [x] Lizenz festgelegt – CC BY-SA 4.0 (`LICENSE.txt`)
- [x] GitHub-Beschreibung und Topics finalisiert – 11 Topics gesetzt
- [x] Grundgerüst: `README.md`, `LICENSE.txt`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`
- [x] Medizinischer Disclaimer formuliert (keine Diagnose-/Behandlungsempfehlung, keine Heilversprechen)

## Struktur & Inhalt

- [x] Unterkategorien festgelegt (Diagnostik, Studien/Forschung, Behandlung/Therapie, Selbsthilfe & Community, Alltag & Versorgung, Hilfsmittel, Recht & Anträge, Fachliteratur, Patientengeschichten)
- [x] Sprachebenen festlegt – Englisch primär, Deutsch, weitere möglich; eigene Sprachfassung pro Datei erlaubt
- [x] Einheitliches Eintragsformat festgelegt – Icon + englischer Marker, kein Datum
- [x] Erste Ressourcen gesammelt – 10 geprüfte Links in beiden Sprachdateien
- [x] Linkprüfung vor dem Publish – alle Links auf Erreichbarkeit geprüft, zwei heikle Seiten mit Marker/Warnung aufgenommen

## Qualität & Sicherheit

- [x] Aufnahmekriterien definiert – in `AGENTS.md` und den Ausschlusslisten der READMEs
- [x] Sprache achten: stigmafreie Begriffe, betroffenenfreundlich, veraltete Bezeichnungen nur mit Hinweis
- [x] Umgang mit umstrittenen Therapien/Studien geregelt – keine Bewertung durch uns, Quellen benennen
- [x] Review-Prozess für Contributions festgelegt – Vorschlag → Anmerkungen → Freigabe → Umsetzung

## Veröffentlichung

- [x] Repo angelegt und gepusht (`main`, Commit `d9d01ce`)
- [x] README-Einstieg geprüft – SEO-Begriffe kommen natürlich vor
- [x] GitHub Pages aktiviert und Build geprüft – `built`, alle Seiten HTTP 200
- [ ] Optional: Eintrag in den awesome-Listen-Index (sindresorhus/awesome) beantragen – erst nach ausreichendem Inhalt
- [ ] Ankündigung in einschlägigen Communities (Selbsthilfe, Forschung) – nur nach Rücksprache, kein Spam

## Nächste Schritte (vom User vorgegeben)

- [ ] Inhalte: erste 10 Links sind drin – weitere Ressourcen sammeln ist der nächste grosse Schritt
- [x] Eigenes GitHub-Repo angelegt: Name genau `awesome-long-covid-mecfs`, ohne README initialisiert
- [x] Ordnerinhalt in das neue Repo kopiert und gepusht
- [x] GitHub Pages aktiviert (Branch `main`, Pfad `/`) – per GitHub-API gesetzt
- [x] Website getestet – Startseite, EN, DE und README-de liefern HTTP 200; `baseurl` war richtig gesetzt

## Basisstruktur reviewen (Schritt für Schritt mit dem User)

- [x] Zusätzliche Melde-Möglichkeit per E-Mail für Personen ohne GitHub-Konto: Adresse `awesome-long-covid-mecfs[at]sags-per-mail.de` in `README.md` und `CONTRIBUTING.md` ergänzt. Gewählte Variante: `[at]` statt `@` (einfach, barrierefrei, schützt vor einfachen Spam-Crawlern). Auch dieser TODO-Eintrag ist entschärft. Bei Bedarf auf eine stärkere Variante wechseln (Bild oder Kontaktformular).
- [x] `AGENTS.md` reviewt – KI prüft Links (Erreichbarkeit, Duplikate, Quellenart, Marker), schreibt Vorschläge und darf nach Freigabe committen/pushen. Kein Stand-Datum.
- [ ] `AGENTS.md`: Wenn alles stimmt, **auf Englisch umstellen** – noch offen.
- [x] Kategorien durch den User geprüft – vorerst unverändert; weitere Kategorien bei Bedarf (Marker-Kombinationen im Auge behalten).

## Mehrsprachigkeit (vom User vorgegeben)

- [x] Primärsprache ist **Englisch**; Deutsch und später weitere Sprachen müssen schnell erreichbar sein – Haupt-`README.md` ist englisch
- [x] Sprachwechsel oben in der README und in jeder Sprachdatei über Links **mit Länderflaggen-Emojis** (🇬🇧 English, 🇩🇪 Deutsch, …)
- [x] Kurzer Verweis in der Haupt-README: „Deutsche Anleitung hier" → `README-de.md` (neue deutsche README)
- [x] Benennung neuer Sprachdateien festlegen (`resources-<lang>.md`) und regeln, wer sie anlegt – steht in `AGENTS.md`
- [x] Beim Anlegen einer neuen Sprache alle Stellen mitaktualisieren: Sprachleiste in allen Dateien, `aux_links` in `_config.yml`, Inhaltsverzeichnisse, Issue-Formular – als Regel in `AGENTS.md` festgehalten

## Abschlusscheck vor Veröffentlichung

- [x] Repo-weite Suche nach zurückgebliebenen PII-Platzhaltern – inklusive `.github/`, Workflows, versteckter Dateien und LICENSE; keine Funde
- [x] Zusätzlich geprüft, dass die E-Mail-Adresse nirgends im Klartext steht (nur `[at]`-Schreibweise) – am 22.11.2026
- [x] Abschlusscheck dokumentiert: keine PII-Platzhalter im veröffentlichten Repo (Prüfung am 22.11.2026)

## Feedback zur Basisstruktur (Stand: umgesetzt)

- [x] **Marker alle auf Englisch** – `MARKERS.md` ist die Quelle; Legende, `AGENTS.md`, Issue-Formular, Templates und alle Einträge umgestellt
- [x] **Marker-Definitionen in `MARKERS.md` ausgelagert** – inklusive Spalte mit deutscher Übersetzung; alle anderen Dateien verweisen darauf
- [x] **GitHub-Issue-Formular auf Englisch** – inklusive „Weiß ich nicht" → „Not sure"; beide Formulare (Link/Broken link) englisch
- [x] **README pro Sprache** – Haupt-`README.md` bleibt die vollständige englische SEO-Seite, zusätzlich `README-de.md` mit Verlinkung per Flaggen-Emojis
- [x] **Reihenfolge der Übersetzungsarbeiten abgestimmt** – Phase 1 (Regeln/Vokabular) → Phase 2 (Sprach-READMEs) → Phase 3 (Inhalte) → Phase 4 (Navigation) → Phase 5 (Veröffentlichung)
- [x] **Repo-Beschreibung SEO-optimiert** – Finaltext in `_config.yml` und TODO; bei Repo-Erzeugung in das GitHub-Feld übernehmen:
  `Curated resources on Long COVID, Post-COVID, ME/CFS (Myalgic Encephalomyelitis / Chronic Fatigue Syndrome), POTS, MCAS, hEDS, fibromyalgia, SIBO, dysautonomia and other post-viral conditions - fatigue, PEM and symptom management for patients, carers and researchers.`
- [x] **`CONTRIBUTING.md`: E-Mail-Kontakt weiter nach oben** – direkt unter die Einleitung gerückt
- [x] **Sortierung: zuerst Englisch, dann Deutsch** – `nav_order` EN 2, DE 3; README-de 4
- [x] **Sprachnavigation über `aux_links`** in `_config.yml` – zentral, eine Zeile pro Sprache, skalierbar für weitere Sprachen
- [ ] **Kapitel in der Seitenleiste** – Entscheidung offen; C (JavaScript) verworfen
  - Befund: just-the-docs baut die linke Navigation ausschließlich aus Seiten-Frontmatter. Die H2-Überschriften einer einzelnen Datei lassen sich dort nicht einblenden; `nav_fold` gilt nur für Collections, und `{:toc}` mit `<details>` erscheint immer im Seiteninhalt.
  - **A (empfohlen):** automatischer, aufklappbarer Inhaltsverzeichnis-Block oben in `resources-en.md` und `resources-de.md` via `<details>` + `{:toc}`. Keine Strukturänderung, SSOT und alle URLs bleiben, das Verzeichnis pflegt sich selbst. Nachteil: nicht in der linken Seitenleiste.
  - **B:** `resources-de/` und `resources-en/` als Ordner mit `index.md` plus 9 Kinderseiten (`parent:`), echte aufklappbare Unterpunkte links. Nachteile: URL-Wechsel (`/resources-de.html` → `/resources-de/`, mit `permalink` abfangbar), Anker-Links werden seitenübergreifend, Sprachleiste und Disclaimer sind 10× zu pflegen, die `AGENTS.md`-Regel „eine Datei pro Sprache, Kategorien als H2" muss geändert werden, und viele Kategorien haben erst 0–1 Einträge.
  - Vergleich anderer Listen: free-programming-books bleibt bei einer Datei pro Sprache plus Anker (keine Kategorie-Navigation); natnew/Awesome-Prompt-Engineering nutzt ~15 flache Kategoriedateien (lange flache Nav); die just-the-docs-Doku selbst nutzt Ordner plus Kinderseiten; awesome-python baut eine eigene Website (zu viel Aufwand für uns).
- [x] **Inhaltsverzeichnis am Anfang jeder Sprachdatei** mit Links zu allen Kategorien (manuell, funktioniert auf GitHub und auf der Website)

## Website-Navigation & Erreichbarkeit

- [x] **Root-URL `https://awesome-long-covid-mecfs.github.io/`** – neues User-Site-Repo `awesome-long-covid-mecfs.github.io` mit statischem `index.html`-Redirect auf `/awesome-long-covid-mecfs/`; Pages auf `main` / `(root)` aktiv. Das Projekt-Repo bleibt unverändert, `baseurl` und `aux_links` bleiben wie sie sind.
- [x] **Meta-Seiten in der Seitenleiste** – `AGENTS.md`, `MARKERS.md`, `TODO.md`, `CONTRIBUTING.md` und `CODE_OF_CONDUCT.md` mit Frontmatter (`title`, `nav_order`) für just-the-docs
- [x] **`RESEARCH.md` entfernt** – die Vorlagenanalyse war nur für die Startphase; der einzige Verweis stand in dieser Datei
- [x] **Kaputte Issue-Links in den READMEs repariert** – `/home/max/CodeSpaces://github.com/...` → `https://github.com/...` in `README.md` und `README-de.md`; der Rest des Repos wurde auf ähnliche Pfad-Verweise geprüft (keine weiteren Funde)
- [ ] **`<html lang>` auf den deutschen Seiten korrigieren** – `locale: de_DE` im Frontmatter setzt nur `og:locale`; just-the-docs liest für `<html lang>` ausschliesslich `site.lang`. Vorschlag: lokale `_layouts/default.html` mit `page.lang | default: site.lang | default: 'en-US'` und `lang: de` in `README-de.md`/`resources-de.md`. Nachteil: die kopierte Layout-Datei bekommt keine automatischen Theme-Updates. Vom User vorerst zurückgestellt.
- [x] **Direkt-Links zu den Inhalten auf der Startseite** – zwei Buttons direkt nach dem Disclaimer in `README.md` und `README-de.md` (`.btn .btn-blue` mit `.mr-2` als Abstand), damit die Ressourcenlisten ohne Scrollen erreichbar sind
- [x] **Obere Sprachleiste eindeutig benannt** – `aux_links` in `_config.yml` heissen jetzt `🇬🇧 English resources` / `🇩🇪 Deutsche Ressourcen`; oben rechts führt der Wechsel immer zu den Ressourcenlisten, nicht zur Anleitung
- [x] **Seitentitel und Inhaltsverzeichnisse eindeutig benannt** – Sidebar `Resources (EN)`, `Ressourcen (DE)`, `Anleitung (DE)`; Contents/Inhalt-Listen in beiden READMEs mit eindeutigen Zielen und Beschreibungen

## Suchmaschinen & KI-Crawler (SEO)

- [x] **`url:` in `_config.yml`** – gesetzt auf `https://awesome-long-covid-mecfs.github.io`; `canonical`, `og:url` und JSON-LD sind damit absolute URLs. `baseurl` bleibt unverändert.
- [x] **`jekyll-sitemap` aktivieren** – unter `plugins:` in `_config.yml` ergänzt (von GitHub Pages unterstützt, Version 1.4.0); `/awesome-long-covid-mecfs/sitemap.xml` wird beim Build erzeugt.
- [ ] **`robots.txt` mit expliziten Allow-Regeln** – gehört in die Root des User-Site-Repos `awesome-long-covid-mecfs.github.io` (Root-Domain), optional zusätzlich im Projekt-Repo unter `/awesome-long-covid-mecfs/robots.txt`. Sichtbarkeit: `Googlebot`, `bingbot`, `Applebot`, `OAI-SearchBot`, `ChatGPT-User`, `Claude-SearchBot`, `Claude-User`, `PerplexityBot`, `Perplexity-User`. Training (bewusste Einwilligung): `GPTBot`, `ClaudeBot`, `Google-Extended`, `Applebot-Extended`, `CCBot`, `meta-externalagent`. Default `User-agent: * / Allow: /`. Die `Sitemap:`-Zeile erst, wenn `sitemap.xml` existiert. User-Fetcher folgen robots.txt teils nicht; ein Allow garantiert keine Aufnahme in KI-Antworten.
- [x] **`locale: de_DE` in `README-de.md` und `resources-de.md`** – im Frontmatter ergänzt; die deutschen Seiten sendeten vorher `<html lang="en-US">` und `og:locale=en_US`.
- [x] **Seitenspezifische `description`** für `resources-en.md` und `resources-de.md` – ergänzt; beide Seiten haben jetzt einen eigenen, sprachpassenden Text.
- [x] **Live-URL in beiden READMEs** – `https://awesome-long-covid-mecfs.github.io/awesome-long-covid-mecfs/` (Kurzlink `https://awesome-long-covid-mecfs.github.io/`) in `README.md` und `README-de.md` ergänzt.
- [x] **GitHub-Feld `homepage` gesetzt** – `https://awesome-long-covid-mecfs.github.io/awesome-long-covid-mecfs/`; per `gh repo view` verifiziert.
- [ ] **Search Console / Bing Webmaster Tools** – Verifizierung durch den User, `webmaster_verifications` in `_config.yml`, danach Sitemap einreichen.
- [ ] **Später optional:** `hreflang`-Tags zwischen EN/DE via Theme-Override `head_custom.html`; `llms.txt` als Hinweisdatei (kein Rankingfaktor).
- [x] **Monatlicher Link-Check existiert bereits** – `link-check.yml` läuft am 1. um 06:00 UTC; keine Änderung nötig.

## Verbesserungsideen (vom User ausgewählt)

- [x] Icons/Symbole **zusätzlich** zum Text-Marker, nicht statt dessen (z. B. 📄 Studie, 🏛️ Behörde, 🤝 Selbsthilfe, ⚠️ veraltet, 💰 Commercial) – Legende in `README.md` entsprechend ergänzt, barrierefrei
- [x] Quellentyp präziser benennen **statt Sterne-/Gut-schlecht-Bewertung**: `[Systematische Übersicht]`, `[Studie]`, `[Leitlinie]`, `[Behörde]`, `[Selbsthilfe]`, `[Erfahrungsbericht]` – auch im Issue-Formular und in `AGENTS.md`
- [x] Warn-Kästen für heikle oder veraltete Quellen – Regel in `AGENTS.md`; nur bei `[veraltet]` oder begründeten Bedenken, nicht bei Preprint/Commercial
- [x] Sprachleiste oben in jeder Sprachdatei (🇬🇧 English | 🇩🇪 Deutsch)
- [x] Eigener Abschnitt „Was wir nicht aufnehmen" in `README.md` (englisch) und `README-de.md` (deutsch) sowie als Hinweis im Issue-Formular

## Weitere Ideen (vorerst zurückgestellt)

- [ ] Hinweis bei Einträgen, deren letzte Prüfung älter als 12 Monate ist
- [ ] `🆕 [neu]`-Marker für die ersten 30 Tage
- [ ] Filter/Tag-Seiten, Statistik, Druckansicht/PDF – erst bei grösserer Liste
- [ ] **Einfach-Satz in Alltagssprache über der langen Einleitung** in `README.md` und `README-de.md` – z. B. „Du suchst etwas zu Long COVID oder ME/CFS? Hier findest du geprüfte Links – auf Englisch und Deutsch." Die ausführliche SEO-Einleitung bleibt darunter.
- [ ] **Drei-Schritte-Klickstrecke unter den Buttons** (beide READMEs) – „1. Sprache wählen · 2. Thema anklicken · 3. Quelle lesen – wir bewerten nicht, wir verlinken nur."
- [x] **Themenliste direkt in den READMEs** – automatisch aus einer Quelle geht das nicht: GitHub rendert READMEs ohne Jekyll/Liquid, `include`-Tags und `site.pages`-Variablen würden als Klartext erscheinen. Umgesetzt mit normalen Markdown-Links (z. B. `resources-de.md#diagnostik`), die auf GitHub und auf der Website funktionieren. Verlinkt sind nur gefüllte Kategorien (DE 4/9, EN 3/9) plus „Alle Themen"; ein HTML-Kommentar weist auf die Sync-Pflicht bei neuen Kategorien hin.
- [x] **Lange Abschnitte einklappen** mit nativem `<details markdown="block">` in beiden READMEs – „Was wir nicht aufnehmen", „Contributing"/„Mitmachen" und „Licence"/„Lizenz". Abweichung vom Vorschlag: drei einzelne Aufklapper statt eines gemeinsamen, damit die geschützte „Legende" an ihrer Stelle sichtbar bleibt; die H2-Überschriften bleiben aussen (Anker und TOC erhalten). Kein JavaScript, GitHub-kompatibel, per Tastatur und Screenreader bedienbar; „Important", „Legende" und die Sprachleiste bleiben unangetastet.
- [ ] **Lesbarkeit auf der Website erhöhen** – `_sass/custom/setup.scss` mit `$font-size-4: 1rem;`, `$font-size-5: 1.125rem;` und `$nav-width: 18rem;` (Fliesstext heute 14 px, Sidebar schmal), dazu `remote_theme` in `_config.yml` auf `just-the-docs/just-the-docs@v0.12.0` pinnern. Wirkt nur auf der Website, nicht in der GitHub-README-Ansicht; die Sass-Datei muss bei Theme-Updates gegengeprüft werden.

---

Anmerkung: Dieses Repo ist jetzt die Arbeitskopie. Die frühere Kopie im Monorepo `CodeSpace` bleibt nur als Archiv liegen und wird nicht weitergepflegt.
