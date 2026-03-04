import time

def extraer_numero(nombre_archivo):
    # Extrae el número del nombre del archivo, asumiendo formato "numero.txt"
    return int(nombre_archivo.split(".")[0])

def crear_archivo_multiplo_cinco(i):
    multiplo_5 = i * 5
    nombre_archivo = f"{multiplo_5}.txt"
    with open(nombre_archivo, "w") as archivo:
        archivo.write(f"Archivo múltiplo de 5 con nombre {multiplo_5}\n")
    print(f"Archivo creado (múltiplo de 5): {nombre_archivo}")
    return nombre_archivo

def crear_archivo_multiplo_cuatro(i):
    multiplo_4 = i * 4
    if multiplo_4 % 5 == 0:
        nombre_num = multiplo_4 + 2
    else:
        nombre_num = multiplo_4
    nombre_archivo = f"{nombre_num}.txt"
    with open(nombre_archivo, "w") as archivo:
        archivo.write(f"Archivo múltiplo de 4 (ajustado) con nombre {nombre_num}\n")
    print(f"Archivo creado (múltiplo de 4): {nombre_archivo}")
    return nombre_archivo

def comparar_diferencia(archivo_5, archivo_4):
    num_5 = extraer_numero(archivo_5)
    num_4 = extraer_numero(archivo_4)
    diferencia = abs(num_5 - num_4)
    if diferencia == 1:
        print(f"Diferencia correcta de 1 entre {num_5} (5) y {num_4} (4)")
    else:
        print(f"Error: La diferencia entre {num_5} (5) y {num_4} (4) no es 1")

def main(cantidad):
    lista_5 = []
    lista_4 = []
    lista_comparacion = []  # Mantendrá hasta dos archivos para comparar
    indice_4 = 0
    indice_5 = 0

    # Crear listas completas de archivos múltiplos de 5 y 4
    for i in range(1, cantidad + 1):
        archivo_5 = crear_archivo_multiplo_cinco(i)
        lista_5.append(archivo_5)
        archivo_4 = crear_archivo_multiplo_cuatro(i)
        lista_4.append(archivo_4)

    # Inicializamos la lista de comparación con el primer par
    lista_comparacion.append(lista_5[indice_5])
    lista_comparacion.append(lista_4[indice_4])
    comparar_diferencia(lista_5[indice_5], lista_4[indice_4])

    while True:
        # Avanzar índice de 4, añadir archivo a lista_comparacion y eliminar primero
        indice_4 += 1
        if indice_4 >= cantidad:
            print("Se alcanzó el final de la lista de múltiplos de 4.")
            break
        lista_comparacion.append(lista_4[indice_4])
        eliminado = lista_comparacion.pop(0)
        print(f"Eliminado de lista_comparacion: {eliminado}")
        comparar_diferencia(lista_comparacion[0], lista_comparacion[1])

        time.sleep(1)

        # Avanzar índice de 5, añadir archivo a lista_comparacion y eliminar primero
        indice_5 += 1
        if indice_5 >= cantidad:
            print("Se alcanzó el final de la lista de múltiplos de 5.")
            break
        lista_comparacion.append(lista_5[indice_5])
        eliminado = lista_comparacion.pop(0)
        print(f"Eliminado de lista_comparacion: {eliminado}")
        comparar_diferencia(lista_comparacion[0], lista_comparacion[1])

        time.sleep(1)

if __name__ == "__main__":
    main(10)

