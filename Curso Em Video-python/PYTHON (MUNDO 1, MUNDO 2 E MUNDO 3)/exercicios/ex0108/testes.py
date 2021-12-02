""" Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os
valores como um valor monetário formatado."""
import moeda

valor = float(input('Digite o valor que deseja interagir: R$ '))
pctgem = float(input("Digite a porcentagem que vc deseja aumentar e diminuir: "))
print(f'Aumento de {pctgem}% : {moeda.moeda(moeda.aumentar(valor, pctgem))}')
print(f'Diminuir em {pctgem}%: {moeda.moeda(moeda.diminuir(valor, pctgem))}')
print(f'O Dobro de {moeda.moeda(valor)} é: {moeda.moeda(moeda.dobrar(valor))}')
print(f'A metade de {moeda.moeda(valor)} é: {moeda.moeda(moeda.metade(valor))}')
