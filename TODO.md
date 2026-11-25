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

## Veröffentlichung

- [ ] Optional: Eintrag in den awesome-Listen-Index (sindresorhus/awesome) beantragen – erst nach ausreichendem Inhalt. Der Index hatPull Requests pausiert und gilt ab dem 22.11.2026 nach 30 Tagen als zu jung; das blockiert die Veröffentlichung nicht. Für später fehlen: GitHub-Topic `awesome` neben `awesome-list`, Awesome-Badge in der README, `Contents` als erste Sektion, keine `Licence`-Sektion in der README und ein Lauf von `awesome-lint`.
- [ ] Ankündigung in einschlägigen Communities (Selbsthilfe, Forschung) – nur nach Rücksprache, kein Spam

## Nächste Schritte (vom User vorgegeben)

- [ ] Inhalte: 80 EN- / 134 DE-Einträge – weitere Ressourcen sammeln ist der nächste grosse Schritt

## Basisstruktur reviewen (Schritt für Schritt mit dem User)

- [ ] `AGENTS.md`: Wenn alles stimmt, **auf Englisch umstellen** – noch offen.

## Feedback zur Basisstruktur

- [ ] **Kapitel in der Seitenleiste** – Entscheidung offen; C (JavaScript) verworfen
  - Befund: just-the-docs baut die linke Navigation ausschließlich aus Seiten-Frontmatter. Die H2-Überschriften einer einzelnen Datei lassen sich dort nicht einblenden; `nav_fold` gilt nur für Collections, und `{:toc}` mit `<details>` erscheint immer im Seiteninhalt.
  - **A (empfohlen):** automatischer, aufklappbarer Inhaltsverzeichnis-Block oben in `links-en.md` und `links-de.md` via `<details>` + `{:toc}`. Keine Strukturänderung, SSOT und alle URLs bleiben, das Verzeichnis pflegt sich selbst. Nachteil: nicht in der linken Seitenleiste.
  - **B:** `resources-de/` und `resources-en/` als Ordner mit `index.md` plus 9 Kinderseiten (`parent:`), echte aufklappbare Unterpunkte links. Nachteile: URL-Wechsel (`/resources-de.html` → `/resources-de/`, mit `permalink` abfangbar), Anker-Links werden seitenübergreifend, Sprachleiste und Disclaimer sind 10× zu pflegen, die `AGENTS.md`-Regel „eine Datei pro Sprache, Kategorien als H2" muss geändert werden, und viele Kategorien haben erst 0–1 Einträge.
  - Vergleich anderer Listen: free-programming-books bleibt bei einer Datei pro Sprache plus Anker (keine Kategorie-Navigation); natnew/Awesome-Prompt-Engineering nutzt ~15 flache Kategoriedateien (lange flache Nav); die just-the-docs-Doku selbst nutzt Ordner plus Kinderseiten; awesome-python baut eine eigene Website (zu viel Aufwand für uns).

## Website-Navigation & Erreichbarkeit

- [ ] **`<html lang>` auf den deutschen Seiten korrigieren** – `locale: de_DE` im Frontmatter setzt nur `og:locale`; just-the-docs liest für `<html lang>` ausschliesslich `site.lang`. Vorschlag: lokale `_layouts/default.html` mit `page.lang | default: site.lang | default: 'en-US'` und `lang: de` in `links-de.md`. Nachteil: die kopierte Layout-Datei bekommt keine automatischen Theme-Updates. Vom User vorerst zurückgestellt.

## Suchmaschinen & KI-Crawler (SEO)

