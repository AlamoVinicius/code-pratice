""" Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
a digitar valores . """
resp = 'S'    # váriaveis de controlador do loop
contador = 0
somador = 0
maior = 0
menor = 0
print('Bem vindo ao analisador de média, maior e menor número.')    # apresentação de boas vindas
while resp == 'S':            # condição para o loop
    n = int(input('Digite um número: '))    # entrada do número que irá ser analisado
    somador += n                           # somador acumulador dos números
    contador += 1                          # contador da quantidade de números insiridos para a realização do calculo
    if contador == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    resp = input('Deseja digitar mais números? [S/N]: ').upper().strip()    # controle do loop
media = somador / contador                                        # calculo da média
print(f'você digitou {contador} números. A média total dos valores digitado foi {media:.1f}')    # exibição final
print(f'O número maior digitado foi {maior} e o menor foi {menor}')
