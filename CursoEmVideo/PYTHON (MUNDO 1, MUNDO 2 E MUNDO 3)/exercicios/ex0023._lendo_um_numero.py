""" faça um programa que leia um numeo de 0 a 9999 e mostre na tela cada um dos seus digitos separados"""

numero = int(input('Digite um numero entre 0 e 9999 para exibir seus valores: '))
u = numero // 1 % 10   # nesse caso eu estou dividino inteiro e pego o resto da divisão
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f'unidade.......: {u}')
print(f'dezena........: {d}')
print(f'Centena.......: {c}')
print(f'Milhar........: {m}')