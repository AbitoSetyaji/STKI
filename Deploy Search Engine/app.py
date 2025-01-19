import streamlit as st
import pandas as pd
from gensim.models import Word2Vec

# Load dataset
dataset_path = 'lemmatized_dataset.csv'
data = pd.read_csv(dataset_path)

# Preprocess dataset
def preprocess_data(data):
    # Asumsikan kolom "text" berisi dokumen yang akan digunakan
    if "text" in data.columns:
        return [doc.split() for doc in data["text"]]
    else:
        st.error("Kolom 'text' tidak ditemukan dalam dataset.")
        return []

documents = preprocess_data(data)

# Train Word2Vec model if no pre-trained model exists
model_path = 'word2vec_model.model'
try:
    model = Word2Vec.load(model_path)
except FileNotFoundError:
    st.warning("Model Word2Vec tidak ditemukan. Melatih model baru...")
    model = Word2Vec(sentences=documents, vector_size=100, window=5, min_count=1, workers=4)
    model.save(model_path)

# Streamlit App
st.title("Pencarian Dokumen dengan Query")

# Input query
query = st.text_input("Masukkan query untuk mencari dokumen:")

# Placeholder untuk hasil
output_placeholder = st.empty()

# Fungsi untuk menemukan dokumen terkait berdasarkan query
def find_similar_words(query, model, topn=5):
    try:
        similar_words = model.wv.most_similar(query, topn=topn)
        return similar_words
    except KeyError:
        return None

# Fungsi untuk mendapatkan isi dokumen dari query
def get_document_from_query(query, data):
    if "text" in data.columns:
        st.write(f"Mencari query: {query} di kolom 'text'")
        matched_docs = data[data["text"].str.contains(query, case=False, na=False)]
        st.write(f"Dokumen yang cocok: {matched_docs}")
        return matched_docs["text"].tolist()
    else:
        st.error("Kolom 'text' tidak ditemukan dalam dataset.")
        return []


# Tombol untuk menjalankan pencarian
if st.button("Cari"):
    if query:
        matched_documents = get_document_from_query(query, data)
        if matched_documents:
            output = f"\n\n{query}"
            output_placeholder.success(f"Hasil pencarian untuk kata kunci '{query}':\n{output}")
        else:
            output_placeholder.error("Dokumen dengan kata kunci tidak ditemukan.")
    else:
        output_placeholder.error("Silakan masukkan query terlebih dahulu.")
