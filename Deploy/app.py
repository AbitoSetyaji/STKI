import streamlit as st
from gensim.models import Word2Vec
import os
from pathlib import Path
import time

# Configure the Streamlit page
st.set_page_config(
    page_title="GitHub Search Engine",
    page_icon="🔍",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
    }
    .search-stats {
        font-size: 0.8rem;
        color: #666;
    }
    .repo-card {
        padding: 1rem;
        border: 1px solid #e1e4e8;
        border-radius: 6px;
        margin-bottom: 1rem;
        background-color: white;
    }
    .repo-header {
        display: flex;
        align-items: center;
        margin-bottom: 0.5rem;
    }
    .repo-name {
        font-size: 1.2rem;
        font-weight: bold;
        color: #0366d6;
    }
    .repo-stats {
        display: flex;
        gap: 1rem;
        color: #586069;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# Load the Word2Vec model
@st.cache_resource
def load_model(file_path):
    try:
        model_path = Path(file_path)
        if not model_path.exists():
            st.error(f"Model file not found at: {model_path}")
            return None
        model = Word2Vec.load(str(model_path))
        return model
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

def main():
    # Sidebar
    with st.sidebar:
        st.image("https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png", width=100)
        st.title("Search Filters")
        
        # Filters
        st.subheader("Language")
        languages = ["All", "Python", "JavaScript", "Java", "C++", "Ruby", "Go"]
        selected_language = st.selectbox("Select Language", languages)
        
        st.subheader("Sort By")
        sort_options = ["Best Match", "Most Stars", "Recently Updated", "Most Forks"]
        sort_by = st.selectbox("Sort Results By", sort_options)
        
        st.subheader("Time Range")
        time_ranges = ["Any time", "Today", "This week", "This month", "This year"]
        time_range = st.selectbox("Select Time Range", time_ranges)
        
        # Advanced filters
        st.subheader("Advanced Filters")
        min_stars = st.slider("Minimum Stars", 0, 10000, 0)
        min_forks = st.slider("Minimum Forks", 0, 1000, 0)
        include_archived = st.checkbox("Include Archived", False)

    # Main content
    st.title("🔍 GitHub Repository Search")
    
    # Search bar with suggestions
    col1, col2 = st.columns([4,1])
    with col1:
        search_query = st.text_input("Search repositories...", 
                                   placeholder="Enter keywords, topics, or repository names")
    with col2:
        search_button = st.button("Search")
        
    # Show example searches
    if not search_query:
        st.markdown("#### Try searching for:")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.button("Machine Learning")
        with col2:
            st.button("Web Development")
        with col3:
            st.button("Data Science")
            
    # Process search
    if search_query or search_button:
        with st.spinner('Searching repositories...'):
            # Simulate search delay
            time.sleep(1)
            
            # Display search stats
            st.markdown(f"<p class='search-stats'>Found 1,234 repositories matching '{search_query}'</p>", 
                       unsafe_allow_html=True)
            
            # Display results
            for i in range(5):
                with st.container():
                    st.markdown(f"""
                    <div class="repo-card">
                        <div class="repo-header">
                            <span class="repo-name">username/repository-{i+1}</span>
                        </div>
                        <p>Sample repository description with matching keywords highlighted.</p>
                        <div class="repo-stats">
                            <span>⭐ {1000 + i*100}</span>
                            <span>🔀 {200 + i*50}</span>
                            <span>📅 Updated 2 days ago</span>
                            <span>💻 Python</span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Action buttons
                    col1, col2, col3 = st.columns([1,1,2])
                    with col1:
                        st.button(f"⭐ Star", key=f"star_{i}")
                    with col2:
                        st.button(f"👁️ Watch", key=f"watch_{i}")
                    with col3:
                        st.markdown(f"[View Repository](https://github.com) • [Download ZIP](https://github.com)")
            
            # Pagination
            col1, col2, col3 = st.columns([2,1,2])
            with col2:
                st.markdown("""
                <div style='display: flex; gap: 1rem; justify-content: center;'>
                    <a href='#'>Previous</a>
                    <span>Page 1 of 50</span>
                    <a href='#'>Next</a>
                </div>
                """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
