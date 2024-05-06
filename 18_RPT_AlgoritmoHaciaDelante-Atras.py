# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import random

# Definimos las posibles direcciones del robot
direcciones = ['Arriba', 'Abajo', 'Izquierda', 'Derecha']

# Definimos las posibles ubicaciones del robot en el laberinto
ubicaciones = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

# Función para simular los movimientos del robot
def simular_movimientos_robot(num_pasos):
    # Empezamos en una ubicación aleatoria
    ubicacion_actual = random.choice(ubicaciones)
    
    # Simulamos los movimientos del robot
    for paso in range(num_pasos):
        # Elegimos aleatoriamente la próxima dirección del robot
        direccion_elegida = random.choice(direcciones)
        
        # Imprimimos el movimiento del robot
        print(f"Paso {paso + 1}: El robot se mueve hacia {direccion_elegida}")
        
        # Actualizamos la ubicación del robot (solo por fines de simulación)
        # En un caso real, deberíamos considerar la lógica para actualizar la ubicación
        # basada en la dirección elegida y las restricciones del laberinto
        ubicacion_actual = random.choice(ubicaciones)

# Simulamos los movimientos del robot durante 5 pasos
print("Simulación de los movimientos del robot en el laberinto:")
simular_movimientos_robot(5)
