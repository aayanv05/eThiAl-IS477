import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

IN = Path("data/final/merged_features.csv")
OUT = Path("results/figures/ml/correlation_barplot.png")

def main():
    df = pd.read_csv(IN)

    feature_cols = [
        "danceability_hp", "energy_hp", "valence_hp", "tempo_hp",
        "loudness_hp", "acousticness_hp", "instrumentalness_hp",
        "speechiness_hp", "liveness_hp"
    ]

    corr = (
        df[feature_cols + ["popularity_hp"]]
        .corr()["popularity_hp"]
        .drop("popularity_hp")
        .sort_values(ascending=False)
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(6, 6))
    sns.barplot(x=corr.values, y=corr.index)
    plt.xlabel("Correlation with track_popularity")
    plt.ylabel("Feature")
    plt.tight_layout()
    plt.savefig(OUT, dpi=200)

if __name__ == "__main__":
    main()
