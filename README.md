# 🎬 Content-Based Movie Recommendation System

##  Project Overview

This project implements a **content-based recommendation system** that suggests similar movies based on textual information such as movie overviews.  
The system was built as part of an end-to-end ML workflow including:

- Data preprocessing
- Text vectorization using TF-IDF
- Similarity computation
- Recommendation generation
- Streamlit application development
- GitHub version control
- Deployment on Render

The goal of this assignment was to understand how a real-world recommendation pipeline moves from experimentation to deployment.

---

## Dataset

Dataset used: **TMDB 5000 Movie Dataset**

Kaggle Link:  
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

Dataset contains:
- Movie titles
- Overview (text description)
- Metadata used for similarity comparison

---

## System Workflow

### Part 1 — Data Preprocessing
- Loaded dataset using Pandas
- Handled missing values
- Converted text to lowercase
- Removed punctuation and stopwords
- Stored cleaned text in `clean_text` column

### Part 2 — Text Vectorization
- Used **TF-IDF Vectorizer**
- Limited features to control memory usage
- Converted movie descriptions into numerical vectors

### Part 3 — Similarity Computation
- Used cosine similarity to measure closeness between movie descriptions
- Recommendations are generated based on highest similarity scores

### Part 4 — Streamlit Application
- Dropdown to select a movie
- Button to generate recommendations
- Displays recommended movies with similarity scores

### Part 5 — Version Control
- Project managed using Git & GitHub
- Structured repository with reproducible setup

### Part 6 — Deployment
- Application deployed on Render platform

---

## Live Deployment

🔗 **GitHub Repository:**  
https://github.com/Kiruthigamutharasu/A20_recommendation-system

🔗 **Render Deployed App:**  
https://a20-recommendation-system.onrender.com

🔗 **Kaggle Dataset:**  
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

---

## Observations

During development, I observed several important points:

- Raw text produced noisy recommendations; preprocessing significantly improved similarity quality.
- Removing stopwords reduced dominance of common words.
- TF-IDF worked well because it highlights important descriptive terms.
- Cosine similarity is effective for text comparison since it focuses on direction rather than magnitude.
- Movies with detailed descriptions generate better recommendations than short summaries.
- Deployment environments behave differently from local environments, especially regarding file paths and memory usage.

---

##  Challenges Faced

### 1. Preprocessing Consistency
Initially, preprocessing was applied only in the notebook and not in the app.  
This caused different recommendation outputs.  
I fixed this by reusing the same preprocessing logic inside `app.py`.

---

### 2. Deployment Path Issues
The dataset loaded locally but failed during deployment due to relative path differences.  
This was solved by dynamically resolving file paths using Python's `os` module.

---

### 3. Memory Limit on Render Free Tier
Creating a full cosine similarity matrix consumed high memory and caused service restarts.  
To resolve this:
- Reduced TF-IDF feature size
- Computed similarity only when required instead of storing the full matrix.

---

### 4. Notebook Upload Issues
The notebook initially appeared invalid on GitHub due to incomplete JSON saving.  
Re-saving and recommitting fixed the issue.

---

##  Why TF-IDF?

TF-IDF was chosen because:
- Simple and interpretable
- Lightweight compared to deep embeddings
- Works well for content-based filtering
- Suitable for assignment constraints

---

## Limitations

- Does not consider user preferences (no collaborative filtering)
- Cold-start problem for new items
- Depends heavily on text quality
- Recommendations are similarity-based, not personalized

---

## Future Improvements

- Add collaborative filtering
- Use sentence embeddings (BERT)
- Add genre/year filters
- Improve explanation of recommendations

---

##  How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py

**Proof of Execution**

Screenshots included in screenshots/ folder:

Local application output
GitHub repository proof
Render deployment proof

Conclusion

This project helped me understand the complete lifecycle of a machine learning application — from preprocessing and modeling to deployment and handling real-world constraints such as memory limits and environment differences.