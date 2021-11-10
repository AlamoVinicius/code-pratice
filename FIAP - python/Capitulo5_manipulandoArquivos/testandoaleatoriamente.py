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
