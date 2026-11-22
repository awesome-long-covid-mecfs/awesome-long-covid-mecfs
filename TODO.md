# ToDo vor der Veröffentlichung

Ziel: Awesome-Liste zu ME/CFS, Post-COVID/Long COVID und verwandten Erkrankungen.
Geplant als GitHub-Repo `awesome-long-covid-mecfs`, mehrsprachig, Sprache als Hauptkategorie.
Vorlagenanalyse anderer Awesome-Listen: [RESEARCH.md](RESEARCH.md).

## Fundament

- [ ] Repo-Namen final auf GitHub prüfen (`awesome-long-covid-mecfs` – die Suche ist ungenau, nur das Anlegen beweist es)
- [ ] Lizenz festlegen (für Inhalte z. B. CC BY-SA 4.0; Code ggf. MIT)
- [ ] GitHub-Beschreibung und Topics finalisieren (u. a. `long-covid`, `mecfs`, `post-viral`, `POTS`, `MCAS`, `awesome-list`)
- [ ] Grundgerüst: `README.md`, `LICENSE`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`
- [ ] Medizinischen Disclaimer formulieren (keine Diagnose-/Behandlungsempfehlung, keine Heilversprechen)

## Struktur & Inhalt

- [ ] Unterkategorien final festlegen (vorläufig: Diagnostik, Studien/Forschung, Behandlung/Therapie, Selbsthilfe & Community, Alltag & Versorgung, Hilfsmittel, Recht & Anträge, Fachliteratur, Patientengeschichten)
- [ ] Sprachebenen festlegen (z. B. Deutsch, English, ggf. weitere) und Umgang mit mehrsprachigen Einträgen klären (Kurzverweis statt Duplikat)
- [ ] Einheitliches Eintragsformat festlegen (Titel, Kurzbeschreibung, Sprache, Quellenart, ggf. Evidenzgrad)
- [ ] Erste Ressourcen je Sprache/Kategorie sammeln – bevorzugt seriöse Quellen (WHO, NIH, RKI, Fachgesellschaften, Selbsthilfeverbände)
- [ ] Linkprüfung vor dem Publish (tote Links aussortieren)

## Qualität & Sicherheit

- [ ] Aufnahmekriterien definieren: seriös, aktuell, nachvollziehbar, keine Heilversprechen oder Verschwörungsquellen
- [ ] Sprache achten: stigmafreie Begriffe, betroffenenfreundlich, veraltete Bezeichnungen nur mit Hinweis
- [ ] Umgang mit umstrittenen Therapien/Studien regeln (keine Bewertung durch uns, Quellen benennen)
- [ ] Review-Prozess für Contributions festlegen (mind. 2 Personen oder 1 Person + Checkliste)

## Veröffentlichung

- [ ] Repo anlegen und pushen
- [ ] README-Einstieg prüfen: Suchbegriffe "Long COVID", "ME/CFS", "Post-COVID" sollten natürlich vorkommen
- [ ] Optional: Eintrag in den awesome-Listen-Index (sindresorhus/awesome) beantragen – erst nach ausreichendem Inhalt
- [ ] Ankündigung in einschlägigen Communities (Selbsthilfe, Forschung) – nur nach Rücksprache, kein Spam

## Nächste Schritte (vom User vorgegeben)

- [ ] Inhalte: Die Kategorien sind angelegt, aber noch leer – das ist der nächste grosse Schritt
- [ ] Eigenes GitHub-Repo anlegen: Name genau `awesome-long-covid-mecfs`, **ohne** README initialisieren
- [ ] Ordnerinhalt in das neue Repo kopieren/pushen (dabei helfe ich dir)
- [ ] In GitHub: Settings → Pages → Source: „Deploy from a branch" → `main` / `/(root)` → Save
- [ ] Website testen – erst nach dem Push sichtbar; URL `https://<dein-Name>.github.io/awesome-long-covid-mecfs/`, `baseurl` in `_config.yml` ist dafür schon richtig gesetzt

## Basisstruktur reviewen (Schritt für Schritt mit dem User)

