""" faça um programa que leia um número inteiro e diga se ele é ou não um número primo """
n = int(input("Verificar numero primo: "))
mult = 0
for count in range(2, n):
    if n % count == 0:
        print(f"Múltiplo de {count}")
        mult += 1
if mult == 0:
    print("É primo")
else:
    print(f'Tem"{mult}" múltiplos acima de 2  abaixo de"{n} portanto não é primo')

''' another méthod: '''


numero = int(input("Digite o número para verifiação: "))
tot = 0
for c in range(1, numero +1):
    if n % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print(f'\n\033[mO número {numero} foi dividido {tot} vezes')
if tot == 2:
    print('portando ele é primo')
else:
    print('portanto ele não é primo')

