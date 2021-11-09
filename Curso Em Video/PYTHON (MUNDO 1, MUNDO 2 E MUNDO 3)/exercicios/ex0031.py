""" Desenvolva um programa que pergunte a distançia de uma viagem em KM. Calcule o preço da passagem ,
cobrando R% 0.50 por km para viagens de ate 200 km e R$ 0.45 para viagend mais longas."""
km_da_viagem = float(input('Distância em km da viágem: '))
if km_da_viagem >= 200:
    preco = km_da_viagem * 0.45
else:
    preco = km_da_viagem * 0.50
print(f'O km da viagem é {km_da_viagem}, o valor total a ser pago é R${preco}')
