""" façça a tabuada do exercício 9 usando o laço for """
numero = int(input('Digite um número para exibir sua tabuada: '))
for c in range(1, 11,):
    calculo = numero * c
    print(f'{numero} X {c} = {calculo}')