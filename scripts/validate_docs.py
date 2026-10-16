"""Validate tracked platform documentation without contacting implementation services."""

import json
import re
import subprocess
import tomllib
from pathlib import Path
from urllib.parse import unquote, urlsplit


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        ["git", "ls-files", "-z"], cwd=root, capture_output=True, text=True, check=True
    )
    documents = 0
    for name in filter(None, result.stdout.split("\0")):
        path = root / name
        if path.suffix == ".toml":
            tomllib.loads(path.read_text())
        if path.suffix != ".md":
            continue
        documents += 1
        for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)(?:\s+[^)]*)?\)", path.read_text()):
            link = urlsplit(target.strip("<>"))
            if link.scheme or link.netloc or not link.path:
                continue
            destination = path.parent / unquote(link.path)
            if not destination.exists():
                raise SystemExit(f"Missing local documentation target in {name}: {link.path}")
    print(json.dumps({"status": "passed", "documents": documents}))


if __name__ == "__main__":
    main()
