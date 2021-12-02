""" escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento:
para salários superiores 1250.00 aumento de 10%, para salários inferiores ou iguais aumento de 15%"""
salario = float(input('Salário para aumento: '))
if salario <= 1250.00:
    salario = salario * 1.15
    print(f'Novo salário: R${salario:.2f}')
else:
    salario = salario * 1.10
    print(f'Novo salário: R${salario:.2f}')

