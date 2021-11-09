""" Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
a - quantas pessoas foram cadastradas. b - uma listagem com as pessoas mais pesadas.
c - uma listagem com as pessoas mais leves. """
temp = []
dados = []
totmais = totmenos = 0
while True:
    temp.append(str(input('Digite o nome: ')))
    temp.append(float(input('Digite o peso: ')))
    if len(dados) == 0:
        totmais = totmenos = temp[1]
    else:
        if temp[1] > totmais:
            totmais = temp[1]
        if temp[1] < totmenos:
            totmenos = temp[1]
    dados.append(temp[:])
    temp.clear()
    perg = input('Deseja adicionar mais um nome: [S/N] ').strip().upper()[0]
    if perg == 'N':
        break

print(f'foram cadastrado {len(dados)} pessoas' )
print(f'O maior peso foi de {totmais}kg, peso de ', end='')
for p in dados:
    if p[1] == totmais:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {totmenos}kg, peso de ', end='')
for p in dados:
    if p[1] == totmenos:
        print(f'[{p[0]}]', end='')
print()

