name = input("Digite um nome: ")
print(f"Olá {name} welcome")
idade = input("Digite sua idade: ")
email = input("Digite seu email: ")
print("======Confirme seus dados====== ")
print(f"idade ---- {idade}\nemail -----{email}")
question = input('Digite yes or not').upper()
while question == "YES" or "NOT":
    if question == "YES":
        print(f"muito bem então, lets start the show! baby :\n"
              f"Então {name} você já tem {idade} anos é bom começar a virar um verdadeiro programador asshole)")
        break
    elif question == "NOT":
        idade = input("Digite sua idade: ")
        email = input("Digite seu email: ")
        print("======Confirme seus dados====== ")
        print(f"idade ---- {idade}\nemail -----{email}")
    else:
        print('Digite "YES" ou "NAO"!')
    question = input("is that correct? ").upper()
