import streamlit as st
from openai import OpenAI
import requests
from io import BytesIO
import os


def generate_SIC(word: str) -> list[BytesIO]:
    api_key = os.getenv("STABILITY_API_KEY")
    prompt = f"A single creature called {word} in cartoon Pokémon style, 2-dimensional and using only flat colors, isolated on pure white background."

    response = requests.post(
        f"https://api.stability.ai/v2beta/stable-image/generate/core",
        headers={
            "authorization": f"Bearer {api_key}",
            "accept": "image/*"
        },
        files={
            "none": ''
        },
        data={
            "prompt": prompt,
            "negative_prompt": "colored background"
        },
    )

    if response.status_code == 200:
        # Check if the response content type is an image
        if 'image' in response.headers.get('Content-Type', ''):
            image_bytes = BytesIO(response.content)
            return [image_bytes]
        else:
            st.error("The response did not contain an image.")
            return []
    else:
        st.error(f"Request failed with status code {response.status_code}: {response.text}")
        return []
    

def generate_SD3T(word: str) -> list[BytesIO]:
    api_key = os.getenv("STABILITY_API_KEY")
    prompt = f"A single creature called {word} in cartoon Pokémon style, 2-dimensional and using only flat colors, isolated on pure white background."

    response = requests.post(
        f"https://api.stability.ai/v2beta/stable-image/generate/sd3",
        headers={
            "authorization": f"Bearer {api_key}",
            "accept": "image/*"
        },
        files={
            "none": ''
        },
        data={
            "prompt": prompt,
            "model": "sd3-turbo"
        },
    )

    if response.status_code == 200:
        # Check if the response content type is an image
        if 'image' in response.headers.get('Content-Type', ''):
            image_bytes = BytesIO(response.content)
            return [image_bytes]
        else:
            st.error("The response did not contain an image.")
            return []
    else:
        st.error(f"Request failed with status code {response.status_code}: {response.text}")
        return []


def generate_SD3(word: str) -> list[BytesIO]:
    api_key = os.getenv("STABILITY_API_KEY")
    prompt = f"A single new LIMBLESS (NO ARMS, NO LEGS) creature called a {word} in cartoon pokemon art style, 2-dimensional, isolated on pure white background."

    response = requests.post(
        f"https://api.stability.ai/v2beta/stable-image/generate/sd3",
        headers={
            "authorization": f"Bearer {api_key}",
            "accept": "image/*"
        },
        files={
            "none": ''
        },
        data={
            "prompt": prompt,
            "model": "sd3"
        },
    )

    if response.status_code == 200:
        # Check if the response content type is an image
        if 'image' in response.headers.get('Content-Type', ''):
            image_bytes = BytesIO(response.content)
            return [image_bytes]
        else:
            st.error("The response did not contain an image.")
            return []
    else:
        st.error(f"Request failed with status code {response.status_code}: {response.text}")
        return []


def generate_DE3(word: str, client: OpenAI) -> list[BytesIO]:
    prompt = f"A single new Pokémon called {word} in cartoon Pokémon style, 2-dimensional and using only flat colors, isolated on pure white background."

    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        style="natural",
        size="1024x1024",
        quality="standard",
    )

    image = requests.get(response.data[0].url)
    image_bytes = BytesIO(image.content)

    return [image_bytes]


def generate_DE2(word: str, n, client: OpenAI) -> list[BytesIO]:
    prompt = f"Graphic art of a single new Pokémon called {word}, 2D, flat colors, isolated on white background"

    response = client.images.edit(
        model="dall-e-2",
        prompt=prompt,
        n=n,
        image=open("assets/white.png", "rb"),
        mask=open("assets/mask.png", "rb"),
        size="1024x1024"
    )

    images = []
    for data in response.data:
        image = requests.get(data.url)
        bytes = BytesIO(image.content)
        images.append(bytes)

    return images