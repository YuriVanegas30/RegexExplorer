import re # Se importa la librería regular expressions la cual es necesaria para que el código funcione con expresiones regulares

texto = input ("Introduzca el texto:") # Se crea la variable que solicita el texto al usuario

los_números_enteros_son = r"\b-?\d+\b" # Se crea la variables
los_números_flotantes_son = r"\b-?\d+\.\d+\b"
los_strings_son = r'"(.*?)"'
las_listas_son = r"\[\s*\d+(?:\s*,\s*\d+)*\s*\]"
Booleanos = r"\b(True|False)\b"


enteros = re.findall(los_números_enteros_son, texto)
flotantes = re.findall(los_números_flotantes_son, texto)
strings = re.findall(los_strings_son, texto)
listas = re.findall(las_listas_son, texto)
Booleans = re.findall(Booleanos, texto, re.IGNORECASE)
print()
print("Enteros:", enteros)
print()
print("Flotantes:", flotantes)
print()
print("Strings:", strings)
print()
print("Listas:", listas)
print()
print("Booleanos encontrados:", Booleans)








