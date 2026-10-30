# Lebanon: law history in git

The law of Lebanon as a git history. Each provision is one file, each law gets one commit on the day it took effect, and the law that made each change is the commit's author. `git blame` names the law behind every paragraph and `git log` lists every change to an article.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `lb/`.

This is a first build: the Constitution and core codes, each as one version, the oldest version available.

## What is in it now

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | Constitution of Lebanon (دستور الجمهورية اللبنانية), 102 articles, preamble and headings | 1 | Current text as published by the Constitutional Council, dated 21 September 1990 (latest amendment its notes name); earlier versions are not in the record |
| `obligations-and-contracts/` | Code of Obligations and Contracts (قانون الموجبات والعقود, law of 9 March 1932), articles 1 to 1107 and headings | 1 | The oldest version available: the Lebanese University text with its amending-law notes, dated 1 July 2019, when Law no. 126 of 29 March 2019 (the latest amendment it names) took effect |
| `commerce/` | Land Commerce Code (قانون التجارة البرية, legislative decree no. 304 of 24 December 1942), articles 1 to 667 with the articles added as bis, and headings | 1 | The oldest version available: the Lebanese University text with its amending-law notes, dated 1 July 2019, when Law no. 126 of 29 March 2019 took effect |
| `penal-code/` | Penal Code (قانون العقوبات, legislative decree no. 340 of 1 March 1943) | 1 | The oldest version available |

## Where the text comes from

The text is the Constitution of Lebanon as published by the Constitutional Council of Lebanon (المجلس الدستوري, cc.gov.lb), one web page per Part, retrieved on 29 October 2026. Before each amended article the Council's text names the constitutional law that amended it (for example the Constitutional Law of 21 September 1990); those notes are kept as the first lines of the article file.

Language: Arabic, the language of the Constitution (art. 11). The Council also offers a French page; this record uses the Arabic only.

Code of Obligations and Contracts: the Legal Informatics Center of the Lebanese University (المركز اللبناني للمعلوماتية القانونية, legiliban.ul.edu.lb), the whole law as one print page, retrieved on 30 October 2026. Each article is printed in Arabic and in French; this record keeps the Arabic only. A note after the article number names the law that amended it.

Land Commerce Code: the same Center, the whole law as one print page, retrieved on 30 October 2026, Arabic text only.

Penal Code: the Center's text.

## Not included yet

- Earlier versions of the Constitution and the text of each amending constitutional law.
- Amendments the Council's notes do not name (for example the 2004 amendment of art. 49), if its text does not reflect them.
- Every other Lebanese law, and the text of the laws that amended the codes.

## Dates

The single version is dated 21 September 1990, the latest amendment named in the Council's notes (the Constitutional Law that put the Taif Agreement into the Constitution). The 1926 Constitution was promulgated on 23 May 1926. The record has no older text, so the commit is authored by the publisher as "oldest version available" and dated noon, Asia/Beirut, on that day.

## How it is checked

Every version is read back from git on the day it took effect and on the day before; both must match the corpus the repository was built from. The results are in `REPRODUCE.md`.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file.

## What "author" means

The author of a commit is the law that made the change. Its e-mail address cannot exist, so `git blame` and `git log --author` name laws. A version with no law of its own (the oldest version available) is authored by the publisher and says so. The committer is always Lexifina.
