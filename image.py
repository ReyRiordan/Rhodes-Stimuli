from openai import OpenAI
import requests
from io import BytesIO


def generate_openai(word: str, client: OpenAI) -> BytesIO:
    prompt = f"A single new Pokémon, 2D cartoon Pokémon style, flat colors, isolated on pure white background, without any textual elements or additional objects"

    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1
    )

    image = requests.get(response.data[0].url)
    image_bytes = BytesIO(image.content)

    return image_bytes


def edit_openai(word: str, client: OpenAI) -> BytesIO:
    prompt = f"Graphic art of a single new Pokémon called {word}, 2D, flat colors, isolated on white background"

    response = client.images.edit(
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