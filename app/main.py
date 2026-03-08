from fastapi import FastAPI, BackgroundTasks
from app.database import engine, Base, SessionLocal
from app.models import Post
from app.ingestion import fetch_data, save_posts
from app.logger import logger

Base.metadata.create_all(bind=engine)

app = FastAPI()


def run_pipeline():

    logger.info("Starting background pipeline")

    data = fetch_data()

    save_posts(data)

    logger.info("Pipeline completed successfully")


@app.get("/run-pipeline")
def trigger_pipeline(background_tasks: BackgroundTasks):

    background_tasks.add_task(run_pipeline)

    return {"message": "Pipeline started in background"}


@app.get("/posts")
def get_posts():

    db = SessionLocal()

    posts = db.query(Post).all()

    db.close()

    return posts
