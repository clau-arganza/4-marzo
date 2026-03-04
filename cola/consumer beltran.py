import os
import time

CARPETA = r"C:\Users\BELTRÁN\Desktop\4-marzo\cola"
archivos_procesados = set()

print("Consumidor iniciado...")

while True:
    try:
        archivos = os.listdir(CARPETA)

        for nombre_archivo in archivos:
            ruta_completa = os.path.join(CARPETA, nombre_archivo)

            # Verificar que sea archivo
            if os.path.isfile(ruta_completa):

                if nombre_archivo not in archivos_procesados:
                    print(f"\nProcesando archivo: {nombre_archivo}")

                    with open(ruta_completa, "r", encoding="utf-8") as f:
                        contenido = f.read()
                        print(contenido)

                    archivos_procesados.add(nombre_archivo)

                    # 🔥 Solo borrar si es .txt
                    if nombre_archivo.lower().endswith(".txt"):
                        os.remove(ruta_completa)
                        print(f"Archivo {nombre_archivo} eliminado")

        time.sleep(2)

    except Exception as e:
        print("Error:", e)
        time.sleep(2)