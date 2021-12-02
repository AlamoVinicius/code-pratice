from math import radians, sin, cos, tan
angulo = float(input('digite o valor do ângulo:'))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O valor de seno é: {seno:.2f}, cosseno é: {cosseno:.2f} e o tangente é: {tangente:.2f}')
