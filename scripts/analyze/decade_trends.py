import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

IN = Path("data/final/merged_features.csv")
OUT_DIR = Path("results/figures/decade/")

def main():
    df = pd.read_csv(IN)
    df["decade"] = (df["release_year_hp"] // 10) * 10

    agg_cols = [
        "danceability_hp", "energy_hp", "valence_hp", "tempo_hp",
        "loudness_hp", "acousticness_hp"
    ]

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    decade_trends = df.groupby("decade")[agg_cols].mean().reset_index()

    for col in agg_cols:
        plt.figure(figsize=(6, 4))
        sns.lineplot(data=decade_trends, x="decade", y=col, marker="o")
        plt.title(f"{col} by decade (high-popularity dataset)")
        plt.tight_layout()
        plt.savefig(OUT_DIR / f"{col}_by_decade.png", dpi=200)
        plt.close()

if __name__ == "__main__":
    main()
