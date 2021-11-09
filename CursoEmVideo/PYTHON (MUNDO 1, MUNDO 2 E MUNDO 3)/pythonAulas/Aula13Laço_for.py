for c in range(0, 6):   # aqui eu estou usando um laço com range limitado a 6 x então tudo que estiver dentro do bloco
# irã acontecer 6x perceba comom é simples.
    print('FIM')
    print(c)   # mandando printar o que está dentro da váriavel ele conta os numeros de x

print(f'{"Contando em decrescente":=^50}')
for c in range(6, 0, -1):   # colocando o - 1 aqui eu faço o programa contar invertido
    print(c)

print(f'{"mostrando exemplo de passo 2":=^50}')
for c in range(0, 10, 2):   # no numero 2 eu especifico os passos para o meu programa contar em 2 e 2.
    print(c)

''' fazendo o programa contar o numero determinado por mim exemplo:'''

n = int(input('Digite um número para contar até ele: '))
for c in range(0, n+1):   # o n+1 foi para não contar um número a menos
    print(c)


''' observe que você pode utilizar as variaveis dentro do range ao invés de numero pré estabelecidos'''

s = 0
for c in range(0, 4):               # realizando um contador
    n = int(input("Digite um número para realizar ir somando: "))
    s += n           # método em python q eu posso simplificar o contador
print(f'O somatório é {s}')
print('FIM')
