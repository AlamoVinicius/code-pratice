#import math ( eu importo todas as funões da biblioteca math e teria que usar math.(nome da funçao) e (variante)
from math import sqrt, floor, ceil
numero = int(input('Digite um numero: '))
raiz = sqrt(numero)
# exemplo de print utilizando o import math(matematica) sqrt(raiz quadrada) com uma quebra de linha, duas casas
# flutuantes e 20 espaços com =:
print(f'A raiz de {numero} é:\n {raiz:=^20.2f}.')
# exemplo de print com arrendodamento para cima :
print(f'A raiz de {numero} é: {ceil(raiz)}')
# exemplo de print com arrendodamento para baixo:
print(f'A raiz de {numero} é: {floor(raiz)}')
print('=========Gerando numeros aleatórios==========')

import random
num0a1 = random.random()
# gera um numero aleátorio entre 0 e 1
print(num0a1)

num1a10 = random.randint(1, 10)
# Gera um número aleátorio de 1 a 10
print(num1a10)

import emojis
print(emojis.encode('hello world :earth_americas:'))
