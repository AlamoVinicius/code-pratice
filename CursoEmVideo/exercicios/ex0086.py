""" Crie um programa que crie uma matriz de dimensção 3x3 e preencha com valores lido pelo teclado.
no final, mostre a matriz na tela, com a formatação correta."""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor da posição [{linha, coluna}]: '))
print('='*40)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'\033[96m[{matriz[linha][coluna]:>5}]\033[m', end='')
    print()




'''' o jeito q eu tinha printado logo a baico mas vou usar o do professor por exigir mais lógica
print(matriz[0])
print(matriz[1])
print(matriz[2])'''
