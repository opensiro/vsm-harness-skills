#!/usr/bin/env python3
"""Check Methodology 0.3.3 assessment artifact structural completeness."""
from __future__ import annotations
import re
import sys
from pathlib import Path
FUNCTIONS = (("s1","S1"),("s2","S2"),("s3","S3"),("s3_star","S3*"),("s4","S4"),("s5","S5"))
COMMON = ("State","Function","Disturbance / variety regulated","Decisive decision or feedback right","Decision owner","Supporting / enforcement mechanisms","Closure path","Why this is / is not agent-owned","Evidence","Basis","Confidence","Caveats")
POSITIVE = {"A","A(P)","C","C(P)","P"}
COMPOSITE = {"A(P)","C(P)"}
EXTRA = {
 "s2": ("Distinct S1 units","Inter-S1 disturbance","Attenuating coordination relation","Feedback into subsequent S1 behaviour","Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation"),
 "s3": ("Whole-system current view","Current-control decision scope"),
 "s3_star": ("Claim being audited","Ordinary reporting path","Complementary access path","Independence boundary","Who acts on findings"),
 "s4": ("External distinction","Future / prospective distinction","Adaptation option generated","Path back into current capability / S3"),
 "s5": ("Identity / ultimate-policy issue","Ultimate authority in each claimed mode","Return-to-operation path"),
}
ABSENCE = ("Surfaces inspected","Plausible first-party paths checked","Why no material first-party path remains")
def frontmatter(text):
    if not text.startswith("---\n"): return {}
    try: raw = text.split("---\n",2)[1]
    except IndexError: return {}
    out={}
    for line in raw.splitlines():
        if ":" in line:
            k,v=line.split(":",1); out[k.strip()]=v.strip()
    return out
def sections(text):
    matches=list(re.finditer(r"^## (S1|S2|S3|S3\*|S4|S5)\b.*$",text,re.MULTILINE)); out={}; rev={v:k for k,v in FUNCTIONS}
    for i,m in enumerate(matches):
        end=matches[i+1].start() if i+1<len(matches) else len(text); out[rev[m.group(1)]]=text[m.start():end]
    return out
def value(section,label):
    m=re.search(rf"^- {re.escape(label)}:\s*(.+?)\s*$",section,re.MULTILINE)
    if not m: return None
    v=m.group(1).strip()
    return None if not v or v in {"...","TBD","TODO"} else v
def check(path):
    failures=[]; text=path.read_text(encoding="utf-8"); fm=frontmatter(text)
    if not fm: return [f"{path}: missing/malformed frontmatter"]
    if fm.get("assessment_procedure_version") != "0.3.3":
        print(f"{path}: skipped (current Methodology {fm.get('assessment_procedure_version','unknown')}, not 0.3.3)"); return []
    if fm.get("status") == "excluded-no-agentic-vsm": return []
    if fm.get("status") != "included": return [f"{path}: unsupported/missing canonical status"]
    body=sections(text)
    for key,title in FUNCTIONS:
        section=body.get(key)
        if section is None: failures.append(f"{path}: missing ## {title} section"); continue
        state=fm.get(f"autonomy_{key}")
        if state is None: failures.append(f"{path}: missing autonomy_{key} frontmatter"); continue
        if value(section,"State") != state: failures.append(f"{path}: {title} State differs from frontmatter {state!r}")
        for label in COMMON:
            if value(section,label) is None: failures.append(f"{path}: {title} missing/non-substantive '{label}:'")
        if state == "—":
            if "### Absence scope" not in section: failures.append(f"{path}: {title}=— missing '### Absence scope'")
            for label in ABSENCE:
                if value(section,label) is None: failures.append(f"{path}: {title}=— missing/non-substantive '{label}:'")
        elif state in POSITIVE:
            for label in EXTRA.get(key,()):
                if value(section,label) is None: failures.append(f"{path}: positive {title} missing/non-substantive '{label}:'")
        elif state != "?": failures.append(f"{path}: {title} has unsupported state {state!r}")
        if state in COMPOSITE:
            if "| Mode | Decisive owner | Trigger | Closure | Evidence |" not in section: failures.append(f"{path}: {title}={state} missing mode matrix header")
            base="A" if state=="A(P)" else "C"
            if f"| Base (`{base}`) |" not in section: failures.append(f"{path}: {title}={state} missing Base (`{base}`) row")
            if "| Parent (`P`) |" not in section: failures.append(f"{path}: {title}={state} missing Parent (`P`) row")
    return failures
def main():
    if len(sys.argv)<2: print("usage: check_assessment_contract.py <assessment.md> [...]",file=sys.stderr); return 2
    failures=[]
    for arg in sys.argv[1:]:
        p=Path(arg)
        if not p.is_file(): failures.append(f"{p}: not a file")
        else: failures.extend(check(p))
    if failures: print("\n".join(failures),file=sys.stderr); return 1
    print("Assessment structural contract check passed"); return 0
if __name__ == "__main__": raise SystemExit(main())
