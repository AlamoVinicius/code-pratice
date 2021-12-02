""" Crie um programa onde o usuário possa digitar sete valores númericos e cadastre-os em uma lista única que
mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente"""

lista_main = []
lista_par = []
lista_impar = []
for c in range(1, 8):   # lógica do programa loop 7 para adicionar 7 números
    num = int(input(f'digite o {c}º número: '))   # váriavel num entrada do usuário
    if num % 2 == 0:                      # comparação de par ou impa para adentrar as suas respectivas listas
        lista_par.append(num)
    elif num % 2 == 1:
        lista_impar.append(num)
lista_par.sort()                   # organização dos números em ordem crescente
lista_impar.sort()
lista_main.append(lista_par)
lista_main.append(lista_impar)     # adcionar as sequencias par e impar na lista principal
# exbição final
print(f'''{'-'*40}
{'lista de números pares e ímpares':^40}
{'-'*40}''')
print(f'\033[94m{lista_main}\033[m')   # obs se eu quiser separar a lista de par ou impar é so usar o
# print(lista[0]) par e lista lista[1] para impar  )

''' a explicação do curso foi bem mais simples pois ele ja declarou a lista no início assim : lista = [[].[]]
apois isso só foi comparar os números impares e pares na suas lista : lista[0] par e lista[1] para impar, essas foram
as maiores observações: https://youtu.be/2-fy24bbMJ4 '''