""" escreva um programa que leia dois números inteiros compare-os, mostrando na tela uma mensagem:
-o primeiro valor é maior / o segundo valor é maior / não exite valor maior, os dois são iguais"""
num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))
if num1 > num2:
    print('O primeiro valor é maior')
elif num2 > num1:
    print('O segundo valor é maior')
else:
    print('Não existe diferença os dois são iguais.')