- [x] Zusätzliche Melde-Möglichkeit per E-Mail für Personen ohne GitHub-Konto: Adresse `awesome-long-covid-mecfs[at]sags-per-mail.de` in `README.md` und `CONTRIBUTING.md` ergänzt. Gewählte Variante: `[at]` statt `@` (einfach, barrierefrei, schützt vor einfachen Spam-Crawlern). Auch dieser TODO-Eintrag ist entschärft. Bei Bedarf auf eine stärkere Variante wechseln (Bild oder Kontaktformular).
- [ ] `AGENTS.md` nochmal reviewen und besprechen: Die KI soll ggf. **mehr Aufgaben übernehmen** – Links automatisch prüfen und bewerten (Erreichbarkeit, Duplikate, Quellenart, Marker, Stand-Datum).
- [ ] `AGENTS.md`: Wenn alles stimmt, **auf Englisch umstellen**.
- [ ] Kategorien durch den User prüfen und ggf. erweitern.

## Mehrsprachigkeit (vom User vorgegeben)

- [x] Primärsprache ist **Englisch**; Deutsch und später weitere Sprachen müssen schnell erreichbar sein – Haupt-`README.md` ist englisch
- [x] Sprachwechsel oben in der README und in jeder Sprachdatei über Links **mit Länderflaggen-Emojis** (🇬🇧 English, 🇩🇪 Deutsch, …)
- [x] Kurzer Verweis in der Haupt-README: „Deutsche Anleitung hier" → `README-de.md` (neue deutsche README)
- [x] Benennung neuer Sprachdateien festlegen (`resources-<lang>.md`) und regeln, wer sie anlegt – steht in `AGENTS.md`
- [x] Beim Anlegen einer neuen Sprache alle Stellen mitaktualisieren: Sprachleiste in allen Dateien, `aux_links` in `_config.yml`, Inhaltsverzeichnisse, Issue-Formular – als Regel in `AGENTS.md` festgehalten

## Abschlusscheck vor Veröffentlichung

- [ ] Repo-weite Suche nach zurückgebliebenen PII-Platzhaltern (spitze Klammern mit `PII type`) – Dateien **inklusive** `.github/`, Workflows, versteckter Dateien und LICENSE prüfen; jeder Fund muss durch einen echten Wert ersetzt werden
- [x] Zusätzlich prüfen, dass die E-Mail-Adresse nirgends im Klartext steht (nur `[at]`-Schreibweise) – geprüft am 22.11.2026
- [ ] Letzter Stand dieses Checks: im Ordner `awesome-long-covid-mecfs` wurden keine PII-Platzhalter gefunden (Prüfung am 22.11.2026)

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
- [ ] **Kategorien in der Seitenleiste** – bewusst zurückgestellt; gewählt wurde Variante A+C (manuelles Inhaltsverzeichnis + aux_links)
- [x] **Inhaltsverzeichnis am Anfang jeder Sprachdatei** mit Links zu allen Kategorien (manuell, funktioniert auf GitHub und auf der Website)

## Verbesserungsideen (vom User ausgewählt)

- [x] Icons/Symbole **zusätzlich** zum Text-Marker, nicht statt dessen (z. B. 📄 Studie, 🏛️ Behörde, 🤝 Selbsthilfe, ⚠️ veraltet, 💰 Commercial) – Legende in `README.md` entsprechend ergänzt, barrierefrei
- [x] Quellentyp präziser benennen **statt Sterne-/Gut-schlecht-Bewertung**: `[Systematische Übersicht]`, `[Studie]`, `[Leitlinie]`, `[Behörde]`, `[Selbsthilfe]`, `[Erfahrungsbericht]` – auch im Issue-Formular und in `AGENTS.md`
- [x] Warn-Kästen für heikle oder veraltete Quellen – Regel in `AGENTS.md`; nur bei `[veraltet]` oder begründeten Bedenken, nicht bei Preprint/Commercial
- [x] Sprachleiste oben in jeder Sprachdatei (🇬🇧 English | 🇩🇪 Deutsch)
- [x] Eigener Abschnitt „Was wir nicht aufnehmen" in `README.md` (englisch) und `resources-de.md` (deutsch) sowie als Hinweis im Issue-Formular

## Weitere Ideen (vorerst zurückgestellt)

- [ ] Hinweis bei Einträgen, deren letzte Prüfung älter als 12 Monate ist
- [ ] `🆕 [neu]`-Marker für die ersten 30 Tage
- [ ] Filter/Tag-Seiten, Statistik, Druckansicht/PDF – erst bei grösserer Liste

---

Anmerkung: Dieser Ordner liegt aktuell im Monorepo `CodeSpace`. Für die Veröffentlichung als eigenes GitHub-Repo muss er später separat dorthin übertragen oder als eigenes Repo angelegt werden.
