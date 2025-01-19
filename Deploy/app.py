import streamlit as st
import pandas as pd
from gensim.models import Word2Vec  # Import the necessary library

# Konfigurasi halaman
st.set_page_config(page_title="Search Engine", layout="centered")

# Header aplikasi
st.title("Search Engine Prototype")
st.write("\nWelcome to this simple search engine UI built with Streamlit!")

# Load model function
def load_model(model_file):
    try:
        model = Word2Vec.load(model_file)  # Load the Word2Vec model
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model_file = "Deploy/word2vec_model.model"  # Path to your Word2Vec model file
model = load_model(model_file)

# Load dataset
def load_data():
    try:
        data = pd.read_csv("Deploy/lemmatized_dataset.csv")  # Path to your dataset
        return data
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return pd.DataFrame()

data = load_data()

if not data.empty:
    # Input pengguna
    query = st.text_input("What are you looking for today?", placeholder="Type your query here...")

    # Tombol pencarian
    if st.button("Search"):
        if query.strip():
            # Filter dataset berdasarkan query
            results = data[data.apply(lambda row: query.lower() in row.to_string().lower(), axis=1)]

            if not results.empty:
                st.success(f"Found {len(results)} result(s) for: {query}")
                for idx, row in results.iterrows():
                    # Hanya menampilkan kolom selain 'Preprocessed_Query' dan 'Tokenized_Query'
                    filtered_row = {k: v for k, v in row.to_dict().items() if k not in ['Preprocessed_Query', 'Tokenized_Query']}
                    st.write(f"**Result {idx + 1}:** {filtered_row}")
            else:
                st.warning(f"No results found for: {query}")
        else:
            st.error("Please enter a valid search query.")
else:
    st.error("No data available to search.")

# Footer
st.write("---")
st.caption("Prototype created with ❤️ using Streamlit.")
