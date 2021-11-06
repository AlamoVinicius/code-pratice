def leia_dinheiro(txt):
    """
    ==> Essa função irá validar número em formatos de dinheiro (BRL)
    :param txt: valor que irá ser formatado.
    :return:  float de txt.
    """
    valido = False
    while not valido:
        entrada = str(input(txt)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO:\"{entrada}\"valor inválido.\033[m')
        else:
            valido = True
            return float(entrada)


def leiaint(txt):
    """
    ==> essa função irá validar apenar um número inteiro.
    :param txt: irá receber o valor em string para converter em inteiro, se não ira receber um erro
    :return:   irá retornar o valor de str em um número inteiro
    """
    while True:
        num = input(txt).strip()
        if num.isnumeric():
            num = int(num)
            break
        else:
            print(f'\033[91mErro! digite apenas um número válido\033[m')
    return num
