from pipeline.ingest import ingest_conversations
from pipeline.embeddings import generate_embedding
from pipeline.storage import create_collection, insert_embedding
from pipeline.relationships import create_relationship
from pipeline.analytics import update_metrics

def run_pipeline():
    count = ingest_conversations()
    collection = create_collection()

    # Example: process one record
    text = "Hello, I want to know more about product X"
    embedding = generate_embedding(text)
    insert_embedding(collection, "user123", "msg001", embedding)
    create_relationship("user123", "campaignA", "interest")
    update_metrics("user123", "campaignA")

if __name__ == "__main__":
    run_pipeline()
