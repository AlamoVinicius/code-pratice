""" Faça um programa que tenha uma função chamada maior(), que receba vários parâmentros com valores
inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""
from time import sleep


def maior(* nums):
    cont = maior_number = 0
    print('=' * 40)
    print('Analisando os valores...')
    for valor in nums:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior_number = valor
        else:
            if valor > maior_number:
                maior_number = valor
        cont += 1
    print(f'foram informados {cont} números')
    print(f'O maior valor informado foi {maior_number}')


# main programing
maior(1, 3, 5, 32, 5, 9)
maior(2, 5, 6, 2, 1, 9)
maior(5, 2)
maior(1, 4, 7)
maior(0)

