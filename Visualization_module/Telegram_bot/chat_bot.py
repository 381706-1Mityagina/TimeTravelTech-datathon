import logging
import os
import pipeline
import sys

from io import BytesIO
from PIL import Image
import requests

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
import podcast_module.audio_beautification.audio_beautification as audio_beauty
import visualization_module.Streamlit.streamlit_app as strlt
import main_module

from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler

# Bot token, replace with your own token
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

CV_SCRIPT_PATH = './pipeline.py'
AUTHOR_MAP_RUS = {
        "camille pissarro": "Камиль Писсарро",
        "claude monet": "Клод Моне",
        "edgar degas": "Эдгар Дега",
        "ivan aivazovsky": "Иван Айвазовский",
        "vincent van gogh": "Винсент Ван Гог",
    }
GENRE_MAP_RUS = {
        "Impressionism": "Импрессионизм",
        "Impressionism": "Импрессионизм",
        "Impressionism": "Импрессионизм",
        "Romanticism": "Романтизм",
        "Realism": "Реализм",
    }

VOICE_SAMPLES_PATH = './samples/russian/'
VOICE_SAMPLES = [
    {'file': 'alloy_rus_sample.mp3', 'text': '1. alloy', 'name': 'alloy'},
    {'file': 'echo_rus_sample.mp3', 'text': '2. echo', 'name': 'echo'},
    {'file': 'fable_rus_sample.mp3', 'text': '3. fable', 'name': 'fable'},
    {'file': 'nova_rus_sample.mp3', 'text': '4. nova', 'name': 'nova'},
    {'file': 'shimmer_rus_sample.mp3', 'text': '5. shimmer', 'name': 'shimmer'},
    {'file': 'onyx_rus_sample.mp3', 'text': '6. onyx', 'name': 'onyx'},
]
author =''

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет ✨ Покажи мне нечто прекрасное ✨ Пришли фото картины, об авторе которой хочешь узнать ✨')

