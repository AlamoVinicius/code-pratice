""" escreva um prpgrama que mostre sua categoria para natação
até 9 anos: mirim
até 14 anos: infantil
até 19 anos: junior
até 25anos: sênior
acima: master """
idade = int(input('Digite a idade do competidor: '))
if idade <= 9:
    print('Categoria MIRIM')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19:
    print('Categoria JÚNIOR')
elif idade <= 25:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')
