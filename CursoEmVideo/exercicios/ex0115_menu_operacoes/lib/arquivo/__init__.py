from exercicios.ex0115_menu_operacoes.lib.interface import *


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
            cabecalho('pessoas cadastradas')
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
                print('usuário cadastrado com sucesso')
    except:
        print('erro ao cadastrar nova pessoa.')
