from openai import OpenAI
import streamlit as st
import requests

client = OpenAI()

st.title("Pokemon Generator?")

prompt = "a white siamese cat"

response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1
)

image_url = response.data[0].url
image = requests.get(image_url)


print(image_url)