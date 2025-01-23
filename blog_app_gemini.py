import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

def get_gemini_response(input_text, no_words, blog_style):
    api_key = os.getenv('GOOGLE_API_KEY')
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"""
    Write a blog for {blog_style} job profile about the topic '{input_text}'
    within {no_words} words.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {str(e)}"

st.set_page_config(page_title="Generate Blogs",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the Blog Topic")

col1, col2 = st.columns([5,5])

with col1:
    no_words = st.text_input('No of Words')
with col2:
    blog_style = st.selectbox('Writing the blog for',
                              ('Researchers','Data Scientist','Common People'), index=0)

submit = st.button("Generate")

if submit:
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        st.error("Gemini API Key not found in .env file")
    elif not input_text or not no_words:
        st.error("Please fill in all fields")
    else:
        try:
            response = get_gemini_response(input_text, no_words, blog_style)
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")