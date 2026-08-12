class Animal: # Clase padre
    def __init__(self, nombre, onomatopeya):
            self.nombre = nombre
            self.onomatopeya = onomatopeya

    def saludo(self):
            print('Hola, soy un', self.tipo ,'y mi sonido es el', self.onomatopeya)

class Gato(Animal):
    tipo = 'gato'
    def __init__(self, nombre, onomatopeya): # Ignoramos al init del padre si tenemos esto asi
         Animal.__init__(self, nombre, onomatopeya)
         print('Hola, soy un gato extendido')
    
class Perro(Animal):
    tipo = 'perro'
    def __init__(self, nombre, onomatopeya):
         super().__init__(nombre, onomatopeya) # Hace referencia siempre a la clase padre, no es necesario poner self
         print('Instanciando un perro')

class Canario(Animal):
    tipo = 'canario'

gato = Gato('Fluffy', 'maullido')
gato.saludo()

perro = Perro('Firulais', 'ladrido')
perro.saludo()

canario = Canario('Piolin', 'silbido')
canario.saludo()