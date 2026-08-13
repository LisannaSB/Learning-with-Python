lista = [] # Definicion de una lista vacia
print(lista) # Impresion de la lista vacia

lista = [1, 2, 3] # Definicion de una lista con elementos
lista2 = lista.copy() # Copia de la lista
lista.append(4) # Agregar un elemento al final de la lista
# lista.clear() # Eliminar todos los elementos de la lista

print(lista) # Impresion de la lista con elementos
print(lista2) # Impresion de la lista copiada
print(lista, lista2.count(5), lista2.count(3)) # Conteo de un elemento en la lista
print(len(lista))

largoLista = len(lista)
largoLista2 = len(lista2)
print(largoLista, largoLista2)

# Acceder a los elementos de la lista por su indice
lista = ['Hola', 'mundo', 'Chanchito feliz'] 
print(lista[0], lista[1], lista[2])

lista.pop() # Elimina el ultimo elemento de la lista
print(lista)

lista.remove('Hola') # Elimina el primer elemento que coincida con el valor especificado
print(lista)

lista = ['Hola', 'mundo', 'Chanchito feliz']
lista.reverse() # Invierte el orden de los elementos de la lista
print(lista)

lista = ['Hola', 'mundo', 'Chanchito feliz']
lista2 = lista.copy()
lista.append(4)
lista.reverse() # Invierte el orden de los elementos de la lista
# lista.sort() # No funcionara porque la lista contiene elementos de diferentes tipos (str y int)
lista.reverse()
lista.pop()
# lista.remove()
lista.append('Chanchito triste')
lista.sort() # Si funciona porque la lista contiene elementos del mismo tipo (str)
print(lista)