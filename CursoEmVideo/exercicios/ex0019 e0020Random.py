from random import choice, shuffle
nomes = []
resposta = 'S'
while resposta == "S":
    nomes.append(input('Digite um nome que participará do sorteio: '))
    resposta = input('Digite "S" para inserir mais um nome no sorteio ou enter para finalizar: ').upper()
print(nomes)
print(f'O nome escolhido foi: {choice(nomes)}')

''' O mesmo professor Gostaria de sortear a ordem dos alunos etnão o código ficaria desse modo:'''
shuffle(nomes)
print(f'A ordem de apresentação é: {nomes}')
