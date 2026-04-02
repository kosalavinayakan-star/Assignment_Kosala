CREATE TABLE engagement_metrics (
    user_id TEXT,
    campaign_id TEXT,
    engagement_count INTEGER,
    PRIMARY KEY (user_id, campaign_id)
);
