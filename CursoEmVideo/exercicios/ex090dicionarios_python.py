""" Faça um programa que leia nome e a média de um aluno, guardando também a situalção em um
dicionário. No final, mostre o conteúdo da estrutura na tela"""
ficha = {'nome': str(input('Nome: ')), 'media': float(input(f'Digite a média: '))}
if ficha['media'] >= 7:
    ficha['situação'] = 'APROVADO'
elif 5 <= ficha['media'] < 7:
    ficha['situação'] = 'RECUPERAÇÃO'
else:
    ficha['situação'] = 'REPROVADO'
print('='*40)
for key, value in ficha.items():
    print(f'{key:.<29}\033[94m{value}\033[m')   # código de cor azul claro inserido na formatação.
