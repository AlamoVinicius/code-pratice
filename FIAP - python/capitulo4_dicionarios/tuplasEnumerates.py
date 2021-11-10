""" exemplo de enumerate"""
usuarios = {}
resp = "S"
emails = []
while resp == "S":
    emails.append(input("Digite um email: ").lower())
    resp = input("Digite <S> para continuar: ").upper()

tupla = list(enumerate(emails))
for chave in range(0, len(tupla)):
    print(f"Email: {tupla[chave][1]}")
    usuarios[tupla[chave]] = [input("Digite o nome"), input("Digite o nível: ")]

for chave, dado in usuarios.items():
    print(f"Usuarios.....:{chave[0]}")
    print(f"Email........:{chave[1]}")
    print(f"Nome.........:{dado[0]}")
    print(f"Nível........:{dado[1]}")
