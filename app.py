import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("cleaned_Atlantic_United_Kingdom.csv")
original = pd.read_csv("Atlantic_United_Kingdom.csv")

st.title("UK Music Market Analysis Dashboard")

# KPI SECTION
st.header("Market Overview")

unique_artists = df["artist_list"].nunique()
collab_ratio = original["artist"].str.contains("&|,").mean()
explicit_ratio = original["is_explicit"].mean()
single_ratio = (original["album_type"]=="single").mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Unique Artists", unique_artists)
col2.metric("Collaboration Ratio", f"{collab_ratio*100:.2f}%")
col3.metric("Explicit Content", f"{explicit_ratio*100:.2f}%")
col4.metric("Single Release Ratio", f"{single_ratio*100:.2f}%")

# ARTIST LEADERBOARD
st.header("Top Artists")

artist_counts = df['artist_list'].value_counts().head(10)

fig = px.bar(
    x=artist_counts.index,
    y=artist_counts.values,
    labels={"x":"Artist", "y":"Appearances"},
    title="Top 10 Artists"
)

st.plotly_chart(fig, use_container_width=True)

# EXPLICIT CONTENT
st.header("Explicit vs Clean Content")

explicit_counts = original["is_explicit"].map({
    True:"Explicit",
    False:"Clean"
}).value_counts()

fig2 = px.pie(
    values=explicit_counts.values,
    names=explicit_counts.index,
    title="Explicit Content Distribution"
)

st.plotly_chart(fig2)

# ALBUM TYPE
st.header("Single vs Album")

album_counts = original["album_type"].value_counts()

fig3 = px.pie(
    values=album_counts.values,
    names=album_counts.index,
    title="Album Type Distribution"
)

st.plotly_chart(fig3)
