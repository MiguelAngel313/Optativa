# Miguel Angel Herrojo Gonzalez
#Tarea 2

temperaturas = [12, 18, 21, 7, -2, 3]

# 1. Añadir un elemento (el 100) de forma que aparezca en la tercera posición de la lista. Se debe imprimir
#el resultado.

temperaturas.insert(2, 100)
print('Temperaturas normales: ',temperaturas)

#2. Crear una nueva lista llamada temp_positivas mediante comprensión que contenga solo las
#temperaturas positivas. Se debe imprimir el resultado.
temp_positivas = [positivo for positivo in temperaturas if positivo > 0]
print('Temperaturas positivas: ',temp_positivas)

#3. Convierte todas las temperaturas positivas a Fahrenheit (preferentemente) mediante una función
#lambda. El resultado debe quedar en una lista llamada F. La forma de convertir una temperatura de
#grados Celsius a grados Fahrenheit es: Fahrenheit = Celsius * 9 / 5 + 32 Se debe imprimir
#el resultado.

F = [celsius * 9 / 5 + 32 for celsius in temp_positivas]
print('TEmperaturas en celsius: ',F)