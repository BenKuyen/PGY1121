lista=["Hola",2,9,3,15]
# ¿Cómo mostrar la lista?
print("Esta es nuestra lista inicial:")
print(lista)
'''O también puede funcionar "for n in lista: print(n)". Esto mostrará la lista de forma vertical.'''

# Mostrar un elemento específico de una lista
print("\nEn esta lista, se mostrará el segundo elemento.\n¿Por qué en el código se coloca '[1]'?\nPorque las listas parten desde cero.")
print("Así que al pedir el elemento '1', estaremos pidiendo el segundo elemento.\nEn este caso, el segundo elemento es:")
print(lista[1])

# Agregar elementos a la lista
lista.append("Buenas tardes")
print("\nEn esta lista, hemos agregado un elemento más, el elemento 'Buenas tardes':")
print(lista)

# Agregar una lista a otra lista
print("\nUsando el comando '.extend', agregaremos elementos de otra lista a nuestra lista principal.\nComo en el siguiente ejemplo:")
lista.extend(["Hola de nuevo","Soy un mensaje agregado de otra lista a esta, ¡genial!"])
print(lista)

# Eliminar un elementos de la lista (.pop o .remove)


print("\n----------------------------------------------------")
print("Sección de práctica, por favor ignore este apartado.\n")

#Sublistas
lista2=[5,6,7,8,9,10,["a","b","c"]]
print(lista2[6][0])