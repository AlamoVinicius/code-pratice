""" Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu stats, de acordo
com a seguinte:
 abaixo de 18.5 abaixo de peso
 entre 18.5 e 25 peso ideal
 25 até 30 sobrepeso
 30 até 40 obesidade
 acima de 40 obesidade mórbida"""

print('Bem vindo a sua calculadora de IMC online.')
peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em mts (exemplo 1.85): '))
imc = peso/(altura ** 2)
print(f'seu IMC é = {imc:.2f}')
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobre peso ')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')

