""" Faça um mini-sistema que ultilize o intective help do python. O usuário vai digitar o comando
e o manual vai aparecer. quando o usuário digitar a palavra 'fim' o programa se encerrará. obs
use cores."""


def pyhelp():
    from time import sleep
    while True:
        print('\033[42m=' * 30)
        print(f"{'sistema de ajuda pyHELP':^30}")
        print('=' * 30)
        print('\033[m')
        func = str(input('Função ou lib (digite "fim" para sair)>'))
        if func == 'fim' or func == 'FIM':
            break
        tam = len(f'Acessando o manual do comando "{func}"') + 4
        print('\033[45m=' * tam)
        print(f'  Acessando o manual do comando "{func}"')
        print('=' * tam)
        print('\033[m')
        sleep(1)
        print(f'\033[7m')
        help(func)
        print(f'\033[m')


pyhelp()
''' Minha solução de acordo com o curso, poderia ter usado as funçoes separadas e o while no meu programa
principal. de acordo com a resolução do curso: https://www.youtube.com/watch?v=BMKYnZoxy88'''