""" Crie um programa que leia dois valores e mostre um menu na tela: [1] somar [2] multiplicar [3] maior
[4] novos números [5] sair do programa / seu programa deverá realizar a operação solicitada em cada caso."""
from time import  sleep
n1 = int(input('Digite o primerio valor: '))
n2 = int(input('Digite o segundo valor: '))
choise = 0
resultado = 0     # estou definindo um a variavel para usar dentro do menu
print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')

while choise != 5:            # condição para o while estár ativo
    choise = int(input('Escolha a opção que deseja: '))  # aqui defino a escolha para o usuário entrar no while
    if choise == 1:           # bloco de execução dentro da condição 1
        resultado = n1 + n2
        print(resultado)

    elif choise == 2:          # bloco de execução dentro da condição 2
        resultado = n1 * n2
        print(resultado)

    elif choise == 3:   # bloco de execução dentro da condição 3/ obs; verificar o que fazer caso tenha mais q 4 números
        if n1 > n2:    # posso verificar o exercício 55 para etender essa situação
            resultado = n1
        else:
            resultado = n2
        print(resultado)

    elif choise == 4:      # bloco de execução para entrada de novos valores.
        n1 = int(input('Digite o primerio valor: '))
        n2 = int(input('Digite o segundo valor: '))
        print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
    elif choise == 5:
        print('finalizando...')
    else:
        print('Opção inválida.')
    sleep(1)
print('Bye!')

''' meu programa estava muito bom, então não vi a necessidade de alterar de acordo com a resolução do curso, porem eu 
poderia exibir melhor os prints das escolhas. mas ta ok deu pra aprender.'''