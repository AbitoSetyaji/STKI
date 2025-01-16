import streamlit as st
import gensim
from gensim.models import Word2Vec

# Load Word2Vec model
@st.cache_resource
def load_model(model_path):
    return gensim.models.KeyedVectors.load(model_path)

# Search functionality
def search_similar_words(model, query, top_n=10):
    try:
        results = model.most_similar(query, topn=top_n)
        return results
    except KeyError:
        return None

# Streamlit app
st.title("Search Engine with Word2Vec")

# Load model
model_path = "word2vec_model.model"
model = load_model(model_path)

# User input query
query = st.text_input("Enter a word or phrase to search:")

# Results display
if query:
    st.write(f"Results for: '{query}'")
    results = search_similar_words(model, query)
    if results:
        for word, similarity in results:
            st.write(f"{word}: {similarity:.4f}")
    else:
        st.write("No similar words found or word not in vocabulary.")

st.write("\n\nUpload your Word2Vec model as 'word2vec_model.model' for customization!")
