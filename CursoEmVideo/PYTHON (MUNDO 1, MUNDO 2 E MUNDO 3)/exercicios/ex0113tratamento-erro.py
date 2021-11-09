"""Reescre a função leiaint() que fizemos no desafio 104, incluindo agora a possibilidade da digitação
de tipo inválido. Aproveite e crie também uma função leiafloat() com a mesma funcionalidade. """


def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except ValueError:
            print(
                '\033[31mERROR, valor inválido, Digite somente números inteiro: \033[m')
            continue   # continue volta para o loop
        except KeyboardInterrupt:
            print('Programa finalizado com sucesso!')
            continue
        else:
            return num


def leiafloat(msg):
    while True:
        try:
            num = float(input(msg))
        except ValueError:
            print(
                '\033[31mERROR, valor inválido, Digite somente números inteiro: \033[m')
            continue
        else:
            return num


n = leiaint('Digite um número inteiro: ')
r = leiafloat('Digite um número Decimal: ')
print(f'Valores digitados: {n} e {r}')
