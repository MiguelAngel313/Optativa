# Miguel Angel Herrojo Gonzalez
# Actividad 2.2
productos = {
'teclado': ('periférico', 25),
'ratón': ('periférico', 15),
'monitor': ('pantalla', 120)
}

# Inserta un elemento nuevo con la siguiente información (la inserción se debe hacer usando instrucciones
# Python):
#  Nombre: pendrive
#  Tipo: periférico
#  Precio: 33.95

productos['pendrive'] = ('periférico', 33.95)

print("Diccionario de productos actualizado: ",productos)

# Crear una función llamada filtrar_por_precio que:
#  Reciba el diccionario.
#  Establezca un valor límite con un valor por defecto de 30.
# Esta función devuelve una lista con los nombres de los productos cuyo precio es inferior al límite.


def filtrar_por_precio(diccionario):
    limite = 30
    productos_filtrados = [productos for productos, (tipo, precio) in diccionario.items() if precio < limite]
    return productos_filtrados

print("Productos con precio inferior a 30: ", filtrar_por_precio(productos))