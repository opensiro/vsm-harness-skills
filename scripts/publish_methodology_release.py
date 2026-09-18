#!/usr/bin/env python3
"""Publish or verify one immutable VSM Harness Methodology release."""
from __future__ import annotations
import argparse,json,os,re,subprocess,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
VERSION_FILE="skills/assess-vsm-harness/VERSION"
CHANGELOG=ROOT/"skills"/"assess-vsm-harness"/"CHANGELOG.md"
SEMVER=re.compile(r"^\d+\.\d+\.\d+$"); SHA=re.compile(r"^[0-9a-f]{40}$")
def run(*args,check=True): return subprocess.run(args,cwd=ROOT,text=True,capture_output=True,check=check)
def notes(version):
    text=CHANGELOG.read_text(encoding="utf-8"); m=re.search(rf"^## {re.escape(version)} — .*?$\n(?P<body>.*?)(?=^## |\Z)",text,re.MULTILINE|re.DOTALL)
    if not m or not m.group("body").strip(): raise SystemExit(f"CHANGELOG missing/empty release section for {version}")
    return m.group("body").strip()
def tag_sha(repo,tag):
    r=run("gh","api",f"repos/{repo}/git/ref/tags/{tag}",check=False)
    if r.returncode!=0: return None
    d=json.loads(r.stdout); kind,sha=d["object"]["type"],d["object"]["sha"]
    if kind=="commit": return sha
    if kind=="tag": return json.loads(run("gh","api",f"repos/{repo}/git/tags/{sha}").stdout)["object"]["sha"]
    raise SystemExit(f"unsupported tag object type: {kind}")
def main():
    p=argparse.ArgumentParser(); p.add_argument("--version"); p.add_argument("--target-sha"); a=p.parse_args()
    version=a.version or (ROOT/VERSION_FILE).read_text(encoding="utf-8").strip(); target=a.target_sha or run("git","rev-parse","HEAD").stdout.strip()
    if not SEMVER.fullmatch(version): raise SystemExit(f"invalid Methodology version: {version!r}")
    if not SHA.fullmatch(target): raise SystemExit(f"invalid release target SHA: {target!r}")
    repo=os.environ.get("GITHUB_REPOSITORY")
    if not repo or not os.environ.get("GH_TOKEN"): raise SystemExit("GITHUB_REPOSITORY and GH_TOKEN are required")
    target_version=run("git","show",f"{target}:{VERSION_FILE}").stdout.strip()
    if target_version!=version: raise SystemExit(f"target {target} contains Methodology {target_version}, expected {version}")
    if run("git","merge-base","--is-ancestor",target,"HEAD",check=False).returncode!=0: raise SystemExit(f"release target {target} is not an ancestor of HEAD")
    tag=f"v{version}"; existing=tag_sha(repo,tag)
    if existing is None: run("gh","api","--method","POST",f"repos/{repo}/git/refs","-f",f"ref=refs/tags/{tag}","-f",f"sha={target}")
    elif existing!=target: raise SystemExit(f"immutable tag {tag} points to {existing}, expected {target}")
    if run("gh","release","view",tag,"--repo",repo,check=False).returncode==0:
        print(f"Release {tag} already exists and tag target is correct"); return 0
    body=notes(version)+f"\n\nRelease target: `{target}`.\n"
    with tempfile.NamedTemporaryFile("w",encoding="utf-8",delete=False) as h: h.write(body); path=h.name
    run("gh","release","create",tag,"--repo",repo,"--title",f"VSM Harness Methodology {tag}","--notes-file",path)
    print(f"Published {tag} at {target}"); return 0
if __name__ == "__main__": raise SystemExit(main())
