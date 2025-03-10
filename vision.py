import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title = "Google Gemini Q&A Demo", page_icon = "🦜")
st.title("Google Gemini Image Vision")

api_key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key = api_key)

with st.sidebar:
    api_key = st.text_input("Enter your Gemini Api Key" , type="password")

user_input = st.text_input("User Input:")


def generate_response(user_input , image):
    model = genai.GenerativeModel("gemini-1.5-flash")
    if input!="":
        response = model.generate_content([user_input,image])
    
    else:
        response = model.generate_content(image)
    return response.text

upload_image = st.file_uploader("choose the image" , type=["jpg" , "png" , "jpeg","webp"])
submit = st.button("Tell me about image")
image=""
if upload_image is not None:
    image = Image.open(upload_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

if submit:
    response = generate_response(user_input,image)
    st.subheader("THe Response is...")
    st.write(response)





    