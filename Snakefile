from pathlib import Path
from snakemake.exceptions import WorkflowError

if not (Path("data/cleaned/High-Popularity-Spotify-Data-Cleaned.csv").exists() and
        Path("data/cleaned/Spotify-Tracks-Dataset-Cleaned.csv").exists()):
    raise WorkflowError("Missing cleaned input datasets. Place them in data/cleaned/")

#if this comment is seen, we utilized AI to help us figure out how to generate multiple images from one script
rule all:
    input:
        expand("results/figures/ml/{plot}.png",
               plot=["correlation_barplot", "rf_feature_importance"]),
        expand("results/figures/decade/{plot}.png",
               plot=[
                   "danceability_hp_by_decade",
                   "energy_hp_by_decade",
                   "valence_hp_by_decade",
                   "tempo_hp_by_decade",
                   "loudness_hp_by_decade",
                   "acousticness_hp_by_decade"
               ]),
        expand("results/figures/distributions/{plot}.png",
               plot=[
                   "danceability_hp_kde",
                   "energy_hp_kde",
                   "valence_hp_kde",
                   "tempo_hp_kde",
                   "loudness_hp_kde",
                   "acousticness_hp_kde"
               ]),
        "results/tables/merged_features_sample.csv"

rule merge_and_engineer:
    input:
        hp="data/cleaned/High-Popularity-Spotify-Data-Cleaned.csv",
        sp="data/cleaned/Spotify-Tracks-Dataset-Cleaned.csv"
    output:
        "data/final/merged_features.csv"
    script:
        "scripts/integrate/merge_and_align.py"

rule correlations:
    input: "data/final/merged_features.csv"
    output: "results/figures/ml/correlation_barplot.png"
    script: "scripts/analyze/compute_correlations.py"

rule rf_importance:
    input: "data/final/merged_features.csv"
    output: "results/figures/ml/rf_feature_importance.png"
    script: "scripts/analyze/rf_feature_importance.py"

rule decade_trends:
    input: "data/final/merged_features.csv"
    output:
        expand("results/figures/decade/{col}_by_decade.png",
               col=[
                   "danceability_hp",
                   "energy_hp",
                   "valence_hp",
                   "tempo_hp",
                   "loudness_hp",
                   "acousticness_hp"
               ])
    script: "scripts/analyze/decade_trends.py"

rule kde_distributions:
    input: "data/final/merged_features.csv"
    output:
        expand("results/figures/distributions/{col}_kde.png",
               col=[
                   "danceability_hp",
                   "energy_hp",
                   "valence_hp",
                   "tempo_hp",
                   "loudness_hp",
                   "acousticness_hp"
               ])
    script: "scripts/analyze/kde_popularity_distributions.py"

rule export_sample:
    input: "data/final/merged_features.csv"
    output: "results/tables/merged_features_sample.csv"
    shell:
        "mkdir -p results/tables && head -n 100 {input} > {output}"
