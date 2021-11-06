#calculando preço de um aluguel de carro sendo q o dia vale 60 reais e o km vale 0.15/km
kmpercorrida = float(input('Quantidade de km percorrida: '))
diadelocacao = int(input('Dias ultilizado na locação: '))
calculo = kmpercorrida * 0.15 + diadelocacao * 60.00
print(f'Valor a ser cobrado: R$ {calculo:.2f}')