
---

# 📄 `architecture.md`

```markdown
# Architecture Design

## Data Flow
1. **Conversation Ingestion**
   - Raw chat JSON ingested into MongoDB.
   - Redis caches recent sessions for low-latency retrieval.

2. **Embedding Generation**
   - Sentence Transformer generates 1024-dim embeddings.
   - Stored in Milvus with metadata (user_id, message_id).

3. **Relationship Mapping**
   - Neo4j graph links users, campaigns, and intents.
   - Enables queries like "which campaigns are connected to similar users?"

4. **Analytics Layer**
   - Aggregated metrics synced to BigQuery (or SQLite mock).
   - Supports engagement frequency ranking.

5. **Hybrid Retrieval API**
   - FastAPI endpoint `/recommendations/<user_id>`:
     - Vector similarity (Milvus)
     - Graph traversal (Neo4j)
     - Ranking (BigQuery/SQLite)

---

## Real-time vs Batch
- **Real-time**: MongoDB, Redis, Milvus, Neo4j
- **Batch**: BigQuery sync jobs

---

## Scaling & Fault Tolerance
- MongoDB sharding
- Milvus cluster mode with GPU acceleration
- Neo4j causal clustering
- BigQuery partitioned tables
- Redis TTL eviction
- Airflow retry policies

---

## Trade-offs
- **Polyglot persistence**: Each DB chosen for its strength
- **Orchestration-first**: Airflow/Prefect ensures modularity
- **Observability baked in**: Logging + anomaly detection
