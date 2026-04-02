# Architecture Diagram: Multi-Database Data Platform


                        ┌─────────────────────────┐
                        │   User Conversations    │
                        │ (user_id, msg, ts)      │
                        └───────────┬──────────── ┘
                                    │
                                    ▼
                        ┌─────────────────────────┐
                        │   Ingestion Layer       │
                        │ (Kafka / API Gateway)   │
                        └───────────┬──────────── ┘
                                    │
                                    ▼
                        ┌─────────────────────────┐
                        │   ETL Orchestration     │
                        │ (Airflow / Prefect)     │
                        └───────────┬──────────── ┘
                                    │
          ┌─────────────────────────┼─────────────────────────┐
          │                         │                         │
          ▼                         ▼                         ▼
┌──────────────────────┐   ┌──────────────────────┐   ┌──────────────────────┐
│   MongoDB            │   │ Sentence Transformer │   │ Redis Cache          │
│ Raw text + metadata  │   │ Generate embeddings  │   │ Recent sessions      │
└───────────┬──────────┘   └───────────┬──────────┘   └───────────┬──────────┘
            │                          │                          │
            ▼                          ▼                          │
┌──────────────────────┐   ┌──────────────────────┐               │
│ Milvus Vector DB     │   │ Neo4j Graph DB       │               │
│ Store embeddings     │   │ User-Campaign-Intent │               │
│ + metadata           │   │ relationships        │               │
└───────────┬──────────┘   └───────────┬──────────┘               │
            │                          │                          │
            └──────────────┬───────────┼───────────────┬──────────┘
                           │           │
                           ▼           ▼
                 ┌─────────────────────────┐
                 │ Analytics Layer         │
                 │ BigQuery / SQLite mock  │
                 │ Aggregated metrics      │
                 └───────────┬──────────── ┘
                             │
                             ▼
                 ┌─────────────────────────┐
                 │ Recommendation API      │
                 │ FastAPI / Flask         │
                 │ Combines:               │
                 │ - Milvus similarity     │
                 │ - Neo4j campaigns       │
                 │ - BigQuery ranking      │
                 └─────────────────────────┘
