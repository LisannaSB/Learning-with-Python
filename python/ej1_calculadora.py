primero = input('Ingrese el primer número: ')
try:
    primero = int(primero) 
except: # Si no lo logramos
    primero = 'chanchito feliz'

if primero == 'chanchito feliz':
    print('Ingresaste mal los datos, prueba de nuevo solo con números')
    exit()

segundo = input('Ingrese el segundo número: ')
try:
    segundo = int(segundo)
except: # Si no lo logramos
    segundo = 'chanchito feliz'

if segundo == 'chanchito feliz':
    print('Ingresaste mal los datos, prueba de nuevo solo con números')
    exit()

simbolo = input('Ingrese operacion (+, -, *, /): ')

if simbolo == '+':
    print('Suma: ', primero + segundo)
elif simbolo == '-':
    print('Resta: ', primero - segundo)
elif simbolo == '*':
    print('Multiplicación: ', primero * segundo)
elif simbolo == '/':
    print('División: ', primero / segundo)
else:
    print('Operación no válida')