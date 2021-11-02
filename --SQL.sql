-- SQLite
CREATE TABLE IF NOT EXISTS fp_logs (
    id integer PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    game TEXT,
    query TEXT,
    last_response INETEGER DEFAULT 0
);