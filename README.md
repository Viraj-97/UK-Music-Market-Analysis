# UK Top 50 Playlist Market Structure Analysis Dashboard

## Project Overview

This project analyzes the structural composition of the United Kingdom Top 50 music playlist to provide market intelligence insights for Atlantic Recording Corporation. The analysis focuses on artist dominance, collaboration trends, explicit content distribution, and release format strategy.

The project includes data cleaning, exploratory data analysis, KPI calculation, and an interactive Streamlit dashboard for visualization.

---

## Business Objective

The goal of this project is to help Atlantic Recording Corporation understand the UK music market structure to improve:

- Artist signing strategy  
- Release format optimization (Single vs Album)  
- Collaboration planning  
- Content strategy  
- Market penetration  

---

## Dataset Description

The dataset contains daily UK Top 50 playlist data with the following fields:

- date — Playlist snapshot date  
- position — Playlist rank (1–50)  
- song — Track title  
- artist — Artist name(s)  
- popularity — Popularity score  
- duration_ms — Track duration  
- album_type — Single or Album  
- total_tracks — Number of tracks in album  
- is_explicit — Explicit content flag  

Dataset scale:

- Total Records: 27,800  
- Total Columns: 10  
- Time Coverage: 556 days  

---

## Key Performance Indicators (KPIs)

| KPI | Value |
|-----|------|
| Unique Artists | 366 |
| Artist Concentration Index | 0.0104 |
| Collaboration Ratio | 59.35% |
| Explicit Content Share | 36.92% |
| Single Release Ratio | 64.18% |

---

## Key Insights

- The UK music market is highly diverse with low artist concentration.
- Collaboration plays a major role, with over 59% of tracks involving multiple artists.
- Single releases dominate the market, accounting for over 64% of playlist entries.
- Explicit content represents a moderate share, indicating balanced listener sensitivity.
- The market structure supports both emerging and established artists.

---

## Dashboard Features

The Streamlit dashboard includes:

- Market KPI overview  
- Artist dominance leaderboard  
- Collaboration vs solo track analysis  
- Explicit vs clean content distribution  
- Single vs album release analysis  
- Track duration distribution  
- Interactive filters  

---

## Tools and Technologies Used

- Python  
- Pandas  
- Plotly  
- Streamlit  
- Jupyter Notebook  

---

## Project Structure

