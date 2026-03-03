# db.py
import sqlite3
from pathlib import Path
from typing import List, Dict, Any
import json
from utils import now_iso

DB_PATH = Path("presencia_lab.db")

SCHEMA = """
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS scenarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    context TEXT,
    profile TEXT,
    state_internal TEXT,
    script TEXT,
    meta JSON,
    created_at TEXT
);

CREATE TABLE IF NOT EXISTS conversations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scenario_id INTEGER,
    role TEXT,             -- 'user' or 'her' or 'system'
    message TEXT,
    ts TEXT,
    FOREIGN KEY(scenario_id) REFERENCES scenarios(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS trainings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    scenario_id INTEGER,
    presence_score REAL,
    notes TEXT,
    created_at TEXT
);

CREATE TABLE IF NOT EXISTS metrics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    conv_id INTEGER,
    metric_key TEXT,
    metric_value REAL,
    created_at TEXT,
    FOREIGN KEY(conv_id) REFERENCES conversations(id) ON DELETE CASCADE
);
"""

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    return conn

def init_db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = get_conn()
    cur = conn.cursor()
    for stmt in SCHEMA.strip().split(";"):
        if stmt.strip():
            cur.execute(stmt)
    conn.commit()
    conn.close()

def save_scenario(context, profile, state_internal, script, meta):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO scenarios (context, profile, state_internal, script, meta, created_at) VALUES (?, ?, ?, ?, ?, ?)",
        (context, profile, state_internal, script, json.dumps(meta, ensure_ascii=False), now_iso())
    )
    conn.commit()
    sid = cur.lastrowid
    conn.close()
    return sid

def append_conversation(scenario_id, role, message):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO conversations (scenario_id, role, message, ts) VALUES (?, ?, ?, ?)",
        (scenario_id, role, message, now_iso())
    )
    conn.commit()
    cid = cur.lastrowid
    conn.close()
    return cid

def list_scenarios(limit=100):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, context, profile, state_internal, script, meta, created_at FROM scenarios ORDER BY id DESC LIMIT ?", (limit,))
    rows = cur.fetchall()
    conn.close()
    out = []
    for r in rows:
        out.append({
            "id": r[0],
            "context": r[1],
            "profile": r[2],
            "state_internal": r[3],
            "script": r[4],
            "meta": json.loads(r[5]),
            "created_at": r[6]
        })
    return out

def save_training(date_str, scenario_id, presence_score, notes=""):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO trainings (date, scenario_id, presence_score, notes, created_at) VALUES (?, ?, ?, ?, ?)",
        (date_str, scenario_id, presence_score, notes, now_iso())
    )
    conn.commit()
    tid = cur.lastrowid
    conn.close()
    return tid

def save_metric(conv_id, key, value):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO metrics (conv_id, metric_key, metric_value, created_at) VALUES (?, ?, ?, ?)",
        (conv_id, key, value, now_iso())
    )
    conn.commit()
    mid = cur.lastrowid
    conn.close()
    return mid