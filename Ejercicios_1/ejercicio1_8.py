# Ej 8 Escribir una aplicacion que reciba una cantidad infinita de numeros hasta decir basta, luego que devuelva la suma de los numeros ingresados

result = 0
numeros = []
basta = False
while not basta:
    numerito = input('Introduce un numero: ')
    if numerito not in ('basta'):
        numeros.append(float(numerito))
    else:
        basta = True 
        for n in numeros:
            result += n
        print('La suma es de: ', result)