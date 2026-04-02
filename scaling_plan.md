# Scaling Plan

## Goal
Evolve prototype to handle **10M+ users**, ensure **sub-100ms vector queries**, and maintain **cost efficiency**.

---

## Scaling Strategies

### 1. MongoDB
- Sharding across multiple nodes
- Use WiredTiger compression for storage efficiency
- TTL indexes for old conversations

### 2. Milvus
- Cluster mode with GPU acceleration
- Use HNSW or IVF_FLAT index for sub-100ms queries
- Redis caching for hot queries

### 3. Neo4j
- Causal clustering for high availability
- Partition graph by campaign or region
- Use relationship indexing for faster traversals

### 4. BigQuery
- Partition tables by date
- Use clustering on `user_id` and `campaign_id`
- Cold storage for historical data

### 5. Redis
- Use Redis Cluster for horizontal scaling
- TTL-based eviction for memory efficiency
- Store session embeddings for ultra-fast retrieval

---

## Cost Efficiency
- Spot instances for batch jobs
- Auto-scaling Kubernetes pods
- Cold storage for old conversations
- Serverless BigQuery queries for pay-per-use analytics

---

## Observability
- Prometheus + Grafana for metrics
- Alerts for anomalies (empty embeddings, missing relationships)
- MLflow for embedding quality tracking
