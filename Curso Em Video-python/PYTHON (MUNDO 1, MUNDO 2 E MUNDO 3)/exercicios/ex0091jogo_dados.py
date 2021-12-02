""" Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. guarde esses resultados
em um dicionário. No final, coloque esse dicionário em ordem. sabendo que o vencedor tirou o maior número no
dado"""
from random import randint
from time import sleep
from operator import itemgetter
jogadas = {}
for c in range(1, 5):
    jogadas[c] = randint(1, 6)
ranking = list()
print('Valores sorteados:')
for keys, values in jogadas.items():
    print(f'O jogador {keys} tirou: {values} no dado.')
    sleep(1)
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)   # método itemgetter busca o dado do meu dict
print('-' * 30)
for i, v in enumerate(ranking):
    print(f'{i+1}ª lugar: Jogador {v[0]} com {v[1]} pts')
    sleep(1)
