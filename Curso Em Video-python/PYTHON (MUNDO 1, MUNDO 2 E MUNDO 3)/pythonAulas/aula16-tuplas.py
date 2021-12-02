""" Aula completona de tuplas """

lanche = ('Hambúrguer', 'suco', 'pizza', 'pudim')
print(lanche)    # tuplas são imutáveis
print(lanche[1])     # formas de manipular uma tupla execute o programa para observar o output
print(lanche[0])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(len(lanche))    # exibi a quantidade de elementos na váriavel composta
print(sorted(lanche))   # a tubla usando o sorted para exibir em ordem

for cont in range(0, len(lanche)):   # exibir a contagem dos numeros
    print(f'usando o len no for {lanche[cont]} posição {cont}')

for pos, comida in enumerate(lanche):   # usando o enumarete para numerar as posições da tupla
    print(f'usando o for sem o len {comida} na posição {pos}')
    # usando o for para percorrer a lista na váriavel comida
print('comi demais!')

# tubla com int
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b   # usando esse operador eu não somo mas simplismente junto as tuplas
print(c)
print(len(c))   # mostra o numeros de elementos
print(c.count(5))   # mostra quantas vezes tem o número 5 ou outro da minha escolha
print(c.index(8))   # exibe a posição de onde está o elemnto 8
print(c.index(2, 5))   # começo em outra posição as contagem

pessoa = ('alamo', 39, 'M', 99.00)   # eu posso colocar mais de um tipo de dado dentro das tuplas
print(pessoa)
del pessoa   # posso mandar deletar toda a tupla mas não posso deletar um elemento dentro da tupla
print(pessoa)   # msg de erro é exibida aqui pois a tupla já foi deletada.
