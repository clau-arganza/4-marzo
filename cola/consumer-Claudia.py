import os
import time

QUEUE_DIR = "cola"

print("[Claudia] Esperando archivos...")

while True:
    files = os.listdir(QUEUE_DIR)

    for file in files:
        if not file.endswith(".txt"):
            continue  # Ignorar cualquier cosa que no sea .txt

        filepath = os.path.join(QUEUE_DIR, file)
        processing_path = filepath + ".processing"

        try:
            os.rename(filepath, processing_path)

            print(f"Procesando {file}")

            with open(processing_path, "r") as f:
                print(f.read().strip())

            os.remove(processing_path)

        except FileNotFoundError:
            pass

    time.sleep(1)