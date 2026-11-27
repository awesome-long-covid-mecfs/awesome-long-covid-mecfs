---
title: AI Rules (AGENTS.md)
layout: default
nav_order: 5
nav_exclude: true
sitemap: false
---

# AGENTS.md – Rules for AI assistants

This file applies to all AI assistants working in this folder. It is binding; in case of conflict with other files, it takes precedence.

## 1. What this project is

A **content collection**, not a program. The result is well-curated Markdown files. The website (GitHub Pages with `just-the-docs`) is generated from them only.

**Single source of truth for content:** `README.md` (GitHub view), `links-de.md`, `links-en.md` and further `links-<language>.md` files.
**Single source of truth for markers:** `MARKERS.md` – the legend, issue forms and entries are derived from it. Everything else is configuration or generated output.

## 2. Principle: proposal → comments → approval → implementation

The normal flow for new content:

1. The user provides a link (or an idea).
2. The AI **checks and proposes** how and where to add the entry – without changing any file yet.
3. The user makes comments and only then says **“approved”** (German: „freigegeben").
4. After this explicit approval, the AI may **do the rest**: write the file, commit and push.

- Without approval: **never** change files, commit or push. If anything is unclear, give a recommendation instead of editing.
- Approval applies only to the specific entry discussed – not as standing permission for anything else.
- Never silently change existing entries to "improve" them. Remove content only when asked and justified (e.g. dead link).
- One logical entry per change. No combined commits of unrelated topics.

## 3. Trust boundary (especially important for health topics)

- **Do not invent medical claims.** Do not state anything that is not in the linked source.
- If the user gave **no description**, the AI may open the page and write **a short summary of its content** – nothing more. No external facts, no assessment, no conclusions.
- Do not "know" from training that a source is reputable. Open and check the link. If it cannot be checked, phrase it neutrally or flag it – never claim it.
- **No promises of cure, no treatment recommendations, no diagnostic help.** Entries link to sources; they do not judge their truth.
- Controversial or outdated sources only with a visible marker (`[Outdated]`, `[Preprint]`) and a neutral description.
- If unsure about evidence, classification or source: **give the user a recommendation before writing anything.**

## 4. Inclusion criteria

Include a source when it:

- fits the topic (Long COVID, ME/CFS, post-viral, POTS, MCAS, hEDS, fibromyalgia as a coexisting condition),
- is self-contained and permanently reachable (stable URL, no URL shorteners),
- does not force payment or registration (otherwise mark `[Commercial]`),
- is not purely promotional (reject affiliate links),
- has a clear origin (authority, professional association, science, self-help, personal experience).

Do not include: miracle cures, conspiracy sources, paywall-only content without a free summary, pure advertising, duplicate links.

**Exception for duplicate links:** The same resource may appear in several language files if there is **a separate language version for each**. The German version goes in `links-de.md`, the English version in `links-en.md`. Two identical links in *the same* file remain undesirable. A resource counts as a separate language version if its app/content is fully usable in the file language, even when the website URL is identical.

## 5. Entry format

```
- **[Name of the source](https://...)** — A neutral sentence describing it. 📄 [Study]
```

- One sentence, short text, ending with a period.
- **A date marker `[Stand: …]` is omitted for now** (user decision). Do not re-add it on your own.
- Always write the icon **together with the text marker** (e.g. `📄 [Study]`), never the emoji alone – otherwise screen readers cannot classify the entry.
- **All markers are in English.** The full list with German translations is in [`MARKERS.md`](MARKERS.md) – add them there, do not copy them here.
- Several markers per entry are allowed. If certain combinations pile up, a new category may emerge – agree with the user first.
- **No stars, no good/bad rating.** Name the source type only – readers judge for themselves.
- The language of the entry determines the file: German sources → `links-de.md`, English → `links-en.md`.
- Only create a new language file after agreeing with the user; filename `links-<lang>.md`. Then update the language bar in **all** files (see section 6).

### Warning boxes

If an entry needs a clear warning, put it directly below:

```
> ⚠️ This source is outdated – please use it only in a historical context.
```

Use only for `⚠️ [Outdated]` or sources with justified concerns (e.g. no longer reachable, controversial – then with a source reference). **Not** for `[Preprint]` or `[Commercial]` – the markers are enough there. Do not put a medical assessment in the box, only a factual note.

## 6. Placement

- Put the entry in the **appropriate thematic subsection** of the language file.
- Within a category, alphabetical by name if the list is alphabetical; otherwise at the end of the category. Do not mix top/bottom arbitrarily.
- No new category without agreement – the provisional categories are in the language files.
- Multilingual source: **one separate language version per language file** – German version in `links-de.md`, English version in `links-en.md`. This is the permitted exception to the duplicate-link rule (see section 4). No short cross-reference needed if both versions exist.
- **Intro of the language files:** Every `links-<language>.md` starts after the front matter with the title `Awesome Long COVID & ME/CFS Resources – <Language>`, two short paragraphs, the hint for submitting links, the ⚠️ and the ℹ️ notice. Then comes the language bar, then the table of contents. There are no language-specific README instructions any more.
- **Changes in all languages:** If the intro is changed, the same change belongs in every `links-<language>.md` – translated, but with the same structure and the same links. `README.md` remains the only README and links only to the lists in its table.

- New language: agree with the user first, then create `links-<lang>.md`. Then update **all** places: the table in `README.md`, the intro, the language bar and the page titles in all `links-*.md` files, and the language list in the issue form. Otherwise orphaned links appear.
- Website language navigation runs through the page titles of the files with front matter (currently `links-en.md` as the home page and `links-de.md`); `nav_exclude` keeps meta pages out of the sidebar. English always comes first, then German, then further languages.

## 7. Protected areas – never change without explicit instruction

- `README.md`: sections "Important"/"Wichtig" (disclaimer), "Legende"
- `MARKERS.md`, `AGENTS.md`, `CONTRIBUTING.md`, `CONTRIBUTING-de.md`, `CODE_OF_CONDUCT.md`
- `_config.yml`, `.github/` (workflows, issue templates)
- `LICENSE.txt`
- Existing entries by other people

## 8. Internal links

Internal links are **always written as `.md`**, e.g. `[Deutsch](links-de.md)`.
The plugin `jekyll-relative-links` converts them into website links at build time.
**Never** manually change `.md` to `.html` – that breaks the links in the GitHub repo and is unnecessary.

## 9. Workflow for a change proposal

1. Check scope: does the entry fit here at all?
2. Check the source/link: reachable, stable, origin clear?
3. Check uniqueness: is the source already listed? (Exception: its own language version in another file – allowed.)
4. Determine placement: correct language file, correct category.
5. Wording: if the user gave no description, open the page and write a **short summary of its content**. Otherwise use the user's wording. No promises of cure, set markers – no date marker.
6. **Return the proposal** – do not change files, commit or push yet.
7. Incorporate user comments and **wait for “approved” / „freigegeben"**.
8. Only after approval: write the file, commit and push. For resource link changes (add/remove/replace), add one commit-body line per entry: `- <add|remove|replace> [<category>]: <Name> — <short description> (<URL>)` (for GitHub commit feed `commits/main.atom`). Then briefly report what happened.

In the proposal briefly report: **decision** (include / reject / recommend only), **which files** would be affected, **which checks** were made, **what is uncertain**.
