# How this repository was made (Lebanon)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Constitutional Council of Lebanon, the Constitution | <https://www.cc.gov.lb/ar/%D8%A7%D9%84%D8%AF%D8%B3%D8%AA%D9%88%D8%B1-%D9%88%D8%A7%D9%84%D9%82%D9%88%D8%A7%D9%86%D9%8A%D9%86/%D8%A7%D9%84%D8%AF%D8%B3%D8%AA%D9%88%D8%B1/> | 2026-10-29 | Official legislation; no licence stated on cc.gov.lb |
| Lebanese University Legal Informatics Center: قانون الموجبات والعقود (Code of Obligations and Contracts, law of 9 March 1932) | <https://legiliban.ul.edu.lb/LawView.aspx?opt=&LawID=244226&TYPE=PRINT&language=ar> | 2026-10-30 | Official legislation published by the Legal Informatics Center of the Lebanese University; no licence stated |
| Lebanese University Legal Informatics Center: قانون التجارة البرية (Land Commerce Code, legislative decree no. 304 of 24 December 1942) | <https://legiliban.ul.edu.lb/LawView.aspx?opt=&LawID=244586&TYPE=PRINT&language=ar> | 2026-10-30 | Official legislation published by the Legal Informatics Center of the Lebanese University; no licence stated |
| Lebanese University Legal Informatics Center: قانون العقوبات (Penal Code, legislative decree no. 340 of 1 March 1943) | <https://legiliban.ul.edu.lb/LawView.aspx?opt=&LawID=244611&TYPE=PRINT&language=ar> | 2026-10-30 | Official legislation published by the Legal Informatics Center of the Lebanese University; no licence stated |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | دستور الجمهورية اللبنانية (The Constitution of Lebanon) | 1 | 1990-09-21 to 1990-09-21 |
| `obligations-and-contracts` | قانون الموجبات والعقود (Code of Obligations and Contracts, law of 9 March 1932) | 1 | 2019-07-01 to 2019-07-01 |
| `commerce` | قانون التجارة البرية (Land Commerce Code, legislative decree no. 304 of 24 December 1942) | 1 | 2019-07-01 to 2019-07-01 |
| `penal-code` | قانون العقوبات (Penal Code, legislative decree no. 340 of 1 March 1943) | 1 | 2022-01-13 to 2022-01-13 |

The build made 4 commits:

| Commits | Kind |
| ---: | --- |
| 4 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 0 laws in the record.
- 4 tags.

## Dates

Each commit is dated at noon (Asia/Beirut) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: No general rule was used. The single version is dated by the latest amendment named in the text. https://www.cc.gov.lb/ar/%D8%A7%D9%84%D8%AF%D8%B3%D8%AA%D9%88%D8%B1-%D9%88%D8%A7%D9%84%D9%82%D9%88%D8%A7%D9%86%D9%8A%D9%86/%D8%A7%D9%84%D8%AF%D8%B3%D8%AA%D9%88%D8%B1/

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `fce20ea64a788decff8d29bda69900abbcf4ab3e1611661426b796d54031f3f5` (1814404 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3e59cb6f05eccb94a9ec14431a7f6781221e83ef`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- Single version: the Constitutional Council publishes only the current text. It is recorded as the oldest version available and dated by the latest amendment its notes name (1990-09-21).
- The notes before each article naming the amending constitutional law are kept as published, as the first lines of the article file.
- The Preamble paragraphs (a to y) are one file; Part and chapter headings are their own files.
- Code of Obligations and Contracts: one version, the Lebanese University text with all its amending-law notes. It is dated 2019-07-01, the day Law no. 126 of 29 March 2019 (published in the Official Gazette no. 18 on 1 April 2019, in force three months later) took effect; that is the latest amendment the text names. The law itself was passed on 9 March 1932 and published on 11 April 1932, to take effect thirty months later (art. 1107). Article 1106 does not appear in the source and has no file.
- Code of Commerce: one version, the Lebanese University text with all its amending-law notes, dated 2019-07-01 (Law no. 126 of 29 March 2019 in force; it added the bis articles). The decree was issued on 24 December 1942 and published on 7 April 1943. Articles printed twice with the same text in the source (121 and 213) are kept once, and the note printed under article 143 is kept as that article's last line.
- Penal Code: one version, the Lebanese University text with all its amending-law notes. It is dated 2022-01-13, the Official Gazette date of the latest amending laws the text names (Laws no. 256, 267 and 268 of 5 January 2022); the laws are assumed to take effect on publication and this was not checked. The decree was issued on 1 March 1943 and published on 27 October 1943. Article 335 is printed twice in the source with different texts (the 1983 text, then a later text); both are kept in its file, in the source order. The articles added by Law no. 164 of 2011 after article 586 are the files art-586-add-01 to 11.
- Codes: only the Arabic text is kept (the source prints each article in Arabic and in French); the notes after each article number naming the amending law are kept as its first line, and the section, book, chapter and part headings are their own files.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none
