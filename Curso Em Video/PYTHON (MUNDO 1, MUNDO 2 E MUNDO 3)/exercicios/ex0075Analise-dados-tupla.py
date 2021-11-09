""" Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. no final, mostre:
a - quantas vezes apareceu o valor 9
b - em que posição foi digitado o primeiro valor 3
c - quais foram os números pares."""
tupla = tuple(int(input('Digite os valores: '))for c in range(0, 4))   # método prático de fazer ao invés do debaixo
# tupla = (int(input('Digite o 1ª número: ')), int(input('Digite o 2ª número: ')), int(input('Digite o 3ª número: ')),
# int(input('Digite o 4ª número: ')))
print(f'Você digitou os números: {tupla}')
print(f'O numero 9 aparece {tupla.count(9)} vezes. ')
if 3 in tupla:
    print(f'O número 3 aparece na {tupla.index(3)+1}ª posiçao ')
else:
    print('O valor 3 não foi digitado nenhuma vez')
print('os números pares são:', end=' ')
for elemento in tupla:
    if elemento % 2 == 0:
        print(elemento, end='|')
