import nltk

from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")

sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):

    score = sia.polarity_scores(text)["compound"]

    if score > 0.05:
        sentiment = "Positive"

    elif score < -0.05:
        sentiment = "Negative"

    else:
        sentiment = "Neutral"

    return sentiment, score