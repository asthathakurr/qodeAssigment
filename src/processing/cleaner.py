import re


def clean_tweets(tweets):
    cleaned = []

    for t in tweets:
        text = re.sub(r"http\S+", "", t["content"])
        text = re.sub(r"[^\w\s#@]", "", text)

        t["cleaned_text"] = text.lower().strip()
        cleaned.append(t)

    return cleaned
