import streamlit as st
from gensim.models import Word2Vec

# Load the Word2Vec model
@st.cache_resource
def load_model(file_path):
    return Word2Vec.load(file_path)

# File path to the uploaded model
model_file = "/mnt/data/word2vec_model.model"
model = load_model(model_file)

# Streamlit UI/UX
st.title("Simple Search Engine")
st.write("Enter a word to find related terms based on the Word2Vec model.")

# Input field
query = st.text_input("Search query", "")

if query:
    try:
        # Fetch similar words
        similar_words = model.wv.most_similar(query)
        st.write("Results:")
        for word, score in similar_words:
            st.write(f"- **{word}**: {score:.4f}")
    except KeyError:
        st.error(f"The word '{query}' is not in the model's vocabulary.")
