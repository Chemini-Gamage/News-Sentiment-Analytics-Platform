import pandas as pd

from fetch_news import get_news

from sentiment import analyze_sentiment

from load_db import save_to_db


articles = get_news()

records = []

for article in articles:

    title = article["title"]

    sentiment, score = analyze_sentiment(title)

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
                score
        }
    )

df = pd.DataFrame(records)

save_to_db(df)

print("Loaded", len(df), "articles")