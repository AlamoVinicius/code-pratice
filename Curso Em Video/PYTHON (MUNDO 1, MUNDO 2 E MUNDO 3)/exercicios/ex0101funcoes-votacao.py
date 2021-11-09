""" Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou
obrigatório nas eleições."""


def voto(year_born):
    from datetime import date
    idade = date.today().year - year_born
    if idade < 16:
        return f'Com idade {idade} voto é "NEGADO"'
    elif 16 <= idade < 18 or idade > 65:
        return f'com idade {idade} voto é "OPCIONAL'
    else:
        return f'Com idade {idade} voto é "OBRIGATÓRIO"'


# main programing
ano_nascimento = int(input('Digite o ano de nascimento: '))
print(voto(ano_nascimento))

