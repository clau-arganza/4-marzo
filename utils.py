import os
import time
import uuid
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
QUEUES_DIR = BASE_DIR / "queues"

INBOX = QUEUES_DIR / "inbox"
PROCESSING = QUEUES_DIR / "processing"
DONE = QUEUES_DIR / "done"
RESULTS = QUEUES_DIR / "results"
LOGS = QUEUES_DIR / "logs"

def ensure_dirs():
    for p in [INBOX, PROCESSING, DONE, RESULTS, LOGS]:
        p.mkdir(parents=True, exist_ok=True)

def unique_name(prefix: str, ext: str = ".txt") -> str:
    return f"{prefix}_{int(time.time()*1000)}_{os.getpid()}_{uuid.uuid4().hex}{ext}"

def atomic_move(src: Path, dst: Path):
    # movimiento atómico (si está en mismo disco)
    os.replace(src, dst)

def write_text_atomic(path: Path, content: str):
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(content, encoding="utf-8")
    os.replace(tmp, path)

def log(msg: str):
    ensure_dirs()
    log_file = LOGS / "system.log"
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    with log_file.open("a", encoding="utf-8") as f:
        f.write(f"[{ts}] {msg}\n")