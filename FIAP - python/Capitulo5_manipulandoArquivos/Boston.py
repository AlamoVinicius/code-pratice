with open("economic-indicators.csv", "r") as boston:
    total_voos = 0
    maiormesano = 0
    total_passageiros = 0
    maior_media_usuario = 0
    ano_usuarop = input("Qual ano deseja Pesquisar: ")
    for linha in boston.readlines()[1:-1]:
        lista = linha.split(",")
        total_voos = total_voos + float(lista[3])

        if float(lista[2]) > float(maiormesano):
            maiormesano = lista[2]
            ano = lista[0]
            mes = lista[1]
        if ano_usuarop == lista[0]:
            total_passageiros = total_passageiros + float(lista[2])
            if float(lista[5]) > float(maior_media_usuario):
                maior_media_usuario = lista[5]
                mes_maior_diaria = lista[1]
    print(f"O total de voos de todos os anos é: {total_voos}")
    print(f"O mês/ano de maior movimento no aeroporto foi: {str(mes)} / {str(ano)}")
    print(f"O total de passageiros do ano {ano_usuarop} foi de {total_passageiros}")
    print(f"O mês do ano {ano_usuarop} com maior média diária de hotel foi: {mes_maior_diaria}")

    """pesquisando o maior mes/ano  que possui a maior taxa de ocupaççao de vagas
    nos hóteis de boston de acordo com nosso banco de dados da coluna hotel_ocup_rate em porcentagem"""
    with open("economic-indicators.csv", "r") as boston:
        maior_tx_ocupacao = 0
        for linha in boston.readlines()[1:-1]:
            lista = linha.split(",")
            if float(lista[4]) > float(maior_tx_ocupacao):
                maior_tx_ocupacao = float(lista[4])
                ano = (lista[0])
                mes = (lista[1])
        print("==========maior porcentagem de ocupação mês/ano==========")
        print(f"A maior porcentagem de taxa de ocupação foi de: {maior_tx_ocupacao} no mês: {mes} do ano de {ano}")

    """pesquisando mês/ano onde ocorre a menor taxa de desemprego em boston observando a coluna a coluna [7] 
    unemp_rate"""
    with open('economic-indicators.csv') as boston:
        menor_tx_desemprego = 100
        for linha in boston.readlines()[1:-1]:
            lista = linha.split(',')
            if float(lista[7]) < float(menor_tx_desemprego):
                menor_tx_desemprego = float(lista[7])
                anotx = (lista[0])
                mestx = (lista[1])
        print(f'A menor taxa de desemprego foi: {menor_tx_desemprego} do mês {mestx} de {anotx}')

