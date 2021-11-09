""" Faça um programa que leia 5 valores numéricos e guarde os em uma lista. no final , mostre qual foi o
maior e o menor valor digitado e as suas respectivas posições na lista."""
lista = []    # definição da minha lista
maior = 0     # entrada das váriaveis para receber os maiores e menores valor
menor = 0
for c in range(0, 5):     # primeiro for para digitar os 5 primeiros númeors
    lista.append(int(input(f'Digite o {c+1}º valor: ')))    # entrada dos números via input
    if c == 0:              # lógica de programação para definir maior e menor número
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print('=' * 30)    # exibição final
print(f'você digitou a lista {lista}')
print(f'O maior número digitado foi {maior} nas posições ', end='')   # exibição do número maior
for i, v in enumerate(lista):     # lógica para buscar o índice do maior número
    if v == maior:
        print(f'{i+1}...', end='')
print()   # quebra de linha
print(f'O menor número digitado foi {menor} nas posições ', end='')    # lógica para buscar o menor número
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i+1}...', end='')
print()
