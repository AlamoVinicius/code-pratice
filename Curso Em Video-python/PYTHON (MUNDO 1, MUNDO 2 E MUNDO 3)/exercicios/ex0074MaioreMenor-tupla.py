""" Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois diss, mostre a listagem
 de números gerados e também indique o menor e o maior valor que estão na tupla."""
from random import randint
# gerar a tupla com os 5 números aleatórios
tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(tupla)   # exibir os números
# indicar o maior e menor número da tupla
print(f'O maior número da sequência foi: {max(tupla)}\nE o menor número da sequência foi: {min(tupla)}')
print()
print('Outro jeito usando o for:')
max_value = None  # another way
min_value = None
for num in tupla:
    if max_value is None or num > max_value:
        max_value = num
    if min_value is None or num < min_value:
        min_value = num
print(f'maior número: {max_value}\nmenor número: {min_value}')