def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except ValueError:
            print('\033[31mERROR, valor inválido, Digite somente números inteiro: \033[m')
            continue  # continue volta para o loop
        except KeyboardInterrupt:
            print('Programa finalizado com sucesso!')
            continue
        else:
            return num


def linha(tam=42):
    return '=' * tam


def cabecalho(txt): 
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[93m{c}\033[m - \033[94m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[95mSua opção:\033[m')
    return opc


