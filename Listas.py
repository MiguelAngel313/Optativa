#1. Crea una lista con 5 frutas y muestra la segunda fruta
frutas = ["manzana", "banana", "naranja", "uva", "pera"]
print(frutas[1])  # Debería mostrar "banana"

#2. Dada una lista de números, cambia el tercer elemento por 100
numeros = [10, 20, 30, 40, 50]
# Tu código aquí

numeros[2] = 100
print("Cambio de tercera posicion por 100: ", numeros)

#3 Dada una lista vacía, agrega 3 colores y luego elimina el último
colores = []
# Tu código aquí
colores.append('verde')
colores.append('azul')
colores.append('rojo')

colores.pop(len(colores)-1)

print("Colores: ",colores)

#4. Dada una lista de animales, muestra cuántos elementos tiene
animales = ["perro", "gato", "pájaro", "pez", "conejo"]
# Tu código aquí

print("Longitud animales: ", len(animales))

#5. Une dos listas en una sola
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
# Tu código aquí

otraLista = lista1 + lista2

print("Otra lista: ", otraLista)

#6. Dada una lista, extrae los elementos del índice 2 al 4 (slicing)
letras = ['a', 'b', 'c', 'd', 'e', 'f']
# Tu código aquí

print(" Ejercicio 6: ",letras[2:4])

#7. Verifica si un elemento específico está en la lista
paises = ["España", "Francia", "Italia", "Alemania"]
# Verifica si "Italia" está en la lista

print("Italia: ", paises.index("Italia"))

#8. Ordena una lista de números de menor a mayor
numeros = [34, 12, 89, 5, 23]
# Tu código aquí

numeros.sort()
print("Lista ordenada: ", numeros)

#9. Invierte el orden de los elementos en una lista
dias = ["lunes", "martes", "miércoles", "jueves", "viernes"]
# Tu código aquí

#10. Crea una matriz 2x2 y accede al elemento en la posición [1][0]
matriz = [[1, 2], [3, 4]]
# Tu código aquí
print("Matriz: ", matriz[1][0])