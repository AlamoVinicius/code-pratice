frase = 'Curso em video Python'
        #012345678901234567892
print(frase[::3])             # nessa linha são formas de cortar uma str, primeiro representa d inicial, segunda
# representa a distancia final desconsiderando ultimo caractere da str, e a terceira representa os passos (pulo de str)
print(frase.count('o'))    # iremos contar quantas vezes a letra o aparece na str.
print(len(frase.strip()))         #len retorna o tamanho da frase e/ou lista e strip() elimina os espaços
print(frase.replace('Python', 'DemonRyze'))    # replace eu troco a string pelo q foi inserido mas somente no print
print('Curso' in frase)     # retonra se é True or False se a str pertence ao objeto.
print(frase.find('Curso'))    # retorna a posição que a lista ou conjunto de cactere esta posicionada.
print(frase.split())          # transfomra minha str em lista


print("""olá estou apenas testando como imprimir uma string inteira
contando com seus espaçõs, sem precisa de eu ficar colocando barra 
invertida + n, maluco isso é muita doidera hehheheh""")