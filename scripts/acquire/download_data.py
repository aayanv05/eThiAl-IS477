import os
from pathlib import Path
import hashlib

BASE = Path("data/cleaned")
FILES = [
    "High-Popularity-Spotify-Data-Cleaned.csv",
    "Spotify-Tracks-Dataset-Cleaned.csv"
]

def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    missing = [f for f in FILES if not (BASE / f).exists()]
    if missing:
        raise FileNotFoundError(f"Missing files: {', '.join(missing)}")

    for f in FILES:
        p = BASE / f
        print(f"{f}: size={p.stat().st_size}, sha256={sha(p)}")

if __name__ == "__main__":
    main()
