""" escreva um programa que leia duas notas de um aluno e calcule sua média. mostrndo uma mensagem no final, de
acoedo com a média atingida: abaixo de 5 reprovado ; entre 5 e 6.9 recuperação; média 7 ou superior APROVADO """
nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota: '))
medianota = (nota1 + nota2) / 2
if medianota < 5:
    print(f'média da nota {medianota} REPROVADO.')
elif 5 <= medianota <= 6.9:
    print(f'Média nota {medianota} RECUPERAÇÃO.')
else:
    print(f'Média da nota {medianota} APROVADO.')
