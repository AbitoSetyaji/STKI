import streamlit as st
import gensim

# Load the Word2Vec model
@st.cache_resource
def load_model():
    return gensim.models.Word2Vec.load("/mnt/data/word2vec_model.model")

# Initialize model
model = load_model()

# UI/UX setup
st.set_page_config(page_title="Semantic Search Engine", layout="centered")
st.title("Semantic Search")
st.write("Search the most relevant words based on your input")

# Search bar
query = st.text_input("Enter a word or phrase:", placeholder="Type something here...")

if query:
    try:
        # Find similar words using Word2Vec model
        results = model.wv.most_similar(query, topn=10)
        
        st.subheader("Results:")
        for word, score in results:
            st.write(f"{word}: {score:.4f}")
    except KeyError:
        st.error("The word you entered is not in the vocabulary of the model.")
