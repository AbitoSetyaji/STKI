import streamlit as st

# Fungsi untuk hasil pencarian simulasi
def search_query(query):
    # Fungsi pencarian sederhana, ini hanya contoh. Anda bisa menggantinya dengan pencarian nyata
    results = [f"Result {i} for '{query}'" for i in range(1, 6)]
    return results

# Atur tampilan UI
st.set_page_config(page_title="Search Engine", page_icon="🔍", layout="centered")

# Header (seperti logo Google)
st.title("My Search Engine")

# Kotak pencarian
search_input = st.text_input("Search", "")

if search_input:
    # Tampilkan hasil pencarian jika ada input
    st.write(f"Hasil pencarian untuk: **{search_input}**")
    results = search_query(search_input)
    for result in results:
        st.markdown(f"- {result}")
else:
    st.markdown("Masukkan kata kunci untuk mencari.")

