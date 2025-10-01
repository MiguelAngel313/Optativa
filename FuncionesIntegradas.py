# 1. Haz una tabla con la utilidad de cada una de las funciones.
# 2. Muestra el menor valor de la lista.
numeros = [44, 8, 15, 6, 23, 43]
print("Menor valor de todos los numeros: ",min(numeros))
# 3. Muestra el mayor valor de la lista.
print("Mayor valor de todos los numeros: ",max(numeros))
# 4. Muestra la suma de todos los números de la lista.
print("Suma de todos los numeros: ",sum(numeros))
# 5. Muestra cuántos elementos tiene la lista.
print("Elementos de la lista: ",len(numeros))
# 6. Calcula la media de todos los elementos de la lista.
media = sum(numeros)/len(numeros)
print("Media: ",media)
# 7. Calcula la media de todos los elementos de la lista y muestra el resultado solo con dos
# decimales.
print("Dos decimales: ",round(media,2))
# 8. Muestra los elementos de la lista ordenados ascendentemente. La lista inicial no debe
# cambiar.
print("Lista ordenada: ",sorted(numeros))
# 9. Ordena los elementos de la lista y muéstralos.
numeros = sorted(numeros)
print("Numeros ordenados: ",numeros)
# 10. ¿Qué diferencia hay entre los dos ejercicios anteriores?
#El ejercicio 9 los ordena y los muestra pero sin llegar a hacer permanente el cambio de posicion mientras que en el ejercicio 10 primero se modifica el orden dejandolo guardado y despues se muestra
# 11. Crea una lista de 5 números con range y muéstrala.
lista1=list(range(5))
print("Lista con range: ",lista1)
# 12. Crea una lista de los 10 primeros números pares usando range y muéstrala.
listaPares=list(range(0, 10, 2))
print("Lista pares: ",listaPares)
# 13. Crea una lista con los siguientes animales: zorro, elefante, gallina
animales = ["zorro", "elefante", "gallina"]
print("Lista animales: ", animales)
# 14. Ordena alfabéticamente la lista.
animales.sort()
print("Lista de animales ordenada: ", animales)
# 15. Redondea el número 7.856 a dos decimales.
print("7.856 redondeado a dos decimales: ", round(7.856, 2))
