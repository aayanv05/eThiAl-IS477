# Evolution of Musical Characteristics in Popular Spotify Tracks

## Contributors

- Aayan Verma
- Tarini Patel

# Summary 
This project explores how the sonic fabric of popular music has shifted over time by analyzing two complementary Spotify datasets: a curated high-popularity subset and a broader 114k-track Spotify universe. The goal is to understand what audio features correlate with popularity, how those features evolve across decades, and whether machine learning can meaningfully predict a track’s success using only its acoustic signature.
After loading, inspecting, and profiling both datasets, we standardized their schema, derived temporal variables (year and decade), and merged them for comparison. The high-popularity dataset spans 1,686 tracks with 28 columns, while the full dataset contains 113,999 tracks and 24 columns. This size difference provides a useful distinction: the HP dataset reflects what becomes popular, while the larger dataset captures the full spectrum of Spotify’s archive.

Our analysis reveals that speechiness shows the strongest negative correlation with popularity (−0.138), hinting that highly lyrical or spoken-word-heavy tracks may receive less mainstream traction on average. Conversely, loudness(0.083) and tempo (~0.017) have mild positive correlations with popularity, though none are strong signals. This supports existing literature suggesting that Spotify’s popularity metric is multifactorial and algorithmically layered, not purely dependent on musical properties alone.

Decade-level trends were particularly revealing. From the 1960s to the 2020s, danceability, energy, and valence have steadily increased, pointing toward a broad cultural shift favoring rhythm-forward, upbeat production. Loudness increased dramatically through the 1990s and 2000s, reflecting the well-documented “loudness war,” before leveling out in the 2010s and beyond. Tempo remained surprisingly stable across decades, suggesting that while textures and energy levels evolved, the fundamental pacing of popular music did not.
To test whether popularity is predictable, we trained a simple baseline classifier distinguishing “popular” vs “not popular” tracks using core audio features. Performance was modest. This aligns with expectations: popularity is a social and algorithmic construct, shaped by playlisting, virality, and cultural context as much as by sound. Still, some features—loudness, energy, danceability—demonstrated higher feature importance scores, reinforcing their role in modern hit-making.

Overall, the project highlights that musical attributes do evolve consistently over time, and some features show mild associations with popularity. However, audio features alone cannot fully explain why certain songs resonate globally while others disappear into the streaming void. This insight paves the way for future work incorporating lyrical sentiment, playlist exposure, and network effects from social media virality.

# Data Profile 

Datasets Used
1. High-Popularity Spotify Dataset
Shape: 1,686 tracks, 28 columns

Source: Kaggle (Maharshi Pandya “Spotify Tracks Dataset”)


Contains detailed audio features (energy, danceability, valence, etc.), popularity scores, release dates, and metadata.

2. Full Spotify Dataset (Universe Dataset)
Shape: 113,999 tracks, 24 columns
Source: Kaggle (114k Spotify tracks; subset filtered during cleaning)
Contains broader track metadata with extensive artist coverage and genre labels.

Data Sources, Storage, & Access
Ethical Considerations
No personal listener data is included.

All track metadata is publicly accessible via Kaggle or generated via Spotify API rules.
Copyrighted audio is not distributed; only metadata and derived numerical attributes are included.
All uses comply with Kaggle dataset licenses and Spotify’s Developer Terms.

Licensing Notes
Kaggle datasets follow Creative Commons licensing requiring attribution.
Spotify metadata must not be redistributed for commercial use.


**Download datasets from Box and place in:**  
`data/cleaned/`

# Data Quality 

Ensuring data quality was a central component of our analysis, particularly because the two datasets we integrated—the “Hit Parade” curated subset and the larger Spotify track dataset—were collected from different sources, contained heterogeneous formats, and represented music spanning nearly a century. This section outlines our procedures for assessing missingness, cleaning and validating fields, enforcing consistent ranges, and acknowledging the limitations that remain after processing.

### **Missing Data**

Across both datasets, several columns contained missing or inconsistent values. Release years were among the most common problem fields; some were missing entirely, while others appeared as invalid strings or ambiguous entries (e.g., “0000,” “196?”, or blank values). Since release year is a foundational variable for almost every historical trend analysis, we treated this as a critical missingness issue. Additionally, audio feature columns such as key, mode, and time_signature sometimes contained nulls or values that fell outside their admissible class categories. Several tracks also exhibited invalid numeric values in tempo, loudness, or duration fields—for example, negative durations resulting from import errors or loudness values outside the expected −60 to 0 dB range.

