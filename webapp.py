import streamlit as st
from openai import OpenAI
import requests
from io import BytesIO
import audio
import image


st.title("Generate Experimental Stimuli")

client = OpenAI()

st.header("Word")
st.session_state['word'] = st.text_input("Word:")


st.header("Audio")

if st.button("Generate Audio") and st.session_state['word']:
    st.session_state['audio'] = audio.generate_openai(st.session_state['word'], client)
    
if 'audio' in st.session_state:
    st.button(label="Play",
              on_click=audio.play,
              args=[st.session_state['audio']])
    st.download_button(label="Download",
                       data=st.session_state['audio'],
                       file_name=st.session_state['word']+".mp3",
                       mime="audio/mpeg")


st.header("Image")

if st.button("Generate Image") and st.session_state['word']:
    st.session_state['image'] = image.edit_openai(st.session_state['word'], client)

if 'image' in st.session_state:
    st.image(image=st.session_state['image'],
             output_format="PNG")
    st.download_button(label="Download",
                       data=st.session_state['image'],
                       file_name=st.session_state['word']+".png",
                       mime="image/png")