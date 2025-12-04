# Evolution of Musical Characteristics in Popular Spotify Tracks

## Contributors

- Aayan Verma
- Tarini Patel

---

# Summary (500–1000 words)

_(You will fill this section with your narrative. Use your status report + notebook outputs.)_

---

# Data Profile (500–1000 words)

Describe:

- Each dataset used (HP dataset + Full Spotify dataset)
- Links, sources, sizes
- Ethical considerations
- Licensing notes
- Mention Box link for cleaned data

**Download datasets from Box and place in:**  
`data/cleaned/`

---

# Data Quality (500–1000 words)

Include:

- Missing data analysis
- Cleaning steps
- Duplicates removed
- Validity checks
- Type enforcement
- Profiled ranges & distributions
- Limitations

---

# Findings (~500 words)

Summaries of:

- Feature correlations
- Decade trends
- Genre-level differences
- ML model results
- Popularity difference vs years since release  
  Use figures from `results/figures/`.

---

# Future Work (500–1000 words)

Examples:

- Incorporate lyrics analysis
- Genre clustering
- More advanced ML models
- Platform effects
- Longitudinal streaming behavior

---

# Reproducing This Project

### 1. Clone the repo

```bash
git clone <your_repo_url>
cd is477-project
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Download cleaned data from Box

Place these files into:

```
data/cleaned/
  High-Popularity-Spotify-Data-Cleaned.csv
  Spotify-Tracks-Dataset-Cleaned.csv
```

### 4. Run the full workflow

```bash
bash run_all.sh
```

This produces:

- `data/final/merged_features.csv`
- Plots in `results/figures/`
- Summary tables in `results/tables/`

### 5. Open and run the notebook interactively

```bash
jupyter notebook notebooks/is477project.ipynb
```

---

# References

- Maharshi Pandya, Spotify Tracks Dataset (Kaggle)
- Spotify Web API Documentation
- Python: pandas, numpy, scikit-learn, seaborn, matplotlib
- Snakemake Workflow Engine
- IS 477 Course Materials

---

# Contribution Statement

- **Aayan Verma:** cleaning, integration pipeline, Snakefile workflow, SQL analysis
- **Tarini Patel:** modeling, visualizations, writing, notebook analysis
- **Both:** EDA, quality assessment, project design, final synthesis
