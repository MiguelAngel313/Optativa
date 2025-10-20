# 1. Pide un número por teclado y muestra uno de los siguientes mensajes: “El número es menor
# que cero”, “El número es mayor que cero” o “El número es cero” según el número
# introducido.
numero = input("Introduce un numero: ")
numero = int(numero)
if numero == 0:
    print("El numero es cero.")
elif numero > 0:
    print("El numero es mayor que cero.")
else:
    print("El numero es menor que cero.")
# 2. Pide la edad de una persona y muestra el mensaje “Eres menor de edad” o “Eres mayor de
# dad” según el valor introducido.
edad = numero
if edad >= 18 and edad <= 116:
    print("Eres mayor de edad.")
elif edad < 18 and edad > 0:
    print("Eres menor de edad.")
else:
    print("Introduce una edad valida.")
# 3. Pide un número e indica si es par o no.
print("{} es par.".format(numero) if numero % 2 == 0 else "{} no es par.".format(numero))
# 4. Pide un número e indica si es divisor de 21.
print("{} es divisor de 21.".format(numero) if 21 % numero == 0 else "{} no es divisor de 21.".format(numero) )
# 5. Pide un número e indica si es negativo o positivo.
print("{} es positivo.".format(numero) if numero > 0 else "{} es negativo.".format(numero))
# 6. Pide al usuario una contraseña. Vuelve a pedirla y verifica si es la misma que antes
# mostrando un mensaje por pantalla.
# 7. Pide un número e indica si es mayor que 100 o no.
# 8. Las calificaciones de un examen pueden ser de 1 a 10 y se clasifican de la siguiente forma:
# De 1 a 4 incluidos: suspenso
# De 5 a 6 incluidos: aprobado
# De 7 a 8 incluidos: notable
# Más de 8 y menos o igual a 10: sobresaliente
# Pide por teclado la edad y muestra la clasificación que le corresponde.
# 9. Pide una cadena de texto e indica si tiene entre 6 y 10 caracteres.
# 10. Pide un número e indica si es múltiplo de 3.
# 11. Pide un carácter e indica si se corresponde con un número.
# 12. Pide un carácter e indica si se corresponde con una letra.
# 13. Pide una letra e indica si es vocal o consonante. En caso de introducir más de un carácter
# indicar un error.