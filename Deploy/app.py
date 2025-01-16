import streamlit as st
from gensim.models import Word2Vec

# Load Word2Vec model
model_path = "word2vec_model.model"
try:
    model = Word2Vec.load(model_path)
    st.success("Word2Vec model loaded successfully!")
except Exception as e:
    st.error(f"Error loading model: {e}")

# Streamlit UI
st.title("Search Engine UI/UX")
st.write("Welcome to the semantic search engine!")

# Search input
query = st.text_input("Enter your search query:")

# Process search query
if query:
    st.write(f"Results for: **{query}**")
    try:
        similar_words = model.wv.most_similar(query, topn=5)
        for word, score in similar_words:
            st.write(f"- {word} (score: {score:.2f})")
    except KeyError:
        st.error("Word not found in the model vocabulary. Please try another query.")
