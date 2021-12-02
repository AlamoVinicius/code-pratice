""" Faça um programa que mostre uma contagem regressiva para o estouro de fogos de artificio, indo de
10 até 0. com uma pausa de 1 segundo entre eles."""
from time import sleep
import emojis
for c in range(10, 0, -1):
    sleep(1)
    print(c)
print(emojis.encode("happy new year!!!:tada::fireworks::fireworks::fireworks: "))