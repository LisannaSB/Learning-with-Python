# Objetos, clases y herencias

# Una clase es como un plano de una casa, la casa representa los objetos
# los objetos son instancias de estas clases

# class Usuario: # siempre la primera letra mayuscula
#     nombre = "Felipe" # instancias siempre minuscula
#     apellido = "Feliz"

# usuario = Usuario() # Mi objeto
# usuario2 = Usuario()

# print(usuario.nombre, usuario.apellido)
# print(usuario2.nombre, usuario2.apellido)

# class Usuario:
#     def __init__(self, nombre, apellido): # self seria como usuario.nombre y usuario.apellido
#         self.nombre = nombre
#         self.apellido = apellido

# usuario = Usuario('Felipe', 'Feliz') # objeto usuario
# usuario2 = Usuario('Chanchito', 'Feliz') # objeto usuario2

# print(usuario.nombre, usuario.apellido, usuario2.nombre, usuario2.apellido)

# class Usuario:
#     def __init__(self, nombre, apellido): # self seria como usuario.nombre y usuario.apellido
#         self.nombre = nombre
#         self.apellido = apellido

#     def saludo(self):
#         print('Hola, mi nombre es ', self.nombre, self.apellido)

    # def saludo2(lala): # es aceptado, pero muy trabajoso para implementar en grupo e identificar las
    #     # instancias de la clase
    #     print('Hola, mi nombre es ', lala.nombre, lala.apellido)

# usuario = Usuario('Felipe', 'Feliz') # objeto usuario
# usuario2 = Usuario('Chanchito', 'Feliz') # objeto usuario2

# usuario.saludo()
# usuario2.saludo()

# usuario.saludo2()
# usuario2.saludo2()

# usuario.nombre = 'Chanchito'
# usuario.saludo()
# del usuario.nombre
# usuario.saludo()
# del usuario
# print(usuario) # usuario no se encuentra definido

# Herencia 

class Usuario:
    def __init__(self, nombre, apellido): # self seria como usuario.nombre y usuario.apellido
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print('Hola, mi nombre es ', self.nombre, self.apellido)

class Admin(Usuario): # Clase herencia, tiene todas las instancias y metodos de Usuario
    def superSaludo(self):
        print('Hola!, me llamo,', self.nombre, 'y soy administrador')

usuario = Usuario('Felipe', 'Feliz')
admin = Admin('Super', 'Feliz')

admin.saludo()
admin.superSaludo()

# usuario.superSaludo() # no se va a poder