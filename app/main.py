from fastapi import FastAPI
import requests

app = FastAPI()

API_URL = "https://jsonplaceholder.typicode.com/posts"

@app.get("/data")
def get_data():
    
    response = requests.get(API_URL)

    if response.status_code != 200:
        return {"error": "API request failed"}

    return response.json()
