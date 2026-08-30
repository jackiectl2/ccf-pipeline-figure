#!/usr/bin/env python3
"""Re-derive every number printed in SKILL.md from the committed corpus files.

⭐ WHY THIS EXISTS. §6 of this skill says a figure must be regenerable from committed code
plus committed data in one command. The skill's own statistics were not: they were typed
into prose from four separate vision passes over four differently sized sets, and the
denominator was usually left out, so a reader could not tell whether "9 figures do this"
meant 9 of 82, of 77, of 36 or of 17. Running this script is that one command.

    python3 assets/audit_corpus.py [path/to/corpus]   # defaults to the bundled one

Every EXPECTED value below is the number as printed in SKILL.md, so this is a regression
test on the prose: a FAIL means the file and the corpus disagree, and the corpus wins.

⚠ It was NOT green on its first run -- 9 of 15 passed. The six failures are kept in §0.3
rather than quietly corrected, because the useful record is what kind of claim went wrong:
four were a number quoted without its denominator, one was "not one" standing in for one of
seventeen, and one was lifted from the wrong key of the right file. All six made the rule
sound stronger than the corpus supports. The expectations below are now the corrected
values, so any future drift between the prose and the data shows up here.

THE FOUR SETS, which is the thing the prose kept eliding:

  A  VISION_A.json     192 figures over 28 award papers, of which 36 are conceptual
  B  VISION_B.json      77 figures over 12 long-context / memory / evaluation papers
  K  KEEP.json          82 figures of this one genre, kept from both groups
  P  FINAL_PICK.json    the same 82, with the human S / K / D grade

A count from one set says nothing about another. §1 and §2.2 are A; §3 is B; §0.2 and the
star-versus-drop lifts are P.
"""
import json
import sys
from collections import Counter
from pathlib import Path
from statistics import mean, median

# ⭐ The corpus travels WITH the skill. It used to default to the host project's
# `literature/`, which meant the numbers could only be re-derived inside the one project
# they came from -- and a rule you cannot re-check is a rule you have to take on faith.
LIT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "corpus"
ORDER = {"low": 0, "medium": 1, "high": 2}
_results = []


def check(section, claim, expected, actual, note=""):
    ok = expected == actual
    _results.append(ok)
    mark = "PASS" if ok else "FAIL"
    print(f"  [{mark}] {section:6s} {claim}")
    if not ok:
        print(f"         SKILL.md says {expected!r}")
        print(f"         data says     {actual!r}")
    if note:
        print(f"         {note}")


