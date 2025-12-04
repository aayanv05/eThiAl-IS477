# Data Dictionary

## Dataset 1: High-Popularity Spotify Tracks (Cleaned)

- **track_id:** Unique Spotify track ID
- **track_artist:** Artist name
- **track_name:** Track name
- **track_popularity:** Popularity metric (0–100)
- **track_album_release_date:** Release date
- **audio features:** danceability, energy, valence, tempo, etc.

## Dataset 2: Spotify Tracks Dataset (Cleaned)

- **id:** Row ID
- **track_id:** Unique Spotify track ID (join key)
- **popularity:** Popularity on full dataset
- **playlist_genre:** Genre label
- **audio features:** danceability, energy, valence, loudness, tempo, etc.

## Output Dataset: merged_features.csv

- All columns from both datasets
- **release_year_hp:** Extracted year
- **years_since_release:** 2023 - release year
- **popularity_difference:** popularity_hp - popularity_sp
