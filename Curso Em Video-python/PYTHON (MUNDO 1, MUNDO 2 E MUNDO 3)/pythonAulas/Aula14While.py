"""for c in range(1, 10):   # exemplo de como fazer a contagem em for in range
    print(c)
print('FIM')"""

'''c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')'''

'''for c in range(1, 5):
    n = int(input('Digite um numero: '))
print('fim')   nesse caso aqui eu tenho um limite de 5 repetições'''

n = 1
while n != 0:     # condição de parada
    n = int(input('Digite um número: '))   # nesse exemplo enquanto n for diferente de zero ele sempre irá se repetir.
print('FIM')

resp = 'S'     # nesse exemplo eu uso o s como uma condição para entrar no loop e utilizo ela para controlar o loop
while resp == 'S':
    numero = int(input('Digite um número: '))
    resp = str(input('Quer continuar [S/N]: ')).upper()
print('FIM')

n = 1        # exemplo de como fazer um contador de números digitados em par ou impar.
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} numeros pares e {impar} ímpares.')