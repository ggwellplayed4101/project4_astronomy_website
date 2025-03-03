import requests
from dotenv import load_dotenv
import os
from datetime import date, timedelta

today = date.today()
yesterday = today - timedelta(days=1)

def astronomy_info_provider(date = yesterday):
    # Getting api key from env variable
    load_dotenv()
    api_key = os.getenv("API_KEY")

    # Sending http reuests
    url = (
        f"https://api.nasa.gov/planetary/apod?api_key={api_key}&"
        "thumbs=false&"
        f"date={yesterday}" 
        )
    response = requests.get(url)

    # Recieved url of the astronomy image
    content = response.json()
    image_url = content["url"]
    image_response = requests.get(image_url) 

    # Loaded image to the file
    with open("image.jpg", "wb") as file:
        file.write(image_response.content)
    
    return (content["title"], content["explanation"])
    
astronomy_info_provider()