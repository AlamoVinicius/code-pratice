""" Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terrno retangular
(largura e comprimento) e mostre a área do terreno."""


def area(a, b):
    calculo = a * b
    print(f'A área do terrendo do terreno {a}x{b} é: {calculo} m²')


largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
