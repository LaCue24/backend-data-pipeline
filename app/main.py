from fastapi import FastAPI
from app.database import engine, Base
from app.models import Post
from app.ingestion import fetch_data, save_posts

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/data")
def get_data():

    data = fetch_data()

    save_posts(data)

    return data
