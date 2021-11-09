""" Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como
parâmentro e mostre uma mensagem com tamanho adaptável."""


def escreva(txt):
    tam = len(txt) + 4
    print(f'{"=" * tam}')
    print(f'  {txt}')
    print(f'{"=" * tam}')


escreva('ola mundo')
escreva('hello world')
escreva('curso em video')
escreva('Álamo Vinícius de Souza')