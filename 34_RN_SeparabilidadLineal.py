# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import matplotlib.pyplot as plt

# Datos de ejemplo
datos_clase_1 = [(1, 2), (2, 3), (3, 4), (4, 5)]
datos_clase_2 = [(1, 4), (2, 5), (3, 6), (4, 7)]

# Graficar los datos
plt.scatter([x[0] for x in datos_clase_1], [x[1] for x in datos_clase_1], color='blue', label='Clase 1')
plt.scatter([x[0] for x in datos_clase_2], [x[1] for x in datos_clase_2], color='red', label='Clase 2')

# Dibujar una línea que separa los datos
plt.plot([0, 5], [2, 7], color='green', linestyle='--', label='Frontera de decisión')

plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Ejemplo de datos linealmente separables')
plt.legend()
plt.grid(True)
plt.show()
