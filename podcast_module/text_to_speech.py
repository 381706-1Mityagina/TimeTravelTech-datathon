from config import OPENAI_API_KEY
import openai

VOICES = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]

def text_to_speech(text, file_name):
    openai.api_key = OPENAI_API_KEY
    chosen_voice = VOICES[0]

    response = openai.audio.speech.create(
        model = "tts-1",
        voice = chosen_voice,
        input = text,
    )

    output_file_name = './podcasts/' + file_name + "_" + chosen_voice + ".mp3"
    response.stream_to_file(output_file_name)

    return output_file_name
