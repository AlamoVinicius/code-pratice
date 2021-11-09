""" Faça um programa que tenha uma função chamada contador(), que receba três parâmentros: iníco,
fim e passo e realize a contagem. Seu programa tem que realizar três contagens através da função criada:
a - de 1 até 10, de 1 em 1
b - de 10 até 0, de 2 em 2
c - uma contagem personalizada."""
from time import sleep


def contador():
    """
    contador irá realizar uma contagem primeiro de 1 até 10 com passo 2;
    segundo um contador de 10 até 0 com passo 2
    e por fim, deve ser inserido 3 válores, início , fim e passo para sua contagem personalizada.
    :return: sem return
    """
    print('=' * 25)
    for c in range(1, 11):
        print(c, end=', ')
        sleep(0.3)
    print('FIM')
    print('=' * 25)
    for c in range(10, -1, -2):
        print(c, end=', ')
        sleep(0.3)
    print('FIM')
    print('=' * 25)
    print('personalize sua contagem')
    inicio = int(input('Digite o início: '))   # personalizado
    fim = int(input('Digite o final: '))
    while True:
        passo = int(input('Digite o passo: '))
        if passo == 0:
            print('ERRO, não é possivel contar com passo 0')
        else:
            break
    if fim < inicio:
        if passo >= 0:
            passo = 0 - passo
            print(f'Contagem de {inicio} até {fim} contando de {passo*-1} em {+(-passo)}')   # 2 formas de negativar
        else:
            passo = passo
            print(f'Contagem de {inicio} até {fim} contando de {passo*-1} em {passo*-1}')
    for c in range(inicio, fim, passo):
        print(c, end=', ')
        sleep(0.3)
    print('FIM')


# programa principal
contador()
