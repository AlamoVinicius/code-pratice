""" Modifique as funções que foram craidas no desafio 107 para que elas aceitem um paâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda() desenvolvida no
desafio 108"""
import moeda

valor = float(input('Digite o valor que deseja interagir: R$ '))
pctgem = float(input("Digite a porcentagem que vc deseja aumentar e diminuir: "))
print(f'Aumento de {pctgem}% : {moeda.aumentar(valor, pctgem, cvsao=True)}')
print(f'Diminuir em {pctgem}%: {moeda.diminuir(valor, pctgem, cvsao=True)}')
print(f'O Dobro de {moeda.moeda(valor)} é: {moeda.dobrar(valor, cvsao=True)}')
print(f'A metade de {moeda.moeda(valor)} é: {moeda.metade(valor, cvsao=True)}')
