# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de las variables de los sensores
temperatura_ambiente = 25  # Temperatura ambiente en grados Celsius
humedad_ambiente = 50  # Humedad relativa del ambiente en porcentaje

# Definición de las variables de los actuadores
luz_encendida = False  # Estado de la luz (apagada inicialmente)
puerta_abierta = False  # Estado de la puerta (cerrada inicialmente)

# Función para encender la luz
def encender_luz():
    global luz_encendida
    luz_encendida = True
    print("¡Luz encendida!")

# Función para apagar la luz
def apagar_luz():
    global luz_encendida
    luz_encendida = False
    print("Luz apagada")

# Función para abrir la puerta
def abrir_puerta():
    global puerta_abierta
    puerta_abierta = True
    print("¡Puerta abierta!")

# Función para cerrar la puerta
def cerrar_puerta():
    global puerta_abierta
    puerta_abierta = False
    print("Puerta cerrada")

# Simulación del comportamiento del sistema
print("Temperatura ambiente:", temperatura_ambiente, "°C")
print("Humedad ambiente:", humedad_ambiente, "%")

# Acciones basadas en las condiciones ambientales
if temperatura_ambiente > 30:
    encender_luz()
elif humedad_ambiente > 60:
    abrir_puerta()
else:
    cerrar_puerta()
