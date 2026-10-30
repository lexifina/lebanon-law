"""Rewrites repo/README.md and repo/LICENSE for the codes listed on the command line (idempotent from the base copies)."""
import pathlib, sys
H = pathlib.Path(__file__).parent
R = H / 'repo'
want = sys.argv[1:]
ROWS = {
 'obligations': "| `obligations-and-contracts/` | Code of Obligations and Contracts (قانون الموجبات والعقود, law of 9 March 1932), articles 1 to 1107 and headings | 1 | The oldest version available: the Lebanese University text with its amending-law notes, dated 1 July 2019, when Law no. 126 of 29 March 2019 (the latest amendment it names) took effect |\n",
 'commerce': "| `commerce/` | Land Commerce Code (قانون التجارة البرية, legislative decree no. 304 of 24 December 1942), articles 1 to 667 with the articles added as bis, and headings | 1 | The oldest version available: the Lebanese University text with its amending-law notes, dated 1 July 2019, when Law no. 126 of 29 March 2019 took effect |\n",
 'penal': "| `penal-code/` | Penal Code (قانون العقوبات, legislative decree no. 340 of 1 March 1943) | 1 | The oldest version available |\n",
}
SRC = {
 'obligations': "Code of Obligations and Contracts: the Legal Informatics Center of the Lebanese University (المركز اللبناني للمعلوماتية القانونية, legiliban.ul.edu.lb), the whole law as one print page, retrieved on 30 October 2026. Each article is printed in Arabic and in French; this record keeps the Arabic only. A note after the article number names the law that amended it.",
 'commerce': "Land Commerce Code: the same Center, the whole law as one print page, retrieved on 30 October 2026, Arabic text only.",
 'penal': "Penal Code: the Center's text.",
}
base = H / 'README.base.txt'
if not base.exists():
    base.write_text((R / 'README.md').read_text(encoding='utf-8'), encoding='utf-8', newline='')
    (H / 'LICENSE.base.txt').write_text((R / 'LICENSE').read_text(encoding='utf-8'), encoding='utf-8', newline='')
s = base.read_text(encoding='utf-8')
s = s.replace("This is a first build: the Constitution only, as one version, the oldest version available.", "This is a first build: the Constitution and core codes, each as one version, the oldest version available.", 1)
i = s.index("| `constitution/`")
j = s.index("\n", i) + 1
s = s[:j] + ''.join(ROWS[w] for w in want) + s[j:]
k = s.index("Language: Arabic")
k2 = s.index("\n", k) + 1
s = s[:k2] + "\n" + '\n\n'.join(SRC[w] for w in want) + "\n" + s[k2:]
s = s.replace("- Every other Lebanese law.", "- Every other Lebanese law, and the text of the laws that amended the codes.")
(R / 'README.md').write_text(s, encoding='utf-8', newline='')
lic = (H / 'LICENSE.base.txt').read_text(encoding='utf-8')
lic = lic.replace("Lexifina's own contributions", "The codes listed in the README are official legislation published by the Legal Informatics Center of the Lebanese University (https://legiliban.ul.edu.lb), which states no licence for them; they are reproduced with this attribution. The Lebanese University does not endorse this repository.\n\nLexifina's own contributions", 1)
(R / 'LICENSE').write_text(lic, encoding='utf-8', newline='')
