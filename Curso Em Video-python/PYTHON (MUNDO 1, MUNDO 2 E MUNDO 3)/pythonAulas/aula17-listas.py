num = [2, 5, 9, 1]   # exemplo de substituição de um elemento da lista
num[2] = 3
num.append(7)   # pra adicionar tenho q usar o método append
num.sort()    # aqui eu ordendo em crescente
print(num)
num.sort(reverse=True)   # aqui eu coloco em ordem decrescente
print(num)
print(f'essa lista tem {len(num)} elemntos')    # função len retorna a quantidade de elementos
num.insert(2, 0)   # com o método insert, eu consigo inserir um valor na posição 2, o número 0
print(num)
num.pop(2)    # pop sem nenhum parâmetro ele elimina o último elemento, se eu colocar um número dentro ele elimina
# o da posição definida
print(num)
num.insert(2, 2)   # aqui eu adicionei outro 2 na posição 2
if 5 in num:
    num.remove(5)    # aqui eu elimino o núm 2 na primeira ocorrência observe
else:
    print('número 4 inexistente ')
print(num)
print('-------------outro jeito ---------------')
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for v in valores:
    print(f'{v}...', end='')

print(f'\n{"-"*10}{"melhor organização":^20}{"-"*10}')
for c, v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v}!')
print('cheguei ao fim da lista. ')

a = [2, 3, 4, 7]    # se eu alterar um número na lista b, as duas listas são alteradas pq criei uma ligação
b = a[:]      # se eu colocar o a dentro de colchetes [:] ai sim eu crio uma cópia e não altero as 2 listas
b[2] = 8
print(f'lista A: {a}')
print(f'lista B: {b}')