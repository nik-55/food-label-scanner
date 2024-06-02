import PIL
import requests
from system_prompt import prompt
from gemini import genai

model = genai.GenerativeModel("models/gemini-pro-vision")

# input from the user

is_additional_info = input("Press yes to provide additional info about the person consuming the food or no to skip: ")

if is_additional_info.lower() == "yes":
    weight = input("Enter the weight of the person: ")
    diseases = input("Enter the list of diseases in comma separated form (A, B, C): ")
    height = input("Enter the height of the person: ")
    gender = input("Enter the gender of the person: ")

    additional_info = {
        "weight": weight,
        "diseases": diseases.split(","),
        "height": height,
        "gender": gender,
    }

    import json
    additional_info = json.dumps(additional_info)

foodlabel = PIL.Image.open(requests.get("https://www.hsph.harvard.edu/nutritionsource/wp-content/uploads/sites/30/2021/06/foodlabel.png", stream=True).raw)

if is_additional_info.lower() == "yes":
    response = model.generate_content([prompt, foodlabel, additional_info])
else:
    response = model.generate_content([prompt, foodlabel])
print(response.text)
