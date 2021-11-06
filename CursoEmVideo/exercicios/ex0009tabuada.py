numero = int(input('Digite um numero para exibir a tabuada: '))
for valor in range(1, 11, 1):
    print(f'{numero} x {valor} = {numero * valor}')
# Detalhes importantes, se não colocar o int no input o resultado de valor será a quantidade de vezes
# que o valor será exibido por exemplo: 2 x 10 = 2222222222
