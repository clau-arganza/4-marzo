import multiprocessing as mp
import time

from producer import produce_tasks
from worker import worker_loop
from collector import collect
from utils import ensure_dirs, log

def run_system(num_workers: int = 4, tasks: int = 30, worker_runtime: float = 8.0):
    ensure_dirs()
    log("CONTROLLER starting system")

    # 1) producir tareas
    produce_tasks(tasks)

    # 2) lanzar workers en paralelo
    procs = []
    for wid in range(1, num_workers + 1):
        p = mp.Process(target=worker_loop, kwargs={"worker_id": wid, "stop_after": worker_runtime})
        p.start()
        procs.append(p)

    # 3) esperar a que terminen
    for p in procs:
        p.join()

    # 4) recolectar resultados
    collect()
    log("CONTROLLER finished system")

if __name__ == "__main__":
    run_system(num_workers=4, tasks=30, worker_runtime=10.0)