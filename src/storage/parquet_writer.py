import pandas as pd


def write_parquet(tweets, path):
    df = pd.DataFrame(tweets)
    df.to_parquet(path, index=False)
