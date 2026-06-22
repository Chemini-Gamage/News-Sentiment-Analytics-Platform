import pandas as pd

from fetch_news import get_news

from sentiment import analyze_sentiment

from category import get_category

from entity_extractor import extract_entities

from keyword_extractor import extract_keywords

from load_db import save_to_db


articles = get_news()

records = []

for article in articles:

    title = article["title"]

    sentiment, score = analyze_sentiment(title)

    category = get_category(title)

    orgs, persons, locations = extract_entities(title)

    keywords = extract_keywords(title)

    records.append(
        {
            "source":
                article["source"]["name"],

            "title":
                title,

            "published_date":
                article["publishedAt"],

            "sentiment":
                sentiment,

            "sentiment_score":
                score,

            "category":
                category,

            "organization":
                orgs,

            "person":
                persons,

            "location":
                locations,

            "keywords":
                keywords,

            "headline_length":
                len(title)
        }
    )

df = pd.DataFrame(records)


# CLEAN STEP (VERY IMPORTANT)
df = df.dropna(subset=["title"])
df = df.drop_duplicates(subset=["title"])
df = df[df["title"].str.len() > 10]

save_to_db(df)

print("Loaded", len(df), "articles")