# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de la posición inicial
posicion_actual = {"x": 0, "y": 0}

# Función para moverse hacia arriba
def mover_arriba(posicion):
    posicion["y"] += 1

# Función para moverse hacia abajo
def mover_abajo(posicion):
    posicion["y"] -= 1

# Función para moverse hacia la izquierda
def mover_izquierda(posicion):
    posicion["x"] -= 1

# Función para moverse hacia la derecha
def mover_derecha(posicion):
    posicion["x"] += 1

# Movimiento inicial
print("Posición inicial:", posicion_actual)
mover_derecha(posicion_actual)
print("Después de moverse hacia la derecha:", posicion_actual)
mover_arriba(posicion_actual)
print("Después de moverse hacia arriba:", posicion_actual)
mover_izquierda(posicion_actual)
print("Después de moverse hacia la izquierda:", posicion_actual)
mover_abajo(posicion_actual)
print("Después de moverse hacia abajo:", posicion_actual)
