import streamlit as st
from googlesearch import search

# Function to search for PDF links
def search_pdf_links(query, num_links=10):
    search_query = f"{query} filetype:pdf"
    pdf_links = []
    for url in search(search_query, stop=num_links):
        pdf_links.append(url)
    return pdf_links

# Main function to create the app
def main():
    # Set page config
    #st.set_page_config(page_title="PDF Link Search", page_icon=":books:", layout="wide", initial_sidebar_state="collapsed")

    st.title("PDF Link Search")
    keyword = st.text_input("Enter the keyword to search for PDFs:")
    
    if st.button("Search"):
        if keyword:
            st.info("Searching for PDFs...")
            pdf_links = search_pdf_links(keyword)
            if pdf_links:
                st.success("Search completed!")
                st.subheader("PDF Links:")
                for idx, link in enumerate(pdf_links, 1):
                    st.write(f"{idx}. {link}")
            else:
                st.warning("No PDFs found for the given keyword.")
        else:
            st.warning("Please enter a keyword to search for PDFs.")
    
# Run the app
if __name__ == "__main__":
    main()
