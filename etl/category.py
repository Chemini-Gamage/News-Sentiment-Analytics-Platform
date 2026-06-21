def get_category(title):

    title = title.lower()

    if any(word in title for word in ["ai", "tech", "software", "apple", "google"]):
        return "Technology"

    if any(word in title for word in ["stock", "market", "economy", "inflation"]):
        return "Business"

    if any(word in title for word in ["war", "military", "politics", "election"]):
        return "Politics"

    if any(word in title for word in ["football", "cricket", "nba", "tournament"]):
        return "Sports"

    return "General"