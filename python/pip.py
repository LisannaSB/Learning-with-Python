# pypi.org de versiones de paquetes de python
# pip install para instalar esos paquetes de python
# camelcase, pip3 install camelcase

from camelcase import CamelCase

c = CamelCase()
s = 'esta oracion necesita CamelCase'

camelcased = c.hump(s)
print(camelcased)

# pip3 list, muestra todos los paquetes instalados
# pip3 unistall modulo, para eliminar el modulo instalado ej pip3 unistall camelcase