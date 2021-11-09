""" Faça um programa que tenha uma função chamada ficha(), que receba dois parâmentros opcionais: O
nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
algum dado não tenha sido informado corretamente."""


def ficha(nome='<desconhecido>', gols=0):
    print(f'{"=" * 30}')
    print(f'{"jogador"}{"gols":>23}')
    print(f'{"=" * 30}')
    print(f'{nome:.<29}{gols}')


n = str(input('Digite o nome do jogador: '))
g = str(input('Digite a qtde de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
