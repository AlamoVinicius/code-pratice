""" Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
dicionário e todos os dicionários em uma lista. No final, msotre:
a - quantas pessoas foram cadastradas/ b - a média de idade do grupo/ c- uma lista com todas as mulheres.
d - uma lista com todas as pessoas com idade acima da média"""
lista = []
mulheres = []
maiores_media_idade = []
pessoas = {}
media = 0
while True:
    pessoas['nome'] = str(input('Nome: '))   # não preciso usar pessoas.clear() pois meu dict automaticamente limpa
    # nos novos elementos quando sobrescritos.
    pessoas['sexo'] = str(input('sexo: [M/F] ')).strip().upper()[0]
    while pessoas['sexo'] not in 'MF':
        pessoas['sexo'] = str(input('Por favor, digite somente "M" ou "F": ')).strip().upper()[0]
    pessoas['idade'] = int(input('idade: '))
    resp = str(input('Deseja continuar? [S/N]: '))
    lista.append(pessoas.copy())
    if resp in 'Nn':
        break

# número de pssoas cadastradas:
print(f"{'='* 40}")
print(f'{"RESULTADOS":^40}')
print(f"{'='* 40}")
print(f'Foram cadastrado {len(lista)} pessoas.')

# média de idade do grupo
for dados in lista:
    media += dados['idade']
media /= len(lista)
print(f'A média do grupo de pessoas é {media:.1f}')

# lista de mulheres no grupo
for dados in lista:
    if dados['sexo'] == 'F':
        mulheres.append(dados['nome'])
print('As mulheres do grupo são: ')
for dados in mulheres:
    print(dados)

# lista de pessoas com idade acima da média
print('As pessoas com idade acima da média são: ')
for dados in lista:
    if dados['idade'] >= media:
        for key, values in dados.items():
            print(f'{key} = {values}; ', end='')

''' Algumas diferençãs relacionadas a solução do curso foram observados, pode ser conferido no seguinte link 
https://youtu.be/ETnExBCFeps mas nada que altere muita coisa em minha solução. '''