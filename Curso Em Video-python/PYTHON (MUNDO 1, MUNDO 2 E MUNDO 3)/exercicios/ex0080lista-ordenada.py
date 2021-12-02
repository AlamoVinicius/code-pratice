""" Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista. já
 na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela."""


lista = []
for c in range(0, 5):
    num = int(input('Digite um número: '))   # entrada de 5 váriaveis na lista
    if c == 0 or num > lista[-1]:    # se c for igual a 0 ou o num for maior que o último da lista (-1)
        lista.append(num)            # adicionamos o numero no final da lista
        print('Número adicionado ao final da lista!')
    else:
        posicao = 0
        while posicao < len(lista):   # enquanto posicao for menor que a quantidade de elementos da lista
            if num <= lista[posicao]:  # se o num for menor ou igual ao numero da lista indicada na posicao
                lista.insert(posicao, num)  # ai sim ele adiciona o número digitado
                print(f'Número adicionado na posição {posicao}')   # indicador da posição que o número foi adicionado
                break   # break se a condição for cumprida
            posicao += 1   # controlador

print(f'Você digitou os números: {lista}')

