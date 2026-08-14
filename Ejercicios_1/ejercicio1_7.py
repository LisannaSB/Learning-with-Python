# Ej 7 Escribir una funcion que indique cuantas vocales tiene una palabra

def vocales(voc):
    count = 0
    for i in voc:
        if i in ('a','e','i','o','u', 'A', 'E', 'I', 'O', 'U'):
            count += 1
    print('Hay un total de ', count, ' vocales')

vocal = input('Introduce una palabra para decirte la cantidad de vocales: ')
vocales(vocal)