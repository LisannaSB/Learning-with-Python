# Ej 6 Escribir una funcion que indique si un numero es par o impar

def esPar(num):
    if num % 2 == 0:
        print('Es par')
    else:
        print('Es impar')

numero = input('Introduce un numero para saber si es par o impar: ')
try:
    numero = int(numero)
    esPar(numero)
except:
    print('Valor no valido para edad')