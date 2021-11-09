""" Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre
na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui."""
import moeda
preco = float(input('Digite o preço: R$'))
porcmais = float(input('Digite a porcentagem que deseja aumentar: '))
porcmenos = float(input('Digite a porcentagem que deseja depreciar: '))
moeda.resumo(preco, porcmais, porcmenos)
