""" Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços."""
frase = input('Digite uma frase para verificar se é ou não palindromo: ').strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''      # tambem posso usar: inverso = junto[::-1] eliminando a possibilidade do for
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(f'O invérso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')
