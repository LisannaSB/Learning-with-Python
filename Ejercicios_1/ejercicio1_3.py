# Ej 3 Escribir una funcion que encuentre el elemento menor de una lista

def elementoMenor(el):
    elMenor = min(el)
    print('El elemento menor de la lista es :', elMenor)

elemento = list(input('Enlistame los elementos de tu lista: '))
largo = len(elemento)

nuevoElemento = []
concatenado = False
# print(elemento)
for i in range(largo):
    if elemento[i] in (' ', ','):
        # print('Hay un espacio o coma, eliminarla')
        continue
    elif i+1 < len(elemento) and elemento[i+1] not in (' ', ','):
        # print('El siguiente str es un numero, unirlos')
        concatenar = elemento[i] + elemento[i+1]  
        nuevoElemento.append(int(concatenar))
        concatenado = True
    else:
        if concatenado:
            concatenado = False
            continue
        else:
            nuevoElemento.append(int(elemento[i]))
# print(nuevoElemento)

elementoMenor(nuevoElemento)

# falta ver si el valor es neg o positivo o tiene más de dos digitos, usar un while