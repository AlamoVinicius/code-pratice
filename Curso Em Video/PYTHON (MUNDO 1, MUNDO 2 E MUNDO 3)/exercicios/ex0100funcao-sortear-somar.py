""" Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e
somaPar(). A primeira funão vai sortear 5 números e vai colocá-los dentro da lista e a segunda função
vai mostrar a soma entre todos os valores PARES sorteados pela função anterior."""
from random import randint
from time import sleep


def sorteio(lista):
    print('Gerando 5 valores da lista: ', end='')
    for c in range(0, 5):
        num = randint(1, 100)
        lista.append(num)
        print(num, end=' ')
        sleep(0.3)
    print('\n5 números gerados com sucesso! ')


def soma_par(lista):
    sompar = 0
    for numero in lista:
        if numero % 2 == 0:
            sompar += numero 
    print(sompar)


numeros = []
sorteio(numeros)
print(f'A soma dos números pares é: ', end='')
soma_par(numeros)
