from typing import TypedDict

CREATE_USAGE_LOG_TABLE = """
CREATE TABLE IF NOT EXISTS usage_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL,
    input_tokens INTEGER NOT NULL,
    output_tokens INTEGER NOT NULL,
    cost REAL NOT NULL,
    model_name TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
"""


CREATE_CURRENT_STATUS_TABLE = """
CREATE TABLE IF NOT EXISTS current_status (
    user_id TEXT PRIMARY KEY,
    total_input_tokens INTEGER NOT NULL DEFAULT 0,
    total_output_tokens INTEGER NOT NULL DEFAULT 0,
    total_cost REAL NOT NULL DEFAULT 0,
    available_cost REAL
)
"""

class CurrentStatus(TypedDict):
    user_id: str
    total_input_tokens: int
    total_output_tokens: int
    total_cost: float
