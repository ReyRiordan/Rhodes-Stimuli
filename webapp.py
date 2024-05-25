import streamlit as st
from openai import OpenAI
import requests
from io import BytesIO
import word
import audio
import image


st.title("Generate Experimental Stimuli")


### WORD GENERATION ###

disable_buttons = True

st.session_state['word_settings'] = st.selectbox(label="Word generation method:",
                                                 options=["Basic",
                                                          "Manual"])

if st.session_state['word_settings'] == "Manual":
    st.session_state['word'] = st.text_input("Enter word:")

elif st.session_state['word_settings'] == "Basic":
    if st.columns(3)[1].button("Generate Word", type="primary", use_container_width=True):
        st.session_state['word'] = word.generate_basic()

if 'word' in st.session_state and st.session_state['word']:
    st.header(st.session_state['word'])
    disable_buttons = False


st.divider()

### AUDIO GENERATION ###

client = OpenAI()

if st.columns(3)[1].button("Generate Audio", type="primary", use_container_width=True, disabled=disable_buttons):
    st.session_state['audio'] = audio.generate_openai(st.session_state['word'], client)

if 'audio' in st.session_state:
    audio_layout = st.columns(4)

    audio_layout[1].audio(data=st.session_state['audio'],
                            format="audio/mpeg")
    
    audio_layout[2].download_button(label="Download",
                    data=st.session_state['audio'],
                    file_name=st.session_state['word']+".mp3",
                    mime="audio/mpeg",
                    use_container_width=True)
    

st.divider()

### IMAGE GENERATION ###

st.session_state['image_settings'] = st.selectbox(label="Image generation method:",
                                                    options=["Stable Diffusion 3.0",
                                                            "Stable Diffusion 3.0 Turbo",
                                                            "Stable Image Core",
                                                            "Dall-E 2",
                                                            "Dall-E 3",])

if st.session_state['image_settings'] == "Dall-E 2":
    num_images = st.select_slider(label="Number of images:", options=[i+1 for i in range(10)])
    if st.columns(3)[1].button("Generate Image(s)", type="primary", use_container_width=True, disabled=disable_buttons):
        st.session_state['images'] = image.generate_DE2(word=st.session_state['word'],
                                                        n=num_images,
                                                        client=client)

elif st.session_state['image_settings'] == "Dall-E 3":
    if st.columns(3)[1].button("Generate Image", type="primary", use_container_width=True, disabled=disable_buttons):
        st.session_state['images'] = image.generate_DE3(word=st.session_state['word'],
                                                        client=client)

elif st.session_state['image_settings'] == "Stable Diffusion 3.0":
    if st.columns(3)[1].button("Generate Image", type="primary", use_container_width=True, disabled=disable_buttons):
        st.session_state['images'] = image.generate_SD3(word=st.session_state['word'])

elif st.session_state['image_settings'] == "Stable Diffusion 3.0 Turbo":
    if st.columns(3)[1].button("Generate Image", type="primary", use_container_width=True, disabled=disable_buttons):
        st.session_state['images'] = image.generate_SD3T(word=st.session_state['word'])

elif st.session_state['image_settings'] == "Stable Image Core":
    if st.columns(3)[1].button("Generate Image", type="primary", use_container_width=True, disabled=disable_buttons):
        st.session_state['images'] = image.generate_SIC(word=st.session_state['word'])

if 'images' in st.session_state:
    for index, img in enumerate(st.session_state['images']):
        image_layout = st.columns([3, 1, 1, 1])

        image_layout[0].image(image=img,
                              output_format="PNG")
        
        # for i in range(4):
        #     image_layout[2].markdown("#")
        image_layout[2].download_button(label="Download",
                                        data=img,
                                        file_name=st.session_state['word']+".png",
                                        mime="image/png",key=index)