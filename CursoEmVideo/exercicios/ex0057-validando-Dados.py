""" Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
digitação novamente até ter um valor correto. """
sexo = input('Digite o sexo da pessoa [M/F] ').upper()
while sexo != 'F' and sexo != 'M':
    sexo = input('Digite o sexo da pessoa [M/F]: ').upper()
print(f'sexo {sexo} registrado!.')


''' another way como o professor fez: '''
sexo = input('Digite o sexo: [M/F] ').upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválids, por favor insira novamente os dados: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')