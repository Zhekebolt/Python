#Generador de contraseñas en python

import random

print('Generador de contraseñas en español')

chars = 'abcdefghijkmnlopqrstuvwxyzñABCDEFGHIJLMNLROPQRSTUVWXYZ!"#$%&/()=?¡0123456789'

number = input ('Cantidad de contraseñas a generar:    ')
number = int(number)

longitud = input ('Cantidad de contraseñas a generar:    ')
longitud = int(longitud)

print ('\nAqui estan tus contraseñas: ')

for pwd in range(number):
    passwords = ''
    for c in range(longitud):
        passwords += random.choice(chars)
    print(passwords)