""" Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar,
para cada palavra, quais são as suas vogais. """
print('EXIBINDO AS VOGAIS')
tupla = ('cadeira', 'alamo', 'blusa', 'amor', 'juntos', 'sempre', 'celular')
for elemento in tupla:
    print(f'\nNa palavra  {elemento.upper()} temos: ',end='')
    for letra in elemento:
        if letra.lower() in 'aeiou':    # posso usar as comparações com os acentos para pegar as palavras  com acentos
            print(f'{letra}', end=' ')   # cada elemento na tupla temos uma lista então da pra comparar
