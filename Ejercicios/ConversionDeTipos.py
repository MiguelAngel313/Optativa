#  Pide por teclado la edad de una persona.
edad = input("Introduce tu edad: ")
#  Muestra la edad leída sumándole 3.
print("Tu edad dentro de 3 años será:", int(edad) + 3)
#  ¿Has obtenido un error? ¿A qué se debe? ¿Cómo se soluciona?
# ---No he obtenido ningun error. Se debe a que la funcion print devuelve un string y no un int por lo que hay que parsearlo.
#  Pide el nombre de una persona, su edad, su estatura y muestra un mensaje en pantalla con
# toda esa información. Debes mostrar la información con un formato “agradable”.
nombre = input("Introduce un nombre: ")
edad2 = input("Introduce una edad: ")
estatura = input("Introduce una estatura: ")
print("Tu nombre es {}, tu edad es {} y mides {}".format(nombre, edad2, estatura)) 

#  Pide un número decimal (float) por teclado y muéstralo en pantalla.
decimal = float(input("Introduce un decimal: "))
print(float(decimal))
#  Pide un número decimal (float) por teclado transfórmalo en entero y muéstralo por pantalla.
entero = int(decimal)
print(entero)
# Ejecuta el programa dos veces, la primera introduce 12.3 y la segunda 12.7. ¿La
# transformación a entero trunca o redondea?
# El programa trunca el numero y se queda con el 12
