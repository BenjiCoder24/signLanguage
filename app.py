from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import base64
from openai import OpenAI
import io
import os
import re
from PIL import Image
from dotenv import load_dotenv  # Import python-dotenv

# Load environment variables from .env file
load_dotenv()  # This will automatically load the variables from .env

app = Flask(__name__)
CORS(app)

# Initialize OpenAI API
# openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()  # The OpenAI client for API requests

# Placeholder for previous words
previous_words = []

# Load or initialize your sign language recognition model here
# For example:
# model = load_sign_language_model()

def recognize_sign_language(image):
    """
    Process the image and return the recognized word.
    This function should use a trained sign language recognition model.
    """
    # For the purpose of this example, we'll return a dummy word
    # Replace this with actual image processing and recognition code
    recognized_word = "hello"  # Placeholder
    return recognized_word

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_image', methods=['POST'])
def process_image():
    global previous_words

    data = request.get_json()
    image_data = data['image']
    previous_words = data['previous_words']

    # Decode the image
    header, encoded = image_data.split(',', 1)
    image_bytes = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(image_bytes))

    # Recognize the sign language gesture in the image
    recognized_word = recognize_sign_language(image)

    # Avoid duplicates
    if not previous_words or recognized_word != previous_words[-1]:
        previous_words.append(recognized_word)

    # Generate the sentence using GPT
    prompt = f"The following words were recognized from sign language gestures: {previous_words}. Construct a coherent sentence from these words."

    messages = [{"role": "user", "content": prompt}]

    # Using OpenAI GPT-4 to generate a sentence based on recognized words
    esponse = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=4096,
        stream=True,
    )
    # response = client.ChatCompletion.create(
    #     model="gpt-4",
    #     messages=messages,
    #     max_tokens=4096,
    #     stream=True,
    # )
    response_text = ""
    for chunk in response:
        if 'choices' in chunk and chunk.choices[0].delta.get('content') is not None:
            response_text += str(chunk.choices[0].delta.get('content'))

    # Clean up the response
    cleaned_response = re.sub(r'```json\n|\n```', '', response_text)

    # Return the updated words and the generated sentence
    return jsonify({
        'previous_words': previous_words,
        'generated_sentence': cleaned_response
    })

if __name__ == '__main__':
    app.run(debug=True)
