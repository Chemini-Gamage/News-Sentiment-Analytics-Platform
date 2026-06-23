# 📰 News Intelligence Platform

> **End-to-end news analytics pipeline** — Live data collection → NLP processing → PostgreSQL storage → Interactive Tableau dashboards

[![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)](https://python.org)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker)](https://docker.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?logo=postgresql)](https://postgresql.org)
[![Tableau](https://img.shields.io/badge/Tableau-Public-E97627?logo=tableau)](https://public.tableau.com/authoring/NewsIntelligencePlatformPythonTableau/HeadlineExplorer-dashboard#1)

**Author:** C Gamage | Data Engineering Portfolio

---

## 🔴 Live Dashboard

**[→ View on Tableau Public](https://public.tableau.com/authoring/NewsIntelligencePlatformPythonTableau/HeadlineExplorer-dashboard#1)**

---

## Overview

The News Intelligence Platform is an end-to-end data analytics solution that collects live news articles, performs Natural Language Processing (NLP) analysis, stores enriched data in PostgreSQL, and visualizes insights through interactive Tableau dashboards.

Designed to simulate a real-world news analytics pipeline used by media monitoring, business intelligence, and market research organizations — combining data engineering, NLP, database management, containerization, and business intelligence into a single workflow.

---

## Architecture

```
                 NewsAPI
                    │
                    ▼
         ┌──────────────────────┐
         │   Python ETL         │
         │   Docker Container   │
         │                      │
         │  ┌────────────────┐  │
         │  │ fetch_news.py  │  │
         │  │ sentiment.py   │  │
         │  │ category.py    │  │
         │  │ entity_        │  │
         │  │  extractor.py  │  │
         │  │ keyword_       │  │
         │  │  extractor.py  │  │
         │  │ load_db.py     │  │
         │  └────────────────┘  │
         └──────────────────────┘
                    │
                    ▼
         ┌──────────────────────┐
         │  NLP Processing      │
         │  • Sentiment (VADER) │
         │  • Categorization    │
         │  • Entity Extraction │
         │  • Keyword Extraction│
         └──────────────────────┘
                    │
                    ▼
         ┌──────────────────────┐
         │    PostgreSQL 16     │
         │    (Docker)          │
         │    port 5433:5432    │
         └──────────────────────┘
                    │
                    ▼ (CSV export for Tableau Public)
         ┌──────────────────────┐
         │   Tableau Public     │
         │   Dashboards         │
         └──────────────────────┘
```

> **Note:** PostgreSQL is the production data store. For Tableau Public (which requires a local data source), data is exported as CSV for dashboard connectivity.

---

## Sample Results — 

| Metric | Value |
|---|---|
| Total Articles Collected | 37 |
| Average Sentiment Score | -0.09 |
| Positive Articles | 24.3% |
| Neutral Articles | 35.1% |
| Negative Articles | 40.5% |
| Date Range | June 19–21, 2026 |

**Key Insight:** Negative sentiment dominates at 40.5% — Politics and General news are the primary drivers. Technology shows the most positive coverage.

---

## Tableau Dashboards

### 1. Executive Overview
High-level KPI summary of the news landscape — total articles, average sentiment, positive/neutral/negative percentages, sentiment trend over time, and category distribution.

**Top Insight:** CBS Sports (0.340), Motley Fool (0.296), and Live Science (0.273) are the most positively framed sources.
<img width="1473" height="962" alt="image" src="https://github.com/user-attachments/assets/f3d24de5-116d-4896-b626-587e3747611f" />

---

### 2. Category Intelligence
Sentiment breakdown by news category with stacked bar charts and the Category Intelligence Map cross-referencing sentiment × category.

| Category | Total Articles | Most Common Sentiment |
|---|---|---|
| General | 17 | Negative |
| Technology | 10 | Mixed |
| Politics | 7 | Negative |
| Sports | 1 | Neutral |
| Entertainment | 1 | Positive |
| Business | 1 | Negative |

---
<img width="835" height="678" alt="image" src="https://github.com/user-attachments/assets/72615ab7-ebaf-4e36-83e4-7152d46737d8" />

### 3. Sentiment Trend Over Time
Tracks how news tone shifts across the June 19–21, 2026 collection window. Negative sentiment holds consistently below zero; neutral content stays flat near zero.

---

### 4. Source Intelligence
Ranks all news outlets by average sentiment score from most positive to most negative.

**Most Positive:** Deadline (0.660), CNET (0.637), InStyle (0.477)

**Most Negative:** Business Insider (-0.459), USA Today (-0.340), Washington Post (-0.318)
<img width="825" height="672" alt="image" src="https://github.com/user-attachments/assets/8e598e0e-1a2d-4d68-a3f4-135d95e50caa" />

---

### 5. Headline Explorer
Fully searchable and filterable article table — filter by source, category, or sentiment to drill into individual headlines.
<img width="882" height="726" alt="image" src="https://github.com/user-attachments/assets/8803a606-b8f7-43c5-9d64-ef66025398d8" />

---

## Technology Stack

| Category | Technology |
|---|---|
| Programming Language | Python 3.11+ |
| Data Processing | Pandas |
| NLP | NLTK (VADER), spaCy |
| Database | PostgreSQL 16 |
| Containerization | Docker, Docker Compose |
| Visualization | Tableau Public |
| Data Source | NewsAPI |
| Development | VS Code |

---

## Database Schema

### `news_articles`

| Column | Type | Description |
|---|---|---|
| id | SERIAL PRIMARY KEY | Unique article identifier |
| source | VARCHAR | News source name |
| title | TEXT | Article headline |
| published_date | TIMESTAMP | Publication timestamp |
| sentiment | VARCHAR | Positive / Neutral / Negative |
| sentiment_score | FLOAT | VADER compound score (-1 to 1) |
| category | VARCHAR | Article category |
| organization | TEXT | Extracted organizations (spaCy) |
| person | TEXT | Extracted people (spaCy) |
| location | TEXT | Extracted locations (spaCy) |
| keywords | TEXT | Extracted keywords |
| headline_length | INTEGER | Headline character count |

---

## Project Structure

```
news-intelligence-platform/
│
├── database/
│   └── init.sql                  # PostgreSQL schema creation
│
├── etl/
│   ├── fetch_news.py             # NewsAPI data ingestion
│   ├── sentiment.py              # VADER sentiment analysis
│   ├── category.py               # Rule-based categorization
│   ├── entity_extractor.py       # spaCy NER (orgs, people, locations)
│   ├── keyword_extractor.py      # Headline keyword extraction
│   ├── load_db.py                # PostgreSQL loader
│   ├── main.py                   # Pipeline orchestrator
│   ├── requirements.txt
│   └── Dockerfile
│
├── docs/
│   ├── architecture.png
│   └── screenshots/
│
├── docker-compose.yml
├── .env
├── .gitignore
└── README.md
```

---

## Setup & Installation

### Prerequisites

- Python 3.11+
- Docker Desktop
- Tableau Public (free) or Tableau Desktop
- [NewsAPI](https://newsapi.org/) free account

### 1. Clone the Repository

```bash
git clone <repository-url>
cd news-intelligence-platform
```

### 2. Configure Environment Variables

Create a `.env` file in the root:

```env
NEWS_API_KEY=your_newsapi_key_here

POSTGRES_USER=admin
POSTGRES_PASSWORD=admin
POSTGRES_DB=newsdb
```

### 3. Start the Pipeline

```bash
docker compose up --build
```

This starts two containers:
- **`db`** — PostgreSQL 16, port `5433:5432`
- **`etl`** — Python pipeline (runs once, then exits — this is expected)
<img width="1747" height="943" alt="Screenshot 2026-06-23 184339" src="https://github.com/user-attachments/assets/2c314cfa-ce33-4674-921e-9a61fb2d4fef" />

### 4. Verify Data Collection

Connect to the database and run:

```sql
SELECT COUNT(*) FROM news_articles;
SELECT sentiment, COUNT(*) FROM news_articles GROUP BY sentiment;
```

Or via Docker:

```bash
docker exec -it <db-container-name> psql -U admin -d newsdb -c "SELECT COUNT(*) FROM news_articles;"
```

### 5. Connect Tableau

Export data to CSV for Tableau Public:

```bash
docker exec -it <db-container-name> psql -U admin -d newsdb \
  -c "\COPY news_articles TO '/tmp/news_articles.csv' CSV HEADER;"
```

Then connect Tableau to the CSV file and use the provided workbook.

---

## Docker Container Status

| Container | Image | Status | Port |
|---|---|---|---|
| `db` | postgres:16 | ✅ Running | 5433:5432 |
| `etl` | python:3.11 | ⚪ Exits after run | — |

> The ETL container exiting after completion is **expected behaviour** — it is a one-time pipeline job, not a persistent service. Re-run with `docker compose up etl` to collect fresh data.

---

## Key Findings

- **Negative sentiment dominates** (40.5%) across June 2026 news cycle, driven by Politics and General categories
- **Technology** is the most balanced category — roughly equal positive, neutral, and negative coverage
- **Entertainment sources** (Deadline, InStyle) score highest for positive sentiment
- **Financial/news outlets** (Business Insider, USA Today) trend most negative
- **Neutral sentiment** holds flat across all three days, while negative fluctuates slightly

---

## Future Enhancements

### Machine Learning
- Replace VADER with **FinBERT** for finance-domain sentiment
- Implement **BERTopic** for automated topic modeling
- Add sentiment confidence scoring

### Data Engineering
- **Scheduled hourly ETL** using cron or Airflow
- Real-time streaming with Kafka
- Incremental data loading (avoid re-processing existing articles)

### Application Layer
- **FastAPI REST API** exposing sentiment endpoints
- Interactive **Streamlit** or **Dash** web dashboard
- Cloud deployment (AWS/GCP)

### Analytics
- Trending topic detection
- Sentiment volatility index
- Daily intelligence digest report

---

## Results

The platform successfully:

- ✅ Collected live news articles from 25+ sources via NewsAPI
- ✅ Performed automated sentiment analysis with VADER
- ✅ Classified articles into 6 categories
- ✅ Extracted named entities (organizations, people, locations) with spaCy
- ✅ Stored enriched data in PostgreSQL
- ✅ Generated 5 executive-level Tableau dashboards
- ✅ Delivered a fully Dockerized, reproducible analytics pipeline

---

## Skills Demonstrated

| Domain | Skills |
|---|---|
| Data Engineering | ETL pipeline design, API ingestion, Docker orchestration |
| NLP | Sentiment analysis, named entity recognition, keyword extraction |
| Database | PostgreSQL schema design, SQL querying |
| Containerization | Docker, Docker Compose, multi-container apps |
| Business Intelligence | Tableau dashboard design, KPI visualization |
| Python | Pandas, NLTK, spaCy, psycopg2 |

---

*Developed as a portfolio project to demonstrate data science, analytics engineering, and business intelligence skills through a real-world news intelligence use case.*
