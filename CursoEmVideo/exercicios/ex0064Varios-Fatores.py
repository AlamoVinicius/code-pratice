""" Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
valor 999. que é a condiçao de parada. no final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag 999)"""

contador = 0   # contador da quantidade de números inserido
soma = 0
print('---Bem vindo ao somatório de números---')
n = int(input('Digite um número ou 999 para encerrar: '))
while n != 999:
    contador += 1
    soma += n
    n = int(input('Digite outro número ou 999 para encerrar: '))
print(f'Você digitou {contador} números e a soma deles foi de {soma}')

''' monha solução ficou igual a do curso então não tem necessidade de mudar nada. nice!!!'''
