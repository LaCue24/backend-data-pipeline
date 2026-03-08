from .database import SessionLocal
from .models import Post
from .logger import logger


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
