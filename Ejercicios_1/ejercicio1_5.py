# Ej 5 Escribir una funcion que indique si el usuario es mayor de edad

def mayorEdad(ed):
    if ed >= 18:
        print('Usted es mayor de edad')
    else:
        print('No entra a la discoteca')

edad = input('Introduce tu edad: ')
try:
    edad = int(edad)
    mayorEdad(edad)
except:
    print('Valor no valido para edad')