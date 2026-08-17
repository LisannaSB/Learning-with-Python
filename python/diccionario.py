diccionario = {
    "nombre": "Chanchito feliz",
    "raza": "Persa",
    "edad": 5
}

# print(diccionario) # Impresion del diccionario
# print(diccionario['nombre']) # Impresion del valor de la clave "nombre"
# print(diccionario.get('nombre')) # Impresion del valor de la clave "nombre" usando el metodo get()

diccionario['nombre'] = 'Fluffy' # Modificacion del valor de la clave "nombre"
# print(diccionario) # Impresion del diccionario modificado

# print(len(diccionario)) # Impresion del largo del diccionario

diccionario['ronronea'] = 'Si' # Agregar una nueva clave-valor al diccionario
# print(diccionario) # Impresion del diccionario con la nueva clave-valor

copiaGatito = diccionario.copy() # Copia del diccionario
copiaGatito = dict(diccionario) # Otra forma de copiar el diccionario

# diccionario.pop('ronronea') # Eliminar la clave-valor "ronronea" del diccionario
# print(diccionario) # Impresion del diccionario después de eliminar la clave-valor

# diccionario.popitem() # Eliminar el ultimo elemento del diccionario
# print(diccionario) # Impresion del diccionario después de eliminar el ultimo elemento

del diccionario['ronronea'] # Eliminar la clave-valor "ronronea" del diccionario
# print(diccionario) # Impresion del diccionario después de eliminar la clave-valor

# print(copiaGatito) # Impresion de la copia del diccionario

diccionario.clear() # Eliminar todos los elementos del diccionario
# print(diccionario) # Impresion del diccionario después de eliminar todos los elementos

# Diccionarios anidados
fluffly = {
        "nombre": "Fluffly",
        "edad": 4,
    }

gatitos = {
    "Fluffly": fluffly,

    "Mamba": {
        "nombre": "Black Mamba",
        "edad": 12,
    }
}
print(gatitos) # Impresion del diccionario anidado

# Otra forma de generar diccionarios
perritos = dict(nombre="Chanchito Feliz", edad=6)
print(perritos) # Impresion del diccionario generado con la funcion dict()