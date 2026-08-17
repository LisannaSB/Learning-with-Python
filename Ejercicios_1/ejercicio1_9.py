# Ej 9 Escribir una funcion que reciba nombre y apellido y los vaya agregando a un archivo

def basedeDatos(nombre, apellido):
    nombreCompleto = nombre + ' ' + apellido
    c = open('ejercicio9.txt', 'a')
    c.write('\n')
    c.write(nombreCompleto)
    c.close()

    c = open('ejercicio9.txt')
    print(c.read())
    c.close()

nom = input('Dame el nombre: ')
ape = input('Dame el apellido: ')

basedeDatos(nom, ape)