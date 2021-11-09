""" Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""
# criação da tupla
nextensos = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
             'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

# lógica do programa
while True:
    escolha = int(input('Escolha un número de 0 a 20 para exibir em extenso: '))
    while escolha < 0 or escolha > 20:
        escolha = int(input('tente novamente escolha un número de 0 a 20 para exibir em extenso: '))
    print(f'Você digitou o número: {nextensos[escolha]}')   # exibição final
    perg = str(input('digite <S/N> para digitar outro número: ')).upper().strip()[0]
    if perg != 'S':
        break
print('Muito obrigado por usar o leitor de números por extenso, volte sempre!!')

''' resolução do curso no link: https://youtu.be/ei2Kr3ccfO0 poucas coisas mudaram em relação ao meu código na qual
não muda o resultao. ele usou while True, eu já usei com variável de controle'''
