"""Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de
texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas."""

from lib.arquivo import *
from lib.interface import *
from time import sleep

arq = 'Curso em video.txt'
if not arq_existe(arq):
    criar_arquivo(arq)
while True:
    resp = menu(['Exibir pessoas cadastradas', 'Cadastrar Pessoa', 'Sair'])
    if resp == 1:
        ler_arquivo(arq)
    elif resp == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastro_pessoa(arq, nome, idade)
    elif resp == 3:
        cabecalho('Saindo do sitema...')
        break
    else:
        print('\033[91mErro, Digite uma opção inválida!\033[m' )
    sleep(1)
