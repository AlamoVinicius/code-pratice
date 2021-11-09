""" Crie um programa que leia o ano de nascimento de sete pessoas. no final, mostre quantas pessoas ainda não
atingiram a maioridade e quantas já são maiores."""
from datetime import date
datahj = date.today().year
maior = 0
menor = 0
for count in range(1, 8):
    data = int(input(f'Digite o {count} ano de nascimento: '))
    conta = datahj - data
    if conta < 21:
        print('Essa pessoa é menor')
        menor += 1
    else:
        print('Essa pessoa é maior')
        maior += 1
print(f'{menor} pessoas ainda não atingiram a maioridade')
print(f'{maior} pessoas já atingiram a maioridade')