# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de funciones para el software robótico

# Función para mover el brazo robótico
def mover_brazo(posicion):
    print(f"Moviendo el brazo a la posición {posicion} grados.")

# Función para abrir o cerrar la pinza del robot
def controlar_pinza(estado):
    if estado == "abrir":
        print("Abriendo la pinza del robot.")
    elif estado == "cerrar":
        print("Cerrando la pinza del robot.")
    else:
        print("Estado de la pinza no reconocido.")

# Función para desplazar el robot móvil
def desplazar_robot(distancia):
    print(f"Desplazando el robot móvil {distancia} metros.")

# Variables
angulo_brazo = 90  # Angulo de posición del brazo robótico
estado_pinza = "abrir"  # Estado inicial de la pinza del robot
distancia_desplazamiento = 5  # Distancia de desplazamiento del robot móvil

# Acciones del software robótico
mover_brazo(angulo_brazo)
controlar_pinza(estado_pinza)
desplazar_robot(distancia_desplazamiento)
