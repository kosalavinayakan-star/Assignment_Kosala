from pymilvus import connections, Collection, FieldSchema, CollectionSchema, DataType
from utils.logger import get_logger

logger = get_logger("storage")

connections.connect("default", host="localhost", port="19530")

def create_collection():
    fields = [
        FieldSchema(name="user_id", dtype=DataType.VARCHAR, max_length=64),
        FieldSchema(name="message_id", dtype=DataType.VARCHAR, max_length=64),
        FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=384)
    ]
    schema = CollectionSchema(fields, description="User message embeddings")
    collection = Collection("embeddings", schema)
    return collection

def insert_embedding(collection, user_id, message_id, embedding):
    collection.insert([[user_id], [message_id], [embedding.tolist()]])
    logger.info(f"Inserted embedding for {message_id}")
