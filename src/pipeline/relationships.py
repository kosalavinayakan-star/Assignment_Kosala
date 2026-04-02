from neo4j import GraphDatabase
from utils.logger import get_logger

logger = get_logger("relationships")

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

def create_relationship(user_id, campaign_id, intent):
    with driver.session() as session:
        session.run("""
            MERGE (u:User {id:$user_id})
            MERGE (c:Campaign {id:$campaign_id})
            MERGE (i:Intent {name:$intent})
            MERGE (u)-[:ENGAGED]->(c)
            MERGE (c)-[:HAS_INTENT]->(i)
        """, user_id=user_id, campaign_id=campaign_id, intent=intent)
        logger.info(f"Linked user {user_id} to campaign {campaign_id} with intent {intent}")
