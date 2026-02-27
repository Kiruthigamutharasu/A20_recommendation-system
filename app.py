# ===================================================
# PART 4 — STREAMLIT APP
# ===================================================

# TASK 6 — Build UI using Streamlit

# Step 1: Import libraries
import streamlit as st
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
import nltk

# I am downloading stopwords here so deployment works
nltk.download('stopwords')

# Step 2: Load dataset safely
try:
    df = pd.read_csv("data/tmdb_5000_movies.csv")
except Exception as e:
    st.error("Dataset not found. Please check file path.")
    st.stop()

df = df[['title','overview']]
df['overview'] = df['overview'].fillna("")

# Step 3: SAME preprocessing as notebook
# I reused same logic to keep vector space consistent

stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

df['clean_text'] = df['overview'].apply(clean_text)

# Step 4: Vectorization
tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1,2))
tfidf_matrix = tfidf.fit_transform(df['clean_text'])

# Step 5: Similarity
similarity = cosine_similarity(tfidf_matrix)

# Step 6: Recommendation function
def recommend(movie_name):

    if movie_name not in df['title'].values:
        return []

    idx = df[df['title']==movie_name].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x:x[1], reverse=True)[1:6]

    return [(df.iloc[i[0]].title, round(i[1],3)) for i in scores]

# ---------------- UI ----------------

st.title(" Movie Recommendation System")

selected_movie = st.selectbox(
    "Choose a Movie",
    df['title'].values
)

if st.button("Recommend"):

    try:
        results = recommend(selected_movie)

        if len(results)==0:
            st.warning("No recommendations found")

        for movie, score in results:
            st.write(f" {movie}  (Similarity: {score})")

    except Exception as e:
        st.error("Something went wrong during recommendation.")