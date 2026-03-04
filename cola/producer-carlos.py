#Crean archivos dentro de cola/
import time
import datetime
from tools import write_cola

while True:
    time.sleep(1)
    #Crear archivo
    print("Soy Carlos y creo un archivo del Atlético de Madrid")
    linea="Carlos,9,Hola colchoneros"
    file_name="Carlos_"+datetime.datetime.now().strftime()
    write_cola(linea,file_name)