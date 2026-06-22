
CREATE TABLE news_articles (
    id SERIAL PRIMARY KEY,
    source TEXT,
    title TEXT,
    published_date TIMESTAMP,
    sentiment TEXT,
    sentiment_score FLOAT,
    category TEXT,   -- 👈 ADD THIS
    organization TEXT,
    person TEXT,
    location TEXT,
    keywords TEXT,
    headline_length INT
);