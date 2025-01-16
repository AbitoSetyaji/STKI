import streamlit as st
from gensim.models import Word2Vec, KeyedVectors

# Load the Word2Vec model
@st.cache_resource
def load_model():
    model_path = 'word2vec_model.model'  # Path to your uploaded model
    model = KeyedVectors.load(model_path)
    return model

model = load_model()

# Streamlit app layout
st.title("Simple Search Engine")
st.write("Enter a word or phrase, and the system will return related words.")

# User input
query = st.text_input("Enter your search query:", value="")

# Handle search
if st.button("Search"):
    if query.strip():
        try:
            # Get most similar words
            results = model.most_similar(query, topn=10)
            st.write(f"Top results for '{query}':")
            for word, similarity in results:
                st.write(f"{word} (Similarity: {similarity:.2f})")
        except KeyError:
            st.error(f"'{query}' not found in the model's vocabulary. Try another word.")
    else:
        st.warning("Please enter a search query.")
