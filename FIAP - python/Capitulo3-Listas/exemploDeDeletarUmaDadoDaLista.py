# exemplo de deletar arquivos dentro da lista utilizando o del e o break resumo em arquivo word.
equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = 'S'
while resposta == 'S':
    equipamentos.append(input('Equipamento: '))
    valores.append(float(input('Valor: ')))
    seriais.append(int(input('Serial: ')))
    departamentos.append(input('Departamentos: '))
    resposta = input('Digite "S" para continuar: ').upper()

for indice in range(0, len(equipamentos)):
    print('Equipamento...: ', [indice + 1])
    print('Nome..........: ', equipamentos[indice])
    print('Valor.........: ', valores[indice])
    print('Serial........:', seriais[indice])
    print('Departamento..:', departamentos[indice])

serial = int(input("Digite o serial do equipamento que será excluido: "))
for indice in range(0, len(departamentos)):
    if seriais[indice] == serial:
        del departamentos[indice]
        del equipamentos[indice]
        del seriais[indice]
        del valores[indice]
        break

for indice in range(0, len(equipamentos)):
    print("Equipamento..: ", (indice + 1))
    print("Nome.........: ", equipamentos[indice])
    print("Valor........: ", valores[indice])
    print("Serial.......: ", seriais[indice])
    print("Departamento.: ", departamentos[indice])
