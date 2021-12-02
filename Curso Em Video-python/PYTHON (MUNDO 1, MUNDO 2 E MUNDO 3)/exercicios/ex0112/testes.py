"""Dentro do pacote utilidadesCev que criamos no desafio 111, temos um módulo chamado dado. Crie uma
função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação
de dados para aceitar apenas valores que sejam monetários."""
from utilidadesCev import moeda, dado
preco = dado.leia_dinheiro('Digite o preço: R$')
porcmais = float(input('Digite a porcentagem que deseja aumentar: '))
porcmenos = float(input('Digite a porcentagem que deseja depreciar: '))
moeda.resumo(preco, porcmais, porcmenos)
