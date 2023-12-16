import streamlit as st
import numpy as np
import cv2
import requests

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


def create_text(artist, selected_language):

    if (selected_language == 'eng'):
        request = 'Create a podcast script for 2 minuts about the art of ' + artist + '. Podcast name is TimeTravelTech'
    else:
        request = 'Напиши текст подкаста на 2 минуты о творчестве ' + artist + '. Название подкаста TimeTravelTech'
    return request


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
    selected_language = "rus"

    if language_option:
        selected_language = LANGUAGE[language_option]

    if art is False:
        artist_option = st.sidebar.selectbox('Выберите художника', CLASS_NAMES.keys())
        if artist_option:
            artist = artist_option
            genre = CLASS_NAMES[artist_option]
        request = create_text(artist, selected_language)

    elif uploaded_file is True:
        podcast_name = genre + '_' + artist + '_' + selected_language
        st.markdown(podcast_name)
        request = create_text(artist, selected_language)

    if st.sidebar.button("Создать текст", type="primary"):
        # code
        # st.markdown(generated_text)
        st.markdown("***")

    podcast = st.sidebar.toggle('Запечатлеть в звуке: сотворите свой арт-подкаст')

    # audio creation
    if podcast:
        voice_option = st.sidebar.selectbox('Выберите голос', VOICE)

        # code
        if st.sidebar.button("Создать подкаст", type="primary"):
            # code
            # st.audio(generated_audio)
            st.markdown("***")
