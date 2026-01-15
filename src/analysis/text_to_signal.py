import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


def generate_signals(parquet_path):
    df = pd.read_parquet(parquet_path)

    vectorizer = TfidfVectorizer(max_features=500)
    X = vectorizer.fit_transform(df["cleaned_text"])

    df["signal_strength"] = X.sum(axis=1)

    df[["timestamp", "signal_strength"]].to_csv(
        "data/signals.csv", index=False
    )
