""" Crie um programa que leia nome e duas notas de vários alunos e guarte tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
de cada aluno individualmente."""
lista_main = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = nota1 + nota2 / 2
    lista_main.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar?[S/N] '))
    if resp in 'Nn':
        break
print('-'*22)
print(f'{"nª":<4}{"nome":<10}{"média":>8}')
print('-'*22)
for indice, aluno in enumerate(lista_main):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    print('-'*30)
    opc = int(input('Mostrar notas de qual aluno? (digite "999" para finalizar)'))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(lista_main) - 1:
        print(f'Notas de {lista_main[opc][0]} são {lista_main[opc][1]}')
