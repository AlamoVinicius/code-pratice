""" Crie um programa que simule o funcionamento de um caixa eltrônico. No iníco , pergunte ao usuário qual será
o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
obs Considere que o caixa possui cédulas de 50, 20, 10 e 1 """
print('='*40)
print(F'{"BANCOS ALAMO":^40}')
print('='*40)
valor = int(input('Digite o valor que será sacado: '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:    # SE VALOR TOTAL FOR MAIOR QUE A CÉDULA ATUAL
        total -= ced    # TOTAL VAI SER - CÉDULA NA RODADA DO LOOP
        totced += 1     # CONTADOR DA QUANTIDADE DA CÉDULA
    else:
        if totced > 0:    # CONDIÇÃO PARA IMPRIMIR A MSG FINAL
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:    # SE A CÉDULA FOR IGUAL AO VALOR DETERMINADO NO SCRIPT Q NO CASO COMEÇA COM 50
            ced = 20     # O VALOR DA CÉDULA TROCA E O LOOP REPETE
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break

