# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Datos observados
datos = [1.5, 2.0, 1.8, 2.2, 1.9]

# Parámetros de la distribución a priori
mu_0 = 0  # Media a priori
lambda_0 = 1  # Precisión a priori (inversa de la varianza)
alfa_0 = 1  # Parámetro de forma a priori para la distribución gamma
beta_0 = 1  # Parámetro de escala a priori para la distribución gamma

# Actualización de la distribución a priori a posteriori
n = len(datos)
mu_datos = sum(datos) / n
suma_cuadrados = sum((x - mu_datos) ** 2 for x in datos)

# Estimación de la media y la precisión a posteriori
lambda_post = lambda_0 + n
mu_post = (lambda_0 * mu_0 + n * mu_datos) / lambda_post

# Estimación de los parámetros de la distribución gamma a posteriori
alfa_post = alfa_0 + n / 2
beta_post = beta_0 + 0.5 * suma_cuadrados + (lambda_0 * n * (mu_datos - mu_0) ** 2) / (2 * lambda_post)

print("Media a posteriori:", mu_post)
print("Precisión a posteriori:", alfa_post / beta_post)
