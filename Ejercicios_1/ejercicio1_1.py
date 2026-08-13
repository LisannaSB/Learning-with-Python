# Ej 1 Multiplicar dos numeros sin usar el simbolo de multiplicacion
factor1 = input('Ingresa el primer factor: ')
try:
    factor1 = int(factor1)
except:
        print('No es una entrada valida para un numero')

factor2 = input('Ingresa el segundo factor: ')
try:
    factor2 = int(factor2)
except:
        print('No es una entrada valida para un numero')

producto = 0
for i in range(factor1):
    producto += factor2


print('El producto final es de: ', producto)
