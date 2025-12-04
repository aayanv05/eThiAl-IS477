import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

IN = Path("data/final/merged_features.csv")
OUT_DIR = Path("results/figures/distributions/")

def main():
    df = pd.read_csv(IN)

    df["is_popular"] = (df["popularity_hp"] >= df["popularity_hp"].median()).astype(int)

    pop = df[df["is_popular"] == 1]
    nonpop_base = df[df["is_popular"] == 0]

    sample_size = min(len(pop), len(nonpop_base))
    nonpop = nonpop_base.sample(n=sample_size, random_state=42)

    feature_cols = [
        "danceability_hp", "energy_hp", "valence_hp", "tempo_hp",
        "loudness_hp", "acousticness_hp"
    ]

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    for col in feature_cols:
        plt.figure(figsize=(6, 4))
        sns.kdeplot(pop[col], label="popular", fill=True)
        sns.kdeplot(nonpop[col], label="not popular", fill=True)
        plt.title(f"{col} distribution: popular vs not popular")
        plt.legend()
        plt.tight_layout()
        plt.savefig(OUT_DIR / f"{col}_kde.png", dpi=200)
        plt.close()

if __name__ == "__main__":
    main()
