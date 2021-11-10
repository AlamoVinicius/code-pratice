with open("teste.txt", "w") as arquivo:
    arquivo.write("Nunca foi tão fácil criar um arquivo.\n"
                  "só um momento estou testando se a linha ficou embaixo ok? ")
    arquivo.write("olá mundo , Hello World in english \n")
#usando o a eu consigo continuar a linha
with open("teste.txt","a") as arquivo:
    arquivo.write("Será que continuou ou sobreescreveu? ")