""" aprimore o desafio anterior, mostrando no final a - a soma de todos os valores pares digitados,
b - a soma dos valores da terceira coluna. c - O maior valor da segunda linha"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = maior = scol = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor da posição [{linha, coluna}]: '))
print('=' * 40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'\033[96m[{matriz[l][c]:>5}]\033[m', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]   # a soma de todos os valores pares digitados:
    print()
print(f'A soma dos números pares é \033[93m{spar}\033[m')
for l in range(0, 3):
    scol += matriz[l][2]
    if l == 0:     # o maior valor da segunda linha
        maior = matriz[1][l]
    else:
        if matriz[1][l] > maior:
            maior = matriz[1][l]

print(f'A soma da terceira coluna é: \033[94m{scol}\033[m')
print(f'O maior número da segunda linha é \033[95m{maior}\033[m')


'''esse foi o jeito que eu tinha feito porem eu reparei que ele não era tão eficaz caso minha matriz tivesse n valores
somador = 0
for linha in range(0, 3):
    for c in range(0, 3):
        if matriz[linha][c] % 2 == 0:
            somador += matriz[linha][c]
print(f'A soma dos números pares é {somador}')
soma = matriz[0][2] + matriz[1][2] + matriz[2][2]   # a soma dos valores da teerceira coluna:
print(f'A soma de todos o números da terceira coluna é: \033[94m{soma}\033[m')
maiorn = [matriz[1][0], matriz[1][1], matriz[1][2]]
print(f'O maior número da segunda linha é: {max(maiorn)}')'''
