import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="Netflix Content Analysis",
    page_icon="🎬",
    layout="wide"
)

# -----------------------------
# Load data
# -----------------------------

df = pd.read_csv("data/netflix_titles.csv")

# -----------------------------
# Data cleaning
# -----------------------------

df = df.drop_duplicates()

df["date_added"] = pd.to_datetime(
    df["date_added"],
    errors="coerce"
)

df["added_year"] = df["date_added"].dt.year

for col in ["director", "cast", "country", "rating", "duration"]:
    df[col] = df[col].fillna("Unknown")


# -----------------------------
# Title
# -----------------------------

st.title("Netflix Content Library Analysis")

st.write(
    "An analysis of Netflix's publicly listed content library, "
    "focusing on content growth, content types, genres and countries."
)

st.divider()


# -----------------------------
# Key metrics
# -----------------------------

total_titles = len(df)

movies = (df["type"] == "Movie").sum()

tv_shows = (df["type"] == "TV Show").sum()

country_count = (
    df["country"]
    .str.split(", ")
    .explode()
    .nunique()
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Titles", f"{total_titles:,}")
col2.metric("Movies", f"{movies:,}")
col3.metric("TV Shows", f"{tv_shows:,}")
col4.metric("Countries", f"{country_count:,}")


# -----------------------------
# Question 1
# -----------------------------

st.header("1. How has Netflix's content library changed over time?")

yearly = (
    df.groupby("added_year")
      .size()
      .reset_index(name="titles_added")
)

fig, ax = plt.subplots(figsize=(12, 5))

sns.lineplot(
    data=yearly,
    x="added_year",
    y="titles_added",
    marker="o",
    ax=ax
)

ax.set_title("Netflix Titles Added Over Time")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Titles")
plt.xticks(rotation=45)

st.pyplot(fig)


# -----------------------------
# Question 2
# -----------------------------

st.header("2. What types and genres dominate Netflix's content library?")

type_counts = df["type"].value_counts()

fig, ax = plt.subplots(figsize=(7, 5))

sns.barplot(
    x=type_counts.index,
    y=type_counts.values,
    ax=ax
)

ax.set_title("Movies vs TV Shows")
ax.set_xlabel("Content Type")
ax.set_ylabel("Number of Titles")

st.pyplot(fig)


# Top genres

genres = (
    df["listed_in"]
    .dropna()
    .str.split(", ")
    .explode()
)

genre_counts = genres.value_counts().head(10)

fig, ax = plt.subplots(figsize=(10, 6))

sns.barplot(
    x=genre_counts.values,
    y=genre_counts.index,
    ax=ax
)

ax.set_title("Top 10 Netflix Genres")
ax.set_xlabel("Number of Titles")
ax.set_ylabel("Genre")

st.pyplot(fig)


# -----------------------------
# Question 3
# -----------------------------

st.header("3. Which countries contribute the most titles?")

countries = (
    df["country"]
    .dropna()
    .str.split(", ")
    .explode()
)

country_counts = countries.value_counts().head(10)

fig, ax = plt.subplots(figsize=(10, 6))

sns.barplot(
    x=country_counts.values,
    y=country_counts.index,
    ax=ax
)

ax.set_title("Top 10 Countries by Number of Netflix Titles")
ax.set_xlabel("Number of Titles")
ax.set_ylabel("Country")

st.pyplot(fig)


# -----------------------------
# Key Findings
# -----------------------------

st.header("Key Findings")

st.write(
    """
**1. Content growth:** Netflix's catalog additions varied across years,
showing periods of stronger and weaker catalog expansion.

**2. Content mix:** The catalog contains both Movies and TV Shows,
with Movies/TV Shows representing the larger share.

**3. Geographic distribution:** A relatively small group of countries
contributes a large number of titles to the catalog.
"""
)


# -----------------------------
# Limitations
# -----------------------------

st.header("Limitations")

st.write(
    """
- The dataset represents Netflix's catalog, not actual viewing figures.
- It does not contain revenue, subscriber or profitability data.
- A title can have multiple countries and genres.
- Missing categorical information cannot always be reliably inferred.
- The dataset represents a historical snapshot and may not reflect
  Netflix's current catalog.
"""
)