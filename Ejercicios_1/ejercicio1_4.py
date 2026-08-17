# Ej 4 Escribir una funcion que devuelva el volumen de una esfera por su radio (4/3 * pi * r **3)
import math

def volumenEsfera(r):
    volumen = 4/3 * math.pi * r ** 3
    print('El volumen de la esfera es: ', volumen)

radio = input('Introduce el radio de la esfera: ')
try:
    radio = float(radio)
    volumenEsfera(radio)
except:
    print('Valor no valido para un radio')

