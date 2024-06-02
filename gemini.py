import dotenv
import os

import google.generativeai as genai

dotenv.load_dotenv()

API_KEY = os.getenv("API_KEY")
genai.configure(api_key=API_KEY)
