def aumentar(x, porc):
    x = x + (x * porc / 100)
    return x


def diminuir(x, porc):
    x = x - (x * porc / 100)
    return x


def dobrar(x):
    x *= 2
    return x


def metade(x):
    x /= 2
    return x
