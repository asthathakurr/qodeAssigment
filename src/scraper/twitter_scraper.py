import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta

from src.scraper.utils import parse_tweet


HASHTAGS = ["#nifty50", "#sensex", "#banknifty", "#intraday"]


def scrape_tweets(target_count=2000):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://twitter.com/search?q=" + "%20OR%20".join(HASHTAGS))

    tweets = []
    start_time = datetime.utcnow() - timedelta(hours=24)

    while len(tweets) < target_count:
        elements = driver.find_elements(By.XPATH, "//article")

        for el in elements:
            tweet = parse_tweet(el)
            if tweet and tweet["timestamp"] >= start_time:
                tweets.append(tweet)

        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(random.uniform(2, 4))

    driver.quit()
    return tweets
