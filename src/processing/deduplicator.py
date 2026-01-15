def deduplicate(tweets):
    seen = set()
    unique = []

    for t in tweets:
        key = hash(t["cleaned_text"] + str(t["timestamp"]))

        if key not in seen:
            seen.add(key)
            unique.append(t)

    return unique
