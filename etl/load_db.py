import pandas as pd

from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://admin:admin@db:5432/newsdb"
)

def save_to_db(df):

    df.to_sql(
        "news_articles",
        engine,
        if_exists="append",
        index=False
    )