saludo = "hola"

print(saludo[::-1])  # Output: aloh

"""Compresion en python"""
''' compresion de listas'''

numeros = [1, 2, 3, 4, 5]

cuadrados = [x**2 for x in numeros if x % 2 == 0]

print(cuadrados)  # Output: [4, 16]