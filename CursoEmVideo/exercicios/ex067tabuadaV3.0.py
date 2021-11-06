""" Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo. """

# exibição da tabuada
while True:
    # entrada do número para exibir a tabuada
    n = int(input('Digite o número para para exibir a tabuada ou qualquer valor negativo para sair: '))
    if n < 0:
        break
    print(f'{"=" * 40}')
    print(f'Exibindo a tabuada do número {n}')
    print(f'{"=" * 40}')
    if n > 0:
        controlador = 0
        while controlador < 10:
            controlador += 1
            produto = n * controlador
            print(f'{n} x {controlador} = {produto}')

# print final do programa
print('Tabuada encerrada, volte sempre!')

''' eu poderia usar o meu for para fazer a tabuada mas como a aula é sobre while e break eu usei o while;
exemplo de como ficaria com o for:
#for c in range(1, 11):
        #produto = n * c
        #print(f'{n} x {c} = {produto}')'''