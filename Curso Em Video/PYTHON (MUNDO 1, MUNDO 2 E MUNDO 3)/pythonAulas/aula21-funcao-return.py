def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')   # usando a função com retorno de valor (return)
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}. {f2} e {f3}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número para saber se é par: '))
print(par(num))   # modo de usaar função como True or false
if par(num):      # também pode fazer uma verificação
    print('É par!')
else:
    print('Não é par!')