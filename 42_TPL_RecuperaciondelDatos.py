# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import csv

# Función para leer datos desde un archivo CSV
def leer_datos_csv(nombre_archivo):
    datos = []
    with open(nombre_archivo, newline='') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            datos.append(fila)
    return datos

# Ejemplo de uso
nombre_archivo = 'datos.csv'
datos = leer_datos_csv(nombre_archivo)

# Imprimir los datos obtenidos
print("Datos recuperados del archivo CSV:")
for dato in datos:
    print(dato)
