def get_category(title):

    title = title.lower()

    tech = ["ai","apple","google","microsoft","openai","nvidia","software","tech"]
    business = ["stock","market","economy","inflation","bank","crypto"]
    politics = ["trump","biden","election","president","government","war","vote","iran"]
    sports = ["football","cricket","nba","fifa","world cup","tennis"]
    entertainment = ["movie","film","box office","celebrity","netflix","hollywood"]

    if any(w in title for w in tech):
        return "Technology"

    if any(w in title for w in business):
        return "Business"

    if any(w in title for w in politics):
        return "Politics"

    if any(w in title for w in sports):
        return "Sports"

    if any(w in title for w in entertainment):
        return "Entertainment"

    return "General"