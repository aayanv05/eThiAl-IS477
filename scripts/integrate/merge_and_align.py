import pandas as pd
from pathlib import Path

HP_PATH = Path("data/cleaned/High-Popularity-Spotify-Data-Cleaned.csv")
SP_PATH = Path("data/cleaned/Spotify-Tracks-Dataset-Cleaned.csv")
OUT_PATH = Path("data/final/merged_features.csv")

def main():
    hp = pd.read_csv(HP_PATH)
    sp = pd.read_csv(SP_PATH)

    merged = hp.merge(sp, on="track_id", how="inner", suffixes=("_hp", "_sp"))

    release_cols = [c for c in merged.columns if "track_album_release_date" in c]
    release_col = release_cols[0]

    merged["release_date_parsed"] = pd.to_datetime(merged[release_col], errors="coerce")
    merged["release_year_hp"] = merged["release_date_parsed"].dt.year

    merged = merged.rename(columns={
        "track_popularity": "popularity_hp",
        "popularity": "popularity_sp"
    })

    merged["years_since_release"] = 2023 - merged["release_year_hp"]
    merged["popularity_difference"] = merged["popularity_hp"] - merged["popularity_sp"]

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    merged.to_csv(OUT_PATH, index=False)

if __name__ == "__main__":
    main()
