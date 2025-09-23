import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

#  App title 
st.title("COVID-19 Publications Exploration")
st.write("Explore publications per year, by journal, and by source independently.")

# Load the data set and clip the number of rows used to 200,000
def load_data():
    df = pd.read_csv("cord_metadata_clean.csv", nrows=200000)
    if "publish_time" in df.columns:
        df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
        df["publish_year"] = df["publish_time"].dt.year
    return df

df = load_data()


#  Publications per Year visualisation

st.subheader("Publications per Year")

if "publish_year" in df.columns:
    # Clean invalid years
    pubs_per_year = df.dropna(subset=["publish_year"])
    pubs_per_year = pubs_per_year[pubs_per_year["publish_year"].between(1900, 2025)]

    min_year = int(pubs_per_year["publish_year"].min())
    max_year = int(pubs_per_year["publish_year"].max())
    year_range = st.slider(
        "Select publication year range:",
        min_year, max_year,
        (min_year, max_year),
        key="year_slider"
    )

    # Apply year filter
    pubs_filtered = pubs_per_year[
        (pubs_per_year["publish_year"] >= year_range[0]) &
        (pubs_per_year["publish_year"] <= year_range[1])
    ]

    pubs_counts = pubs_filtered["publish_year"].value_counts().sort_index()


#Plot the data
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x=pubs_counts.index, y=pubs_counts.values, palette="viridis", ax=ax)
ax.set_xlabel("Year")
ax.set_ylabel("Number of Publications")
ax.set_title("Publications per Year")


plt.xticks(rotation=45)

st.pyplot(fig)


#  Publications by Journal Visualisation

st.subheader("Publications by Journal")

if "journal" in df.columns:
    top_journals = df["journal"].value_counts().head(50).index.tolist()
    selected_journals = st.multiselect("Select journals to display:", top_journals, default=top_journals[:10], key="journal_select")

    journal_counts = df[df["journal"].isin(selected_journals)]["journal"].value_counts()
    fig, ax = plt.subplots(figsize=(10,6))
    sns.barplot(x=journal_counts.values, y=journal_counts.index, palette="magma", ax=ax)
    ax.set_xlabel("Number of Publications")
    ax.set_ylabel("Journal")
    ax.set_title("Publications by Journal")
    st.pyplot(fig)


#  Publications by Source visualisation

st.subheader("Publications by Source")

if "source_x" in df.columns:
    top_sources = df["source_x"].value_counts().head(20).index.tolist()
    selected_sources = st.multiselect("Select sources to display:", top_sources, default=top_sources, key="source_select")

    source_counts = df[df["source_x"].isin(selected_sources)]["source_x"].value_counts()
    fig, ax = plt.subplots(figsize=(10,6))
    sns.barplot(x=source_counts.values, y=source_counts.index, palette="coolwarm", ax=ax)
    ax.set_xlabel("Number of Publications")
    ax.set_ylabel("Source")
    ax.set_title("Publications by Source")
    st.pyplot(fig)


#  Word Cloud of Paper Titles 

st.subheader("Word Cloud of Paper Titles")

if "title" in df.columns:
    # Combine all titles into one string
    text = " ".join(title for title in df["title"].dropna().astype(str))

    # Generate word cloud with 
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color="white",
        stopwords=set(STOPWORDS),
        colormap="viridis"
    ).generate(text)

    # Plot in Streamlit
    fig, ax = plt.subplots(figsize=(10,5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)
else:
    st.warning("Column 'title' not found in dataset.")
