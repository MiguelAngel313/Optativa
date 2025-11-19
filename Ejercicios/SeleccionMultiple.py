# 1. Sobre la imagen anterior cambia el menú por el siguiente:
#   1.- entrada completa
#   2.- entrada simplificada
#   3.- salir
print("1.-Entrada completa.")
print("2.-Entrada simplificada.")
print("3. -Salir.")

opcion = int(input("Elige una opcion: "))
match opcion:
    case 1:
        print("Has elegido entrada comlpeta.")
    case 2:
        print("Has elegido entrada simplificada.")
    case 3:
        print("Has elegido salir.")
    case _:
        print("Opcion incorrecta.")

# 2. Analiza qué hace este programa:

# si la longitud de la cadena introducida no es igual a 1 muestra un mensaje
# En caso de que la cadena introducida no sea una letra mostrara un mensaje indicandolo
# Si ninuna de estas dos condiciones se cumple se utilizara un match que recibe la letra en minuscula
# para saber si la letra es consonante o vocal y mostrar su respectivo mensaje.

# 3. Pide un número por teclado. Si está entre 1 y 7 muestra el día de la semana al que
# corresponde.
numero = int(input("Introduce un numero entre 1 y 7: "))

if numero >= 1 & numero <= 7:
    match numero:
        case 1:
            print("Lunes")
        case 2:
            print("Martes")
        case 3:
            print("Miercoles")
        case 4:
            print("Jueves")
        case 5:
            print("Viernes")
        case 6:
            print("Sabado")
        case 7:
            print("Domingo")
else:
    print("El valor introducido no es valido.")


# 4. Pide una nota (0 a 10) y muestra la calificación:
#   0–4: Suspenso
#   5–6: Aprobado
#   7–8: Notable
#   9–10: Sobresaliente

nota = int(input("Introduce una nota: "))

match nota:
    case 0 | 1 | 2 | 3 | 4:
        print("Suspenso.")
    case 5 | 6:
        print("Aprobado.")
    case 7 | 8:
        print("Notable.")
    case 9 | 10:
        print("Sobresaliente.")
    case _:
        print("No es una nota valida.")

op1 = int(input("Introduce un operador: "))
op2 = int(input("Introduce otro operador: "))


print("+ para sumar")
print("- para restar")
print("* para multiplicar")
print("/ para dividir")

op3 = input("Selecciona una opcion: ")

match op3:
    case "+":
        print("Resultado: ",op1+op2)
    case "-":
        print("Resultado: ",op1-op2)
    case "*":
        print("Resultado: ",op1*op2)
    case "/":
        print("Resultado: ",op1/op2)
    case _:
        print("Opcion no valida.")
