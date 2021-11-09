""" Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. no final do programa, moste:
- a média de idade do grupo
= qual é o nome do homem mais velho
quantas mulheres têm menos de 20 anos """
somaidade = 0      # primeiro de tudo é criar as váriaveis que irão receber os valores no loop
mediaidade = 0
idademaisvelho = 0
nomevelho = ''
totmulher = 0

for c in range(1, 5):    # aqui eu determino o numero de vezes que o loop será realizado e por onde começa e termina.
    print(f'----{c}ª PESSOA-----')      # print da posição da pessoa
    nome = str(input('Nome: ')).strip()        # entrada dos dados da pessoa desconsiderando os espaços
    idade = int(input('idade: '))
    sexo = str(input('Sexo M/F: ')).upper().strip()   # entrada do gênero desconsiderando letras mínusculas.
    somaidade += idade                 # soma acumulativa da idade dentro do loop
    if c == 1 and sexo in 'M':          # condição para substiuir as váriaveis zerada
        idademaisvelho = idade
        nomevelho = nome
    if sexo in 'M' and idade > idademaisvelho:   # condição para substituição da idade e nome do homem mais velho
        idademaisvelho = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:      # condição para o contador de mulheres abaixo de 20 anos
        totmulher += 1                  # contador da quantidade de mulheres caso cumpra a condição
mediaidade = somaidade / 4              # calculo da média de idade geral
print(f'A média de idade do grupo é {mediaidade} anos')            # apresentação final no output
print(f'O homem mais velho tem {idademaisvelho} e se chama: {nomevelho}')
print(f'O numero de mulheres são: {totmulher} com menos de 21 anos')
