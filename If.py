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
pass1 = input("Introduce una contrasena:")
pass2 = input("Vuelve a introducirla: ")
print("Perfecto¡" if pass1 == pass2 else "Las contrasenas no coinciden.")
# 7. Pide un número e indica si es mayor que 100 o no.
print("Es mayor que 100." if numero > 100 else "Es menor que 100.")
# 8. Las calificaciones de un examen pueden ser de 1 a 10 y se clasifican de la siguiente forma:
calificacion = int(input("Introduce una calificacion: "))
# De 1 a 4 incluidos: suspenso
if calificacion >= 1 and calificacion <= 4:
    print("Suspenso.")
# De 5 a 6 incluidos: aprobado
elif calificacion == 5 or calificacion == 6:
    print("Aprobado.")
# De 7 a 8 incluidos: notable
elif calificacion == 7 or calificacion == 8:
    print("Notable.")
# Más de 8 y menos o igual a 10: sobresaliente
elif calificacion > 8 and calificacion <= 10:
    print("Sobresaliente.")
else:
    print("No es una nota valida.")
# Pide por teclado la edad y muestra la clasificación que le corresponde.
# 9. Pide una cadena de texto e indica si tiene entre 6 y 10 caracteres.
cadena = input("Introduce una cadena: ")
print("{} tiene entre 6 y 10 caracteres.".format(cadena) if len(cadena) >=6 and len(cadena) <= 10 else "{} no tiene entre 6 y 10 caracteres".format(cadena)) 
# 10. Pide un número e indica si es múltiplo de 3.
print("{} es multiplo de 3.".format(numero) if numero % 3 == 0 else "{} no es multiplo de 3".format(numero))
# 11. Pide un carácter e indica si se corresponde con un número.
caracter = input("Introduce un numero: ")
print("{} es un numero.".format(caracter) if caracter.isnumeric() else "{} no es un numero.".format(caracter))
# 12. Pide un carácter e indica si se corresponde con una letra.
charLetra = input("Introduce una letra: ")
print("{} es una letra.".format(charLetra) if charLetra.isalpha() else "{} no es una letra.".format(charLetra))
# 13. Pide una letra e indica si es vocal o consonante. En caso de introducir más de un carácter
# indicar un error.
letra = input("Introduce una letra: ")
if len(letra) > 1:
    print("Solo puedes introducir una letra.")
elif letra.isalpha():
    vocales = ['a','e','i','o','u']
    if letra.lower() in vocales:
        print("La letra introducida es una vocal.")
    else:
        print("La letra introducida es una consonante.")
else:
    print("El caracter introducido no es una letra")