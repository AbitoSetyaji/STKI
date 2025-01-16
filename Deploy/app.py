import streamlit as st
import gensim
import numpy as np

# Load the Word2Vec model
@st.cache_resource
def load_model():
    return gensim.models.Word2Vec.load("/mnt/data/word2vec_model.model")

# Function to calculate similarity
def calculate_similarity(query, documents, model):
    query_vec = np.mean([model.wv[word] for word in query.split() if word in model.wv], axis=0)
    similarities = []
    for doc in documents:
        doc_vec = np.mean([model.wv[word] for word in doc.split() if word in model.wv], axis=0)
        sim = np.dot(query_vec, doc_vec) / (np.linalg.norm(query_vec) * np.linalg.norm(doc_vec))
        similarities.append(sim)
    return similarities

# Main Streamlit app
def main():
    st.title("Document Search Engine")
    
    # Load model
    model = load_model()
    
    # Sample documents (replace with your actual documents)
    documents = [
        "Artificial intelligence is the simulation of human intelligence processes by machines.",
        "Machine learning is a subset of AI focused on building systems that learn from data.",
        "Deep learning involves neural networks with many layers for complex pattern recognition.",
        "Natural language processing enables machines to understand and respond to text or speech."
    ]

    # Input query
    query = st.text_input("Enter your search query:")

    if st.button("Search"):
        if query:
            similarities = calculate_similarity(query, documents, model)
            
            # Display results
            sorted_results = sorted(zip(documents, similarities), key=lambda x: x[1], reverse=True)
            
            st.write("### Search Results:")
            for i, (doc, sim) in enumerate(sorted_results):
                st.write(f"**Result {i+1}:** {doc} (Similarity: {sim:.2f})")
        else:
            st.warning("Please enter a search query.")

if __name__ == "__main__":
    main()