- [ ] **`robots.txt` mit expliziten Allow-Regeln** – gehört in die Root des User-Site-Repos `awesome-long-covid-mecfs.github.io` (Root-Domain), optional zusätzlich im Projekt-Repo unter `/awesome-long-covid-mecfs/robots.txt`. Sichtbarkeit: `Googlebot`, `bingbot`, `Applebot`, `OAI-SearchBot`, `ChatGPT-User`, `Claude-SearchBot`, `Claude-User`, `PerplexityBot`, `Perplexity-User`. Training (bewusste Einwilligung): `GPTBot`, `ClaudeBot`, `Google-Extended`, `Applebot-Extended`, `CCBot`, `meta-externalagent`. Default `User-agent: * / Allow: /`. Die `Sitemap:`-Zeile erst, wenn `sitemap.xml` existiert. User-Fetcher folgen robots.txt teils nicht; ein Allow garantiert keine Aufnahme in KI-Antworten.
- [ ] **Search Console / Bing Webmaster Tools** – Verifizierung durch den User, `webmaster_verifications` in `_config.yml`, danach Sitemap einreichen.
- [ ] **Später optional:** `llms.txt` als Hinweisdatei (kein Rankingfaktor).
- [ ] **GSC-Sitemap nachprüfen (ca. 26.11.2026)** – Der Sitemap-Report zeigte zeitweise „Sitemap could not be read", ohne Fehlerursache; der Live-Test der Sitemap-URL war erfolgreich, und der Abruf mit Googlebot-User-Agent liefert 200/`application/xml` mit gültigem XML und absoluten URLs. Nach 2–3 Tagen Status der Sitemap erneut prüfen; falls weiter fehlerhaft, den genauen Grund aus GSC ergänzen. Kein Code-Change nötig, solange der Live-Test grün bleibt.
- [ ] **Bing Webmaster Tools: Site anlegen** – Import aus der Search Console nutzen, gleiche Sitemap einreichen. Davon profitiert auch DuckDuckGo.
- [ ] **Verifizierungsdateien ablegen** – sobald Google/Bing die HTML-Dateien liefern: Datei für den Projektpfad in diesem Repo, Datei für die Root-Domain im Repo `awesome-long-covid-mecfs.github.io`; danach Build und HTTP 200 prüfen.
- [ ] **Sichtbarkeit nach 1–4 Wochen prüfen** – Suche `site:awesome-long-covid-mecfs.github.io/awesome-long-covid-mecfs` in Google. Falls weiterhin nichts auftaucht: ein paar echte Verweise aus relevanten Selbsthilfe-/Fachcommunities oder bestehenden Sammlungen setzen (kein Spam).

## Weitere Ideen (vorerst zurückgestellt)

- [ ] Hinweis bei Einträgen, deren letzte Prüfung älter als 12 Monate ist
- [ ] `🆕 [neu]`-Marker für die ersten 30 Tage
- [ ] Filter/Tag-Seiten, Statistik, Druckansicht/PDF – erst bei grösserer Liste
- [ ] **Drei-Schritte-Klickstrecke unter den Buttons** (beide READMEs) – „1. Sprache wählen · 2. Thema anklicken · 3. Quelle lesen – wir bewerten nicht, wir verlinken nur."

## Vorbereitung Community-Vorschlag (vom User angeregt, 25.11.2026)

- [ ] Repo aufräumen (verwaiste Dateien und Konfigurationsreste prüfen)

**Versand erst nach separater Freigabe.**

### Vorlage für die Ankündigungs-E-Mail (DE + EN)

**Deutsch**

> **Betreff: 📚 Neue Ressourcenliste zu Long COVID & ME/CFS – gerne weiterteilen**
>
> Hallo [Name],
>
> ich habe eine kostenlose, kuratierte Liste mit deutsch- und englischsprachigen Ressourcen zu Long COVID und ME/CFS erstellt: [Link]
>
> 📚 Die Liste verlinkt auf bestehende Angebote, ohne Quellen zu bewerten oder medizinische Empfehlungen zu geben.
>
> 🙌 Du darfst den Link gerne veröffentlichen und weiterteilen – es ist ein privates, nicht-kommerzielles Projekt.
>
> 💬 Ich freue mich über Rückmeldungen und hilfreiche Links aus der Community! Die E-Mail-Adresse dafür steht auf der Website.
>
> Liebe Grüße
> [Name]

**English**

> **Subject: 📚 New resource list on Long COVID & ME/CFS – feel free to share**
>
> Hi [Name],
>
> I've put together a free, curated list of German- and English-language resources on Long COVID and ME/CFS: [link]
>
> 📚 The list links to existing resources without rating sources or giving medical advice.
>
> 🙌 Feel free to publish and share the link – it's a private, non-commercial project.
>
> 💬 I'd love to hear from you and get helpful links from the community! My email address for that is on the website.
>
> Best,
> [Name]

### Info: wen ich kontaktieren kann (Kontaktwege geprüft am 25.11.2026)

Adressen stammen aus den Impressums- und Kontaktseiten der verlinkten Angebote. **Noch nichts versenden — Versand nur nach separate Freigabe.** Fünf Anbieter widersprechen ausdrücklich unaufgeforderter Werbung oder Informationspost (lebenszeit, ME/CFS-Wiki, startaMEvolution, Fasynation, ME-CFS Portal): Nachricht kurz, sachlich, nicht werblich halten.

