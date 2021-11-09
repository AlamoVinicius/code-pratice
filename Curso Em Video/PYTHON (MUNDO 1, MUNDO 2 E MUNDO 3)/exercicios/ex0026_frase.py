""" Faça um programa que leia uma frase e diga o seguinte:
 - quantas vezes aparece aparece a letra 'a'
 - em que posição ela aparece na primira vez
 - Em que posição ela aparece da ultima vez """

texto = str(input('Escreva aqui seu texto: ')).strip().upper()
print(f'A letra a aparece {texto.count("A")} vezes" ')
print(f'A letra a aparece na posiçao de {texto.find("A") + 1} pela primeira vez!')
print(f'A letra a aparece na posiçção de {texto.rfind("A") + 1} pela ultima vez')
