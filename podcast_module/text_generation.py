from config import OPENAI_API_KEY
import openai

def generate_text(text):
    openai.api_key = OPENAI_API_KEY

    response = openai.completions.create(
        model = "text-davinci-003",
        prompt = text,
        temperature = 0.6,
        max_tokens = 1500,
    )
    
    generated_text = response.choices[0].text
    print(generated_text)

    return generated_text
