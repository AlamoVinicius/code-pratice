""" Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função
input() do python, só que fazendo a validação para aceitar apenas um valor numérico,"""


def leiaint(str):
    """
    ==> essa função irá validar apenar um número inteiro.
    :param str: irá receber o valor em string para converter em inteiro, se não ira receber um erro
    :return:   irá retornar o valor de str em um número inteiro
    """
    while True:
        num = input(str).strip()
        if num.isnumeric():
            num = int(num)
            break
        else:
            print(f'\033[91mErro! digite apenas um número válido\033[m')
    return num


n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')
help(leiaint)
