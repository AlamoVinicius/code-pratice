""" aula sobre lista 18 repare como as listas podem ser incluidas dentro de uma lista. """

teste = []
teste.append('Álamo')
teste.append(26)
galera = []
galera.append(teste[:])   # é preciso fazer uma cópia com [:] para o sistema não duplicar
teste[0] = 'Francielli'
teste[1] = 22
galera.append(teste)
print(galera[:])
" another way"
galera2 = [['joão', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera2[0])   # desse modo eu mostro apenas o elemento 0 da principal lista
print(galera2[0][0])   # desse modo eu mando mostrar apenas o elementeo 0 da lista 0
print('usando o for para mostrar as os dados')
for p in galera2:
    print(p[0])

galera3 = []
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera3.append(dado[:])   # cuidado pra nçao esquecer do [:] pois ele cria uma cópia dos dados, se não eu apagaria
    # as duas listas
    dado.clear()   # aqui eu limpo a lista dado
print(galera3)

for dados in galera3:   # somar maiores de idade
    if dados[1] >= 21:   # se o dado 1 [idade]
        print(f'{dados[0]} é maior de idade. ')
        totmai += 1
    else:
        print(f'{dados[0]} é menor de idade ')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade. ')