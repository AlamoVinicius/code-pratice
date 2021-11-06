""" Faça um programa que calcule a soma entre todos os núemros impares que são múltiplos de três e que se encontram no
intervalo de 1 até 500"""
print('mostrando a soma total  dos numeros impares divido por 3 entre 1 e 500: ')
contador = 0
s = 0
for c in range(1, 501): # selecionando os números que serão avaliados posso usar váriaveis inputadas no lugar
    contador += 1
    if c % 2 == 1:         # separando os números impares
        if c % 3 == 0:     # separandos os núemros ímpares divido por 3
            s += c         # somando os númeos toda as vezes que o loop for acontece
print(s)                   # exibindo resultado final
print(contador)            # repare que nesse modo o script realizou 500x o loop
""" vou fazer agora com um contador e com menos processamento: """
soma = 0
count = 0
for c in range(1,501,2):
    count += 1
    if c % 3 == 0:
        soma += c

print(f'a soma de todos os  é {soma}')
print(count)             # repare que aqui foram só 250 x o lop consumindo menos processamento.