To ensure high data integrity, we relied on a systematic approach: rows that were entirely unusable (e.g., missing both release year and release date) were dropped; fields with partial missingness were coerced to standard formats; and numeric columns were normalized using robust type enforcement. Date fields were converted using `pd.to_datetime` with `errors="coerce"`, which automatically transformed malformed dates into NaT values, enabling us to identify and isolate records needing further cleaning.

### **Cleaning Steps**

Once missingness and data type issues were identified, we applied a structured cleaning workflow grounded in reproducible transformation steps.

1. **Duplicate Removal**:
   Because Spotify’s APIs and user-generated metadata often introduce duplicate entries, we removed duplicates using both a unique identifier (`track_id`) and a composite key consisting of `(track_name, artist, duration_ms)`. This eliminated re-released versions and redundant entries while preserving special editions when they differed meaningfully in duration or metadata.

2. **Date and Time Normalization**:
   After converting release dates to datetime objects, we extracted the year and decade for use in temporal aggregation. Tracks with unresolvable dates were removed only if they were also missing key analytical attributes, ensuring that we preserved as much historically meaningful data as possible.

3. **Value Range Enforcement**:
   Spotify’s audio features follow expected numeric boundaries. To enforce validity:

   * **Danceability, valence, and energy** values were restricted to the range [0, 1].
   * **Loudness** values were constrained to [−60, 0] dB.
   * **Tempo** values outside 40–250 BPM were considered erroneous, as they typically resulted from parsing errors or missing decimal points.
     Tracks falling outside these ranges were either corrected (if systematic) or removed.

4. **Categorical Validation**:
   Key, mode, and time_signature were validated against known categories. Any entries outside Spotify’s defined classes were flagged and addressed via imputation, removal, or category normalization.

These cleaning steps produced a streamlined, structurally consistent dataset suitable for cross-decade comparisons and predictive modeling.

### **Validity Checks**

To confirm the integrity of cleaned data, we conducted a series of validity and sanity checks. Extracted years were plotted to ensure the distribution aligned with historical expectations—specifically, an increase in track density from the 1960s onward and a tapering of data before 1950 due to limited digitized content. Decade-level patterns generated from audio features were then compared with known music history trends, such as the rise of danceability and energy beginning in the disco era, and greater acousticness in earlier decades. These consistent patterns confirmed that our date parsing and feature validation were working as intended.

Additionally, distributions and correlations between features revealed no structural anomalies. For example, tracks with extremely high energy appropriately correlated with higher loudness, and acoustic tracks displayed lower loudness and lower danceability, matching expectations from signal processing principles.

### **Profiled Feature Ranges**

Analyzing feature distributions further demonstrated internal coherence. Speechiness exhibited a strong right skew, showing that most commercial music contains low levels of spoken-word components. Energy, danceability, and valence clustered around mid-to-high ranges, consistent with patterns in modern pop and electronic music. Tempo distributions displayed a long right tail, driven largely by high-BPM genres such as EDM, trance, and hardcore.

These profiled ranges helped confirm that the cleaned dataset was both reliable and representative of real musical patterns.

### **Limitations**

Despite extensive cleaning, several inherent limitations remain. Spotify’s popularity metric is dynamic and changes over time based on user engagement, making it difficult to compare popularity across decades. Genre labels vary widely in consistency because Spotify assigns genres at the artist level rather than the track level, leading to coarse or sometimes misleading categorizations. Historical data, especially pre-1980, is sparse and biased toward well-preserved or re-released recordings. Finally, popularity cannot be normalized across eras because Spotify has revised its internal scoring methods over time.

These limitations do not invalidate our analyses but do shape the interpretability of long-term musical trends and predictive models.

# Findings

Our analysis uncovered several key insights about musical evolution, audio characteristics, and their relationship to popularity on Spotify. By examining feature correlations, decade-level summaries, and a baseline machine learning model, we identified consistent structural patterns in how music has changed over time and how listeners engage with it. While audio features alone cannot fully explain popularity, they provide meaningful clues about broader cultural and production trends.


