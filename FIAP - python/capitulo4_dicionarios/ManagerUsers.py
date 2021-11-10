from funcoes.funcoes_Dicionario import *
usuarios = {}
opcao = perguntar()
while opcao == 'I' or opcao == 'P' or opcao == 'E' or opcao == "L":
    if opcao == 'I':
        inserir(usuarios)
    if opcao == "P":
        pesquisar(usuarios, input('Qual login deseja pesquisar?: ').upper())
    if opcao == 'E':
        excluir(usuarios, input('Digite o login que deseja excluir: ').upper())
    if opcao == 'L':
        listar(usuarios)
    opcao = perguntar()
