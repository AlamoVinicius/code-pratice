"""" faça um programa que leia trÊs números e mostre qual é o maior é qual e o menor. """
n1 = int(input())
n2 = int(input())
n3 = int(input())
print(f'The choice number are: {n1}, {n2} and {n3} ')
menor = n1              # calculando o menor núemro
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1     # calculando o maior número
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O menor numero é {menor} e o maior número é {maior}')
