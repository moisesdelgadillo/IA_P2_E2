# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import random

# Definimos los estados ocultos del modelo (soleado y lluvioso)
soleado = 'Soleado'
lluvioso = 'Lluvioso'

# Definimos las observaciones (si las personas llevan paraguas o no)
con_paraguas = 'Con paraguas'
sin_paraguas = 'Sin paraguas'

# Definimos las probabilidades de transición entre los estados ocultos
# Estas son las probabilidades de cambiar de un estado oculto a otro
probabilidades_transicion = {
    soleado: {soleado: 0.8, lluvioso: 0.2},
    lluvioso: {soleado: 0.4, lluvioso: 0.6}
}

# Definimos las probabilidades de observación para cada estado oculto
# Estas son las probabilidades de observar si las personas llevan paraguas o no
probabilidades_observacion = {
    soleado: {con_paraguas: 0.1, sin_paraguas: 0.9},
    lluvioso: {con_paraguas: 0.8, sin_paraguas: 0.2}
}

# Función para simular el modelo oculto de Markov y predecir el clima
def simular_clima(num_dias):
    # Empezamos en un estado oculto aleatorio
    estado_actual = random.choice([soleado, lluvioso])
    
    # Simulamos el clima para el número de días especificado
    for dia in range(1, num_dias + 1):
        # Simulamos la observación del clima (si las personas llevan paraguas o no)
        observacion = random.choices([con_paraguas, sin_paraguas], 
                                     weights=list(probabilidades_observacion[estado_actual].values()))[0]
        
        # Imprimimos la predicción del clima para el día actual
        print(f"Día {dia}: El clima es {estado_actual} y las personas están {observacion}")
        
        # Actualizamos el estado oculto para el próximo día basado en las probabilidades de transición
        estado_actual = random.choices(list(probabilidades_transicion[estado_actual].keys()), 
                                       weights=list(probabilidades_transicion[estado_actual].values()))[0]

# Simulamos el clima para 7 días
print("Simulación del modelo oculto de Markov para predecir el clima:")
simular_clima(7)
