import requests
from dotenv import load_dotenv
import os

# Getting api key from env variable
load_dotenv()
api_key = os.getenv("API_KEY")

# Sendind http reuests
url = (
    f"https://api.nasa.gov/planetary/apod?api_key={api_key}&"
    "thumbs=false"
    )
response = requests.get(url)

content = response.json()
image_url = content["url"]

image_binary = requests.get(image_url) 

with open("image.jpg", "wb") as file:
    file.write(image_binary.content)