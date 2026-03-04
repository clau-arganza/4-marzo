import os
import time

QUEUE_DIR = "cola"
counter = 0

print("[Carlos] Iniciando...")

while True:
    filename = f"p1_{counter}.txt"
    filepath = os.path.join(QUEUE_DIR, filename)

    with open(filepath, "w") as f:
        f.write(f"Generado por Carlos 1\n")

    print(f"[Carlos] Generó {filename}")
    
    counter += 1

    time.sleep(1)