# 1. Pedir un número por teclado y mostrar su tabla de multiplicar. La información debe salir
# encolumnada.
numero = int(input("Introduce un numero: "))
valor = numero
for i in range(0, 11):
    print(numero, " x ", i, " = ", numero * i)

# 2. Pedir un número por teclado y mostrar la suma de todos los números que hay desde 0 hasta
# el número dado.
    resultado = 0
for i in range(0, numero):
    resultado += i
print("Resultado de la suma: ", resultado)
# 3. Pedir números hasta que el usuario introduzca un número negativo.

while numero > 0:
    numero = int(input("Introduce un numero positivo: "))
numero = valor
# 4. Pedir números hasta que el usuario introduzca un número negativo. En ese momento
# mostrar:
contador = 0
suma = 0
media = 0

while numero > 0:
    contador += 1
    suma += numero
    media = suma / contador
    numero = int(input("Introduce un numero ppositivo: "))

#  El número total de números introducidos.
#  La suma de los números introducidos.
#  La media de los números introducidos.

print("Se han introducido {} numeros, la suma total de todos ellos es {} y la media es {}".format(contador, suma, media))

# 5. Pedir un número por teclado y mostrar su factorial. Recuerda que no existe el factorial de
# números negativos y que el factorial de 0 es 1.

numero = valor
factorial = 1

for i in range (1, numero+1):
    factorial = factorial*i
print("El factorial de {} es {}".format(numero, factorial))
# 6. Pedir 5 números por teclado y mostrar la suma de los números que son negativos y la suma
# de los que son positivos
lista = []
contador = 0
positivos = 0
negativos = 0
while contador < 5:
    num = int(input("Introduce un numero: "))
    contador += 1
    lista.append(num)

for i in lista:
    if i >= 0:
        positivos += i
    else:
        negativos += i
print("La suma de los numeros positivos es {} y la de los negativos es {}.".format(positivos, negativos))