def main():
    A = json.loads((LIT / "award-figs/VISION_A.json").read_text())
    B = json.loads((LIT / "amnesia-adjacent/VISION_B.json").read_text())
    P = {i["file"]: i for i in json.loads((LIT / "FINAL_PICK.json").read_text())["images"]}
    K = {f["file"]: f for f in json.loads((LIT / "KEEP.json").read_text())["figures"]}

    print(f"set A: {A['opened_count']} figures, {A['census']['packet_papers']} award papers")
    print(f"set B: {B['opened_count']} figures, 12 direction papers")
    print(f"set P/K: {len(P)} figures of the genre\n")

    # ---------------------------------------------------------------- §0.2 grading
    v = Counter(P[f]["human"] for f in P)
    check("§0.2", "human grades S / K / D",
          (17, 34, 30), (v["star"], v["keep"], v["drop"]))
    check("§0.2", "graded figures (82 collected, one carries no verdict)",
          81, sum(n for k, n in v.items() if k),
          "the ungraded one: " + ", ".join(f for f in P if not P[f]["human"]))

    def source(f):
        p = K[f]["provenance"]
        return "xhs" if isinstance(p, dict) and p.get("source") == "xiaohongshu" else "arxiv"

    t = Counter((source(f), P[f]["human"] or "ungraded") for f in P)
    check("§0.2", "social-media figures: S / K / D",
          (16, 3, 2), (t[("xhs", "star")], t[("xhs", "keep")], t[("xhs", "drop")]))
    check("§0.2", "arXiv award figures: S / K / D",
          (1, 31, 28), (t[("arxiv", "star")], t[("arxiv", "keep")], t[("arxiv", "drop")]))
    check("§0.2", "share of the drops that are arXiv award figures",
          28, t[("arxiv", "drop")],
          "the prose under that table said 26, contradicting the table itself")

    # ---------------------------------------------------------------- §1 census (set A)
    ns = [p["n_conceptual"] for p in A["census"]["conceptual_figures_per_paper"]["per_paper"]]
    d = Counter(ns)
    check("§1", "conceptual figures per award paper: 0 / 1 / 2 / >=3",
          (10, 8, 6, 4), (d[0], d[1], d[2], sum(n for k, n in d.items() if k >= 3)))
    check("§1", "median / mean / max",
          (1, 1.29, 6), (median(ns), round(mean(ns), 2), max(ns)))
    fr = A["census"]["opening_figure_role"]["counts"]
    n28 = sum(fr.values())
    pct = lambda x: round(100 * x / n28)
    check("§1", "Figure 1 in award papers: conceptual / data / qualitative / hybrid",
          (39, 25, 18, 18),
          (pct(fr["conceptual"]), pct(fr["data_plot"]), pct(fr["qualitative"]), pct(fr["hybrid"])))

    # ---------------------------------------------------------------- §1 direction (set B)
    lead = {k: len(v) for k, v in B["leads_with"].items()}
    nlead = sum(lead.values())
    pb = lambda k: round(100 * lead.get(k, 0) / nlead)
    check("§1", "Figure 1 in the direction: conceptual / data / qualitative / hybrid",
          (20, 60, 10, 10),
          (pb("conceptual"), pb("data_plot"), pb("qualitative"), pb("hybrid")),
          f"denominator is {nlead} papers with a recorded lead, not 12")

    # ---------------------------------------------------------------- §2 house style (set A)
    des = A["census"]["conceptual_figure_design"]
    lay = {x["layout"]: x["count"] for x in des["three_most_common_layouts"]}
    check("§2.1", "left_to_right among the conceptual figures of set A",
          (29, 36), (lay.get("left_to_right"), des["n"]))
    check("§2.2", "median meaning-carrying colours", 4, des["median_colour_roles"])
    check("§2.4", "median text density", "medium", des["median_text_density"])

    # ---------------------------------------------------------------- §2.1 lift (set P)
    star = [f for f in P if P[f]["human"] == "star"]
    drop = [f for f in P if P[f]["human"] == "drop"]
    layer = lambda f: str(K[f].get("layout", "")).lower()
    plain = lambda f: layer(f) in ("left_to_right", "top_to_bottom")
    n_star_chain = sum(plain(f) for f in star)
    check("§2.1", "starred figures that are a plain chain",
          1, n_star_chain,
          "the exception: " + ", ".join(f.split("/")[-1] for f in star if plain(f)))
    check("§2.1", "plain-chain lift, drop% -> star%",
          (67, 6), (round(100 * sum(plain(f) for f in drop) / len(drop)),
                    round(100 * n_star_chain / len(star))))

    # ---------------------------------------------------------------- §2.3 icons (set P)
    devs = lambda f: " | ".join(str(x).lower() for x in P[f]["devices"])
    for term in ("actor", "icon"):
        s = sum(term in devs(f) for f in star)
        p = sum(term in devs(f) for f in drop)
        print(f"  [ -- ] §2.3   device string contains {term!r}: "
              f"star {s}/17 = {round(100*s/17)}%, drop {p}/30 = {round(100*p/30)}%")
    check("§2.3", "'icon' lift, star% -> drop%",
          (41, 17), (round(100 * sum("icon" in devs(f) for f in star) / len(star)),
                     round(100 * sum("icon" in devs(f) for f in drop) / len(drop))))
    check("§2.4", "starred figures with LOW text density",
          0, sum(K[f].get("text_density") == "low" for f in star),
          "against 12 of the 30 dropped")
    # ---------------------------------------------------------------- §3 devices (set B)
    check("§3.1", "distinct renderings of a long context",
          21, len(B["how_the_haystack_is_drawn"]),
          "SKILL.md tabulates 8 of them; references/direction-devices.md lists all 21")

    print()
    bad = _results.count(False)
    print(f"{len(_results) - bad} passed, {bad} failed, out of {len(_results)} checks.")
    print("⚠ A FAIL is not a bug in this script. It means SKILL.md and the corpus disagree,")
    print("  and the corpus is the authority.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
