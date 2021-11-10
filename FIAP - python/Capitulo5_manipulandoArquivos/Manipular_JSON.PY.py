# logo abaixo estou importanto arquivo json
import json
import os   # aqui eu verifico se o arquivo ja existe ou não
if os.path.exists('inventaio_json.json'):
    with open('inventaio_json.json', 'r') as arq_json:
        inventario = json.load(arq_json)  # método load dentro do json descarrega o conteudo do arquivo na váriavel
else:
    inventario = {}
opcao = int(input('Digite: '
                  '<1> para registrar ativo '
                  '<2> para exibir ativos '))  # aqui eu criei minha chamada de operaçao
while 0 < opcao < 3:  # aqui eu crio meu loop para poder controlar a adição de inventário
    if opcao == 1:
        resp = "S"
        while resp == "S":
            inventario[input("Digite o numero patrimonial: ")] = [
                input('Digite a data da última atualização: '),
                input('Digite a descrição: '),
                input('Digite o departamento: ')]
            resp = input('Digite <S> para continuar: ').upper()  # aqui é o controlador para finaizar meu loop
        with open('inventaio_json.json', 'w') as arq_json:   # manipulação de arquivo json
            json.dump(inventario, arq_json)      # método dump do json garante os 2 paramètros de abertura
        print('JSON gerado!!!!')
    elif opcao == 2:
            for chave, dado in inventario.items():   # aqui estou percorrendo meus arquivos e seus dados nos dicionáios
                print(f'Data..........:{dado[0]}')   # aqui eu inicio minha formatação para uma melhor visualização do
                print(f'Descrição.....:{dado[1]}')   # usuário final.
                print(f'Departamento..:{dado[2]}')
    opcao = int(input('Digite: '                     # aqui é onde eu starto novamento minha possibilidade de ações.
                      '<1> para registrar ativo'
                      '<2> para exibir ativos '))
