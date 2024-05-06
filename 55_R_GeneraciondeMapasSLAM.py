# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de las variables para la generación de mapas
posicion_actual = (0, 0)  # Posición inicial del robot en coordenadas (x, y)
mapa = {}  # Mapa del entorno

# Función para mover el robot y actualizar el mapa
def mover_robot(destino):
    global posicion_actual, mapa
    # Actualizar posición del robot
    posicion_actual = destino
    # Actualizar mapa con nueva posición
    if destino not in mapa:
        mapa[destino] = "Desconocido"
    print("El robot se ha movido a", destino)
    print("Mapa actualizado:", mapa)

# Simulación de la generación de mapas utilizando SLAM
print("Inicio de la generación de mapas")

# Movimientos del robot y actualización del mapa
mover_robot((1, 0))
mover_robot((1, 1))
mover_robot((2, 1))
mover_robot((2, 2))
