---
title: ToDo
layout: default
nav_order: 7
nav_exclude: true
sitemap: false
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
- [x] Erste Ressourcen gesammelt – aktuell 80 geprüfte Links in `links-en.md` und 134 in `links-de.md`
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

- [ ] Inhalte: 80 EN- / 134 DE-Einträge – weitere Ressourcen sammeln ist der nächste grosse Schritt
- [x] Eigenes GitHub-Repo angelegt: Name genau `awesome-long-covid-mecfs`, ohne README initialisiert
- [x] Ordnerinhalt in das neue Repo kopiert und gepusht
- [x] GitHub Pages aktiviert (Branch `main`, Pfad `/`) – per GitHub-API gesetzt
- [x] Website getestet – Startseite, EN, DE und README-de liefern HTTP 200; `baseurl` war richtig gesetzt

## Basisstruktur reviewen (Schritt für Schritt mit dem User)

- [x] Zusätzliche Melde-Möglichkeit per E-Mail für Personen ohne GitHub-Konto: Adresse `awesome-long-covid-mecfs[at]sags-per-mail.de` in `README.md` und `CONTRIBUTING.md` ergänzt. Gewählte Variante: `[at]` statt `@` (einfach, barrierefrei, schützt vor einfachen Spam-Crawlern). Auch dieser TODO-Eintrag ist entschärft. Bei Bedarf auf eine stärkere Variante wechseln (Bild oder Kontaktformular).
- [x] `AGENTS.md` reviewt – KI prüft Links (Erreichbarkeit, Duplikate, Quellenart, Marker), schreibt Vorschläge und darf nach Freigabe committen/pushen. Kein Stand-Datum.
- [ ] `AGENTS.md`: Wenn alles stimmt, **auf Englisch umstellen** – noch offen.
- [x] **Weitere Dokumente auf Englisch** – umgesetzt in `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `.github/PULL_REQUEST_TEMPLATE.md` und `footer_content` (`_config.yml`). `MARKERS.md` bleibt bewusst zweisprachig, `README-de.md`/`links-de.md` bleiben deutsch; `AGENTS.md` hat einen eigenen offenen Punkt.
- [x] **`CONTRIBUTING.md` als drei Optionen** – E-Mail ohne GitHub, GitHub-Issue mit Konto, Pull Request. Neue deutsche Fassung `CONTRIBUTING-de.md` mit gleicher Struktur und Sprachleiste; `README-de.md` verweist auf die deutsche Fassung, die englische auf beide. Beide Dateien haben `nav_exclude: true` und bleiben aus der Seitenleiste.
- [x] Kategorien durch den User geprüft – vorerst unverändert; weitere Kategorien bei Bedarf (Marker-Kombinationen im Auge behalten).

## Mehrsprachigkeit (vom User vorgegeben)

- [x] Primärsprache ist **Englisch**; Deutsch und später weitere Sprachen müssen schnell erreichbar sein – Haupt-`README.md` ist englisch
- [x] Sprachwechsel oben in der README und in jeder Sprachdatei über Links **mit Länderflaggen-Emojis** (🇬🇧 English, 🇩🇪 Deutsch, …)
- [x] Kurzer Verweis in der Haupt-README: „Deutsche Anleitung hier" → `README-de.md` (neue deutsche README)
- [x] Benennung neuer Sprachdateien festlegen (`links-<lang>.md`) und regeln, wer sie anlegt – steht in `AGENTS.md`
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
  - **A (empfohlen):** automatischer, aufklappbarer Inhaltsverzeichnis-Block oben in `links-en.md` und `links-de.md` via `<details>` + `{:toc}`. Keine Strukturänderung, SSOT und alle URLs bleiben, das Verzeichnis pflegt sich selbst. Nachteil: nicht in der linken Seitenleiste.
  - **B:** `resources-de/` und `resources-en/` als Ordner mit `index.md` plus 9 Kinderseiten (`parent:`), echte aufklappbare Unterpunkte links. Nachteile: URL-Wechsel (`/resources-de.html` → `/resources-de/`, mit `permalink` abfangbar), Anker-Links werden seitenübergreifend, Sprachleiste und Disclaimer sind 10× zu pflegen, die `AGENTS.md`-Regel „eine Datei pro Sprache, Kategorien als H2" muss geändert werden, und viele Kategorien haben erst 0–1 Einträge.
  - Vergleich anderer Listen: free-programming-books bleibt bei einer Datei pro Sprache plus Anker (keine Kategorie-Navigation); natnew/Awesome-Prompt-Engineering nutzt ~15 flache Kategoriedateien (lange flache Nav); die just-the-docs-Doku selbst nutzt Ordner plus Kinderseiten; awesome-python baut eine eigene Website (zu viel Aufwand für uns).
- [x] **Inhaltsverzeichnis am Anfang jeder Sprachdatei** mit Links zu allen Kategorien (manuell, funktioniert auf GitHub und auf der Website)

## Website-Navigation & Erreichbarkeit

- [x] **Root-URL `https://awesome-long-covid-mecfs.github.io/`** – neues User-Site-Repo `awesome-long-covid-mecfs.github.io` mit statischem `index.html`-Redirect auf `/awesome-long-covid-mecfs/`; Pages auf `main` / `(root)` aktiv. Das Projekt-Repo bleibt unverändert, `baseurl` und `aux_links` bleiben wie sie sind.
- [x] **Meta-Seiten mit Frontmatter versehen** – `AGENTS.md`, `MARKERS.md`, `TODO.md`, `CONTRIBUTING.md` und `CODE_OF_CONDUCT.md` (`title`, `nav_order`); ursprünglich in der Seitenleiste, jetzt per `nav_exclude: true` ausgeblendet (siehe nächster Punkt)
- [x] **Meta-Seiten aus der Seitenleiste ausgeblendet** – `nav_exclude: true` in den fünf Dateien; sie bleiben über Links erreichbar (README/Ressourcen → `AGENTS.md`, `MARKERS.md`, `CONTRIBUTING.md`; `CONTRIBUTING.md` → `CODE_OF_CONDUCT.md`; README → `TODO.md`). Nur verlinkt, nicht mehr in der Navigation.
- [x] **`RESEARCH.md` entfernt** – die Vorlagenanalyse war nur für die Startphase; der einzige Verweis stand in dieser Datei
- [x] **Kaputte Issue-Links in den READMEs repariert** – `/home/max/CodeSpaces://github.com/...` → `https://github.com/...` in `README.md` und `README-de.md`; der Rest des Repos wurde auf ähnliche Pfad-Verweise geprüft (keine weiteren Funde)
- [ ] **`<html lang>` auf den deutschen Seiten korrigieren** – `locale: de_DE` im Frontmatter setzt nur `og:locale`; just-the-docs liest für `<html lang>` ausschliesslich `site.lang`. Vorschlag: lokale `_layouts/default.html` mit `page.lang | default: site.lang | default: 'en-US'` und `lang: de` in `links-de.md`. Nachteil: die kopierte Layout-Datei bekommt keine automatischen Theme-Updates. Vom User vorerst zurückgestellt.
- [x] **Direkt-Links zu den Inhalten auf der Startseite** – zwei Buttons direkt nach dem Disclaimer in `README.md` und `README-de.md` (`.btn .btn-blue` mit `.mr-2` als Abstand), damit die Ressourcenlisten ohne Scrollen erreichbar sind
- [x] **Obere Sprachleiste eindeutig benannt** – `aux_links` in `_config.yml` heissen jetzt `🇬🇧 English resources` / `🇩🇪 Deutsche Ressourcen`; oben rechts führt der Wechsel immer zu den Ressourcenlisten, nicht zur Anleitung
- [x] **Seitentitel und Einstieg eindeutig benannt** – Sidebar `🇬🇧 Links (EN)`, `🇩🇪 Links (DE)` (deutsche Anleitung ausgeblendet); die READMEs haben statt Sprachleiste/Contents/Themenliste nur noch die Tabelle mit dem Hinweis darüber
- [x] **Bezeichnung „Links" statt „Ressourcen"** – Navigation und Tabelle in `README.md`, `README-en.md`, `README-de.md` sowie Seitentitel der `links-*.md` mit Länderflaggen. H1, Site-Titel und Meta-Descriptions behalten „Resources" als Suchbegriff. Regel in `AGENTS.md` §6: README-Änderungen immer in allen Sprachfassungen mitmachen.
- [x] **ℹ️-Hinweis präzisiert** – Hinweis auf unterschiedliche Quellen und regionale Angebote, ergänzt um das Beispiel, dass viele wissenschaftliche Studien auf Englisch erscheinen. In allen drei Readmes synchron (DE/EN) umgesetzt.
- [x] **Link-Seiten angepasst** – Titel und Warnhinweis mit ⚠️ stehen jetzt ganz oben in `links-en.md`/`links-de.md`; danach der Hinweis zum Link-Einreichen, dann das Inhaltsverzeichnis und darunter die Sprachleiste mit Kurzhinweis; Satz zu Markern/Aufnahmekriterien entfernt; deutsche H1 heißt jetzt „Deutsche Ressourcen". Englischer Tabellenkopf in `README.md`/`README-en.md` auf „Guide" korrigiert.
- [x] **README-Kopf verschlankt** – Sprachleiste, Contents/Inhalt-Liste und Themenliste aus allen drei Readmes entfernt; der ℹ️-Hinweis steht jetzt über der Tabelle. Zeilen: „🇬🇧 English"/„🇩🇪 Deutsch", Spalten: „Anleitung"/„Links". Linktexte „Anleitung" und „Guide".

