## 📊 Observations

During the development of this content-based recommendation system, I observed the following:

- Text preprocessing has a significant impact on recommendation quality. When I initially tested with raw text, many unrelated movies appeared in recommendations.
- Converting text to lowercase and removing punctuation helped reduce duplicate word representations.
- Removing stopwords improved similarity results because common words like "the", "is", and "and" were dominating TF-IDF scores.
- Using bigrams (ngram_range=(1,2)) slightly improved recommendations because phrases like "space mission" or "love story" were captured instead of individual words.
- Cosine similarity worked well because it measures semantic closeness between movie descriptions rather than text length.
- Movies with very short overviews sometimes produced weaker recommendations due to limited textual information.

---

## ⚠️ Challenges Faced

While building this project, I faced several practical challenges:

1. **Preprocessing Consistency**
   - Initially, preprocessing was applied in the notebook but not in the Streamlit app.
   - This caused different recommendation results.
   - I solved this by reusing the same cleaning function in both notebook and app.py.

2. **NLTK Stopwords Issue**
   - During Streamlit execution, stopwords were downloading repeatedly.
   - I handled this using a conditional download check.

3. **Handling Missing Data**
   - Some movies had missing overview values.
   - This caused vectorization errors.
   - I replaced missing values with empty strings.

4. **Deployment Errors**
   - Render deployment initially failed because the port number was not specified.
   - Adding a Procfile with the correct start command fixed the issue.

5. **Understanding TF-IDF Parameters**
   - Choosing max_features and ngram_range required experimentation to balance performance and recommendation quality.

---

## 🧠 Learning Outcomes

Through this assignment, I learned:

- End-to-end ML workflow from preprocessing to deployment.
- Importance of consistent data pipelines between experimentation and production apps.
- How TF-IDF converts text into numerical vectors.
- Why cosine similarity is commonly used for text-based recommendation systems.
- Basics of deploying ML applications using Streamlit and Render.
- Version control workflow using Git and GitHub.

---

## 🚧 Limitations of the System

- This is a content-based system and does not learn from user behavior.
- Cold-start problem exists for new items with limited descriptions.
- Recommendations depend heavily on text quality.
- Collaborative filtering could improve personalization in future work.