""" Desenvola um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
se o valor digitado for impar, desconsidere-o"""
s = 0
contador = 0
for c in range(1, 7):
    numeros = int(input(f'Digite o {c} número para soma-lo só irão ser considerado os pares: '))
    if numeros % 2 == 0:    # aqui eu só considero os números pares para a condição do if
        s += numeros        # essa soma só irá ser realizada de acordo com a condição do if anterior dentro de outro if
        contador += 1
print(f'Você informou {contador} pares, A soma dos números pares digitados é {s}')
