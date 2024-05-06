# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

datos = [
    {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Barcelona'},
    {'nombre': 'María', 'edad': 30, 'ciudad': 'Madrid'},
    {'nombre': 'Carlos', 'edad': 28, 'ciudad': 'Sevilla'}
]

# Función para filtrar datos por edad
def filtrar_por_edad(datos, edad_limite):
    return [persona for persona in datos if persona['edad'] < edad_limite]

# Función para filtrar datos por ciudad
def filtrar_por_ciudad(datos, ciudad):
    return [persona for persona in datos if persona['ciudad'] == ciudad]

# Aplicar filtros
datos_filtrados_edad = filtrar_por_edad(datos, 30)
datos_filtrados_ciudad = filtrar_por_ciudad(datos, 'Madrid')

# Imprimir resultados
print("Personas con menos de 30 años:")
for persona in datos_filtrados_edad:
    print(persona)

print("\nPersonas que viven en Madrid:")
for persona in datos_filtrados_ciudad:
    print(persona)
