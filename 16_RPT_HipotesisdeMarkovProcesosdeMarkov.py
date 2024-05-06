# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Supongamos que queremos simular el clima diario en una ciudad utilizando un modelo de Markov, donde el clima de mañana depende únicamente del clima de hoy.

import random

# Definimos los posibles estados del clima
soleado = 'Soleado'
nublado = 'Nublado'
lluvioso = 'Lluvioso'

# Definimos la matriz de transición de estados
matriz_transicion = {
    soleado: {soleado: 0.8, nublado: 0.1, lluvioso: 0.1},
    nublado: {soleado: 0.3, nublado: 0.4, lluvioso: 0.3},
    lluvioso: {soleado: 0.2, nublado: 0.3, lluvioso: 0.5}
}

# Función para simular el clima diario utilizando el modelo de Markov
def simular_clima_diario(matriz_transicion, dias_simulacion):
    # Empezamos con un día soleado
    clima_actual = soleado
    
    # Simulamos el clima para cada día
    print("Simulación del clima para {} días:".format(dias_simulacion))
    for dia in range(1, dias_simulacion + 1):
        print("Día {}: {}".format(dia, clima_actual))
        
        # Calculamos el clima del día siguiente utilizando la matriz de transición
        clima_siguiente = random.choices(list(matriz_transicion[clima_actual].keys()), 
                                         weights=list(matriz_transicion[clima_actual].values()))[0]
        
        # Actualizamos el clima actual para el próximo día
        clima_actual = clima_siguiente

# Simulamos el clima diario para 7 días
simular_clima_diario(matriz_transicion, 7)
