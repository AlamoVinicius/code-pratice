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