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

![](https://github.com/381706-1Mityagina/TimeTravelTech-datathon/blob/main/posters/poster-0.png)

## 🎧 Flow:
`Photo of the painting` ->
`CV module` ->
`Recognized author name` ->
`Text generation` ->
`Text to Speech` ->
`Audio effects` ->
`Podcast` ->
`Image generation`

## 🎧 Datasets:
The original `Wikiart` dataset is a collection of art images obtained from the website www.wikiart.org with information about works of art. It contains 80,020 unique images from 1,119 artists in 27 styles. The dataset was found on Kaggle.

For this work, the original data set was reduced.
Data preprocessing:
5 artists were selected - camille pissarro, claude monet, edgar degas, ivan aivazovsky, vincent van gogh
For each artist, only one main style in his work is left - Impressionism, Romanticism, Realism. Within the framework of this work, these 3 styles are recorded in the artist-style connection; in the future, we need to move away from this approach (see further steps).

For the final dataset, 4168 images with 5 classes were prepared:
- claude coin 1320
- vincent van gogh 884
- camille pissarro 787
- edgar degas 600
- ivan aivazovsky 577
The final dataset was divided into a training and test set in a `70/30` ratio.


## 🎧 Models:
- `inception_v3` is the model that was chosen for this work. Initially, more complex models from the `EfficientNet` family were considered, but the training took place on a laptop, so the level of complexity of the architecture had to be reduced.
- `text-davinci-003` can do language tasks with better quality and consistency than the curie, babbage, or ada models. Will be deprecated on Jan 4th 2024.	4,096 tokens. The model was found in OpenAI API.
- `tts-1` TTS is an AI model that converts text to natural sounding spoken text. The model was found in OpenAI API.
- `dall-e-3` DALL-E is a AI system that can create realistic images and art from a description in natural language. DALL·E 3 currently supports the ability, given a prompt, to create a new image with a specific size. The model was found in OpenAI API.

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
- Go to `visualization_module/Streamlit` or `visualization_module/Telegram_bot` and follow the instructions there.
- Or you can go to the separate modules and test them OR you can run `main_module.py` (uncomment main()) to see pars of the project in use.

To view the Streamlit demo video, please follow the link `visualization_module/Streamlit/demo/demo_streamlit.mp4`.

![](https://github.com/381706-1Mityagina/TimeTravelTech-datathon/blob/main/Visualization_module/Streamlit/demo/demo_streamlit.gif)

To view the Telegram demo video, please follow the link `visualization_module/Telegram_bot/demo/demo_telegram.mp4`.

![](https://github.com/381706-1Mityagina/TimeTravelTech-datathon/blob/main/Visualization_module/Telegram_bot/demo/demo_telegram.gif)
