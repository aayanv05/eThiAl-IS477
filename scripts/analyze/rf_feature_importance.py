import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from pathlib import Path

IN = Path("data/final/merged_features.csv")
OUT = Path("results/figures/ml/rf_feature_importance.png")

def main():
    df = pd.read_csv(IN)

    ml_features = [
        "danceability_hp", "energy_hp", "valence_hp", "tempo_hp",
        "loudness_hp", "acousticness_hp", "instrumentalness_hp",
        "speechiness_hp", "liveness_hp"
    ]

    df["is_popular"] = (df["popularity_hp"] >= df["popularity_hp"].median()).astype(int)

    X = df[ml_features]
    y = df["is_popular"]

    rf = RandomForestClassifier(random_state=42)
    rf.fit(X, y)

    importances = pd.Series(rf.feature_importances_, index=ml_features).sort_values()

    OUT.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(6, 6))
    sns.barplot(x=importances.values, y=importances.index)
    plt.xlabel("Feature importance")
    plt.tight_layout()
    plt.savefig(OUT, dpi=200)

if __name__ == "__main__":
    main()
