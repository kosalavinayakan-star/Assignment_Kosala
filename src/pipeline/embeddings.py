from sentence_transformers import SentenceTransformer
import numpy as np
from utils.logger import get_logger

logger = get_logger("embeddings")

model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embedding(text: str):
    embedding = model.encode(text)
    if embedding is None or len(embedding) == 0:
        logger.error("Empty embedding detected")
    return np.array(embedding)
