# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de un diccionario de traducción
diccionario_traduccion = {
    "hello": "hola",
    "world": "mundo",
    "how": "cómo",
    "are": "estás",
    "you": "tú"
}

# Función para traducir una frase
def traducir_frase(frase, diccionario):
    # Dividir la frase en palabras
    palabras = frase.split()
    
    # Inicializar una lista para almacenar las palabras traducidas
    traduccion = []
    
    # Traducir cada palabra en la frase
    for palabra in palabras:
        # Buscar la traducción en el diccionario
        if palabra.lower() in diccionario:
            traduccion.append(diccionario[palabra.lower()])
        else:
            # Si la palabra no tiene traducción, mantenerla igual
            traduccion.append(palabra)
    
    # Unir las palabras traducidas en una sola frase
    frase_traducida = " ".join(traduccion)
    
    return frase_traducida

# Frase de ejemplo en inglés
frase_ingles = "Hello world! How are you?"

# Traducir la frase al español
frase_traducida = traducir_frase(frase_ingles, diccionario_traduccion)

# Mostrar la frase traducida
print("Frase en inglés:", frase_ingles)
print("Frase traducida:", frase_traducida)
