""" Escreva um programa que leia  a velocidade de um carro se ele ultrapassa 80 km/h
mostre uma msg dizendo que ele foi multado
a multa vai custar 7.00 por km a cima do limite."""

velocidade = int(input('Velocidade do carro: '))
calculo_da_multa = (velocidade - 80) * 7
if velocidade > 80:
    print(f'Infelizmente você foi multado em R$ {float(calculo_da_multa)}')
else:
    print('Velocidade Permitida.')
