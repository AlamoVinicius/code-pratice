""" escreva um prgrama que leia um número inteiro qualquer e peça para o usuário escolhar qual será
a base de conversão
1 para binário     2 para octal      3 para hexadecimal"""
num = int(input("digite um numero: "))
escolha = int(input('Escolha <1> para converter para binário <2> para octal e <3> para hecadecimal '))
if escolha == 1:
    print(f'{bin(num)[2:]} em binário.')    # bin transforma o numero da váriavel para binário com tratamento de str
elif escolha == 2:
    print(f'{oct(num)[2:]} em octal.')
elif escolha == 3:
    print(f'{hex(num)[2:]} em hexadecimal. ')
else:
    print('opção inválida.')