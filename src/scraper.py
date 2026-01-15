from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time
from src.utils import random_delay, clean_text, ts

HASHTAGS = ["nifty50", "sensex", "intraday", "banknifty"]

class TweetScraper:
    def __init__(self, target_count=2000):
        self.target_count = target_count
        self.tweets = []

    def init_driver(self):
        opt = Options()
        opt.add_argument("--headless=new")
        opt.add_argument("--disable-blink-features=AutomationControlled")
        # Add more options as needed in your environment
        return webdriver.Chrome(options=opt)

    def scrape(self):
        driver = self.init_driver()
        try:
            for tag in HASHTAGS:
                url = f"https://twitter.com/search?q=%23{tag}&f=live"
                driver.get(url)
                time.sleep(5)
                while len(self.tweets) < self.target_count:
                    soup = BeautifulSoup(driver.page_source, "html.parser")
                    articles = soup.find_all("article")
                    for a in articles:
                        try:
                            content = clean_text(a.get_text())
                            if len(content) < 10:
                                continue
                            self.tweets.append({
                                "hashtag": tag,
                                "content": content,
                                "timestamp": ts(),
                                "username": "NA",
                            })
                            if len(self.tweets) >= self.target_count:
                                break
                        except Exception:
                            continue
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    random_delay(2, 4)
        finally:
            driver.quit()
        return pd.DataFrame(self.tweets)
