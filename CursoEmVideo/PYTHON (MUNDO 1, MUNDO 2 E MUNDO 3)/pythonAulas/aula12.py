nome = str(input("Qual é o seu nome: "))
if nome == 'Álamo':
    print('Great name!!')
elif nome == 'Pedro' or nome == "Maria" or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('your name is a comum name.')
print(f'Have a nice Day {nome}')