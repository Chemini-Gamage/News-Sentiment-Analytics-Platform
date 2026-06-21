import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")

URL = (
    f"https://newsapi.org/v2/top-headlines?"
    f"language=en&pageSize=100&apiKey={API_KEY}"
)

def get_news():

    response = requests.get(URL)

    data = response.json()

    return data["articles"]