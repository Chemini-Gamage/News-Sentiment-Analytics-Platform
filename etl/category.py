def get_category(title):

    title = title.lower()

    tech = [
        "ai","artificial intelligence",
        "google","microsoft",
        "apple","tesla",
        "openai","nvidia"
    ]

    business = [
        "market","stock",
        "economy","inflation",
        "finance","bank"
    ]

    politics = [
        "election","government",
        "president","minister",
        "parliament","war"
    ]

    sports = [
        "football","cricket",
        "nba","fifa",
        "olympics"
    ]

    health = [
        "covid","hospital",
        "health","medicine",
        "vaccine"
    ]

    if any(word in title for word in tech):
        return "Technology"

    if any(word in title for word in business):
        return "Business"

    if any(word in title for word in politics):
        return "Politics"

    if any(word in title for word in sports):
        return "Sports"

    if any(word in title for word in health):
        return "Health"

    return "General"