## Suchmaschinen & KI-Crawler (SEO)

- [x] **`url:` in `_config.yml`** – gesetzt auf `https://awesome-long-covid-mecfs.github.io`; `canonical`, `og:url` und JSON-LD sind damit absolute URLs. `baseurl` bleibt unverändert.
- [x] **`jekyll-sitemap` aktivieren** – unter `plugins:` in `_config.yml` ergänzt (von GitHub Pages unterstützt, Version 1.4.0); `/awesome-long-covid-mecfs/sitemap.xml` wird beim Build erzeugt.
- [ ] **`robots.txt` mit expliziten Allow-Regeln** – gehört in die Root des User-Site-Repos `awesome-long-covid-mecfs.github.io` (Root-Domain), optional zusätzlich im Projekt-Repo unter `/awesome-long-covid-mecfs/robots.txt`. Sichtbarkeit: `Googlebot`, `bingbot`, `Applebot`, `OAI-SearchBot`, `ChatGPT-User`, `Claude-SearchBot`, `Claude-User`, `PerplexityBot`, `Perplexity-User`. Training (bewusste Einwilligung): `GPTBot`, `ClaudeBot`, `Google-Extended`, `Applebot-Extended`, `CCBot`, `meta-externalagent`. Default `User-agent: * / Allow: /`. Die `Sitemap:`-Zeile erst, wenn `sitemap.xml` existiert. User-Fetcher folgen robots.txt teils nicht; ein Allow garantiert keine Aufnahme in KI-Antworten.
- [x] **`locale: de_DE` in `README-de.md` und `links-de.md`** – im Frontmatter ergänzt; die deutschen Seiten sendeten vorher `<html lang="en-US">` und `og:locale=en_US`.
- [x] **Seitenspezifische `description`** für `links-en.md` und `links-de.md` – ergänzt; beide Seiten haben jetzt einen eigenen, sprachpassenden Text.
- [x] **Live-URL in beiden READMEs** – `https://awesome-long-covid-mecfs.github.io/awesome-long-covid-mecfs/` (Kurzlink `https://awesome-long-covid-mecfs.github.io/`) in `README.md` und `README-de.md` ergänzt.
- [x] **GitHub-Feld `homepage` gesetzt** – `https://awesome-long-covid-mecfs.github.io/awesome-long-covid-mecfs/`; per `gh repo view` verifiziert.
- [ ] **Search Console / Bing Webmaster Tools** – Verifizierung durch den User, `webmaster_verifications` in `_config.yml`, danach Sitemap einreichen.
- [x] **`hreflang`-Tags zwischen EN/DE** – lokales `_includes/head_custom.html` (vom Theme-Hook in `head.html` eingebunden) setzt die drei alternaten Links auf `links-en.md` und `links-de.md`; eine `page.path`-Bedingung hält Meta-Seiten frei.
- [ ] **Später optional:** `llms.txt` als Hinweisdatei (kein Rankingfaktor).
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
- [x] **Einfach-Satz in Alltagssprache** – erledigt durch den neuen Einstieg auf den Link-Seiten; die sprachbezogenen Readmes gibt es nicht mehr.
- [ ] **Drei-Schritte-Klickstrecke unter den Buttons** (beide READMEs) – „1. Sprache wählen · 2. Thema anklicken · 3. Quelle lesen – wir bewerten nicht, wir verlinken nur."
- [x] **Kurzer Hinweis zum Link-Hinzufügen** – steht nach dem Einleitungsabsatz „Für Betroffene …" (User-Wunsch), nicht mehr direkt unter der H1; Issue-Vorlage „Suggest a link", E-Mail und Link auf `CONTRIBUTING.md`. Die frühere Sprachleiste in den Readmes wurde durch die Tabelle ersetzt.
- [x] **Dateien umbenannt** – `resources-en.md` → `links-en.md`, `resources-de.md` → `links-de.md`, inklusive aller Verweise in READMEs, `AGENTS.md`, `CONTRIBUTING.md` und diesem ToDo. Neue URLs `/links-en.html` und `/links-de.html`; die alten URLs werden nicht weitergeleitet (User: keine Links in Verwendung).
- [x] **README-Struktur und Einstieg** – `README-en.md` ist jetzt Website-Startseite (`permalink: /`), `README.md` bleibt die GitHub-README ohne Frontmatter und wird per `exclude` nicht gebaut. Buttons und Live-Link entfernt; stattdessen eine 2×2-Tabelle „Anleitung/Ressourcen × Deutsch/Englisch" mit Hinweis auf sprach- und regionsspezifische Quellen. Warnung gekürzt und mit ⚠️ versehen. Verweise in `links-*.md`, `MARKERS.md` und `AGENTS.md` auf `README-en.md` umgestellt.
- [x] **Themenliste direkt in den READMEs** – automatisch aus einer Quelle geht das nicht: GitHub rendert READMEs ohne Jekyll/Liquid, `include`-Tags und `site.pages`-Variablen würden als Klartext erscheinen. War als normale Markdown-Liste umgesetzt und auf Wunsch des Users wieder aus den Readmes entfernt; die Kategorienlisten stehen weiterhin oben in `links-*.md`.
- [x] **Lange Abschnitte einklappen** mit nativem `<details markdown="block">` in beiden READMEs – „Was wir nicht aufnehmen", „Contributing"/„Mitmachen" und „Licence"/„Lizenz". Abweichung vom Vorschlag: drei einzelne Aufklapper statt eines gemeinsamen, damit die geschützte „Legende" an ihrer Stelle sichtbar bleibt; die H2-Überschriften bleiben aussen (Anker und TOC erhalten). Kein JavaScript, GitHub-kompatibel, per Tastatur und Screenreader bedienbar; „Important" und „Legende" bleiben unangetastet; die Sprachleiste wurde später aus den Readmes entfernt.
- [x] **Lesbarkeit auf der Website erhöhen** – vom User am 25.11.2026 als erledigt bestätigt; Live-CSS liefert desktop `html{font-size:1rem}`, mobil `.875rem`. Die ursprünglich genannte Datei `_sass/custom/setup.scss` existiert nicht (nur `_sass/custom/custom.scss`). Wirkt nur auf der Website, nicht in der GitHub-README-Ansicht.
- [x] **IndexNow eingerichtet** – öffentlicher Key `36116e1a-ab38-4110-b67a-2cae8b6b3e42.txt` im Repo; `.github/workflows/indexnow.yml` meldet bei Push auf `main` (nach gewartetem Pages-Build) und manuell die zwei Seiten an Bing/Yandex/Seznam/Naver/Yep; `workflow_run` funktioniert für den Pages-Workflow nicht. Google ist nicht Teil des Protokolls und braucht weiterhin Search Console. Bei Repo-Umzug Key und `keyLocation` mitziehen.
- [x] **SEO-Metadaten aktualisiert** – `description` beider Link-Seiten entspricht jetzt dem neuen Einstieg (inkl. SIBO, Dysautonomie, PEM); sechs Meta-Seiten haben `sitemap: false` und erscheinen nicht mehr in der Sitemap.
- [x] **Google Search Console: Property angelegt** – URL-Präfix `https://awesome-long-covid-mecfs.github.io/awesome-long-covid-mecfs/`. Verifizierung per HTML-Datei `google2da9e7ad2ffa83cd.html` (live HTTP 200), Sitemap eingereicht und Indexierung für `/` und `/links-de.html` angefordert. Die Google Indexing API ist für diese Seite nicht nutzbar (nur JobPosting/BroadcastEvent).
- [ ] **GSC-Sitemap nachprüfen (ca. 26.11.2026)** – Der Sitemap-Report zeigte zeitweise „Sitemap could not be read", ohne Fehlerursache; der Live-Test der Sitemap-URL war erfolgreich, und der Abruf mit Googlebot-User-Agent liefert 200/`application/xml` mit gültigem XML und absoluten URLs. Nach 2–3 Tagen Status der Sitemap erneut prüfen; falls weiter fehlerhaft, den genauen Grund aus GSC ergänzen. Kein Code-Change nötig, solange der Live-Test grün bleibt.
- [ ] **Bing Webmaster Tools: Site anlegen** – Import aus der Search Console nutzen, gleiche Sitemap einreichen. Davon profitiert auch DuckDuckGo.
- [ ] **Verifizierungsdateien ablegen** – sobald Google/Bing die HTML-Dateien liefern: Datei für den Projektpfad in diesem Repo, Datei für die Root-Domain im Repo `awesome-long-covid-mecfs.github.io`; danach Build und HTTP 200 prüfen.
- [ ] **Sichtbarkeit nach 1–4 Wochen prüfen** – Suche `site:awesome-long-covid-mecfs.github.io/awesome-long-covid-mecfs` in Google. Falls weiterhin nichts auftaucht: ein paar echte Verweise aus relevanten Selbsthilfe-/Fachcommunities oder bestehenden Sammlungen setzen (kein Spam).
- [x] **Footer-Link auf GitHub** – `footer_content` in `_config.yml` um „Source on GitHub" mit dem Repo-Link ergänzt; stärkt Suchanfragen wie „awesome long covid mecfs github" und ist für Leser nützlich.
- [x] **Einstieg der Link-Seiten nachformatiert** – die Begriffe Long COVID / Post-COVID, ME/CFS und die Zielgruppe sind wieder fett; die Sprachleiste steht direkt unter dem ℹ️-Hinweis und vor dem Inhaltsverzeichnis (beide Sprachen).
- [x] **Sprachbezogene Readmes entfernt** – `README-de.md` und `README-en.md` gelöscht; ihr Einstieg steht jetzt übersetzt auf `links-en.md`/`links-de.md`, `links-en.md` ist die Website-Startseite (`permalink: /`), und die Tabelle in `README.md` hat nur noch die Spalte „Links". Alle Verweise in `AGENTS.md`, `CONTRIBUTING*.md`, `MARKERS.md`, `_config.yml` und diesem ToDo sind angepasst.
- [x] **Seitenleisten-Titel umgebrochen** – lokale `_includes/title.html` schreibt „Awesome" in die erste Zeile, den Rest darunter; Schrift und Padding im CSS angepasst, damit die Zeilen in die Kopfzeile passen.
- [x] **Seitenleisten-Layout korrigiert** – `_sass/custom/custom.scss` verkleinert den Site-Titel und entfernt den ungenutzten Platz links der Seitenleiste (`.side-bar` auf 16.5rem, innere Elemente auf 100%). Die Datei muss bei Theme-Updates gegengeprüft werden.

