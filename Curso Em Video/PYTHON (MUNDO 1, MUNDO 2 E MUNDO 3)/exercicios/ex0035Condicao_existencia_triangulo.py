"""Desenvolva um programa que leia o comprimento de trÊs retas e diga ao usuário se eles podem ou não
formar um triangulo."""
r1 = float(input())   # a
r2 = float(input())   # b
r3 = float(input())   # c
# fórmula para condição de existência de um triangulo:
if r1 < r2 + r3 and  r2 < r1 + r3 and r3 < r1 + r2:
    print('Sim, as retas formam um triangulo.')
else:
    print('Não, as retas não formam um triangulo.')