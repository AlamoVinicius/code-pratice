""" Refaçã o Desafop 051, lendo o primeiro termo e a razão de uma pa mostrando os 10 primeiros termos da progressão
usando a estrutura while."""
termo1 = int(input('Digite o primeiro termo da p.a: '))   # entrada do valor da prmeira posição da PA
razao = int(input("Digite a razão da p.a: "))    # entrada da razão da P.A
termo = termo1       # aqui eu crio uma nova variável recebendo o valor do primeiro termo
controlador = 1      # aqui eu crio uma váriavel de controla para meu loop
print('Exibindo os 10º valores da P.A:')
while controlador <= 10:     # aqui eu defino o limite do meu loop
    print(termo, end=' - ')    # aqui eu exibi minha P.A dentro do meu loop
    termo += razao           # aqui é a equação da PA
    controlador += 1         # aqui eu colocoo controlador + 1 para ele se tornar true e finalizar o loop dps de 10 x
print('fim')
