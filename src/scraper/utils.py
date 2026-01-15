from datetime import datetime


def parse_tweet(element):
    try:
        text = element.text
        timestamp = datetime.utcnow()

        return {
            "username": "unknown",
            "timestamp": timestamp,
            "content": text,
            "likes": 0,
            "retweets": 0,
            "hashtags": [],
            "mentions": []
        }

    except Exception:
        return None
