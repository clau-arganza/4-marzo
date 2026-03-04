from pathlib import Path
from utils import ensure_dirs, INBOX, unique_name, write_text_atomic, log

def produce_tasks(n: int = 20):
    ensure_dirs()
    for i in range(1, n + 1):
        # ejemplo: cada tarea es un número a procesar
        msg = f"task_id={i}\nnumber={i}\noperation=square\n"
        filename = unique_name("msg")
        out_path = INBOX / filename
        write_text_atomic(out_path, msg)
        log(f"PRODUCER created {filename}")

if __name__ == "__main__":
    produce_tasks(30)