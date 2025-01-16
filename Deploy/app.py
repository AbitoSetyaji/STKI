import streamlit as st
import gensim
from gensim.models import Word2Vec
import os

# Load Word2Vec model
@st.cache_resource
def load_model(model_path):
    return gensim.models.KeyedVectors.load(model_path)

# Load your Word2Vec model
model_path = 'word2vec_model.model'
if os.path.exists(model_path):
    model = load_model(model_path)
else:
    st.error("Word2Vec model not found. Please upload a valid model.")
    st.stop()

# Dummy document corpus
documents = [
    "Machine learning is fascinating.",
    "Natural Language Processing is a branch of AI.",
    "Streamlit makes it easy to build web apps.",
    "Word embeddings like Word2Vec help in semantic search.",
    "Python is a versatile programming language."
]

def search_documents(query, model, documents):
    """Perform semantic search using Word2Vec."""
    query_vector = model.infer_vector(query.split())
    scores = []
    for doc in documents:
        doc_vector = model.infer_vector(doc.split())
        similarity = model.wv.cosine_similarities(query_vector, [doc_vector])[0]
        scores.append((similarity, doc))
    scores = sorted(scores, key=lambda x: x[0], reverse=True)
    return scores

# Streamlit UI
st.title("Document Search Engine")
st.write("Search documents using semantic queries powered by Word2Vec.")

# Input query
query = st.text_input("Enter your search query:", "")

# Search button
if st.button("Search"):
    if query.strip():
        results = search_documents(query, model, documents)
        st.subheader("Search Results:")
        for score, doc in results:
            st.write(f"- {doc} (Score: {score:.4f})")
    else:
        st.warning("Please enter a query to search.")
