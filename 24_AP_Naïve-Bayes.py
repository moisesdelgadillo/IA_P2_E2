# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Datos de ejemplo (características y etiquetas)
datos = [
    {"altura": "Alta", "peso": "Normal", "sexo": "Hombre", "etiqueta": "Deportista"},
    {"altura": "Baja", "peso": "Bajo", "sexo": "Mujer", "etiqueta": "No deportista"},
    {"altura": "Media", "peso": "Normal", "sexo": "Mujer", "etiqueta": "Deportista"},
    {"altura": "Alta", "peso": "Alto", "sexo": "Hombre", "etiqueta": "Deportista"},
    {"altura": "Baja", "peso": "Normal", "sexo": "Hombre", "etiqueta": "No deportista"}
]

# Función para calcular las probabilidades a priori de las etiquetas
def calcular_probabilidades_a_priori(datos):
    etiquetas = [dato["etiqueta"] for dato in datos]
    probabilidades = {}
    total = len(etiquetas)
    for etiqueta in set(etiquetas):
        probabilidades[etiqueta] = etiquetas.count(etiqueta) / total
    return probabilidades

# Función para calcular las probabilidades condicionales de las características
def calcular_probabilidades_condicionales(datos, caracteristica, valor, etiqueta):
    coincidencias_etiqueta = [dato for dato in datos if dato["etiqueta"] == etiqueta]
    coincidencias = [dato for dato in coincidencias_etiqueta if dato[caracteristica] == valor]
    total_etiqueta = len(coincidencias_etiqueta)
    total_coincidencias = len(coincidencias)
    if total_etiqueta == 0:
        return 0
    return total_coincidencias / total_etiqueta

# Función para predecir la etiqueta de un nuevo dato
def predecir(datos, nuevo_dato):
    probabilidades_a_priori = calcular_probabilidades_a_priori(datos)
    probabilidades_prediccion = {}
    for etiqueta, probabilidad in probabilidades_a_priori.items():
        probabilidad_prediccion = probabilidad
        for caracteristica, valor in nuevo_dato.items():
            probabilidad_condicional = calcular_probabilidades_condicionales(datos, caracteristica, valor, etiqueta)
            if probabilidad_condicional == 0:
                probabilidad_prediccion = 0
                break
            probabilidad_prediccion *= probabilidad_condicional
        probabilidades_prediccion[etiqueta] = probabilidad_prediccion
    return max(probabilidades_prediccion, key=probabilidades_prediccion.get)

# Ejemplo de uso
nuevo_dato = {"altura": "Media", "peso": "Normal", "sexo": "Hombre"}
prediccion = predecir(datos, nuevo_dato)
print("Predicción:", prediccion)
