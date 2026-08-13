# Ej 2 Ingresar nombre y apellido e imprimirlo al reves
nombre = input('Indicame tu nombre: ')
apellido = input('Indicame tu apellido: ')

nombreCompleto = nombre + ' ' + apellido

nombreAlReves = nombreCompleto[::-1]

print('Tu nombre al reves es: ', nombreAlReves)