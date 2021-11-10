from funcoes.funcoes_Arquivos import *

inventario = {}
opcao = chamarmenu()
while 0 < opcao < 4:
    if opcao == 1:
        registrar(inventario)
    elif opcao == 2:
        persistir(inventario)
    elif opcao == 3:
        resultado = exibir()
        for linha in resultado:
            # nesse print eu usei o find para percorrer a str logo após o "/"
            print(linha[linha.find(";") + 1:-1])
            # nesse eu usei o slice cortei minha lista pelas caracteres.
            print(linha[2:-1])
            # another method
            print(f"{linha[2:-1]} and {linha[linha.find(';')+1:-1]}")
        for linha in resultado:
            lista = linha.split(";")
            print(f"data..........:{lista[1]}")
            print(f"Descrição.....:{lista[2]}")
            print(f"Departamento..:{lista[3]}")
    opcao = chamarmenu()
