import queue
import threading
from app.ingestion import fetch_data, save_posts
from app.logger import logger

job_queue = queue.Queue()


def worker():

    while True:

        job = job_queue.get()

        if job == "run_pipeline":

            logger.info("Worker started pipeline job")

            data = fetch_data()

            save_posts(data)

            logger.info("Worker completed pipeline job")

        job_queue.task_done()


def start_worker():

    thread = threading.Thread(target=worker, daemon=True)

    thread.start()
