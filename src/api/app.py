from fastapi import FastAPI
from pymilvus import Collection
from neo4j import GraphDatabase
import sqlite3

app = FastAPI()

@app.get("/recommendations/{user_id}")
def recommend(user_id: str):
    # Step 1: Vector search in Milvus
    collection = Collection("embeddings")
    results = collection.search(data=[[0.1]*384], anns_field="embedding", param={"metric_type":"L2"}, limit=5)

    similar_users = [hit.entity.get("user_id") for hit in results[0]]

    # Step 2: Fetch campaigns from Neo4j
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j","password"))
    campaigns = []
    with driver.session() as session:
        for u in similar_users:
            res = session.run("MATCH (u:User {id:$id})-[:ENGAGED]->(c:Campaign) RETURN c.id", id=u)
            campaigns.extend([r["c.id"] for r in res])

    # Step 3: Rank campaigns by engagement frequency
    conn = sqlite3.connect("analytics.db")
    cursor = conn.cursor()
    ranked = []
    for c in campaigns:
        cursor.execute("SELECT engagement_count FROM engagement_metrics WHERE campaign_id=?", (c,))
        count = cursor.fetchone()
        ranked.append({"campaign_id": c, "score": count[0] if count else 0})
    conn.close()

    ranked.sort(key=lambda x: x["score"], reverse=True)
    return {"user_id": user_id, "recommended_campaigns": ranked[:5]}
