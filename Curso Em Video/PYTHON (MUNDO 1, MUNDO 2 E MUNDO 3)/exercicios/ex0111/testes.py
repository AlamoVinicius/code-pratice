"""Crie um pacote chamado utilidadesceV que tenha dois módulos internos chamados moeda e dado.
transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo
funcionando."""
from utilidadesCev import moeda
preco = float(input('Digite o preço: R$'))
porcmais = float(input('Digite a porcentagem que deseja aumentar: '))
porcmenos = float(input('Digite a porcentagem que deseja depreciar: '))
moeda.resumo(preco, porcmais, porcmenos)
