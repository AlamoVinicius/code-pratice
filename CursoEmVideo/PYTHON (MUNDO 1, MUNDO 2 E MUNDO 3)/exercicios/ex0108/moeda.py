def aumentar(x=0, porc=0):
    rtn = x + (x * porc / 100)
    return rtn


def diminuir(x=0, porc=0):
    rtn = x - (x * porc / 100)
    return rtn


def dobrar(x=0):
    x *= 2
    return x


def metade(x=0):
    x /= 2
    return x


def moeda(x=0, moeda='R$'):
    return f'{moeda}{x:.2f}'.replace('.', ',')