1. Feature Correlations with Popularity
Correlation analysis revealed relatively weak linear relationships between audio features and Spotify popularity scores. Speechiness showed a modest negative correlation of approximately −0.138, indicating that tracks with a higher proportion of spoken-word elements—including rap, dialogue, or interludes—tend to have slightly lower popularity on the platform. This aligns with Spotify’s mainstream audience preferences, which often favor melodic or rhythm-heavy songs over spoken formats.
Loudness demonstrated a mild positive correlation (+0.083), suggesting that highly produced, punchier tracks tend to perform somewhat better. This is consistent with the “loudness wars” trend in commercial music production, where tracks are engineered to sound fuller, brighter, and more attention-grabbing.
Tempo correlated only weakly with popularity (+0.017), indicating that pace alone has limited influence on listener engagement. More broadly, no audio feature exhibited a strong correlation (|r| > 0.2), a finding that reinforces the idea that popularity is shaped by complex social factors—such as marketing, algorithmic placement, artist visibility, playlist culture, and listener trends—beyond raw acoustic characteristics.


2. Evolution of Audio Features Across Decades
Decade-level aggregation revealed clear long-term trends in musical style and production. Danceability shows a steady upward trajectory from the 1960s to today, reflecting the growing influence of disco, pop, hip-hop, EDM, and dance-oriented genres. Energy and valence follow similar patterns, with both features rising notably through the 1990s and into the 2000s. These increases suggest a broader cultural shift toward brighter, high-energy, emotionally upbeat music.
Loudness underwent the most dramatic change, increasing sharply from the 1960s onward and peaking in the mid-2000s due to industry-wide competition to master tracks at increasingly high loudness levels. Although the industry has recently adjusted toward more dynamic range, contemporary music still remains significantly louder than recordings from earlier decades.
Tempo, in contrast, has remained remarkably stable over time. Its consistency indicates that pacing, unlike timbral or emotional characteristics, is not subject to drastic cultural or production-driven shifts. Modern tracks average around 120–125 BPM, closely aligned with dance and pop conventions that emphasize rhythmic accessibility.
Overall, the 2020s exhibit high values across several dimensions: danceability (~0.69), energy (~0.65), valence (~0.52), tempo (~122 BPM), and loudness (≈ −6.4 dB). These values reflect the contemporary preference for polished, energetic, streaming-optimized music.


3. Predicting Popularity
To explore whether audio features can predict popularity, we implemented a baseline machine learning classifier using the cleaned dataset. Overall predictive performance was modest, confirming that musical success on Spotify is influenced by far more than acoustic profiles. Nonetheless, certain features consistently ranked higher in importance—specifically loudness, energy, and danceability—indicating that engaging, high-energy songs tend to fare better on average.
The model’s limitations echo the broader correlation findings: popularity is not an inherent property of the audio signal. Instead, it emerges from cultural dynamics, playlist placement, social media trends, artist branding, and Spotify’s recommendation ecosystem. Machine learning results ultimately reinforce that while audio features contribute to listener perception, they represent only one layer of a much larger hit-making process.

# Future Work

While the current analysis provides a strong foundation for understanding long-term musical evolution and the relationship between audio features and popularity, there are several key areas where deeper, more advanced analyses would significantly enhance the project’s scope and insight. Future work should focus on expanding the dataset beyond acoustic features, incorporating lyrical content, applying modern unsupervised clustering techniques, experimenting with more sophisticated machine learning models, and integrating external cultural signals that influence musical success. Additionally, longitudinal modeling would help reveal how songs rise and fall in popularity over time.

### **Lyrics and NLP Integration**

One of the most impactful extensions involves incorporating lyrical data. While audio features offer valuable insights into musical texture and energy, lyrics capture emotional tone, narrative content, and cultural themes—dimensions that often impact listener engagement and long-term resonance. Integrating natural language processing (NLP) techniques would enable several new analytical directions.

First, sentiment analysis could quantify the emotional valence of lyrics, allowing comparisons between lyrical tone and the valence of the audio signal itself. This could reveal whether happy-sounding songs tend to use positive language or whether modern pop exhibits the common phenomenon of “sad lyrics over happy beats.” Topic modeling (using methods such as LDA or BERTopic) would help uncover recurring lyrical themes—such as love, heartbreak, ambition, rebellion, or social commentary—and how these themes evolve over decades. Additionally, measuring lexical complexity, vocabulary richness, rhyme density, and readability metrics would enable a more nuanced understanding of how songwriting complexity changes over time. Combining lyrical sentiment with acoustic features could strengthen predictive models and deepen cultural interpretations of music trends.

