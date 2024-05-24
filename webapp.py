from openai import OpenAI
import streamlit as st
import requests
from io import BytesIO


def generate_openai(word: str) -> BytesIO:
    prompt = f"Graphic art of a single new Pokémon named {word} in the official Pokémon cartoon style, 2D, flat colors, isolated on pure white background, no additional objects"

    response = CLIENT.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1
    )

    image = requests.get(response.data[0].url)
    image_bytes = BytesIO(image.content)

    return image_bytes

def edit_openai(word: str) -> BytesIO:
    prompt = f"Graphic art of a single new Pokémon named {word}, 2D, flat colors, isolated on white background, no additional objects"

    response = CLIENT.images.edit(
        model="dall-e-2",
        image=open("white.png", "rb"),
        mask=open("mask.png", "rb"),
        prompt=prompt,
        size="1024x1024",
        n=1
    )

    image = requests.get(response.data[0].url)
    image_bytes = BytesIO(image.content)

    return image_bytes


st.title("Pokemon Generator")

CLIENT = OpenAI()

st.header("Word")
word = st.text_input("Word:")


st.header("Image")
image_bytes = None

if st.button("Generate") and word:
    image_bytes = edit_openai(word)

if image_bytes:
    st.image(image=image_bytes,
             output_format="PNG")
    
    st.download_button(label="Download",
                       data=image_bytes,
                       file_name=word+".png",
                       mime="image/png")