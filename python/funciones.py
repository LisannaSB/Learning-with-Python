def miFuncion():
    print('Mi primera función')

def imprimeDato(nombre, apellido):
    print('El nombre completo es:', nombre, apellido)

def imprimeDato2(*nombre):
    print('El nombre completo es:', nombre[0])

def nombreCompleto(apellido, nombre):
    print('El nombre completo es:', nombre, apellido)

def nombreCompleto2(**kwargs): # Argumentos por llave
    print('El nombre completo es:', kwargs['nombre'], kwargs['apellido'])

def miFuncion2(argumento = 'Chanchito'):
    print(argumento)

def miFuncionLista(lista):
    for elemento in lista:
        print(elemento)

def concatenaNombres(lista):
    i = ''
    for elemento in lista:
        i = i + elemento + ' '
    return i
        
# miFuncion()

# imprimeDato('Chanchito', 'Feliz')
# imprimeDato2('Chanchito', 'Feliz', 'lala', 'lele')

# nombreCompleto(nombre='Chanchito', apellido='Feliz')
# nombreCompleto2(nombre='Chanchito', apellido='Feliz')

# miFuncion2()
# miFuncion2('Batman')
# miFuncionLista(['Chanchito', 'Feliz', 'Batman'])

# nombres = concatenaNombres(['Chanchito', 'Feliz'])
# print(nombres)

# Recursividad

def recursion(i):
    if i < 1:
        return i
    print(i)
    recursion(i-1)

recursion(6)