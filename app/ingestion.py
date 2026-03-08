import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_data():

    response = requests.get(API_URL)

    if response.status_code != 200:
        raise Exception("Failed to fetch data")

    return response.json()
