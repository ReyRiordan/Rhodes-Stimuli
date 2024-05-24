import streamlit as st
from openai import OpenAI
import requests
from io import BytesIO
import image


st.title("Pokemon Generator")

client = OpenAI()

st.header("Word")
word = st.text_input("Word:")


st.header("Image")
image_bytes = None

if st.button("Generate") and word:
    image_bytes = image.edit_openai(word, client)

if image_bytes:
    st.image(image=image_bytes,
             output_format="PNG")
    
    st.download_button(label="Download",
                       data=image_bytes,
                       file_name=word+".png",
                       mime="image/png")