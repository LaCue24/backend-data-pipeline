import requests
from .logger import logger

API_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_data():

    logger.info("Fetching external API data")

    response = requests.get(API_URL)

    if response.status_code != 200:
        logger.error("API request failed")
        raise Exception("Failed to fetch data")

    logger.info("Data ingestion successful")

    return response.json()
