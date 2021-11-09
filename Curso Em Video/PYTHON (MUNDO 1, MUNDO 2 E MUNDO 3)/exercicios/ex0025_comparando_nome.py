""" crie um programa que leia um nome de uma pessoa e diga se ela tem 'Silva' no nome """

nome = input('Digite seu nome completo: ').upper()
if 'SILVA' in nome:
    print('O nome possui Silva :D')
else:
    print('O nome não possui Silva')