### **Genre Clustering Beyond Spotify Labels**

Spotify’s genre labels are known to be inconsistent, often assigned at the artist level and overly broad. Therefore, a promising direction for future work is the development of data-driven genre clusters using unsupervised learning. A workflow could begin with dimensionality reduction using PCA or UMAP on normalized audio embeddings, followed by clustering via algorithms such as KMeans or HDBSCAN.

These clusters would represent organic genre-like groupings derived from the acoustic characteristics of the tracks themselves. This approach would reduce reliance on flawed metadata and would likely reveal nuanced genre families—such as differentiating between multiple EDM subgenres, distinguishing acoustic indie folk from mainstream pop, or separating trap-influenced hip-hop from old-school rap based purely on sound. Once established, these genre clusters could be used to study how different clusters evolve over time, how they correlate with popularity, and whether certain sonic “families” are more resilient or trend-driven than others.

### **Advanced Machine Learning Modeling**

While the baseline machine learning models demonstrated the difficulty of predicting Spotify popularity from audio features alone, more sophisticated modeling approaches offer an opportunity to improve performance and uncover deeper patterns. Gradient-boosted tree models such as XGBoost or LightGBM could capture nonlinear interactions between features more effectively than standard classifiers. Neural networks, particularly those trained on embeddings from models like VGGish or CLMR, may learn richer representations of timbre, rhythm, and genre characteristics.

A particularly promising direction is multimodal modeling that combines lyrics, audio features, metadata, and possibly even album art or social context features. Such models would more realistically reflect how listeners engage with music—through both sound and meaning—and could potentially reveal why certain songs become hits while others with similar audio profiles do not. Even if predictive accuracy remains limited, feature importance analysis could highlight the relative contributions of different modalities.

### **Platform and Social Effects**

Popularity is not solely a function of musical characteristics; it is also driven by social and platform dynamics. Future analyses should compare Spotify popularity with performance metrics from Billboard, Apple Music, YouTube, or Shazam to identify platform-specific effects. Incorporating playlist placement—such as inclusion in Spotify’s editorial playlists or major algorithmic playlists—would provide insight into how recommendation systems amplify certain tracks. Additionally, modern virality often emerges from TikTok trends; even simple proxies such as TikTok sound usage counts or social media engagement metrics could dramatically strengthen explanatory models of how songs break into mainstream culture.

### **Longitudinal Popularity Decay**

Finally, future work should examine how popularity evolves over time using survival analysis techniques. Kaplan–Meier estimators and Cox proportional hazards models could reveal how long songs remain “hot” on the platform and which musical or lyrical traits prolong or shorten a track’s life cycle. This shift from snapshot analysis to time-dependent modeling would identify which features contribute to evergreen hits—songs that retain relevance for years—versus those that experience rapid boom-and-bust trajectories. Decay curves could also vary by genre cluster, allowing deeper insights into the life cycles of musically distinct communities.

# Reproducing This Project

### 1. Clone the repo

```bash
git clone <https://github.com/aayanv05/eThiAl-IS477.git>
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

### 6: Script Path
All the files in results/figures/ml path come from this script:

# Correlation Barplot (ML) - compute_correlations.py
IN = Path("data/final/merged_features.csv")
OUT = Path("results/figures/ml/correlation_barplot.png")

# Decade-Level Figures - decade_trends.py
IN = Path("data/final/merged_features.csv")
OUT_DIR = Path("results/figures/decade/")

# Distribution Plots - kde_popularity_distributions.py
IN = Path("data/final/merged_features.csv")
OUT_DIR = Path("results/figures/distributions/")

# Random Forest Feature Importance (ML) - fr_feature_importance.py
IN = Path("data/final/merged_features.csv")
OUT = Path("results/figures/ml/rf_feature_importance.png")

---

# References

- Maharshi Pandya, Spotify Tracks Dataset (Kaggle)
- Spotify Web API Documentation
- Python: pandas, numpy, scikit-learn, seaborn, matplotlib
- Snakemake Workflow Engine
- IS 477 Course Materials

# Contribution Statement

- **Aayan Verma:** cleaning, integration pipeline, Snakefile workflow, SQL analysis
- **Tarini Patel:** modeling, visualizations, writing, notebook analysis
- **Both:** EDA, quality assessment, project design, final synthesis
