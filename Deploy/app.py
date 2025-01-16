import streamlit as st
from PIL import Image

# Set up page configuration
st.set_page_config(
    page_title="Simple Search Engine",
    page_icon="🔍",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Create a Google-style search engine interface
def main():
    # Center align the content
    st.markdown(
        """
        <style>
        .centered {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            height: 100vh;
        }
        .search-bar {
            width: 40%;
            max-width: 600px;
            min-width: 300px;
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: 25px;
            font-size: 16px;
        }
        .search-button {
            background-color: #f8f9fa;
            color: #202124;
            padding: 10px 20px;
            border: none;
            border-radius: 25px;
            font-size: 14px;
            cursor: pointer;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Centered container
    st.markdown('<div class="centered">', unsafe_allow_html=True)

    # Display Google-style logo
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/512px-Google_2015_logo.svg.png",
        use_column_width=False,
        width=300,
    )

    # Search bar input
    query = st.text_input("", "", key="search_input")

    # Search button
    if st.button("Search"):
        if query:
            preprocessed_query = query.lower().strip()  # Example preprocessing
            # Simulated search results (replace with actual search logic if needed)
            search_results = [
                f"Result 1 for '{preprocessed_query}'",
                f"Result 2 for '{preprocessed_query}'",
                f"Result 3 for '{preprocessed_query}'",
                f"Result 4 for '{preprocessed_query}'",
                f"Result 5 for '{preprocessed_query}'",
            ]
            st.write("### Search Results:")
            for result in search_results:
                st.write(f"- {result}")
        else:
            st.warning("Please enter a search query.")

    # Close centered container
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
