"""Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do
jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final
, tudo isso será guardado em um dicionário, incluindo total de gols feito durante o campeonato."""
# entrada das váriaveis principais
jogador = {'nome': str(input('Nome do jogador: '))}
numero_paridas = int(input(f'Digite quantidade de jogos realizado por {jogador["nome"]}: '))
total_gols = 0
gols = []
for c in range(0, numero_paridas):   # loop/lógica para adicionarmos dados em nosso dict
    gols.append(int(input(f'Quantos gols na {c+1}º partida: ')))
jogador['gols'] = gols[:]    # dicionário jogador recebe uma cópia da lista de gols
jogador['total_gols'] = sum(gols)
# exibição final
print(f'''{'='*40}   
{'ESTATÍSTICAS':^40}
{'='*40}''')
print(f'\033[93m{jogador}\033[m')
print('='*40)
for key, values in jogador.items():
    print(f'{key:.<33}{values}')
print('=' * 40)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} jogos: ')
for i, v in enumerate(jogador['gols']):
    print(f'==> Na {i+1}º partida, fez {v} gols.')
print(f'Total de {jogador["total_gols"]} gols. ')

''' essa é a minha solução, a solução do curso pode ser consultada no seguinte link: https://youtu.be/5yKiud-YNaE '''
