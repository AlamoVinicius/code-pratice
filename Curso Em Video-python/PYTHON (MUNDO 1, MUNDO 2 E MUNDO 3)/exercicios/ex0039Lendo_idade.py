""" faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
se ele ainda vai se alistar no serviço militar ; se é a hora de se alistar ; se já passou do tempo de alistar.
programa deve também mostrar o tempo que falta ou que passou do prazo """
import datetime    # biblioteca usada para o programa
ano_sys = datetime.date.today().year    # biblioteca e seu método para extrair o ano atual do sistema.
ano_nascimento = int(input('Digite o ano de nascimento: '))   # entrada do ano de nascimento em inteiro
soma = ano_sys - ano_nascimento     # calculo da idade para usar nas conidções.

if soma == 18:
    print('Está na hora de se alistar. ')
elif soma > 18:
    print(f'Já passou da hora de se alistar! já era pra ter se alistado a {soma - 18} anos atrás.')
else:
    print(f'Ainda não precisa se alistar, faltam {18 - soma} anos para poder se alistar. ')