**Vereine und Portale mit E-Mail-Adresse**

- DG ME/CFS: `info@dg.mecfs.de` (Kontaktformular deaktiviert)
- ME-Hilfe e. V.: `kontakt@me-hilfe.de`
- Verein ME/CFS & PAIVS Hilfe: `info@mecfs-paivs-hilfe.de`
- startaMEvolution e. V.: `hello@startamevolution.org`, Impressum `johanna.w@startamevolution.org` — Widerspruch gegen Werbe-E-Mails
- Fasynation: `info@fasynation.de`, Formular unter `/kontakt-2/` — Postfach derzeit pausiert, bei Bedarf „Wichtig oder Unaufschiebbar" markieren; keine persönliche Beratung oder Arztvermittlung
- Das ME-CFS Portal: `info@me-cfs.net` — Regeln: keine kommerzielle Werbung ohne Absprache, keine privaten Spendenaufrufe, kein Spam; Team beantwortet keine allgemeinen Fragen
- ME/CFS-Wiki: `sb_impressum2026@bursch.com` oder Feedbackformular auf jeder Seite — Widerspruch gegen Werbung und Meinungsforschung
- ME/CFS – und nun?: `mecfsundnun@gmail.com`
- mecfs-help.de: `mecfs.hilfe@gmail.com`
- Tee mit Molly: `hallo@teemitmolly.de`, zusätzlich Formular unter `/kontakt/`
- Tipps für LC, PV und ME/CFS Betroffene (Padlet): `tipps.fuer.lc.pv.und.me-cfs.betroffene@gmx.de` — Erreichbarkeit unbekannt
- lebenszeit-mecfs.de: `lebenszeit-cfs@web.de` — Widerspruch gegen unaufgeforderte Werbung und Informationsmaterialien
- No longer!: `tobims79@proton.me` (Impressumsadresse; auf der Startseite steht zusätzlich eine veraltete Yahoo-Adresse)
- Long COVID Deutschland: Kontaktformular — ausdrücklich keine individuellen Diagnose-/Therapiefragen, sachlicher Ressourcen-Hinweis passt
- Fatigatio e. V.: Kontaktformular / Presseformular
- CrunchME: Kontakt über die Website (Datenbank und Advocacy)
- #MEAction, Long COVID Support, Patient-Led Research Collaborative: Kontaktformular bzw. Community-Team
- Leben mit ME/CFS: **kein öffentlicher Kontaktweg gefunden** (Impressum leer) — nur Kommentarfunktion, keine Adresse erfinden

**Reminder: Facebook- und WhatsApp-Gruppen**

- Nicht massenhaft anschreiben, nur Admin-Kontakt; Regeln zu Eigenwerbung in jeder Gruppe vorher prüfen.
- Facebook: Gruppen aus `links-de.md` (u. a. Long COVID Deutschland, ME/CFS Treffpunkt Österreich), nur sachlicher Hinweis durch Admins.
- Signal/WhatsApp: „Plaudergarten" (`me-cfs-chat.net`) hat keinen veröffentlichten E-Mail-Kontakt; Beitrittshilfe per SMS/Text an `+41 78 758 11 81`, keine Telefonate. `hello@email.com` dort ist ein unbearbeiteter Platzhalter im HTML — **nicht verwenden**.
- Der WhatsApp-Kanal aus `links-de.md` braucht ebenfalls Admin-Kontakt; Login-Wand nicht geprüft.

## Optional (nach der Veröffentlichung)

- [ ] **Manuelle Linkprüfung vor einer grösseren Ankündigung** – `.github/workflows/link-check.yml` nutzt bewusst `fail: false` (viele Gesundheitsseiten blockieren Bot-Prüfer); Workflow bleibt unverändert. Stichprobe vom 25.11.: 11 markierte URLs alle HTTP 200; Mediathek-/Geo-Sperren und WhatsApp-Login bleiben ungeprüft. Vor dem Versand erneut stichprobenhaft prüfen.

---

Anmerkung: Dieses Repo ist jetzt die Arbeitskopie. Die frühere Kopie im Monorepo `CodeSpace` bleibt nur als Archiv liegen und wird nicht weitergepflegt.
