# Ej 8 Escribir una aplicacion que reciba una cantidad infinita de numeros hasta decir basta, luego que devuelva la suma de los numeros ingresados

basta = False
while not basta:
    numerito = input('Introduce un numero: ')
    if numerito in ('basta'):
        basta = True 