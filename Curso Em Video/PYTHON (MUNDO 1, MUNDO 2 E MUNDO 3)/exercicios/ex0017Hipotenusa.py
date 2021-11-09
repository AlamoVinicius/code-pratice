from math import hypot
ctooposto = float(input('Digite o cateto oposto: '))
ctoadjacente = float(input('Digite o cateto adjacente: '))
print(f'hipotenusa igual a: {hypot(ctooposto, ctoadjacente):.2f}')

'''Outra forma de realizar  a conta sem import de "hypot"'''
c1 = float(input('Digite o valor do cateto oposto: '))
c2 = float(input('Digite o valor do cateto adjacente: '))
h = (c1 ** 2 + c2 ** 2) ** (1/2)
print(f'Hipotenusa igual a: {h:.2f}')