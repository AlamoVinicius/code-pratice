""" Aprimore o Desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização
do aproveitamento de cada jogador."""
lista_main = []
while True:
    jogador = {'nome': str(input('Nome do jogador: '))}
    numero_partidas = int(input(f'Digite quantidade de jogos realizado por {jogador["nome"]}: '))
    total_gols = 0
    gols = []    # poderia usar o gols.clear() mas desse jeito ele tmb limpa a lista gols
    for c in range(0, numero_partidas):   # loop/lógica para adicionarmos dados em nosso dict
        gols.append(int(input(f'Quantos gols na {c+1}º partida: ')))
    jogador['gols'] = gols[:]    # dicionário jogador recebe uma cópia da lista de gols
    jogador['total_gols'] = sum(gols)
    lista_main.append(jogador.copy())   # lista principal recebe uma cópia do dicionário "jogador"
    resp = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if resp in 'Nn':
        break

# exibição do cabeçalho da minha tabela:
print('='*50)
print('Cod  ', end='')
for i in jogador.keys():
    print(f'{i:<18}', end='')
print()
print('='*50)
for i, dados in enumerate(lista_main):
    print(f'{i:<3}  ', end='')
    for d in dados.values():
        print(f'{str(d):<18}', end='')
    print()
print('='*50)

# sistema de análise individual dos jogadores:
choise = int(input("Mostrar dados de qual jogador? (999 para encerrar) "))
while choise != 999:
    if choise < len(lista_main):
        for i, dados in enumerate(lista_main):
            if i == choise:
                print(f'Levantamendo do jogador "{dados["nome"].upper()}"')
                for indice, elementos in enumerate(dados['gols']):
                    print(f'No {indice+1}º jogo fez {elementos} gols')
    else:
        print('Código do jogador inexistente')
    print('=' * 50)
    choise = int(input("Mostrar dados de qual jogador? (999 para encerrar) "))
print('ENCERRANDO...')

''' Algumas diferenças foram observado da minha solução para o do curso, pode ser conferido no seguinte link:
https://youtu.be/mw1So0r317Y?t=1050'''