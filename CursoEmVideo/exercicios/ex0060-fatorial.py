""" Faça um programa que leia um número qualquer e mostre o seu fatorial. ez 5! = 5x4x3x2x1 = 120"""
n = int(input('Digite um número para exibir seu fatorial: '))
fatorial = n
soma = 1  # quando se trata de multiplicação temos que começar com 1 para a multiplicação funcionar.
print(f'Calculando o fatorial de {n}')
print(f'{n}! = ', end='')
while fatorial > 0:
    print(f'{fatorial}', end=' ')
    print('x' if fatorial > 1 else '=', end=' ')
    soma *= fatorial
    fatorial -= 1
print(soma)
print('''
calculando de outro modo: 
''')

''' another way with library'''
from math import factorial  # esse import deveria ser no início mas como é so para o meu estudo ok

n2 = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n2)
print(f'O fatorial de {n2} é {f}')
print('''
calculando outro jeito usando o for in range
''')

'''another way with for '''
soma2 = 1
for c in range(n2, 0, -1):
    soma2 *= c
    print(f'{c}', end=' ')
    print('x' if c > 1 else '=', end=' ')
print(soma2)
