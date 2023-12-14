from config import OPENAI_API_KEY
import openai

def generate_image(text):
    openai.api_key = OPENAI_API_KEY
    response = openai.images.generate(
        model = "dall-e-3",
        prompt = text,
        size = "1024x1024",
        quality = "standard",
        n = 1,
    )
    image_url = response.data[0].url
    print(image_url)