## Vorbereitung Community-Vorschlag (vom User angeregt, 25.11.2026)

**Vom User vorgegeben**

- [ ] Forschung/Studien weiter unterteilen und aufräumen (Unterkategorien prüfen, Einträge verschieben)
- [ ] Restliche offene ToDos in dieser Datei abarbeiten
- [ ] Nicht verwendete Kategorien entfernen oder in die englische Liste verweisen
- [ ] Prüfen, welche Seiten und Gruppen sich für eine E-Mail-Ankündigung eignen (Themenpassung, Regeln, Kontaktweg)
- [ ] Vorlage für die Ankündigungs-E-Mail erstellen (deutsch und englisch)
- [ ] ToDo-Liste aktualisieren und Bearbeitungsreste bereinigen
- [ ] Repo aufräumen (verwaiste Dateien und Konfigurationsreste prüfen)

**Befunde aus der Inhaltsprüfung (25.11.2026, Stand nach Commit `dcb38ea`)**

- [x] ToDo-Inhaltsstand korrigieren: **80 EN- / 134 DE-Einträge** statt „erste 10 Links" (Zeilen 30 und 50 dieser Datei)
- [ ] `## Research & Studies` (EN, 20 Einträge) und `## Studien & Forschung` (DE, 9) unterteilen; neue H3 brauchen User-Abstimmung und müssen in **beide** Inhaltsverzeichnisse
- [ ] Leere Kategorien auflösen: EN 6 (`Guidelines`, `MCS`, `Facebook`, `Instagram`, `Legal & Benefits`, `Professional Literature`), DE 3 (`SIBO`, `Instagram`, `Open-Source-Projekte / Code`)
- [x] Veralteten DE-Hinweis bei SIBO korrigieren: verweist jetzt auf die vorhandenen englischen SIBO-Einträge statt auf die leere Leitlinien-Sektion
- [x] **Marker-Set weiter bereinigen** – mehr Übersicht, nur wichtige Marker: fehlende 📋 bei den drei DE-Leitlinien, 🤝 am WhatsApp-Kanal, abgehängte Marker wieder am Eintrag; 💬 bei Erfahrungsberichten bleibt offen
- [ ] Falsche Marker korrigieren: 📊 `[Systematic review]` an der DE-Forschungsförderung und 📖 `[Professional literature]` an der DG ME/CFS (passender 🤝/📣)
- [x] Widersprüchliche Marker korrigieren: 🆓 [Partly free] bei blue-ME (14 Tage kostenlos) und Elara Health (Basisversion kostenlos) ergänzt
- [ ] Zwei Warn-Kästen prüfen: ⚠️-Sichtbarkeit auch am Eintrag selbst sicherstellen — aber **keinen** `[Outdated]`-Marker vergeben, solange die Quelle nicht veraltet ist (AGENTS.md §5 erlaubt Warn-Kästen auch bei begründeten Bedenken)
- [x] Ungenutzte Marker klären: 🎧 `[Podcast]` auf den zwei DE-Podcasts ergänzt; `[Preprint]` nur bei Bedarf behalten, `[Outdated]` **behalten** (AGENTS.md §5 regelt dafür die Warn-Kästen)
- [ ] Umgang mit DocCheck-Login als Zugangshürde festlegen (bisher kein Marker dafür)
- [x] **Einträge mit fragilen Zielen geprüft (DE):** 8 URLs per HTTP alle 200 (YouTube, ARD, ZDF, 3sat, Charité-PDF, Freiburg-PDF, linktr.ee, WhatsApp). Mediathek-/Geo-Sperren, YouTube-Verfügbarkeit und WhatsApp-Login-Wand sind damit nicht geklärt; Einträge unverändert
- [x] **Einträge mit fragilen Zielen geprüft (EN):** `oiresource.com/cfsscale.htm` liefert 200; Lizenz-/Kurskosten-Einträge ohne Marker-Änderung belassen (braucht Rücksprache)
- [x] Formatierung: zwei fehlende Leerzeilen zwischen Einträgen in `links-de.md` ergänzt (Schlusspunkte waren überall vorhanden)
- [ ] DE-Einstieg: unübersetztes Label „Suggest a link" anpassen
- [ ] Doppelten Guava-Link klären: gleiche URL in beiden Sprachdateien, DE-Beschreibung nennt zwar 20+ Sprachen, eine eigene DE-Fassung ist aber nicht verlinkt
- [ ] **Entscheidung: Verteilung EN/DE bleibt bewusst asymmetrisch** – für die vielen DE-Themen (Recht, Berichterstattung) sind keine guten englischen Quellen bekannt; keine Angleichung anstreben
- [ ] **Inhaltsverzeichnisse aufräumen** (EN 30 / DE 44 Zeilen): leere Einträge entfernen; bei leeren **DE**-Kategorien auf die englische Fassung verweisen — **nicht umgekehrt** (EN-Kategorien nicht auf DE umleiten)
- [ ] Sitemap-Eintrag der Google-Verifizierungsdatei `google2da9e7ad2ffa83cd.html` entfernen (live bestätigt)
- [ ] Leeres GitHub-Wiki deaktivieren oder füllen; Projects ebenfalls prüfen
- [ ] **Info, keine Blockade für die Veröffentlichung:** der `sindresorhus/awesome`-Index ist derzeit gesperrt (PRs pausiert, 30-Tage-Regel ab 22.11., 4 fremde PRs zu reviewen). Fehlende Voraussetzungen für später: GitHub-Topic **`awesome`** neben `awesome-list`, **Awesome-Badge** in der README, `Contents` als erste Sektion, keine `Licence`-Sektion in der README, `awesome-lint` laufen lassen. Liste kann unabhängig davon veröffentlicht und in Communities vorgeschlagen werden
- [ ] **Community-Info per E-Mail – Zielgruppen mit Kontaktweg:** DG ME/CFS (`info@dg.mecfs.de`, Kontaktformular deaktiviert); Long COVID Deutschland (Kontaktformular, bittet ausdrücklich um keine individuellen Diagnose-/Therapiefragen → sachlicher Ressourcen-Hinweis); Fatigatio e.V. (Kontaktformular/Presse); Fasynation (`info (at) fasynation.de`, ehrenamtliches Portal, Podcast, Fasy.Mail); CrunchME (Datenbank/Advocacy, Kontakt über die Website); ME/CFS-Wiki und weitere Betroffenen-Portale, Wikis und Blogs; #MEAction, Long COVID Support, Patient-Led Research Collaborative. WhatsApp- und Facebook-Gruppen nur über die Admins, nicht massenhaft anschreiben — Regeln zu Eigenwerbung vorher prüfen
- [ ] **E-Mail-Vorlage erstellen** (DE + EN): kurzer sachlicher Hinweis auf die Liste, keine medizinische Bewertung, Bitte um Feedback statt um Weiterleitung

## Optional (nach der Veröffentlichung)

- [ ] **Manuelle Linkprüfung vor einer grösseren Ankündigung** — `.github/workflows/link-check.yml` nutzt bewusst `fail: false` (seit Initial-Import `d9d01ce`, Kommentar: viele Gesundheitsseiten blockieren Bot-Prüfer). Der Check meldet Probleme, bricht aber nichts ab. Keine Änderung am Workflow geplant; bei Bedarf stichprobenartig von Hand prüfen

---

Anmerkung: Dieses Repo ist jetzt die Arbeitskopie. Die frühere Kopie im Monorepo `CodeSpace` bleibt nur als Archiv liegen und wird nicht weitergepflegt.