def picture(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Подожди немного, твоя картина скоро будет доступна ⌛ Готовься любоваться ✨')
    image_url = main_module.create_image(author)
    response_image = requests.get(image_url)
    img = Image.open(BytesIO(response_image.content))
    
    image_path = './generated_images/' + author + '.png'
    img.save(image_path)
    
    with open(image_path, 'rb') as img_file:
        context.bot.send_document(update.message.chat_id, document=img_file)
    
    update.message.reply_text('Надеюсь, что тебе понравилось наше общение 💗 Приходи еще и нажимай /start ✨')

def podcast(update: Update, context: CallbackContext) -> None:
    for sample in VOICE_SAMPLES:
        voice_file = os.path.join(VOICE_SAMPLES_PATH, sample['file'])
        text_file = sample['text']

        context.bot.send_voice(update.message.chat_id, voice=open(voice_file, 'rb'))
        context.bot.send_message(update.message.chat_id, text=text_file)

    # Provide buttons for selection
    keyboard = [[f"Select {i+1}" for i in range(len(VOICE_SAMPLES))]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    update.message.reply_text('Какой голос нравится? ✨', reply_markup=reply_markup)
    

def handle_photo(update: Update, context: CallbackContext) -> None:
    global author
    if update.message.photo:
    ### REPLY TO THE PICTURE PROVIDED - start
        gif_path = './gifs/wow.gif'  
        title = 'Как красиво ✨ Ты знаешь толк в искусстве ✨'
        with open(gif_path, 'rb') as gif_file:
            context.bot.send_document(update.message.chat_id, document=gif_file)
        context.bot.send_message(update.message.chat_id, text=title)
    ### REPLY TO THE PICTURE PROVIDED - end

        file_id = update.message.photo[-1].file_id
        file = context.bot.get_file(file_id)
        image_path_rel = './downloaded_images/input_photo.jpg'
        file.download(image_path_rel)

    # GET AUTHOR AND GENRE - start
        author, genre = pipeline.get_author_and_genre(image_path_rel)
        author = AUTHOR_MAP_RUS[author]
        genre = GENRE_MAP_RUS[genre]
        context.bot.send_message(update.message.chat_id, text=f'Автором этой работы является известнейший {author}, работавший в стиле {genre} 😍')
        context.bot.send_message(update.message.chat_id, text=f'Если хочешь услышать небольшой рассказ об этом талантливом человеке, укажи команду /podcast ✨')
        context.bot.send_message(update.message.chat_id, text=f'Если хочешь получить картину коня в стиле {author}, укажи команду /picture ✨')

    # GET AUTHOR AND GENRE - end
    else:
    ### REPLY TO NO PICTURE PROVIDED - start
        gif_path = './gifs/where.gif'  
        title = 'Как так ✨ А где красота? ✨'
        with open(gif_path, 'rb') as gif_file:
            context.bot.send_document(update.message.chat_id, document=gif_file)
        context.bot.send_message(update.message.chat_id, text=title)
    ### REPLY TO NO PICTURE PROVIDED - end

def podcast_beautification(raw_podcast_path, root_path):
    background_music = "./samples/background-0_silent-wood.mp3"
    audio_beauty.mix_audio(raw_podcast_path, background_music, raw_podcast_path, background_volume_reduction=20)
   
def generate_podcast(update: Update, context: CallbackContext, chosen_voice_name) -> None:
    global author
    gif_path = './gifs/world.gif'  
    title = f'Подожди немного, твой подкаст скоро будет доступен ⌛ Готовься погрузиться в мир искусства ✨'
    with open(gif_path, 'rb') as gif_file:
        context.bot.send_document(update.message.chat_id, document=gif_file)
    context.bot.send_message(update.message.chat_id, text=title)
    
    if not chosen_voice_name:
        chosen_voice_name = 'onyx'
    generated_text = strlt.create_podcast_script(author, 'rus')
    podcast_path = './'

    raw_podcast_path = text_2_speech.text_to_speech(generated_text, f'generated_podcast{author}', chosen_voice_name, podcast_path)
    podcast_beautification(raw_podcast_path, podcast_path)

    gif_path = './gifs/done.gif'  
    title = 'Готово 🎉'
    with open(gif_path, 'rb') as gif_file:
        context.bot.send_document(update.message.chat_id, document=gif_file)
    context.bot.send_message(update.message.chat_id, text=title)

    context.bot.send_audio(update.message.chat_id, audio=open(raw_podcast_path, 'rb'))

def handle_selection(update: Update, context: CallbackContext) -> None:
    global chosen_voice_name
    selected_option = update.message.text.replace("Select ", "")
    if selected_option.isdigit() and 1 <= int(selected_option) <= len(VOICE_SAMPLES):
        selected_sample = VOICE_SAMPLES[int(selected_option) - 1]
        chosen_voice_name = selected_sample['name']
        
        context.bot.send_message(update.message.chat_id, text=f'Отличный выбор! Мне тоже нравится {chosen_voice_name} ✨')
    else:
        gif_path = './gifs/where.gif'  
        title = 'Промах 🙈 Постарайся попасть по кнопкам 😅'
        with open(gif_path, 'rb') as gif_file:
            context.bot.send_document(update.message.chat_id, document=gif_file)
        context.bot.send_message(update.message.chat_id, text=title)

    generate_podcast(update, context, chosen_voice_name)
    # Remove the custom keyboard
    context.bot.send_message(update.message.chat_id, text='Наслаждайся ✨', reply_markup=ReplyKeyboardRemove())

def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.photo & ~Filters.command & ~Filters.forwarded, handle_photo))
    
    dispatcher.add_handler(CommandHandler("podcast", podcast))
    dispatcher.add_handler(MessageHandler(Filters.regex(r'^Select \d+$'), handle_selection))
    
    dispatcher.add_handler(CommandHandler("picture", picture))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
