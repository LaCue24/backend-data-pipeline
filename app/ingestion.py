import requests
from .database import SessionLocal
from .models import Post
from .logger import logger

API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_data():

    logger.info("Fetching data from external API")

    response = requests.get(API_URL)

    if response.status_code != 200:
        logger.error("API request failed")
        raise Exception("Failed to fetch data")

    logger.info("API data fetched successfully")

    return response.json()


def save_posts(posts):

    db = SessionLocal()

    for post in posts:

        record = Post(
            id=post["id"],
            title=post["title"],
            body=post["body"]
        )

        db.merge(record)

    db.commit()
    db.close()

    logger.info("Posts successfully stored in database")
