with open("teste.txt", "r") as arquivo:
    conteudo = arquivo.readlines()
print("Tipo de dado da váriavel", type(conteudo))
print(f"conteudo do arquivo: {conteudo}")