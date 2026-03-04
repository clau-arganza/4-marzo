import os
import time


QUEUE_DIR = "cola"

print("[Carlos] Iniciando...")

counter = 0

while True:
    filename = f"p2_{counter}.txt"
    filepath = os.path.join(QUEUE_DIR, filename)

    with open(filepath, "w") as f:
        f.write(f"Generado por Producer 2\n")

    print(f"[Carlos] Generó {filename}")
    
    counter += 1

    time.sleep(1)