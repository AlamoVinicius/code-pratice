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
    print('Equipamento...: ', [indice+1])
    print('Nome..........: ', equipamentos[indice])
    print('Valor.........: ', valores[indice])
    print('Serial........:', seriais[indice])
    print('Departamento..:', departamentos[indice])

depreciacao = input('Digite o nome do equipamento que será depreciado em: ')
for indice in range(0, len(equipamentos)):
    if depreciacao == equipamentos[indice]:
        print(f'Valor antigo do equipamento: {valores[indice]}')
        valores[indice] *= 0.9
        print(f'Novo Valor: {valores[indice]}')
