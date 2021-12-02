""" Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idadde)
em um dicionário se por acaso a ctps for diferente de zero, o dicionário receberá também o ano de contra
tação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""
from datetime import datetime
aposentadoria = 0
trabalhador = dict()
trabalhador['nome'] = str(input('Digite o nome: '))
ano_nascimento = int(input('Digite o ano de nascimento: '))
idade = int(datetime.now().year - ano_nascimento)
trabalhador['idade'] = idade
trabalhador['ctps'] = int(input('Digite o número da carteira de trabalho: (0 para sem ctps) '))
if trabalhador['ctps'] != 0:
    trabalhador['ano_contratação'] = int(input('Digite o ano de contratação: '))
    trabalhador['salario'] = float(input('Digite o salário: R$'))
    aposentadoria = idade + (35 - (datetime.now().year - trabalhador['ano_contratação']))
    trabalhador['aposentadoria_idade'] = aposentadoria
print(f'='*40)
print(f'Estrutura: {trabalhador}')
print(f'='*40)
for keys, values in trabalhador.items():
    print(f'{keys:.<30}{values}')
