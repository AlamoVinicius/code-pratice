""" REfaça o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triângulo será
formado:
equilátero = todos os lados iguais;  isósceles = dois lados iguais; escaleno = todos os lados diferentes"""
r1 = float(input('Digite o primeiro valor de um dos lados do triângulo: '))   # a
r2 = float(input('Digite o segundo valor    de um dos lados do triângulo: '))   # b
r3 = float(input('Digite o terceiro valor de um dos lados do triângulo: '))   # c
if r1 < r2 + r3 and  r2 < r1 + r3 and r3 < r1 + r2:   # fórmula para condição de existência de um triangulo:
    print('Sim, as retas formam um triangulo.')
    if r1 == r2 == r3:
        print('Triângulo equilátero')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r1 == r3 != r2:
        print('Triângulo isósceles')
    elif r1 != r2 != r3 != r1:
        print('Triândulo escaleno')
    else:
        print('triângulo inválido.')
else:
    print('Não, as retas não formam um triangulo.')


