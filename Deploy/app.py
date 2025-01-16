import streamlit as st
from gensim.models import Word2Vec

# Load the Word2Vec model
@st.cache_resource
def load_model(file_path):
    try:
        model = Word2Vec.load(file_path)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

# File path to the uploaded model
model_file_path = '/mnt/data/word2vec_model.model'
model = load_model(model_file_path)

# Streamlit UI
st.title("Search Engine with Word2Vec Model")

if model:
    st.subheader("Enter a word to find similar terms")
    query = st.text_input("Search query:")

    if query:
        try:
            # Fetch the most similar words
            results = model.wv.most_similar(query, topn=10)
            st.subheader("Results")
            for word, similarity in results:
                st.write(f"{word}: {similarity:.4f}")
        except KeyError:
            st.error("Word not found in the vocabulary. Please try another word.")
else:
    st.error("Failed to load the model. Please check the uploaded file.")
