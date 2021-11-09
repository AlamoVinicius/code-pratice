""" Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma
sequència de Fibonacci. ex 0 → 1 → 1 → 2 → 3 → 5 → 8  """
n = int(input('Digite um  número para mostrar os termos da sequência de Fibonacci: '))
numanterior = 0
numproximo = 0
controlador = 1
while controlador <= n:
    numproximo += numanterior
    numanterior = numproximo - numanterior
    controlador += 1
    if numproximo == 0:
        numproximo += 1
    print(f'{numanterior}', end='  ')
    print(f' 'if controlador > n else'→', end=' ')   # aqui defino que → só irá parar no fnal se controlador for maior
    # que 'n'
''' obs: existe outras formas de resolver este número a do professor guanabara eu posso conferir a lógica da resolução
deste exerício no seguinte link: https://youtu.be/w7yn1_Mfu0E no curso em vídeo.'''