import interface


def arq_existe(nome):
    try:
        with open(nome, 'rt') as arq:
            return True
    except FileNotFoundError:
        return False


def criar_arquivo(nome):
    try:
        with open(nome, 'wt') as a:
            print(f'Arquivo {nome} criado com sucesso!')
    except:
        print('Houve um ERRO na criação do arquivo!')


def ler_arquivo(nome):
    try:
        with open(nome, 'rt') as a:
            interface.cabecalho('pessoas cadastradas')
            for linha in a:
                dado = linha.split(';')
                dado[1] = dado[1].replace('\n', '')
                print(f'{dado[0]:.<30}: {dado[1]}  ANOS')
    except:
        print('erro, na leitura do arquivo.')


def cadastro_pessoa(arq, nome='desonhecido', age=0):
    try:
        with open(arq, 'at') as a:
            try:
                a.write(f'{nome};{age}\n')
            except:
                print('Houve um erro ao cadastrar nova pessoa')
            else:
                print(f'{nome} cadastrado com sucesso')
    except:
        print('erro ao cadastrar nova pessoa.')


def deletar_pessoa(arq):
    try:
        nomes = open (arq, 'r').readlines()
        for i, dado in enumerate(nomes):
            print(f'{i}.............{dado[:-4]}')
        choise = interface.leiaint('Escolha o número para deletar: ')
        print(f'{nomes[choise][:-4]} Deletado com sucesso.')
        del nomes[choise]
        nomes = ''.join(nomes)
        with open(arq, 'wt') as a:
            a.write(nomes)
    except IndexError:
        print('\033[31merro, número inválido\033[m')
        