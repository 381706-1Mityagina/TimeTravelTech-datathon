# ✨ TimeTravelTech. Datathon ✨
## ✨ Hear the Art, Know the Artist – Turning Your Visual Experience into A Vivid Auditory Journey! ✨

## 🎧 Idea: "Podcasts about art and it's history."

We initially discussed deducing some information about the painting and the artist from the photo, maybe even some kind of historical summary. So, we can go further and convert this text into audio format.

Podcasts are very popular now.
Users will be able to immerse themselves in the atmosphere and learn something new. You no longer have to waste valuable time reading text results.
When you walk through a museum or city, all your attention is focused on the works of art, and not on reading the text. You just need to listen.

## 🎧 Result:
The user takes a photograph of a work of art (be it a painting, sculpture, building, etc.), and as a result receives a pleasant story (in a form of a podcast) about the author, era and so much more.

That is, there will be Image recognition and Speech Synthesis.

We can train the network or take a pre-trained one that will return the title and/or author from the photo, and then we’ll feed this result into gpt and get a small text and convert it to audio.

## 🎧 Flow:
`Photo` -> `CV model` -> `Title of the work/Author` -> `gpt (with a specific request, they say, write a story in this style in so many words)` -> `text` -> `audio podcast`.

## 🎧 Datasets:
TBD

## 🎧 Models:
TBD

## 📂 Project structure:

- `cv_module` - contains the source files needed for CV processing
- `images_generation_module` - contains the source files needed for images generation
    - `images` - generated images (a few examples)
- `podcast_module` - contains the source files needed for text generation and text-to-speech conversion
    - `podcasts` - generated podcasts (a few examples)
    - `audio_beautification` - audio effects (such as background music)
- `podcasts` - podcasts collection
- `visualization_module` - demos
    - `Streamlit`
    - `Telegram_bot`

## 💫 Usage/demonstartion:
There are a few ways to see the TimeTravelTech Podcast creator in use:
(but you will need to know `OPENAI_API_KEY` and `TELEGRAM_HTTP_API`).
- Go to `visualization_module/Streamlit` and follow the instructions there.
- There is a Telegram chat bot called TimeTravelTech. *TBD* ???
- Or you can go to the separate modules and test them OR you can run `main_module.py` (uncomment main()) to see pars of the project in use.

To view the demo video, please follow the link `visualization_module/Streamlit/demo/demo_streamlit.mp4`.

![](https://github.com/381706-1Mityagina/TimeTravelTech-datathon/blob/streamlit/Visualization_module/Streamlit/demo/demo_streamlit.gif)
