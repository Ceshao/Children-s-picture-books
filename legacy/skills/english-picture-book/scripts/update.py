#!/usr/bin/env python3
"""Self-update the english-picture-book skill from GitHub.

Behavior:
- If the skill lives inside a git checkout of the repo -> `git pull --ff-only`.
- Otherwise -> download the latest skill files from GitHub and overwrite the local copy.
Fails gracefully (offline / no permission) so it NEVER blocks the skill — it just keeps
using the local version and says so.

Usage:
    python3 scripts/update.py
"""
import subprocess
import tempfile
import shutil
import tarfile
import urllib.request
from pathlib import Path

REPO = "Ceshao/Children-s-picture-books"
BRANCH = "main"
SKILL_SUBPATH = "skills/english-picture-book"

# .../skills/english-picture-book  (this file is in .../scripts/update.py)
SKILL_DIR = Path(__file__).resolve().parent.parent


def local_version() -> str:
    f = SKILL_DIR / "VERSION"
    return f.read_text(encoding="utf-8").strip() if f.exists() else "(unknown)"


def _run(cmd, cwd=None):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)


def try_git() -> bool:
    """Return True if this is a git checkout (handled here), False otherwise."""
    probe = _run(["git", "-C", str(SKILL_DIR), "rev-parse", "--show-toplevel"])
    if probe.returncode != 0:
        return False
    top = probe.stdout.strip()
    before = local_version()
    _run(["git", "-C", top, "fetch", "--quiet"])
    pull = _run(["git", "-C", top, "pull", "--ff-only"])
    if pull.returncode != 0:
        print(f"[update] git pull failed; continuing with local version v{before}.")
        if pull.stderr.strip():
            print("         " + pull.stderr.strip().splitlines()[0][:200])
        return True
    after = local_version()
    if "Already up to date" in pull.stdout or before == after:
        print(f"[update] Already current (v{after}).")
    else:
        print(f"[update] Updated via git: v{before} -> v{after}.")
    return True


def try_download() -> None:
    """Standalone install (not a git checkout): pull latest skill files from GitHub."""
    before = local_version()
    url = f"https://codeload.github.com/{REPO}/tar.gz/refs/heads/{BRANCH}"
    try:
        with tempfile.TemporaryDirectory() as td:
            tarball = Path(td) / "repo.tar.gz"
            urllib.request.urlretrieve(url, tarball)
            with tarfile.open(tarball) as t:
                try:
                    t.extractall(td, filter="data")  # py3.12+ safe extraction
                except TypeError:
                    t.extractall(td)
            roots = [p for p in Path(td).iterdir() if p.is_dir() and p.name != "__MACOSX"]
            if not roots:
                print(f"[update] download empty; continuing with local version v{before}.")
                return
            src = roots[0] / SKILL_SUBPATH
            if not src.exists():
                print(f"[update] skill not found in download; continuing with v{before}.")
                return
            for item in src.rglob("*"):
                dest = SKILL_DIR / item.relative_to(src)
                if item.is_dir():
                    dest.mkdir(parents=True, exist_ok=True)
                else:
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(item, dest)
        after = local_version()
        if before == after:
            print(f"[update] Already current (v{after}).")
        else:
            print(f"[update] Updated from GitHub: v{before} -> v{after}.")
    except Exception as exc:  # offline, DNS, etc.
        print(f"[update] couldn't check for updates ({type(exc).__name__}); "
              f"continuing with local version v{before}.")


def main() -> None:
    if not try_git():
        try_download()


if __name__ == "__main__":
    main()
