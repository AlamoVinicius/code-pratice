nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))
doenca_infectocontagiosa = input('Suspeita de doença infectocontagiosa?: ').upper()
while doenca_infectocontagiosa != 'SIM' and doenca_infectocontagiosa != 'NAO':
    print("Digite SIM ou NAO ")
    doenca_infectocontagiosa = input('Suspeita de doença infecto-contagiosa? ').upper()
if doenca_infectocontagiosa == 'SIM':
    print('Encaminhe o paciente para a sala AMARELA')
else:
    print('Encaminhe o paciente para a sala BRANCA')
if idade >= 65:
    print('Paciente com prioridade')
else:
    genero = input('Digite o gênero do paciente: ').upper()
    if genero == 'FEMININO' and idade > 10:
        gravidez = input('A paciente está gravida?: ').upper()
        if gravidez == 'SIM':
            print('Paciente COM prioridade')
        else:
            print('Paciente  prioridade')
    else:
        print('Paciente SEM prioridade')
