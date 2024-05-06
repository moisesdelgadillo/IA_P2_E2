# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de la función para calcular la acción de control
def calcular_accion_control(posicion_actual, referencia_deseada, Kp, Ki):
    # Calcular el error de posición
    error_posicion = referencia_deseada - posicion_actual
    
    # Calcular la acción proporcional
    accion_proporcional = Kp * error_posicion
    
    # Calcular la acción integral
    accion_integral = Ki * error_posicion
    
    # Calcular la acción de control total
    accion_control = accion_proporcional + accion_integral
    
    return accion_control

# Variables
posicion_actual = 10  # Posición actual del sistema
referencia_deseada = 20  # Posición de referencia deseada
Kp = 0.5  # Ganancia proporcional
Ki = 0.1  # Ganancia integral

# Calcular la acción de control
accion_control = calcular_accion_control(posicion_actual, referencia_deseada, Kp, Ki)

# Imprimir la acción de control calculada
print("La acción de control calculada es:", accion_control)
