""" Melhore o jogo do desafio 28 onde o computadr vai 'pensar' em um número ebtre 0:10. só que agora o jogador
 vai tentar adivinhar até acertar. mostrando no final quantos palpites foram necessários para vencer"""
from random import randint
jogadapc = randint(1, 10)
jogadaplayer = 0
contador = 0
while jogadaplayer != jogadapc:
    contador += 1
    jogadaplayer = int(input("tente adivinhar um numero entre 1 e 10 que o computador pensou: "))
print(f'Parabéns!!! acertou, você precisou de {contador} tentativas :D')


''' resolução do curso: '''


jogadapc = randint(1, 10)
print('''Sou seu computador acabei de pensar em um número entre 0 e 10 será que você consegue adivinhar?''')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == jogadapc:
        acertou = True
print(f'Acertou com {palpites} tentativas. Parabéns')

