""" Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
a - quantos números foram digitados, b - a lista de valores, ordenada de forma decrecente.
c - se o valor 5 foi digitado e está ou não na lista."""
# entrada dos números
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    perg = input('Deseja continuar? [S/N]').upper().strip()[0]
    if perg == 'N':
        break
# exibição de quantos números foram digitados:
print(f'Foram digitadors \033[95m{len(lista)}\033[m números')
lista.sort(reverse=True)
print(f'Os números em ordem decrescente: \033[94m{lista}\033[m')
if 5 in lista:
    print('Número 5 está na lista nas posições: ', end='')
    for v, c in enumerate(lista):
        if c == 5:
            print(f'{v+1}...', end='')
else:
    print('Número 5 não se encontra na lista')