primero = input('Ingrese el primer número: ')
segundo = input('Ingrese el segundo número: ')

# print(primero + segundo) # Concatenación de cadenas
# print(int(primero) + int(segundo)) # Suma de números

try:
    primero = int(primero) 
except: # Si no lo logramos
    primero = 'chanchito feliz'

try:
    segundo = int(segundo)
except: # Si no lo logramos
    segundo = 'chanchito feliz'

if primero == 'chanchito feliz' or segundo == 'chanchito feliz':
    print('Ingresaste mal los datos, prueba de nuevo solo con números')
else:
    print(primero + segundo)