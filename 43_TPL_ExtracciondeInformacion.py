# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de un texto de ejemplo
texto = """
Juan Pérez nació el 5 de mayo de 1980 en Ciudad de México. Es un reconocido científico e investigador en el campo de la inteligencia artificial.
"""

# Función para extraer información relevante del texto
def extraer_informacion(texto):
    # Dividir el texto en oraciones
    oraciones = texto.split(".")
    
    # Inicializar variables para almacenar la información extraída
    nombre = ""
    fecha_nacimiento = ""
    profesion = ""
    
    # Buscar información relevante en cada oración
    for oracion in oraciones:
        # Buscar el nombre en la oración
        if "nació" in oracion:
            nombre = oracion.split(" nació")[0]
        
        # Buscar la fecha de nacimiento en la oración
        if "nació el" in oracion:
            fecha_nacimiento = oracion.split(" nació el ")[1].split(" en")[0]
        
        # Buscar la profesión en la oración
        if "científico" in oracion or "investigador" in oracion:
            profesion = "científico"
    
    return nombre, fecha_nacimiento, profesion

# Extraer información del texto
nombre, fecha_nacimiento, profesion = extraer_informacion(texto)

# Mostrar la información extraída
print("Nombre:", nombre)
print("Fecha de nacimiento:", fecha_nacimiento)
print("Profesión:", profesion)
