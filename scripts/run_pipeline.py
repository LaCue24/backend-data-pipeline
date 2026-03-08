from app.ingestion import fetch_data
from app.validation import validate_post

def run_pipeline():

    data = fetch_data()

    for post in data:
        validate_post(post)

    print("Pipeline completed successfully")

if __name__ == "__main__":
    run_pipeline()
