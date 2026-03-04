import time
from pathlib import Path
from utils import ensure_dirs, INBOX, PROCESSING, DONE, RESULTS, atomic_move, unique_name, write_text_atomic, log

POLL_SECONDS = 0.2  # cada cuánto mirar la cola

def parse_message(text: str) -> dict:
    data = {}
    for line in text.strip().splitlines():
        if "=" in line:
            k, v = line.split("=", 1)
            data[k.strip()] = v.strip()
    return data

def process_task(data: dict) -> str:
    number = int(data["number"])
    op = data.get("operation", "square")
    if op == "square":
        result = number * number
    elif op == "cube":
        result = number * number * number
    else:
        result = number
    return f"task_id={data.get('task_id')}\nnumber={number}\noperation={op}\nresult={result}\n"

def worker_loop(worker_id: int, stop_after: float = 10.0):
    ensure_dirs()
    start = time.time()
    log(f"WORKER {worker_id} started")

    while True:
        if time.time() - start > stop_after:
            log(f"WORKER {worker_id} stopping (time limit)")
            break

        msgs = sorted(INBOX.glob("*.txt"))
        if not msgs:
            time.sleep(POLL_SECONDS)
            continue

        msg_path = msgs[0]
        processing_path = PROCESSING / msg_path.name

        # Intento de "lock" moviéndolo a processing
        try:
            atomic_move(msg_path, processing_path)
        except FileNotFoundError:
            # otro worker lo pilló antes
            continue
        except PermissionError:
            continue

        try:
            raw = processing_path.read_text(encoding="utf-8")
            data = parse_message(raw)
            output = process_task(data)

            res_name = unique_name(f"result_w{worker_id}")
            res_path = RESULTS / res_name
            write_text_atomic(res_path, output)

            done_path = DONE / processing_path.name
            atomic_move(processing_path, done_path)

            log(f"WORKER {worker_id} processed {done_path.name} -> {res_name}")

        except Exception as e:
            log(f"WORKER {worker_id} ERROR on {processing_path.name}: {e}")
            # si falla, lo dejamos en processing para inspección
            time.sleep(POLL_SECONDS)

if __name__ == "__main__":
    # si lo lanzas a mano, worker_id=1 por defecto
    worker_loop(worker_id=1, stop_after=30.0)