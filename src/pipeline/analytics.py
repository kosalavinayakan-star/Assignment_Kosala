import sqlite3
from utils.logger import get_logger

logger = get_logger("analytics")

def update_metrics(user_id, campaign_id):
    conn = sqlite3.connect("analytics.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS engagement_metrics (
            user_id TEXT,
            campaign_id TEXT,
            engagement_count INTEGER,
            PRIMARY KEY (user_id, campaign_id)
        )
    """)
    cursor.execute("""
        INSERT INTO engagement_metrics (user_id, campaign_id, engagement_count)
        VALUES (?, ?, 1)
        ON CONFLICT(user_id, campaign_id)
        DO UPDATE SET engagement_count = engagement_count + 1
    """, (user_id, campaign_id))
    conn.commit()
    conn.close()
    logger.info(f"Updated metrics for user {user_id}, campaign {campaign_id}")