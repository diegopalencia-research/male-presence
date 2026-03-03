# utils.py
from datetime import datetime, timezone

def now_iso():
    return datetime.now(timezone.utc).isoformat()

def ts_to_sec(iso_ts):
    dt = datetime.fromisoformat(iso_ts)
    return dt.timestamp()