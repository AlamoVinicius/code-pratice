""" Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar. No final, mostre:
a - quantas pessoas tem mais de 18 anos
b - quantos homens foram cadastrados.
c - quantas mulheres tem menos de 20 anos """

contador_maior_18 = 0
contador_mulher_menor20 = 0
contador_homens = 0
while True:   # loop
    print(f'''{"="*40}
          CADASTRE UMA PESSOA
{"="*40}''')
    idade = int(input('Idade: '))  # definir váriaveis
    sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]
    while True:
        if sexo != 'M' and sexo != 'F':
            sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]
        else:
            break
    if idade >= 18:   # lógica da programação
        contador_maior_18 += 1
    if sexo == "F" and idade < 20:
        contador_mulher_menor20 += 1
    if sexo == 'M':
        contador_homens += 1
    perg = input('Quer continuar? [S/N] ').upper().strip()[0]
    while True:
        if perg != 'S' and perg != "N":
            perg = input('Quer continuar? [S/N] ').upper().strip()[0]
        else:
            break
    if perg == 'N':
        break
print(f'''O total de pessoas com mais de 18 anos é : {contador_maior_18}      
O total de homens cadastro foi de: {contador_homens}
O total de mulheres com menos de 20 anos foi: {contador_mulher_menor20}''')   # exibição final

''' obs final: eu poderia ter usado para a validação de input o exemplo q o professor usou no canal vide aula, youtube
https://www.youtube.com/watch?v=4Ca6iRJo3M0 o while sexo not in 'MF': '''
