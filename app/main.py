from fastapi import FastAPI
from app.database import engine, Base, SessionLocal
from app.models import Post
from app.queue_worker import job_queue, start_worker

Base.metadata.create_all(bind=engine)

app = FastAPI()

start_worker()


@app.get("/run-pipeline")
def trigger_pipeline():

    job_queue.put("run_pipeline")

    return {"message": "Pipeline job submitted to worker queue"}


@app.get("/posts")
def get_posts():

    db = SessionLocal()

    posts = db.query(Post).all()

    db.close()

    return posts
