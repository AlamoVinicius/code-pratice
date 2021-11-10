def preencherinventario(lista):
    resp = 'S'
    while resp == 'S':
        equipamento = [input('Equipamento: '),
                       float(input('Valor? ')),
                       int(input('Digite o sérial: ')),
                       input('Departamento: ')]
        lista.append(equipamento)
        resp = input('Digite "S" para inserir mais itens, e enter para finalizar: ').upper()


def exibirinventario(lista):
    for elemento in lista:
        print(f'Nome..........:{elemento[0]}')
        print(f'Valor.........:{elemento[1]}')
        print(f'serial........:{elemento[2]}')
        print(f'Departamento..:{elemento[3]}')


def localizarpornome(lista):
    busca = input('Digite o nome do equipamento que deseja buscar: ')
    for elemento in lista:
        if busca == elemento[0]:
            print(f'Valor..:{elemento[1]}')
            print(f'Serial..{elemento[2]}')


def depreciarpornome(lista, porc):
    depreciacao = input('Digite o nome do equipamento que deseja depreciar: ')
    for elemento in lista:
        if depreciacao == elemento[0]:
            print(f'Valor antigo: {elemento[1]}')
            elemento[1] = elemento[1] * (1 - porc / 100)
            print(f'Novo valor: {elemento[1]}')


def excluirporserial(lista):
    serial = int(input('Digite o serial do equipamento que será excluido:'))
    for elemento in lista:
        if elemento[2] == serial:
            lista.remove(elemento)
    return 'Itens Excluídos. '

def resumivalores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores) > 0:
        print(f'O equipamento mais caro custa: R${max(valores)}')
        print(f'O equipamento mais barato custa: R${min(valores)}')
        print(f'valor totalé de : R${sum(valores)}')
