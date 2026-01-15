# Market Intelligence System (Qode Assignment)

A real-time Twitter scraping + analysis system built without paid APIs.

## Features
- Scrapes 2000+ tweets using Selenium
- Cleans, processes, deduplicates data
- Stores in Parquet format
- TF-IDF vectorization
- PCA lightweight visualization
- Fully documented and scalable

## Run (high level)
1. pip install -r requirements.txt
2. Configure chromedriver (compatible version) and ensure it's in PATH
3. python main.py

Outputs:
- data/tweets.parquet
- output/signal_plot.png
