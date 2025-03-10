import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st

import google.generativeai as genai


import google.generativeai as genai

models = genai.list_models()
for model in models:
    print(model.name)


api_key = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key = api_key)

##function to load model and get response

model = genai.GenerativeModel("gemini-1.5-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

##streamlit configuration
st.set_page_config(page_title = "Google Gemini Q&A Demo", page_icon = "🦜")
st.title("Google Gemini Application")
with st.sidebar:
    api_key = st.text_input("Enter your Google Api Key", type="password")

user_input = st.text_input("User Input:")
submit = st.button("Ask your Question")

if submit:
    response = get_gemini_response(user_input)
    st.subheader("The Response is:")
    st.write(response)