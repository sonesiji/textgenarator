import streamlit as st
import google.generativeai as genai

# Configure API key
api_key = "AIzaSyCBHJzNyEhusj_bDljUkTvKYQU95hgcDag"
genai.configure(api_key=api_key)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_text(user_input):
    try:
        # Call generate_content
        response = model.generate_content(user_input)
        # Access the text directly if it's an attribute
        return response.text if hasattr(response, 'text') else 'No text found'
    except Exception as e:
        return f'Error: {str(e)}'

# Streamlit app interface
st.title("Text Generator")

user_input = st.text_input("Enter text to generate content")

if st.button("Generate"):
    if user_input:
        generated_text = generate_text(user_input)
        st.write("Generated Text:")
        st.write(generated_text)
    else:
        st.write("Please enter some input text.")
