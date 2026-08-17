if 2 < 5:
    print('2 es menor que 5') 

# La diferencia entre '' y "" es que '' es un string de un solo caracter, mientras que
#  "" es un string de varios caracteres.

# a == b: a es igual a b
if 2 == 5:
    print('2 es igual a 5')
# a != b: a es diferente a b
if 2 != 5:
    print('2 es diferente a 5')
# a > b: a es mayor que b
if 2 > 5:
    print('2 es mayor que 5')
# a < b: a es menor que b
if 2 < 5:
    print('2 es menor que 5')
# a >= b: a es mayor o igual que b
if 2 >= 5:
    print('2 es mayor o igual que 5')
# a <= b: a es menor o igual que b
if 2 <= 5:
    print('2 es menor o igual que 5')
# a and b: a y b son verdaderos
if 2 < 5 and 3 < 5:
    print('2 es menor que 5 y 3 es menor que 5')
# a or b: a o b son verdaderos
if 2 < 5 or 3 > 5:
    print('2 es menor que 5 o 3 es mayor que 5')
# not a: a es falso
if not 2 > 5:
    print('2 no es mayor que 5')
# a in b: a está en b
if 2 in [1, 2, 3]:
    print('2 está en la lista [1, 2, 3]')
# a not in b: a no está en b
if 2 not in [1, 2, 3]:
    print('2 no está en la lista [1, 2, 3]')

if 2 > 5:
    print('lala')
elif 2 < 5:
    print('2 es menor que 5 en elif')

if 2 < 5:
    print('2 es menor a que 5 en if')
elif 2 < 5:
    print('2 es menor que 5 en elif')

if 2 > 5:
    print('lala')
elif 3 > 5:
    print('3 es menor que 5 en elif')
else:
    print('Todas las condiciones anteriores son falsas, por lo que se ejecuta el else')


# If cortos y ternarios
if 2 < 5: print('Esta es una sentencia if corta')

print('cuando devuelve True') if 5 > 2 else print('cuando devuelve False')
print('cuando devuelve True') if 5 < 2 else print('cuando devuelve False')

