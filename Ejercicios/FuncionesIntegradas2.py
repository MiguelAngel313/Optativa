# 1. Pide una cadena por teclado y muéstrala en mayúsculas.
cadena = input("Introduce una cadena :")
print(cadena.upper())
# 2. Pide una cadena por teclado y muéstrala en minúsculas.
print(cadena.lower())
# 3. Pide una cadena por teclado y muéstrala convirtiendo la inicial de cada palabra en
# mayúscula. Sugerencia: mira qué hace la función title()
print(cadena.title())
# 4. Pide una cadena por teclado y muestra el número de caracteres que tiene de la
# forma: “La cadena que has introducido tiene __ caracteres.”.
print("La cadena que has introducido tiene {} caracteres.".format(len(cadena)))
# 5. Pide una cadena por teclado y muestra los caracteres que están en las posiciones
# impares.
print(cadena[1::2])
# 6. Pide una cadena por teclado y muestra los caracteres que están en las posiciones
# pares.
print(cadena[0::2])
# 7. Pide dos cadenas por teclado y muestra True si la primera cadena es mayor que la
# segunda.
print("Cadena mayor que: ")
cadena1 = input("Introduce una cadena: ")
cadena2 = input("Introduce una cadena: ")
print(cadena1 > cadena2)
# 8. Pide dos cadenas por teclado y muestra True si ambas cadenas son iguales y
# false en caso contrario. Considerar mayúsculas y minúsculas.
print("Cadena igual que: ")
print(cadena1 == cadena2)
# 9. Pide dos cadenas por teclado y muestra True si ambas cadenas son iguales y
# false en caso contrario. No considerar mayúsculas y minúsculas.
print("cadena igual que sin considerar mayusculas ni minusculas: ")
resultado = cadena1.lower() == cadena2.lower()
print("Resultado: ", resultado)
# 10. Pide por teclado dos cadenas y muestra 0 si la primera está contenida en la
# segunda y -1 en caso contrario.
print("Cadena contenida en otra: ")
if(cadena1 in cadena2):
    print("0")
else:
    print("-1")
# 11. Diseña un ejercicio para el uso de strip.
# 11.1 Elimina el caracter inicial de una cadena pedida por teclado
print("Eliminacion de un caracter son strip(): ")
print(cadena.strip())
# 12. Diseña un ejercicio para el uso de replace.
# 12.1 Remplaza en la cadena "manolo" los caracteres que creas necesarios para formar otra palabra
cadena3 = "manolo"
print("Cadena inicial: ", cadena3)
print("Cadena remplazada: ", cadena.replace("man", "cho"))
# 13. Diseña un ejercicio para el uso de split.
# 13.1 Divide la cadena Juan/Alberto/Miguel con split.
cadena4 = "Juan/Alberto/Miguel"
print("Cadena inicial: ", cadena4)
print("Cadena separada: ", cadena4.split("/"))
# 14. Pide por teclado una cadena y muestra True si todos sus caracteres son letras.
cadena5 = input("Introduce una cadena que solo sean letras o no: ")
print("Es solo letras: ",cadena5.isalpha())
# ¿Cómo se considera el espacio en blanco?
#Lo toma como un caracter especial
# 15. Pide por teclado una cadena y muestra True si todo su contenido son números
cadena6 = input("Introduce una cadena que solo sean numeros o no: ")
print("Es solo numeros: ",cadena6.isdigit())
