import requests
import dotenv
import os

dotenv.load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/sd-community/sdxl-flash"
HUGGINGFACE_TOKEN = os.getenv("HUGGING_FACE_API")
headers = {"Authorization": f"Bearer {HUGGINGFACE_TOKEN}"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content


image_bytes = query(
    {
        "inputs": "Astronaut riding a horse",
    }
)
# You can access the image with PIL.Image for example
import io
from PIL import Image

image = Image.open(io.BytesIO(image_bytes))
image.save("generated_img.jpg")
