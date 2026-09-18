#!/usr/bin/env python3
"""Verify that every explicitly versioned Methodology release has a tag and GitHub Release."""
from __future__ import annotations
import json,os,re,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CHANGELOG=ROOT/"skills"/"assess-vsm-harness"/"CHANGELOG.md"; VERSION_FILE="skills/assess-vsm-harness/VERSION"; TRACK_FROM=(0,2,0)
def run(*args,check=True): return subprocess.run(args,cwd=ROOT,text=True,capture_output=True,check=check)
def versions():
    found=re.findall(r"^## (\d+\.\d+\.\d+) —",CHANGELOG.read_text(encoding="utf-8"),re.MULTILINE)
    return [v for v in found if tuple(map(int,v.split('.')))>=TRACK_FROM]
def tag_sha(repo,tag):
    r=run("gh","api",f"repos/{repo}/git/ref/tags/{tag}",check=False)
    if r.returncode!=0: return None
    d=json.loads(r.stdout); kind,sha=d["object"]["type"],d["object"]["sha"]
    if kind=="commit": return sha
    if kind=="tag": return json.loads(run("gh","api",f"repos/{repo}/git/tags/{sha}").stdout)["object"]["sha"]
    return None
def main():
    repo=os.environ.get("GITHUB_REPOSITORY")
    if not repo or not os.environ.get("GH_TOKEN"): print("GITHUB_REPOSITORY and GH_TOKEN are required",file=sys.stderr); return 2
    failures=[]
    for version in versions():
        tag=f"v{version}"; sha=tag_sha(repo,tag)
        if sha is None: failures.append(f"{tag}: missing Git tag"); continue
        r=run("git","show",f"{sha}:{VERSION_FILE}",check=False)
        if r.returncode!=0 or r.stdout.strip()!=version: failures.append(f"{tag}: target {sha} does not contain VERSION {version}")
        if run("gh","release","view",tag,"--repo",repo,check=False).returncode!=0: failures.append(f"{tag}: missing GitHub Release")
    if failures: print("\n".join(failures),file=sys.stderr); return 1
    print(f"Release tracking complete for {len(versions())} Methodology versions"); return 0
if __name__ == "__main__": raise SystemExit(main())
