# Gestion de archivos

# 'r' es default, siempre lee, read
# 'a' nos deja agregar mas texto
# 'w' para editar el archivo, en caso que no existe, el lo crea
# 'x' para crear archivos en python, si ya esta creado manda un error

# c = open('chanchito.txt')

# Read

# print(c.read()) # nos devuelve todo el archivo

# print(c.readline())
# print(c.readline())
# print(c.readline()) # va a ir bajando linea por linea conforme se dice la funcion

# for x in c: # va a ir linea por linea pero todas las lineas
#     print(x) 

# Append
# c = open('chanchito.txt', 'a')
# c.write('agregaremos una nueva linea a nuestro archivo')
# c.write('\nagregaremos una nueva linea a nuestro archivo') # para anadir en una nueva linea
# c.close() # siempre cerrar el archivo al terminar de usarlo

# c = open('chanchito.txt')
# print(c.read())
# c.close()

# Write (editar)
# c = open('chanchito.txt', 'w')
# c.write('\nagregaremos una nueva linea a nuestro archivo') # elimina todo lo existente y agrega solo este texto
# c.close()

# c = open('chanchito.txt')
# print(c.read())
# c.close()

# Para eliminar archivos
# import os

# if os.path.exists('chanchito.txt'):
#     os.remove('chanchito.txt')
# else:
#     print('El archivo no existe')

# os.rmdir('micarpeta')

# Crear archivos
# c = open('chanchito.txt', 'x')
# c.close()

# c = open('chanchito.txt')
# print(c.read())
# c.close()

