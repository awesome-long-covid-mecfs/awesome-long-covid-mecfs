# Vorlagen-Analyse: Awesome-Listen als Vorbild

Stand: 2026-11-22. Quelle: GitHub-REST-Metadaten, `raw.githubusercontent.com`, Webrecherche.
Zweck: Bausteine fuer unsere Liste `awesome-long-covid-mecfs` sammeln, bevor wir Inhalte anlegen.
Alle Aussagen zu `AGENTS.md` sind gegen echte Raw-URLs geprueft (404 = nicht vorhanden).

## 1. Uebersicht

| Repo | Sterne | AGENTS.md | Struktur | Website / Pages | Warum interessant |
| --- | --- | --- | --- | --- | --- |
| [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | ~540k | nein (explizit anti-KI) | 1 readme + Side-Docs | keine | Kanon der Gattung, `awesome-lint`, CC0 |
| [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | ~402k | nein | ~50 Sprachdateien + Index | Jekyll (`remote_theme`) | **beste Mehrsprachigkeit** |
| [vinta/awesome-python](https://github.com/vinta/awesome-python) | ~336k | **ja** + `CLAUDE.md` | README + `website/` | Generator → awesome-python.com | **Eintragsqualitaet + KI-Regeln** |
| [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | ~339k | nein | 3 Repos, YAML als Quelle | Sphinx/hecat | **Anti-Vorbild** fuer Single-Source-of-Truth |
| [public-apis/public-apis](https://github.com/public-apis/public-apis) | ~500k | nein | 1 README | keine | Tabellenfelder, strenge Validierung, taeglicher Linkcheck |
| [kakoni/awesome-healthcare](https://github.com/kakoni/awesome-healthcare) | ~4.1k | nein | 1 README | keine | **naechster Health-Verwandter**, aber ohne Disclaimer |
| [avelino/awesome-go](https://github.com/avelino/awesome-go) | ~195k | **ja** + Copilot-Stub | README → Generator | Netlify | KI-Regeln, `out/` nicht committen |
| [rust-unofficial/awesome-rust](https://github.com/rust-unofficial/awesome-rust) | ~60k | nein | 1 README + Checker | keine | Lint-/Workflow-Setup |
| [natnew/Awesome-Prompt-Engineering](https://github.com/natnew/Awesome-Prompt-Engineering) | ~116 | **ja** + `CLAUDE.md` + Copilot | Index + Topic-Seiten | Jekyll `just-the-docs` | **beste KI-Pflege-Regeln** |
| [natnew/awesome-rl-for-agents](https://github.com/natnew/awesome-rl-for-agents) | ~4 | **ja** + `CLAUDE.md` | README + generiertes JSON | keine | **schlankestes KI-Protokoll**, Issue-Templates |
| [github/awesome-copilot](https://github.com/github/awesome-copilot) | ~41k | **ja** (354 Zeilen) | viele Ordner + `website/` | GitHub Pages | Warnung: ~60 Workflows, zu schwer |
| [shuaibiyy/awesome-terraform](https://github.com/shuaibiyy/awesome-terraform) | - | nein | 1 README | keine | Emoji-Legende (💀 veraltet, 💲 kommerziell) |

Nur 5 von 11 geprueften Listen haben KI-Anweisungen. Wir muessen unsere eigenen schreiben.

## 2. Regeln zum Hinzufuegen von Links

- **sindresorhus/awesome** – `pull_request_template.md`: kurze, objektive Beschreibung, Grossbuchstabe am Anfang, Punkt am Ende, Eintrag **unten** in der passenden Kategorie, `awesome-lint` ausfuehren, Liste >= 30 Tage alt, Abschnitt heisst `Contents` (nicht "Table of Contents"), kein Hard-Wrapping, keine CI-Badges. Achtung: *"Fully AI-generated pull requests are not accepted"*.
- **EbookFoundation/free-programming-books** – `docs/CONTRIBUTING.md`: *"You don't have to know Git … please open an Issue"*; alphabetisch einfuegen; CI prueft Alphabetisierung. Blacklist: Google Drive, Dropbox, Mega, Scribd, Issuu, URL-Shortener; HTTPS und Autorenquellen bevorzugt.
- **vinta/awesome-python** – `CONTRIBUTING.md`: *"a shortlist, not a catalog"*; max. 3 offensichtliche + 2 Herausforderer pro Use Case, hartes Maximum 5; One-in-one-out; Repo aktiv <= 12 Monate; `Aim for a rendered line of 100 characters or fewer`; explizite `Automatic Rejection`-Liste.
- **kakoni/awesome-healthcare** – `CONTRIBUTING.md`: ein PR pro Vorschlag, `[item](link) - description.`, ein Link pro Item, englisch, `(Commercial Software)` markieren, keine Bezahlung/Registrierung (ausser Newsletter).
- **public-apis** – `CONTRIBUTING.md`: feste Tabellenspalten, Aufzaehlung erlaubter Werte, Description <= 100 Zeichen, **ein Link pro PR**, PR-Titel `Add Api-name API`.
- **natnew/awesome-rl-for-agents** – `CONTRIBUTING.md`: `- **[Title](url)** — ein Satz`, stabile URLs (arXiv `/abs/`, ACL Anthology), keine Paywall-/Affiliate-Links, Reihenfolge der Umgebung folgen.
- **avelino/awesome-go** – ein Item pro PR, richtige Kategorie + alphabetisch, Repo >= 5 Monate, Lizenz vorhanden, `go.mod`, Kategorie braucht >= 3 Items.

**Fuer uns:** "ein Eintrag pro PR", Kurzform `[Name](URL) — Beschreibung.`, alphabetisch oder bewusst kuratiert, Blacklist fuer Shortener/Paywall/Affiliate, und einen **einfachen Issue-Weg** fuer Menschen ohne Git-Kenntnisse (wichtig fuer Betroffene!).

## 3. AGENTS.md – echte KI-Regeln

### 3.1 natnew/Awesome-Prompt-Engineering (reichhaltigste Vorlage)
`https://github.com/natnew/Awesome-Prompt-Engineering/blob/main/AGENTS.md`
- *"It is content, not an application: the deliverable is high-signal Markdown published to GitHub Pages via Jekyll. README.md is the primary artefact."*
- **Trust Boundary:** *"Do not invent facts about a resource … If a claim cannot be verified, neutralise it or flag it — never assert it."*
- **Decision Matrix:** accept / maintainer edit / request changes / close / park.
- **Protected Areas:** Badges, Announcements, Contributors, Sponsoren, Lizenz, `_config.yaml`, `_layouts/`.
- *"When placement, scope, source credibility, or maintainer intent is uncertain, recommend before editing."*
- *"Maintenance is manual-first — a human reviews and merges."*
- `CLAUDE.md` verweist auf `.github/instructions/*.instructions.md`; `.github/workflows/claude.yml` laeuft **read-only**.

### 3.2 natnew/awesome-rl-for-agents (schlank)
`https://github.com/natnew/awesome-rl-for-agents/blob/main/AGENTS.md`
- *"README.md is the canonical product"*, *"Modify files only when asked"*.
- 5-Punkt-Checkliste: Scope, Quelle/Link, Einzigartigkeit, Platzierung, Formulierung.
- **Nie** `data/resources.json` oder den `<!--entry-count-->`-Marker von Hand editieren (generiert); Pruefung mit `python scripts/build_index.py --check`.
- "Protected changes" → erst fragen. Abschlussmeldung: Entscheidung, Dateien, Validierung, Unsicherheit.

### 3.3 vinta/awesome-python
`https://github.com/vinta/awesome-python/blob/master/AGENTS.md`
- *"[README.md] is the source of truth for entries … Apply CONTRIBUTING.md whenever adding, removing, or rewording an entry, direct commits included."*
- *"Training-data recollections are not evidence."*
- Checks bleiben read-only; nie installieren/ausfuehren, um eine Quelle zu pruefen.
- Ein Eintrag pro Commit; Sponsoren beeinflussen nie die Liste.
- `CLAUDE.md` besteht aus **einer Zeile**: `@AGENTS.md` – sauberes Import-Muster.

### 3.4 avelino/awesome-go
`https://github.com/avelino/awesome-go/blob/main/AGENTS.md` – *"LLM Contribution Guide"*
- CONTRIBUTING.md beachten, *"Do not drop existing content unless removal is requested and justified"*, generiertes `out/` nie committen, AGENTS.md bei Konventionsaenderung mitpflegen.
- Copilot-Datei ist nur ein Ein-Zeilen-Stub: `AGENTS.md`.

**Fuer uns:** `AGENTS.md` als kanonische KI-Datei, `CLAUDE.md` = `@AGENTS.md`, Copilot-Stub. Kernregeln: keine medizinischen Behauptungen erfinden, Quellen verifizieren, bei Unsicherheit empfehlen statt editieren, menschliche Freigabe vor Merge, generierte Artefakte nicht von Hand aendern.

## 4. Struktur – eine Datei oder mehrere?

- **Eine Datei:** sindresorhus, public-apis, awesome-healthcare, awesome-rust. Einfach, aber unuebersichtlich bei > 200 Eintraegen und schlecht fuer Sprachwechsel.
- **Mehrere Dateien, Sprache zuerst:** free-programming-books – `books/free-programming-books-<lang>.md` (~50 Sprachen), Root-README als Sprachindex, `docs/CONTRIBUTING-<lang>.md` etc. uebersetzt.
- **Index + Themen-Seiten:** natnew/Awesome-Prompt-Engineering – README als Index, `Basic_Prompting.md`, `AI_Tools.md`, `foundations/`, `patterns/` ...
- **Generiert:** awesome-go (README → `out/`), awesome-python (README → Website), awesome-selfhosted (YAML → README + HTML).

**Fuer uns:** Root-`README.md` als Einstieg/Sprachwechsel + `resources-de.md`, `resources-en.md`, ... als **Single Source of Truth**. Thematische Unterkategorien als `###` innerhalb jeder Sprachdatei (nicht extra Dateien pro Kategorie – sonst explodiert die Dateianzahl bei 9 Kategorien x N Sprachen).

## 5. GitHub Pages / schickere Ansicht bei Markdown als Quelle

| Ansatz | Repo | Wie | Bewertung |
| --- | --- | --- | --- |
| Jekyll Remote-Theme | free-programming-books | `_config.yml` mit `remote_theme: pages-themes/minimal@v0.2.0`, `jemoji`, `jekyll-relative-links` | **einfachste Pages-Variante**, kein Build-Skript |
| Jekyll `just-the-docs` | natnew/Awesome-Prompt-Engineering | `_config.yaml`, `_layouts/`, `assets/css/`, Links im README zeigen auf `.html` (generiert!), nicht `.md` | schoene Doku-Optik, aber Achtung bei内部 Links |
| Custom Generator + Pages Action | vinta/awesome-python | `Makefile`, `pyproject.toml`, `.github/workflows/deploy-website.yml`, `upload-pages-artifact@v5` + `deploy-pages@v5`, taeglich Stars/PyPI-Downloads | maechtig, aber viel Code |
| Netlify + Generator | avelino/awesome-go | `main.go`, `tmpl/`, `netlify.toml` (`publish = "out/"`), `site-deploy.yaml` | gut, aber externaler Host |
| Docsify (Idee, nicht in den Repos geprueft) | - | `index.html` + `_sidebar.md`, Markdown direkt rendert | null Build, aber weniger Kontrolle |
| Sphinx/hecat | awesome-selfhosted | YAML → Sphinx → HTML | **verwerfen** (Quelle ist YAML) |

**Empfehlung:** Jekyll Remote-Theme (minimal oder `just-the-docs`) direkt aus den Markdown-Dateien. Kein Generator noetig, solange die Markdown-Dateien die Quelle sind. Falls spaeter eine Suche oder Statistiken gewuenscht sind: vinta-Setup als Upgrade-Pfad.

## 6. Marker, Tags, Eintragsformate

- Standard: `- [Name](url) - Description.`; Satzanfang gross, Punkt am Ende; `Contents` als erster Abschnitt; `Footnotes` am Ende.
- **awesome-terraform-Legende:** `👻` nicht kompatibel, `💀` veraltet, `💲` kommerziell – direkt uebertragbar auf unsere Quellen.
- **awesome-healthcare:** `(Commercial Software)` als Kennzeichnung.
- **free-programming-books:** `*( :construction: in process)*`, `*( :card_file_box: archived)*`, Lizenz in Klammern; RTL/LTR-Linter (`scripts/rtl_ltr_linter.py`) fuer gemischte Schriftrichtungen.
- **awesome-python:** `(part of Parent)` wird vom Generator als "Bundled"-Badge geparst; kursive Abschnitts-Intros.
- **public-apis:** feste Spalten mit erlaubten Werten (`OAuth`, `apiKey`, `No`, `Yes/No/Unknown`) – fuer uns z. B. `Evidenztyp`, `Sprache`, `Zugang`.

**Fuer uns (Vorschlag):** Einheitsformat
`- **[Name](URL)** — Ein Satz Beschreibung. [Evidenztyp] [Stand] [Zugang]`
z. B. `[Studie]`, `[Leitlinie]`, `[Selbsthilfe]`, `[Patientenbericht]`, `[Commercial]`, `[Preprint]`, `[veraltet]`, `[DE]`, `[EN]`.
Eine `Legende` direkt im README. Dazu: **keine Heilversprechen**, Quelle benennen, Datum der letzten Pruefung.

## 7. Automatisierung

- **lychee** Linkcheck in natnew/Awesome-Prompt-Engineering (`.github/workflows/link-check.yml`, `.lychee-ignore`) und awesome-rl-for-agents (`.lycheeignore`).
- **awesome-lint** in sindresorhus/awesome und awesome-selfhosted.
- **awesome_bot** in awesome-healthcare (`--allow-redirect --white-list`).
- **Taeglicher Linkcheck** in public-apis (`.github/workflows/validate_links.yml` + `scripts/validate/links.py`).
- **Generated `--check` Gate** in awesome-rl-for-agents (`python scripts/build_index.py --check`).
- **Issue-Templates** in awesome-rl-for-agents: `add-resource`, `broken-link`, `new-section`.
- **Alphabetisierungs-CI** in free-programming-books.

**Fuer uns:** lychee bei jedem PR, der `*.md` anfasst + ein monatlicher Cron-Job. Issue-Templates `add-resource` und `broken-link`. Kein awesome-lint-Zwang, solange unser Format abweicht (sonst staendig False Positives).

## 8. Sonstiges

- **Lizenz:** CC0 bei sindresorhus/awesome, awesome-python? (awesome-rust), awesome-healthcare; CC BY 4.0 bei free-programming-books; CC BY-SA 3.0 bei awesome-selfhosted; MIT bei public-apis/natnew.
- **Code of Conduct:** fast ueberall vorhanden; free-programming-books uebersetzt ihn in 30+ Sprachen.
- **Disclaimer:** awesome-healthcare hat **keinen** medizinischen Disclaimer – das ist unsere Luecke und unser Alleinstellungsmerkmal. Solve M.E. bzw. `kuriocity/long-covid` formulieren explizite Non-Goals: *"❌ Medical advice"*, *"❌ A substitute for a physician"*.
- **Sponsoren:** vinta hat Sponsor-Slots, aber AGENTS.md verbietet Einfluss auf die Liste. Wir brauchen das erst gar nicht.
- **Uebersetzungen:** free-programming-books uebersetzt CONTRIBUTING/HOWTO/CoC – fuer uns erst, wenn die Liste steht.

## 9. Empfehlung – welche Vorlagen wir nehmen

### Platz 1: natnew/Awesome-Prompt-Engineering
Am naechsten an unserem Fall: Inhalt statt Code, Markdown → Jekyll → Pages, Index + mehrere Themen-Seiten, lychee, und die ausgereifteste `AGENTS.md` (Trust Boundary, Decision Matrix, Protected Areas, Mensch merged).
**Anpassen:** Themen-Seiten → Sprach-Seiten; medizinische Trust-Boundary ergaenzen (keine Therapieversprechen, Evidenztyp Pflicht).

### Platz 2: natnew/awesome-rl-for-agents
Das schlanke Gegenstueck: README kanonisch, generiertes JSON + Entry-Count mit `--check`, drei Issue-Templates, 5-Punkt-Checkliste.
**Fast unverändert uebernehmen**, nur Scope/URLs aendern und den Generator auf alle Sprachdateien erweitern.

### Platz 3: EbookFoundation/free-programming-books
Die Referenz fuer Mehrsprachigkeit: `resources-<lang>.md`, Sprachindex, uebersetzte Regeln, Alphabetisierungs-CI, RTL/LTR-Linter.
**Anpassen:** Dateibenennung und Uebersetzungs-Workflow; Markdown bleibt Quelle (anders als bei awesome-selfhosted).

### Unterstuetzend
- **vinta/awesome-python** – Eintragsqualitaet und `CLAUDE.md = @AGENTS.md`.
- **public-apis** – strenge Feldwerte, ein Link pro PR.
- **awesome-terraform** – Emoji-Legende.
- **awesome-healthcare** – `(Commercial Software)`-Marker, aber ohne unseren Disclaimer.

### Bewusst NICHT uebernehmen
- awesome-selfhosted: YAML als Quelle + 3 Repos + force-push generierte READMEs → verletzt "Markdown als Single Source of Truth".
- sindresorhus/awesome: "Fully AI-generated pull requests are not accepted" → widerspricht unserem KI-Pflege-Ziel.
- github/awesome-copilot: ~60 Workflows, Frontmatter-Maschinerie → voellig ueberdimensioniert.
- vinta: harte 5-Eintraege-pro-Use-Case-Grenze → fuer ein Ressourcen-Verzeichnis zu restriktiv.

## 10. Offene Punkte zum Durchgehen

1. Dateiaufbau: `README.md` + `resources-de.md` / `resources-en.md` – okay, oder doch eine einzige README mit Sprach-Abschnitten?
2. Pages-Variante: Jekyll Remote-Theme (einfach) vs. `just-the-docs` (schicker) vs. Docsify (null Build)?
3. Eintragsformat: kurze Zeile mit Marker-Suffix vs. strikte Tabelle wie public-apis?
4. Wie streng soll die KI-Regel sein – "nie direkt editieren, nur empfehlen" oder "kleine Aenderungen direkt erlauben"?
5. Wollen wir einen Generator (JSON-Index/Entry-Count) oder bleibt es bei reinen Markdown-Dateien?
6. Lizenz: CC0 (max. Weiterverwendung) oder CC BY-SA 4.0 (Zuschreibung bleibt)?
