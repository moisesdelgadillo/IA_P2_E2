# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import random

# Definimos los estados ocultos del clima
ESTADOS_CLIMA = ['Soleado', 'Nublado', 'Lluvioso']

# Definimos las observaciones de los sensores
OBSERVACIONES = ['Seco', 'Húmedo']

# Matriz de probabilidades de transición entre estados del clima
prob_transicion_clima = {
    'Soleado': {'Soleado': 0.7, 'Nublado': 0.2, 'Lluvioso': 0.1},
    'Nublado': {'Soleado': 0.3, 'Nublado': 0.5, 'Lluvioso': 0.2},
    'Lluvioso': {'Soleado': 0.2, 'Nublado': 0.4, 'Lluvioso': 0.4}
}

# Matriz de probabilidades de emisión de los sensores dado el clima
prob_emision_clima = {
    'Soleado': {'Seco': 0.9, 'Húmedo': 0.1},
    'Nublado': {'Seco': 0.6, 'Húmedo': 0.4},
    'Lluvioso': {'Seco': 0.1, 'Húmedo': 0.9}
}

# Función para simular una secuencia de observaciones y estados ocultos
def simular_secuencia(longitud):
    secuencia_clima = []
    secuencia_observaciones = []
    estado_actual = random.choice(ESTADOS_CLIMA)
    for _ in range(longitud):
        secuencia_clima.append(estado_actual)
        observacion = random.choices(OBSERVACIONES, weights=[prob_emision_clima[estado_actual][o] for o in OBSERVACIONES])[0]
        secuencia_observaciones.append(observacion)
        estado_actual = random.choices(ESTADOS_CLIMA, weights=[prob_transicion_clima[estado_actual][e] for e in ESTADOS_CLIMA])[0]
    return secuencia_clima, secuencia_observaciones

# Ejemplo de uso
secuencia_clima, secuencia_observaciones = simular_secuencia(7)
print("Secuencia de estados del clima:", secuencia_clima)
print("Secuencia de observaciones:", secuencia_observaciones)
