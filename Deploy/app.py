import streamlit as st
from gensim.models import Word2Vec
import os
from pathlib import Path

# Load the Word2Vec model
@st.cache_resource
def load_model(file_path):
    try:
        # Convert to Path object for better path handling
        model_path = Path(file_path)
        
        # Check if file exists
        if not model_path.exists():
            st.error(f"Model file not found at: {model_path}")
            st.info("Please ensure the model file is in the correct location")
            return None
            
        # Try to load the model
        model = Word2Vec.load(str(model_path))
        st.success("Model loaded successfully!")
        return model
        
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

def main():
    # Streamlit UI/UX
    st.title("Simple Search Engine")
    st.write("Enter a word to find related terms based on the Word2Vec model.")
    
    # File path to the model
    # You can modify this path to match your model location
    model_file = "word2vec_model.model"  # Default to current directory
    
    # Try to load model
    model = load_model(model_file)
    
    # Only show search interface if model is loaded
    if model is not None:
        # Input field
        query = st.text_input("Search query", "")
        
        if query:
            try:
                # Fetch similar words
                similar_words = model.wv.most_similar(query)
                
                # Display results
                st.write("Results:")
                for word, score in similar_words:
                    st.write(f"- **{word}**: {score:.4f}")
                    
            except KeyError:
                st.warning(f"The word '{query}' is not in the model's vocabulary.")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please ensure the model file is available before searching.")

if __name__ == "__main__":
    main()
