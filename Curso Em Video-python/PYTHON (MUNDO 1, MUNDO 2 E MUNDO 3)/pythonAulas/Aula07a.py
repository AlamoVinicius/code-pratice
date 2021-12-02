n1 = int(input("Digite um numeo: "))
n2 = int(input('Digite outro numero : '))
date = int(input('Digite sua data de aniversario sem traços'))
confirmacao = input('Podemos utilizar sua data para a soma? digite "S" ou "N": ').upper()
if confirmacao == "S":
    print(f'a soma da total = {n1 + n2 + date :=^20}')
else:
    print('TO BAD!!!')
