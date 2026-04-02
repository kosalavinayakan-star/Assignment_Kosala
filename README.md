# Scalable Multi-Database Data Platform for AI-Driven Marketing Personalization

## Overview
This project demonstrates a modular, production-ready data platform that integrates:
- **MongoDB** for raw conversation storage
- **Milvus** for vector embeddings
- **Neo4j** for user-campaign-intent relationships
- **Redis** for caching recent sessions
- **SQLite/BigQuery** for analytics

It supports both **real-time** and **batch pipelines**, orchestrated via Python DAGs (Airflow/Prefect ready).

---

## Setup

### Prerequisites
- Docker & Docker Compose
- Python 3.9+
- Pipenv or virtualenv

### Installation
```bash
git clone <repo-url>
cd project-root
pip install -r requirements.txt
docker-compose up -d
