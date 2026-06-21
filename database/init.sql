CREATE TABLE IF NOT EXISTS news_articles (

    id SERIAL PRIMARY KEY,

    source VARCHAR(100),

    title TEXT,

    published_date TIMESTAMP,

    sentiment VARCHAR(20),

    sentiment_score FLOAT

);