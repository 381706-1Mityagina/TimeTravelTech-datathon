from config import OPENAI_API_KEY
import openai

VOICES = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]

def text_to_speech(text, file_name, voice_option, root_path):
    openai.api_key = OPENAI_API_KEY

    response = openai.audio.speech.create(
        model = "tts-1",
        voice = voice_option,
        input = text,
    )

    output_file_name = root_path + '/podcasts/' + file_name + "_" + voice_option + ".mp3"
    response.stream_to_file(output_file_name)

    return output_file_name
