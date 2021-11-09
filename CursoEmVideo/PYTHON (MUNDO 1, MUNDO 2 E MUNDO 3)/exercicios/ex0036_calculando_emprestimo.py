""" Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar
o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode excedr 30% do salário ou então o empréstimo será
 negado. """

valor_casa = float(input('Digite o valor da casa: R$'))   # entrada do valor total da casa
qtd_juros = float(input('Digite a porcentagem de juros ao ano: '))   # valor dos juros por ano
qts_year_fina = float(input('Digite a quantidade de anos que irá ser realizado o financiamento: '))
salario = float(input('Digite o salário do interessado: R$'))     # renda do comprador
valor_casa = valor_casa + valor_casa * (qtd_juros * qts_year_fina/100)    # calculo para saber o valor total da casa
# c/juros
prest_mensal = valor_casa / (qts_year_fina * 12)   # cálculo para saber o valor da prestação mensal
porcentagem = prest_mensal * 100 / salario   # cálculo porcentagem da prestação mensal em relação ao salário

print(f'prestação mensal = R${prest_mensal:.2f}. O valor da mensalidade representa {porcentagem:.2f}% do salário.')
# texto exibido para o usuário com as formatações necessarias
if prest_mensal <= salario * 0.30:    # condição para aprovação do financiamento
    print('Financiamento aprovado. ')
    print(f'valor da prestação mensal é R${prest_mensal:.2f} em {int(qts_year_fina * 12)} vezes.')
else:
    print('Financiamento negado.')
print(f'Valor total do financiamento com juros R${valor_casa}')
