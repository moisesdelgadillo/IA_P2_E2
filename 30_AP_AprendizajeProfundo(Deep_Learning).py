# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import random
import math
# Definición de la función de activación sigmoide
def sigmoide(x):
    return 1 / (1 + math.exp(-x))

# Definición de la función de derivada de la función de activación sigmoide
def derivada_sigmoide(x):
    return sigmoide(x) * (1 - sigmoide(x))

# Definición de la red neuronal
class RedNeuronal:
    def __init__(self, num_entradas, num_ocultas, num_salidas):
        self.num_entradas = num_entradas
        self.num_ocultas = num_ocultas
        self.num_salidas = num_salidas

        # Inicialización de los pesos
        self.pesos_entrada_oculta = [[random.uniform(-1, 1) for _ in range(num_entradas)] for _ in range(num_ocultas)]
        self.pesos_oculta_salida = [[random.uniform(-1, 1) for _ in range(num_ocultas)] for _ in range(num_salidas)]

    # Método para realizar una predicción
    def predecir(self, entrada):
        # Calcular la salida de la capa oculta
        salida_oculta = [0] * self.num_ocultas
        for j in range(self.num_ocultas):
            salida_oculta[j] = sigmoide(sum(entrada[i] * self.pesos_entrada_oculta[j][i] for i in range(self.num_entradas)))

        # Calcular la salida final
        salida_final = [0] * self.num_salidas
        for k in range(self.num_salidas):
            salida_final[k] = sigmoide(sum(salida_oculta[j] * self.pesos_oculta_salida[k][j] for j in range(self.num_ocultas)))

        return salida_final

    # Método para entrenar la red neuronal utilizando backpropagation
    def entrenar(self, entradas, salidas, tasa_aprendizaje, epocas):
        for _ in range(epocas):
            for entrada, salida in zip(entradas, salidas):
                # Paso forward
                salida_oculta = [0] * self.num_ocultas
                for j in range(self.num_ocultas):
                    salida_oculta[j] = sigmoide(sum(entrada[i] * self.pesos_entrada_oculta[j][i] for i in range(self.num_entradas)))

                salida_final = [0] * self.num_salidas
                for k in range(self.num_salidas):
                    salida_final[k] = sigmoide(sum(salida_oculta[j] * self.pesos_oculta_salida[k][j] for j in range(self.num_ocultas)))

                # Paso backward
                errores_salida = [0] * self.num_salidas
                for k in range(self.num_salidas):
                    errores_salida[k] = (salida[k] - salida_final[k]) * derivada_sigmoide(salida_final[k])

                errores_oculta = [0] * self.num_ocultas
                for j in range(self.num_ocultas):
                    errores_oculta[j] = sum(errores_salida[k] * self.pesos_oculta_salida[k][j] for k in range(self.num_salidas)) * derivada_sigmoide(salida_oculta[j])

                # Actualizar pesos
                for j in range(self.num_ocultas):
                    for i in range(self.num_entradas):
                        self.pesos_entrada_oculta[j][i] += tasa_aprendizaje * errores_oculta[j] * entrada[i]

                for k in range(self.num_salidas):
                    for j in range(self.num_ocultas):
                        self.pesos_oculta_salida[k][j] += tasa_aprendizaje * errores_salida[k] * salida_oculta[j]

# Ejemplo de uso
red = RedNeuronal(2, 2, 1)
entradas = [[0, 0], [0, 1], [1, 0], [1, 1]]
salidas = [[0], [1], [1], [0]]
red.entrenar(entradas, salidas, 0.5, 1000)

# Prueba
print("Predicciones después del entrenamiento:")
for entrada in entradas:
    print(entrada, red.predecir(entrada))
