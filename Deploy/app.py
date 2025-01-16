import streamlit as st
from gensim.models import Word2Vec

# Load the Word2Vec model (path to your uploaded model)
model_path = '/mnt/data/word2vec_model.model'

try:
    model = Word2Vec.load(model_path)
    model_loaded = True
except Exception as e:
    model_loaded = False
    error_message = str(e)

# Streamlit UI
st.set_page_config(page_title="Google-like Search Engine", layout="centered")
st.title("Welcome to Word2Vec Search")

if not model_loaded:
    st.error(f"Failed to load the model. Error: {error_message}")
else:
    st.text_input("Search", placeholder="Type something...", key="search_query")

    query = st.session_state.get("search_query", "")

    if query:
        try:
            # Get similar words based on the query
            results = model.wv.most_similar(query, topn=10)

            st.write("## Results")
            for word, similarity in results:
                st.write(f"- {word} (Similarity: {similarity:.2f})")
        except KeyError:
            st.error("Sorry, the word is not in the vocabulary.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
