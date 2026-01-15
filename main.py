from src.scraper.twitter_scraper import scrape_tweets
from src.processing.cleaner import clean_tweets
from src.processing.deduplicator import deduplicate
from src.storage.parquet_writer import write_parquet
from src.analysis.text_to_signal import generate_signals

import logging
import os


os.makedirs("logs", exist_ok=True)
os.makedirs("data", exist_ok=True)

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


if __name__ == "__main__":
    logging.info("Pipeline started")

    raw_tweets = scrape_tweets()

    cleaned = clean_tweets(raw_tweets)
    unique = deduplicate(cleaned)

    write_parquet(unique, "data/tweets.parquet")

    generate_signals("data/tweets.parquet")

    logging.info("Pipeline completed successfully")
