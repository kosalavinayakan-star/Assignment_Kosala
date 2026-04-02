import json
import pymongo
from utils.logger import get_logger

logger = get_logger("ingest")

def ingest_conversations(file_path="src/data/sample_conversations.json"):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["chatdb"]
    collection = db["conversations"]

    with open(file_path, "r") as f:
        data = json.load(f)

    for record in data:
        collection.insert_one(record)
        logger.info(f"Ingested record {record['message_id']}")

    return len(data)
