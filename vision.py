
from dotenv import load_dotenv
load_dotenv()  ## loading all the envvironment variables

import streamlit as st
import os
import pathlib
import textwrap
import google.generativeai as genai
from PIL import Image

os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

## function to load Gemini Pro model and get response

def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input != '':
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text

## initialize our streamlit app

st.set_page_config(page_title="Gemini Image Demo")

st.header('Gemini Applocation')
input = st.text_input('Input Prompt: ',key='input')

upload_file = st.file_uploader('Choose an image..', type=['jpg','jpeg','png'])
image = ''
if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image,caption='Uploaded Image.', use_column_width=True)

submit = st.button('Tell me about the image')

##if submit is clicked
if submit:
    response = get_gemini_response(input,image)
    st.subheader('The response is')
    st.write(response)