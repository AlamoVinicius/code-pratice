""" Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem
de colocação. Depois mostre: a- apenas os 5 primeiros colocados. b- os últimos 4 colocados na tabela, c- uma lista
com os times em ordem alfabética. d- em que posição na tabela está o time da Chapecoense."""
tupla = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
         'Bragantino', 'Athlético-PR', 'Internacional', 'Fluminense', 'América-MG',
         'Atlético-GO', 'Cuiabá', 'Ceará SC', 'São Paulo', 'Juventude',
         'Santos', 'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')
print(f'Ordem de classificação dos 20 times do Brasileirão: {tupla}')
print(f'{"-="*50}')
print(f'os cincos primeiros classificados são: {tupla[0: 5]}')
print(f'{"-="*50}')
print(f'Os últimos 4 colocados na tabela: {tupla[-4:]}')
print(f'{"-="*50}')
print(f'Lista dos times em ordem alfabética: {sorted(tupla)}')
print(f'{"-="*50}')
print(f'O chapecoense se encontra na {tupla.index("Chapecoense")+1}ª posição')
