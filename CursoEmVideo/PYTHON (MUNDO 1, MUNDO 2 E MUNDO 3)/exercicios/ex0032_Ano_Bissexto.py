""" Faça um programa que leia um  ano e diga se ele é bissexto"""
from datetime import date    # biblioteca datetime para importar data atual.
ano = int(input("Digite o ano para saber se é bissexto ou (0) para saber o ano atual: "))
if ano == 0:
    ano = date.today().year   # com essa funão eu consigo pegar o ano atual da máquina.
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(f'Ano {ano} Bissexto!')
else:   
    print(f'Não, {ano}não é um ano bissexto!')
