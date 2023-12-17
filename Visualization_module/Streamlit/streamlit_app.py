from io import BytesIO
from PIL import Image
import requests

import streamlit as st
import numpy as np
import cv2
import requests

import sys
import os

# TODO: refactor this part with relative path?
# Your relative path
relative_path = "../../"
# Get the current working directory
current_directory = os.getcwd()
# Combine the current directory with the relative path
full_path = os.path.abspath(os.path.join(current_directory, relative_path))
sys.path.append(full_path)

import podcast_module.text_generation as text_gen
import podcast_module.text_to_speech as text_2_speech
import main_module

LANGUAGE = {
        "Русский": 'rus',
        "Английский": 'eng'
    }

IMAGE_SIZE = (299, 299)

CLASS_NAMES = {
        "camille pissarro": "Impressionism",
        "claude monet": "Impressionism",
        "edgar degas": "Impressionism",
        "ivan aivazovsky": "Romanticism",
        "vincent van gogh": "Realism",
    }

VOICE = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]

HOST = "localhost"
PORT = "7777"
api_host = "http://" + HOST + ":" + PORT + "/predict/artist"
headers = {'Content-Type': 'image/jpeg'}

uploaded_file = False
selected_language = "rus"
voice_option = "alloy"
generated_text = ''
podcast_name = ''
request_text = ''
artist = ''

def get_request(artist, selected_language):
    if (selected_language == 'eng'):
        request = 'Create a podcast script for 2 minuts about the art of ' + artist + '. Podcast name is TimeTravelTech'
    else:
        request = 'Напиши текст подкаста на 2 минуты о творчестве ' + artist + '. Название подкаста TimeTravelTech'
    return request

def create_podcast_script(artist, selected_language):
    request_text = get_request(artist, selected_language)
    generated_text = text_gen.generate_text(request_text)
    
    return generated_text

st.sidebar.header('Time Travel Tech')
st.sidebar.caption('Платформа на базе ИИ для погружения в искусство')
st.sidebar.markdown("***")

art = st.sidebar.toggle('Раскрыть тайну творца')

# artist prediction
if art:
    uploaded_file = st.file_uploader("Загрузите изображение", type="jpg")

    if uploaded_file is not None:
        data_b = uploaded_file.read()
        response = requests.post(api_host, data=data_b, headers=headers)
        predicted_index = int(response.text)

        file_bytes = np.asarray(bytearray(data_b), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        st.image(image, channels="BGR")

        artist, genre = list(CLASS_NAMES.items())[predicted_index]

        st.markdown(f"Художник: {artist}")
        st.markdown(f"Жанр: {genre}")
        st.markdown("***")

history = st.sidebar.toggle('Заглянуть за историческую кулису')

# history creation
if history:
    language_option = st.sidebar.selectbox('Выберите язык', LANGUAGE.keys())

    if language_option:
        selected_language = LANGUAGE[language_option]

    if art is False:
        artist_option = st.sidebar.selectbox('Выберите художника', CLASS_NAMES.keys())
        if artist_option:
            artist = artist_option
            genre = CLASS_NAMES[artist_option]

    elif uploaded_file is not None:
        podcast_name = genre + '_' + artist + '_' + selected_language
        # st.markdown(podcast_name)
        
    create_text_option = st.sidebar.button("Создать текст", type="primary")

    if create_text_option:
        generated_text = create_podcast_script(artist, selected_language)
        st.markdown(generated_text)
        st.markdown("***")

    podcast = st.sidebar.toggle('Запечатлеть в звуке: сотворите свой арт-подкаст')

    # audio creation
    if podcast:
        voice_option = st.sidebar.selectbox('Выберите голос', VOICE)
        create_podcast_option = st.sidebar.button("Создать подкаст", type="primary")
        # code
        if create_podcast_option:
            if generated_text == '':
                generated_text = create_podcast_script(artist, selected_language)

            raw_podcast_path = text_2_speech.text_to_speech(generated_text, podcast_name, voice_option, full_path)
            # Step 2. Podcast beautification (backgroung music).
            main_module.podcast_beautification(raw_podcast_path, full_path)
            
            audio_file = open(raw_podcast_path, 'rb')
            generated_audio = audio_file.read()

            st.audio(generated_audio)
            st.markdown("***")
    # audio creation

    image = st.sidebar.toggle('Создать моего коня')
    # image creation
    if image:
        # Step 3. Image generation.
        image_url = main_module.create_image(artist)
        # Save the image
        response_image = requests.get(image_url)
        img = Image.open(BytesIO(response_image.content))
        
        image_path = '../../images_generation_module/images/' + artist + '.png'
        img.save(image_path)
        st.image(image_path, caption='Generated Image', use_column_width=True)
    # image creation

