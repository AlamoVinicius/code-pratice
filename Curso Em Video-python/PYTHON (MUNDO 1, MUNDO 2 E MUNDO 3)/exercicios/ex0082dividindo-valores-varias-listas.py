""" Crie um programa que vai ler vários números e colcoar em uma lista. Depois disso, crie duas listas
extras que vão conter apenas os valores pares e os valores impares digitados respectivamente
Ao final. mostre o conteúdo das três listas geradas."""
lista = []
lista_par = []
lista_impar = []
while True:
    n = int(input('Digite um número para adicionar na lista: '))
    lista.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    elif n % 2 == 1:
        lista_impar.append(n)
    perg = str(input('Deseja adicionar outro valor? [S/N] ')).upper().strip()[0]
    if perg in 'Nn':
        break
print(f'Lista com todos números: \033[91m{lista}\033[m')
print(f'lista de números pares: \033[96m{lista_par}\033[m')
print(f'Lista com números ímpares: \033[92m{lista_impar}[m')

''' obs no curso em video o professor só contou os números pares no final usando um for com indice e dados, para
comparar os números ímpares e pares e adicionar em suas respectivas listas'''
