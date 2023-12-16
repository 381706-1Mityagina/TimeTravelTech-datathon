import podcast_module.text_generation as text_gen
import podcast_module.text_to_speech as text_2_speech
import podcast_module.audio_beautification.audio_beautification as audio_beauty
import images_generation_module.image_generation as img_gen

# TODOs:
# 1. import input preprocessing module - TBD (by Elvira)
# 2. import CV module - TBD
# 3. import/implement beautifications of the audio (by Daria)
#      - background music - DONE
#      - interesting into
#      - add an option with dialogue between two people (?)
#      - code cleanup - WIP
#      - image generation in a style of an artist - DONE
#           - need to save generated image localy using recieved link - TBD
# 4. Add visualization module
#      - Streamlit - WIP (by Elvira)
#      - Telegram ChatBot (by Daria)
#           - graphics for the chat / demo (?)
#           - maybe stickers (?)

LANGUAGE = 'eng'

def create_podcast(genre, author):
    name_of_the_podcast = genre + '_' + author + '_' + LANGUAGE
    if (LANGUAGE == 'eng'):
        request = 'Create a podcast script for 2 minuts about the art of ' + author + '. Podcast name is TimeTravelTech'
    elif (LANGUAGE == 'rus'):
        request = 'Напиши текст подкаста на 2 минуты о творчестве ' + author + '. Название подкаста TimeTravelTech'
    
    generated_text = text_gen.generate_text(request)
    output_file_name = text_2_speech.text_to_speech(generated_text, name_of_the_podcast)

    return output_file_name

def create_image(author):
    request = 'Create an image of a horse in a style of' + author # Need to change a common image theme
    img_gen.generate_image(request)

def podcast_beautification(raw_podcast_path):
    background_music = "./podcast_module/audio_beautification/background-0_silent-wood.mp3"
    # Replace raw_podcat with an edited one
    audio_beauty.mix_audio(raw_podcast_path, background_music, raw_podcast_path, background_volume_reduction=20)

def main():
    # Step 0. The CV module prepares and processes the input file (photo).
    #   calls to the input preparation - TBD
    #   calls to CV module - TBD
    #   -> Result of the CV module is `genre` and `author`

    # Placeholder. Soon these variables will contain output of a Step 0.
    genre = 'Renaissance'
    author = 'Leonardo da Vinci'
    
    # Step 1. Podcast content preparation.
    raw_podcast_path = create_podcast(genre, author)
    # Step 2. Podcast beautification (backgroung music).
    podcast_beautification(raw_podcast_path)
    # Step 3. Image generation.
    create_image(author)

main()
