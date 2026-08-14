# Ej 3 Escribir una funcion que encuentre el elemento menor de una lista

def elementoMenor(el):
    elMenor = min(el)
    print('El elemento menor de la lista es :', elMenor)

elemento = input('Enlistame los elementos de tu lista: ')
strings = elemento.replace(',', ' ').split()
nuevoElemento = [float(p) for p in strings]
print(nuevoElemento)
elementoMenor(nuevoElemento)
