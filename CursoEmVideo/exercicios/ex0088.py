""" Faça um programa que ajude um jogador da Mega sena a criar palpites. O programa vai pergutanr quantos
jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo. cadastrando tudo em uma lista composta"""
from random import randint
from time import sleep
lista_temp = []
jogos_mega = []
qtde = int(input('Quantos jogos você deseja sortear? '))
tot = 1
while tot <= qtde:
    cont = 0
    while True:
        numeros = randint(1, 60)
        if numeros not in lista_temp:
            lista_temp.append(numeros)
            cont += 1
        if cont == 6:
            break
    lista_temp.sort()
    jogos_mega.append(lista_temp[:])
    lista_temp.clear()
    tot += 1
print(f'''{'-'*40}
\033[95m{'PALPITES MEGA-SENA':^40}\033[m
{'-'*40}''')
for indice, dados in enumerate(jogos_mega):
    print(f'\033[96mexibindo o {indice+1}º jogo: {dados}\033[m')
    sleep(1)
print(f'\033[92m{"BOA SORTE!!":^40}\033[M')