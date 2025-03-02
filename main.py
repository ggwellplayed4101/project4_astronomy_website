import requests
from dotenv import load_dotenv
import os

# Getting api key from env variable
load_dotenv()
api_key = os.getenv("API_KEY")

# Sendind http reuests
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
response = requests.get(url)

print(response.json())