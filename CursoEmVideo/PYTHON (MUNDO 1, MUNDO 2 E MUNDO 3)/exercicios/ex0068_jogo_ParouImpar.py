"""FAça um programa que jogue par ou impar com o computadr. O jogo só será interrompido quando o jogador PERDER,
mostrando o total de vitórias consecutivas que conquistou no final do jogo"""
from random import randint

print(f'''{"-=" * 20}
PAR OU IMPAR
{"-=" * 20}''')
contador = 0
while True:
    jogadapc = randint(0, 10)  # entrada das váriaveis
    while True:     # aqui eu fiz um input pra validação em caso de tipo de dado errado. não era obrigatório mas ok
        try:
            jogadaplayer = int(input('Escolha um número: '))
        except ValueError:
            print('jogada inválida')
        else:
            break
    par_impar = str(input('par ou impar? [P/I]: ')).strip().upper()
    soma = jogadapc + jogadaplayer

    if par_impar == 'P':  # lógica do programa
        if soma % 2 == 0:
            print(f'você jogou: {jogadaplayer} e o computador jogou {jogadapc} total = {soma} (PAR)')
            print('VOCÊ VENCEU!')
        else:
            print(f'você jogou: {jogadaplayer} e o computador jogou {jogadapc} total = {soma} (impar)')
            print('VOCÊ PERDEU!')
            break

    elif par_impar == 'I':
        if soma % 2 == 0:
            print(f'você jogou: {jogadaplayer} e o computador jogou {jogadapc} total = {soma} (PAR)')
            print('VOCÊ PERDEU!')
            break
        else:
            print(f'você jogou: {jogadaplayer} e o computador jogou {jogadapc} total = {soma} (impar)')
            print('VOCÊ VENCEU!')
    else:
        print('jogada inválida')
    contador += 1

print(f'Você ganhou {contador} vezes consecutivas.')  # exibição final

'''O resultado do professor deu menos e linha e um pouco de diferença na lógica mas nada tão importante pode conferir
no curso em video a resolução desse exercício'''