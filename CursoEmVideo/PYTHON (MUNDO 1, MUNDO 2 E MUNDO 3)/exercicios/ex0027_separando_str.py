""" Faça um programa que leia o nome completo mostrando o primeiro e ultimo nome separadamente """
nome = str(input('Digite o nome completo: ')).strip()   # sempre lembrar de usar o strip para desconsiderar os epaços
separacao = nome.split(' ')
print(f'O primeiro nome é {separacao[0]}')
print(f'O ultimo nome é {separacao[-1]}')
print(separacao)