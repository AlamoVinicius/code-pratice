""" Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
 valor 999, uqe é a condição de parada. No final, mostre quantos números foram figitados e qual foi a soma entre eles
 desconsiderando o flag"""
contador = 0
soma = 0
while True:
    n = int(input('Digite um número (999 para finalizar)'))
    if n == 999:
        break
    contador += 1
    soma += n
print(f'foram inseridos {contador} números e a soma total deles foi de: {soma}')

''' resultado do meu código foi perfeito com a do professor sem necessidades de alter'''
