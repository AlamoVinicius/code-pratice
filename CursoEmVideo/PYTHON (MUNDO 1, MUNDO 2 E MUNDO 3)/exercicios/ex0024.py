""" crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o
nome SANTO"""

cidade = input('Digite uma cidade: ').upper()
separacao_nome = cidade.split(' ')
if separacao_nome[0] == 'SANTO':
    print(f'A cidade começa com o nome SANTO!')
else:
    print('A cidade não começa com o nome SANTO!')