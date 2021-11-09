""" Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário
vai continuar, no final mostre:
 a - qual é o total de gasto na compra
 b - quantos produtos custam mais de 1000
 c - qual é o nome do produto mais barato. """
contador = 0   # definiçoes das váriaveis
somavalor = 0
produto_mais_1000 = 0
nome_produto_barato = ''
preco_menor = 0

print(f'{"="*40}')
print(f'{"CONTROLE DE COMPRAS DO ALAMO":^20}')
print(f'{"="*40}')
while True:
    nome_produto = str(input('Digite o nome do produto: '))   # entrada das variaveis
    preco = float(input('Preço do produto: R$'))   # definição do preço
    somavalor += preco
    contador += 1
    if preco >= 1000:    # condição para contar produto mais caro que mil reais
        produto_mais_1000 += 1

    if contador == 1 or preco < preco_menor:  # condição para definir o menor preço e assim condicionar a váriavel
        # que irá receber o nome do produto mais barato nessa rodada do loop while.
        preco_menor = preco
        nome_produto_barato = nome_produto

    validacao = ' '
    while validacao not in 'SN':
        validacao = str(input('Deseja continuar: [S/N]')).strip().upper()[0]
    if validacao == 'N':
        break
print(f'O total gasto foi de R$ {somavalor}\ntotal de {produto_mais_1000} produtos mais caro que R$ 1000.00\n'
      f'O produto mais barato foi: {nome_produto_barato} que custa {preco_menor}')
