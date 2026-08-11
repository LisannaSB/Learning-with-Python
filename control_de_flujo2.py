# Vamos a tratar a los while
i = 0
while i < 5:
    # print("El valor de i es:", i)
    if i == 3:
        # print("i es igual a 3, saliendo del bucle")
        i = 0
        break
    i += 1

while i < 5:
    i += 1
    if i == 3:
        continue
    # print("El valor de i es:", i)

# For loops
usuarios = ['Chanchito feliz', 'felipe', 'roberto', 'nicolas']

# for usuario in usuarios:
#     print(usuario)

# for usuario in usuarios:
#     if usuario == 'roberto':
#         break
#     print(usuario)

# for usuario in usuarios:
#     if usuario == 'roberto':
#         continue
#     print(usuario)

# usuario = 'Chanchito feliz'
# for c in usuario:
#     print(c)

# for x in range(3,30,3):
#     print(x)
# else:
#     print("El bucle ha terminado")

edades = [24, 25, 26, 35]

# for usuario in usuarios:
#     for edad in edades:
#         print(f"El usuario {usuario} tiene {edad} años")

# Funciones

def miFuncion():
    print('Mi primera función')

miFuncion()