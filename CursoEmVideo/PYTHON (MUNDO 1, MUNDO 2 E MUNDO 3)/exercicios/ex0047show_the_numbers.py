""" faça um programa que mostre na tela todos os números pares que est~~ao no intervalo entre 1 a 50"""
print('Exibindo todos os números pares entre 0 e 50')
for c in range(0, 51, 2):
    print(c, end=" ")
print()
''' ou eu posso fazer assim tambem: '''
for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=' ')
