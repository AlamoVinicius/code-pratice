""" Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
condição do pagamento:
- á vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preçp normal
- 3x ou mais no cartão: 20% de juros"""
print(f'{"LOJAS ÁLAMO":=^40}')

valor_produto = float(input('Digite o valor do produto: '))
forma_pagamento = input(""" escolha a forma de pagamento: 
(dinheiro/cheque): 10% de desconto
(a vista no cartão): 5% de desconto
(2x no cartão): preçp normal
(3x ou mais no cartão): 20% de juros: """).strip()

if forma_pagamento == 'dinheiro/cheque':
    valor_produto = valor_produto * 0.90
    print(f'Valor do produto a ser pago é R${valor_produto}')
elif forma_pagamento == 'a vista no cartão':
    valor_produto = valor_produto * 0.95
    print(f'Valor do produto a ser pago é R${valor_produto}')
elif forma_pagamento == '2x no cartão':
    print(f'Valor do produto a ser pago é R${valor_produto}')
elif forma_pagamento == '3x ou mais no cartão':
    valor_produto = valor_produto * 1.20
    print(f'Valor do produto a ser pago é R${valor_produto}')
else:
    print('Forma de pagamento inválida. confira as letras maíusculas e minusculas.')



''' EU PODERIA TER USADO NUMEROS INTEIROS AO INVÉS DE STR. MAS DEIXA ASSIM MESMO...'''
