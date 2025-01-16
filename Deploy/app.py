import streamlit as st
from gensim.models import Word2Vec
import os

# Load Word2Vec Model
def load_model(model_path):
    if os.path.exists(model_path):
        return Word2Vec.load(model_path)
    else:
        st.error("Model file not found!")
        return None

# Retrieve documents based on query
def search_documents(query, model):
    # Check if the query is valid
    if not query:
        return []

    # Generate similar words using the model
    try:
        similar_words = model.wv.most_similar(query, topn=10)
        return [word for word, _ in similar_words]
    except KeyError:
        st.warning("Query not found in the vocabulary. Try a different word.")
        return []

# Streamlit UI
def main():
    st.title("Document Search Engine")
    st.markdown("### Search documents using a pre-trained Word2Vec model")

    # Load the model
    model_path = 'word2vec_model.model'  # Path to the uploaded model
    model = load_model(model_path)

    if model:
        # Input field for query
        query = st.text_input("Enter your search query:")

        # Search button
        if st.button("Search"):
            results = search_documents(query, model)
            if results:
                st.success("Results found!")
                st.write("### Top Results:")
                for i, result in enumerate(results, start=1):
                    st.write(f"{i}. {result}")
            else:
                st.warning("No results found.")

if __name__ == "__main__":
    main()
