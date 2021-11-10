inventario = []
resposta = 'S'
while resposta == 'S':
    equipamento = [input('Equipamentos: '),
                   float(input('Valor: ')),
                   int(input('Número de Serial: ')),
                   input("Departamento: ")]
    inventario.append(equipamento)
    resposta = input('Digite "S" para continuar: ').upper()

for elemento in inventario:
    print(f'Nome...........: {elemento[0]}')
    print(f'valor:.........:{elemento[1]}')
    print(f'Serial.........:{elemento[2]}')
    print(f'Departamento....:{elemento[3]}')

busca = input('Digite o nome do equipamento que deseja buscar: ')
for elemento in inventario:
    if busca == elemento[0]:
        print(f'valor..:{elemento[1]}')
        print(f'Serial.?{elemento[2]}')

depreciacao = input('Digite o nome do equipamento que será depreciado: ')
for elemento in inventario:
    if depreciacao == elemento[0]:
        print(f'Valor antigo: {elemento[1]}')
        elemento[1] *= 0.9
        print(f'Novo Valor: {elemento[1]}')

serial = int(input('Digite o numero do Serial que será excluido: '))
for elemento in inventario:
    if elemento[2] == serial:
        inventario.remove(elemento)

for elemento in inventario:
    print(f'Nome...........: {elemento[0]}')
    print(f'valor:.........:{elemento[1]}')
    print(f'Serial.........:{elemento[2]}')
    print(f'Departamento....:{elemento[3]}')

valores = []
for elemento in inventario:
    valores.append(elemento[1])
if len(valores) > 0:
    print(f'O equipamento mais caro custa{max(valores)}')
    print(f'O equipamento mais barato custa: {min(valores)}')
    print(f'O total de equipamentos é de: R${sum(valores)} ')
