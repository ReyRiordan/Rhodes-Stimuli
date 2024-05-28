import streamlit as st
from openai import OpenAI
# from google.cloud import texttospeech
from io import BytesIO
import base64


def play(audio_bytes: BytesIO):
    # Convert the audio data in the BytesIO buffer to base64
    audio_base64 = base64.b64encode(audio_bytes.getvalue()).decode('utf-8')
    # Generate the HTML audio tag with autoplay
    audio_tag = f'<audio autoplay="true" src="data:audio/wav;base64,{audio_base64}">'
    # Display the audio tag using Streamlit markdown
    st.markdown(audio_tag, unsafe_allow_html=True)


def generate_openai(word: str, client: OpenAI) -> BytesIO:
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=word
    )

    audio_bytes = BytesIO(response.content)

    return audio_bytes


# def generate_google(word: str) -> BytesIO:
#     client = texttospeech.TextToSpeechClient()
#     synthesis_input = texttospeech.SynthesisInput(text=word)
#     voice = texttospeech.VoiceSelectionParams(language_code="en-US",
#                                               ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)
#     audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

#     response = client.synthesize_speech(input=synthesis_input,
#                                         voice=voice,
#                                         audio_config=audio_config)

#     audio_bytes = BytesIO(response.audio_content)
    
#     return audio_bytes