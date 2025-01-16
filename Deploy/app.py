import streamlit as st
from gensim.models import Word2Vec

# Load Word2Vec model
@st.cache_resource
def load_model():
    try:
        model = Word2Vec.load("word2vec_model.model")
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

# Streamlit UI
st.title("Search Engine UI with Streamlit")

# Sidebar settings
st.sidebar.header("Search Settings")
top_n = st.sidebar.slider("Number of Results", min_value=1, max_value=20, value=5)

# Load model
model = load_model()
if model:
    # Search bar
    query = st.text_input("Enter your search query:")

    if query:
        # Generate search results
        try:
            results = model.wv.most_similar(query, topn=top_n)

            # Display results
            st.subheader("Search Results:")
            for i, (word, similarity) in enumerate(results, 1):
                st.write(f"{i}. {word} (Similarity: {similarity:.2f})")
        except KeyError:
            st.warning("The query word is not in the vocabulary of the model.")
else:
    st.warning("Please upload a valid Word2Vec model to use the search functionality.")
