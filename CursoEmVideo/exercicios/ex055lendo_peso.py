""" faça um programa que leia o peso de cinco pessoas. no final, mostre qual foi o maior e o menor peso lidos"""
lista = []
for c in range(1, 6):
    lista.append(float(input(f"Digite o {c}ª pesos: ")))
print(f'{max(lista)} é o maior peso lista')
print(f'{min(lista)} é o menor peso na lista')

''' acabei que eu usei um método ainda não mostrado no curso em video. abaixo segue outro modo para a realização: '''
''' esse modo foi gênial!!! lol'''
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Digite o {p}º peso: '))
    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}kg')
print(f'O menor peso lido foi de {menor}kg')
