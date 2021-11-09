""" Escreva um programa que faça o computador 'Pensar' em um número inteiro entre valor determinado
e peça para que o usuário tente descobrir qual foi o número escolhido pelo computador. O programa deverá
escrever na tela se o usuário ganhou ou perdeu."""

from random import randint
'''numero = randint(0, 5)
escolha = int(input('Escolha um numero de 0 a 5 para tentar adivinhar: '))
if numero == escolha:
    print('Parabens acertou!!!')
else:
    print('Tente outra vez.') '''


""" Posso tambem montar um jogo dentro de uma estrutura de WHILE para que eu não precise empre ficar reiniciando o
jogo e tmb da algumas dicas para facilitar em caso de valores maiores, observe: """

question = input('Would you like to do it now? "PLAY" to play the game or "NOTHING" to leave. ').upper()
print('Bem vindo!! vocÊ tem 5 tentativas para tentar acertar ao numero:\nDiz a lenda que se vc acertar nessas'
      ' 5 tentativas, sua sorte está em dia e vc pode jogar na Mega sena! XD\nBoa sorte!')


if question == 'PLAY':
    playgame = 0
    n = randint(0, 100)
    print(n)
    while playgame < 5:
        playgame = playgame + 1
        choise = int(input('Tente adivinhar um numero entre 0 e 100: '))
        if choise == n:
            print('Parabens acertou!!! Vá imediamente jogar na loteria! XD')
            exit()
        elif choise > n:
            print('O numero é menor que o escolhido.')
        else:
            print('o numero é maior que o escolhido.')
    print(f'O numero da vez era {n} boa sorte na sua próxima tentativa.')
    print('Não foi dessa vez!! fique longe da loteria em! :D')
else:
    exit()



