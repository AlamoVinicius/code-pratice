""" Crie um programa que tenha uma função fatorial() que receba dois parâmentros: o primeiro que indique
o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado
ou não na tela o processo de cálculo do fatorial."""


def fatorial(num, show=False):
    """
    => calcula fatorial de um determinado número
    :param num: valor que será calculado o fatorial
    :param show: (opcional) mostra a conta do fatorial
    :return: O valor do fatorial de 'num'
    """
    fat = 1
    for c in range(num, 0, -1):
        fat *= c
    if show:
        print(f'{num}!', end=' ')
        for c in range(num, 0, -1):
            print(f'{c}', end=' ')
            print('x' if c > 1 else '=', end=' ')
    return fat


# main programinig
fator = fatorial(5, show=True)
print(fator)