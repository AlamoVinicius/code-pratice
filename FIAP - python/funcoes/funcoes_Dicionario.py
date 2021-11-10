def perguntar():
    return input('O que deseja realizar?\n'
                 '<I> - para inserir um usuário \n'
                 '<P> - para pesquisar um usuário\n'
                 '<E> - para excluir um usuário \n'
                 '<L> - para listar um usuário: ').upper()


def inserir(dicionario):
    dicionario[input('Matricula: ').upper()] = [input('Digigte o nome: ').upper(),
                                                input('Digite a última data de acesso: '),
                                                input('qual a ultima estação acessada? ').upper(),
                                                input('Digite o login: ').upper(),
                                                input('Digite a hora de login: ')]


def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista is not None:
        print(f'Nome..........  :{lista[0]}')
        print(f'Último acesso...:{lista[1]}')
        print(f'Última estação..:{lista[2]}')


def excluir(dicioanario, chave):
    if dicioanario.get(chave) is not None:
        del dicioanario[chave]
    print('Objeto eliminado!')


def listar(dicionario):
    for chave, valor in dicionario.items():
        print('Objeto......')
        print(f'Login: {chave}')
        print(f'Dados: {valor}')



