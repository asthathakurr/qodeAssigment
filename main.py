from src.scraper import TweetScraper
from src.processor import Processor
from src.storage import Storage
from src.analysis import Analyzer

if __name__ == '__main__':
    scraper = TweetScraper(target_count=2000)
    df = scraper.scrape()

    processor = Processor()
    df = processor.clean(df)

    store = Storage()
    store.save_parquet(df)

    analysis = Analyzer()
    X = analysis.vectorize(df)
    analysis.plot_sample(X)

    print("Pipeline complete!")
