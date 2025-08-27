# Reto 1: Buscar enteros en un texto usando regex
# Paso a paso:
# 1. Leer el texto de entrada.
# 2. Definir una expresión regular para encontrar números enteros.
# 3. Buscar todos los enteros en el texto.
# 4. Imprimir los resultados.

import re

texto = "En 2023, había 16 estudiantes y 10 profesores, 10 tienen papá y 16 no tienen. "

# Expresión regular para enteros (positivos y negativos)
# patron = r"-?\\b\\d+\\b"
patron = r"\b-?\d+\b" #se movían los signos al lado de la primera b y se quitaban algunos \

# Buscar todos los enteros
enteros = re.findall(patron, texto)

print("Enteros encontrados:", enteros)
# Paso a paso:
# 1. Cambia el texto de prueba.
# 2. Modifica la expresión regular si es necesario.
# 3. Ejecuta el script y observa los resultado.
