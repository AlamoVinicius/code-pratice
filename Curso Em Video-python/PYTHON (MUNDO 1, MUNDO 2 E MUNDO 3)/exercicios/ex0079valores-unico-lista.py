""" Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista
caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
digitados em ordem crescente."""
lista = []
resp = 'S'
while resp == 'S':
    num = int(input('Digite um valor: '))
    if num in lista:
        print('Número já existe! não adicionado!')
    else:
        lista.append(num)
        print('Número adicionado com sucesso!')

    resp = input('Digite "S" para adicionar mais um número: ').upper().strip()[0]
    lista.sort()    # aqui eu modifico e coloco minha lista em ordem crecente o sorted eu só exibo
print(f'{"-"*10}Exibindo os números em ordem crescente{"-"*10} \n{lista}')

''' na resolução do progessor do curso ele usou while True e comparou usando o if num not in lista, mais o resultado
é o mesmo então continuo com minha solução.'''
