# 1. Pide una cadena por teclado y muestra su longitud.
cadena = "mecagoentodo"
print(len(cadena))

# 2. Pide una cadena por teclado y concaténala con si misma mostrando el resultado.
cadena2=input("Introduce una cadena: ")
cadena2=cadena2+cadena2
print(cadena2)
# 3. Pide una cadena por teclado y determina si tiene la subcadena hoy
print(cadena2.find("hoy"))
# 4. Pide una cadena por teclado y reemplaza todas las apariciones de la letra z por c
print(cadena2.replace("z","c"))
# 5. Pide una cadena por teclado y determina cuántas vocales tiene.
vocales=0
vocales+=cadena2.count("a")
vocales+=cadena2.count("e")
vocales+=cadena2.count("i")
vocales+=cadena2.count("o")
vocales+=cadena2.count("u")

print("Numero de vocales: ", vocales)
# 6. Pide una cadena por teclado y determina cuántas veces aparece la a y cuántas veces
# aparece la i
a=0
i=0
a+=cadena2.count("a")
i+=cadena2.count("i")
print("La letra a aparece {} y la letra i aparece {} veces." .format(a,i))
# 7. Pide una cadena por teclado y muéstrala con todas las letras en mayúsculas.
print("Mayusculas: ",cadena2.upper())
# 8. Pide una cadena por teclado y muéstrala con todas las letras en minúsculas.
print("Mayusculas: ",cadena2.lower())
# 9. Pide una cadena por teclado y muéstrala en rojo y negrita.
# 10. En la cadena “Seremos capaces de ir muy lejos” muestra la posición y la última de la letra s
# 11. Pide una cadena por teclado y muéstrala al revés




