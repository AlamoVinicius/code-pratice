def soma(a, b):
    print(f'a = {a} e b = {b}')   # definição da minha função soma para usar no programa principal
    s = a + b
    print(f'A soma de A + B = {s}')


# programa principal
soma(b=4, a=5)   # a ordem pode ser alterada no parâmentro
soma(8, 9)
soma(2, 1)

'''é possivel passar vários parâmentros usando o "*", desta forma empacotamos tudo dentro da minha váriavel da função
empacotando todos os valores em uma tupla'''


def contador(* num):
    tam = len(num)
    print(tam)


contador(1, 2, 1, 4, 3, 2)
contador(2, 4)

print('=' * 30)
print(f'{"another way":^30}')
print('=' * 30)
# tambem posso trabalhar com listas:


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [1, 3, 4, 6, 5]
dobra(valores)     # criei uma função que dobra todos os valores da lista ocmo pode ser percebido
print(valores)

# soma de vários valores usando o *


def soma_varios(* numbers):
    s = 0
    for num in numbers:
        s += num
    print(f'somando os valores {numbers} temos o total de {s}')


soma_varios(2, 3, 4, 5, 1)
