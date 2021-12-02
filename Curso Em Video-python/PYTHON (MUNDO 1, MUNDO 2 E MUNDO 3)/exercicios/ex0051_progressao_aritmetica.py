""" Desenvolva um programa que leia o primeiro termo e a razão de uma PA. no final, mostre os 10
primeiros termos dessa progressão."""
print('Criando uma P.A progressão aritmética')
termo1 = int(input('Digite o primeiro valor da P.A: '))
razao = int(input('Digite o valor da sua razão: '))
for c in range(0, 10, 1):
    termo1 += razao
    print(termo1 - razao, end=' ')  # resolvi diminui uma vez a razão para poder começar minha PA no número digitado
print()

'''Outra forma de fazer tambem '''

primeiro = int(input('Digite o primeiro termo:'))
razon = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * razon
for c in range(primeiro, decimo + razon, razon):
    print(c, end=' ')
