def aumentar(x=0, porc=0, cvsao=False):
    """
    ==> (EN-US) increasses the value by a set percentage.
    :param x: Value that will receive the change
    :param porc: percentage value that will change x value
    :param cvsao: option if you want to show the converted value
    :return: return the percentagem of the value, with or whithout conversion to local currency.
    """
    rtn = x + (x * porc / 100)
    return rtn if cvsao is False else moeda(rtn)


def diminuir(x=0, porc=0, cvsao=False):
    """
    ==> (PT-BR) Diminui o valor de x na porcentagem definida.
    :param x:  Valor que irá ser depreciado
    :param porc: Valor da porcentagem que irá calcular sobre x
    :param cvsao: (opcional) se deseja ou não retornar o valor convertido na moeda local (BRl)
    :return: retorno do valor depreciado, com ou não conversão para moeda local
    """
    rtn = x - (x * porc / 100)
    if cvsao:
        rtn = moeda(rtn)
    return rtn


def dobrar(x=0, cvsao=False):
    """
    ==> Dobra o valor de x.
    :param x: valor recebido.
    :param cvsao: opcional, se deseja ou não exibir o valor convertido em moeda local
    :return: retorna o valor dobrado de x convertido ou não em moeda local.
    """
    x *= 2
    if cvsao:
        x = moeda(x)
    return x


def metade(x=0, cvsao=False):
    """
    ==> Divide o valor de x pela metade
    :param x: valor recebido.
    :param cvsao: (opcional) Se deseja ou não exibir o valor convertido em moeda local
    :return: valor de x pela metade com ou não conversão para moeda local.
    """
    x /= 2
    if cvsao:
        x = moeda(x)
    return x


def moeda(x=0.0, moeda='R$'):
    """
    ==> Formata valor de x para f'string de moeda local (BRL).
    :param x: Valor que será formatado.
    :param moeda: Cifrão da moeda local (BRL).
    :return: retorna f'string formatada para moeda local (BRL).
    """
    return f'{moeda}{x:.2f}'.replace('.', ',')
