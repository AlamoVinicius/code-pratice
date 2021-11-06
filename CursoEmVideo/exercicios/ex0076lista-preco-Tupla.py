""" Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
no final, mostre uma listagem de preços, organizando os dados em forma tabular."""

'''precos = tuple(str(input('Digite o nome do produto: '))for c in range(0,2)),\
 #       tuple(float(input('Digite o preço do produto: R$'))for c2 in range(0, 2))'''  # uma forma de fazer

compras = ('arroz', 3.45, 'feijão', 4.72, 'bicicleta', 120.00, 'brinquedo', 22.00, 'jogo_xadrez', 43.59,
           'nutela', 32.59, 'pasta_amendoim', 43.57, 'patinete', 129.90, 'Celular', 899.90, 'mouse', 25.99)
print(f'''{80*'-'}
{'LISTAGEM DE PREÇOS':^80}
{80*'-'}''')
for indice in  range(0, len(compras), 2):
    print(f'{compras[indice]:.<70}R$ {compras[indice+1]:>7.2f}')
print('-'*80)

'''Essa é minha solução o professor usou  uma comparação com if para saber se é par ou impar, achei essa solução um
pouco mais simples de fazer '''