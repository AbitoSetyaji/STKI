# -*- coding: utf-8 -*-
"""STKI.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cnoCODChMPOHQPhe_wZ0Osesyy6Hg8Wa
"""

!  pip install kaggle

from google.colab import drive
drive.mount('/content/drive')

! mkdir ~/.kaggle

! cp /content/kaggle.json ~/.kaggle/

! chmod 600 ~/.kaggle/kaggle.json

cd /content/drive/MyDrive

!pwd

#!/bin/bash
! kaggle datasets download dmaso01dsta/cisi-a-dataset-for-information-retrieval

!unzip /content/drive/MyDrive/cisi-a-dataset-for-information-retrieval.zip -d /content/drive/MyDrive/Dataset

"""# **Konversi dataset menjadi csv**#"""

from sklearn.feature_extraction.text import TfidfVectorizer

# Fungsi untuk menerapkan TF-IDF pada kueri dan dokumen
def apply_tfidf(train_data, test_data):
    vectorizer = TfidfVectorizer(stop_words='english', max_df=0.85, max_features=1000)

    # Gabungkan kueri dan dokumen untuk melatih model
    corpus = train_data['QUERY'] + train_data['TEXT']

    # Fit TF-IDF vectorizer
    tfidf_matrix = vectorizer.fit_transform(corpus)

    # Transformasi untuk data pengujian
    test_corpus = test_data['QUERY'] + test_data['TEXT']
    test_tfidf_matrix = vectorizer.transform(test_corpus)

    return tfidf_matrix, test_tfidf_matrix, vectorizer

# Terapkan TF-IDF
train_tfidf, test_tfidf, vectorizer = apply_tfidf(train_data_processed, test_data_processed)

"""Pembersihan dataset"""

# Import pustaka yang diperlukan
import pandas as pd
import nltk
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import precision_score, recall_score, f1_score
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
!pip install nltk
import nltk
nltk.download('punkt_tab')

# Unduh dataset yang diupload
dataset_path = "/content/drive/MyDrive/Dataset/cisi_dataset.csv"

# Memuat dataset
df = pd.read_csv(dataset_path)

# Melihat struktur dataset
print("Dataset Head:")
print(df.head())

# Mengunduh sumber NLTK jika belum
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Inisialisasi alat NLTK
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Fungsi preprocessing teks
def preprocess_text(text):
    # Check if the input is a string; if not, convert it to one
    if not isinstance(text, str):
        text = str(text)
    # Tokenisasi
    tokens = nltk.word_tokenize(text.lower())
    # Penghapusan stop words dan tanda baca
    tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]
    # Stemming dan lemmatization
    tokens = [stemmer.stem(lemmatizer.lemmatize(word)) for word in tokens]
    return " ".join(tokens)

# Terapkan preprocessing pada kolom TEXT
df['processed_text'] = df['TEXT'].apply(preprocess_text)

# Memisahkan data menjadi training dan testing
X_train, X_test, y_train, y_test = train_test_split(
    df['processed_text'], df['QUERY'], test_size=0.2, random_state=42
)

# Menggunakan TF-IDF Vectorizer
tfidf = TfidfVectorizer()
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

# Model sederhana untuk pencarian (cosine similarity)
from sklearn.metrics.pairwise import cosine_similarity

def search(query, vectorizer, doc_vectors):
    query_vec = vectorizer.transform([preprocess_text(query)])
    similarities = cosine_similarity(query_vec, doc_vectors).flatten()
    most_similar_idx = similarities.argsort()[-5:][::-1]
    return most_similar_idx, similarities[most_similar_idx]

# Contoh pencarian
query = "Information retrieval techniques"
indices, scores = search(query, tfidf, X_train_tfidf)

print("\nTop 5 Dokumen Paling Relevan:")
for idx, score in zip(indices, scores):
    print(f"Judul: {y_train.iloc[idx]} | Skor: {score:.4f}")

# Evaluasi
# Untuk evaluasi, perlu memberikan ground truth kueri yang lebih terstruktur.