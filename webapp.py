import streamlit as st
from openai import OpenAI
import requests
from io import BytesIO
import audio
import image


st.title("Generate Experimental Stimuli")

client = OpenAI()

st.session_state['word'] = st.text_input("Word:")


st.divider()

if st.columns(3)[1].button("Generate Audio", type="primary", use_container_width=True) and st.session_state['word']:
    st.session_state['audio'] = audio.generate_openai(st.session_state['word'], client)
    
if 'audio' in st.session_state:
    audio_layout = st.columns(4)

    audio_layout[1].button(label="Play",
              on_click=audio.play,
              args=[st.session_state['audio']],
              use_container_width=True)
    
    audio_layout[2].download_button(label="Download",
                       data=st.session_state['audio'],
                       file_name=st.session_state['word']+".mp3",
                       mime="audio/mpeg",
                       use_container_width=True)


st.divider()

if st.columns(3)[1].button("Generate Image", type="primary", use_container_width=True) and st.session_state['word']:
    st.session_state['image'] = image.edit_openai(st.session_state['word'], client)

if 'image' in st.session_state:
    image_layout = st.columns([3, 1, 1, 1])

    image_layout[0].image(image=st.session_state['image'],
             output_format="PNG")
    
    for i in range(4):
        image_layout[2].markdown("#")
    image_layout[2].download_button(label="Download",
                       data=st.session_state['image'],
                       file_name=st.session_state['word']+".png",
                       mime="image/png")