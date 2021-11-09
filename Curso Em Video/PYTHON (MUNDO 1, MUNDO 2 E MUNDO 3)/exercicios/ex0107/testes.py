""" Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir() dobrar()
e metade(). faça uambém um programa que importe esse módulo e use algumas dessas funções."""
from exercicios.ex0107 import moeda

valor = float(input('Digite o valor que deseja interagir: R$ '))
pctgem = float(input("Digite a porcentagem que vc deseja aumentar e diminuir: "))
print(f'Aumento de {pctgem}% : {moeda.aumentar(valor, pctgem)}')
print(f'Diminuir em {pctgem}%: {moeda.diminuir(valor, pctgem)}')
print(f'O Dobro de {valor} é {moeda.dobrar(valor)}')
print(f'A metade de {valor} é: {moeda.metade(valor)}')
