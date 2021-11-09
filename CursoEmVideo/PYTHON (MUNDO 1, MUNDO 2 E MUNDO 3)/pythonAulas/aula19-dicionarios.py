pessoas = {'nome': 'Álamo', 'sexo': 'M', 'idade': '26'}
print(pessoas['nome'])    # quando eu passo o nome da chave dentro de colchetes ele me dá o item dessa chave
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')    # print formatado
print(pessoas.keys())   # me retorna todas as chaves
print(pessoas.values())   # me mostra todos os dados dentros das chaves
print(pessoas.items())   # me mostra uma lista composta com todos os items dentro de tupla
for key in pessoas.keys():   # posso usar as funçoes dentro do for para me mostrar os dados
    print(key)
pessoas['nome'] = 'Leandro'    # troco o alamo por leandro adicionar um novo dado substitui
pessoas['peso'] = 98.5        # adicionei um novo elemento dentro do dic
for key, values in pessoas.items():
    print(f'{key} = {values}')
#  del pessoas[sexo]     apaga a chave sexo

brasil = []     # exemplo de dicionário dentro de lista
estado1 = {'uf': 'Minas Gerais', 'sigla': 'MG'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])    # o primeiro indíce dentro de colchetes representa o primeiro dict adcionado
print(brasil[0]['sigla'])    # aqui eu eu mostro o que esta dentro do indíce de sigla no dict zero

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())    # no dicionário o médoto de cópia [:] não funciona é necessaário utilizar o
# copy() para acrescentar uma cópia na minha lista estado sem criar uma ligação
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
for e in brasil:                   # usando o laço for para organizar meus prints
    for v in e.values():
        print(v, end=' ')
    print()
