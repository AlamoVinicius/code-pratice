""" Exemplo de uso de tuplas: """
ips = {}
resp = 'S'
while resp == 'S':
    ips[(input('Digite os dois primeiros octetos: '),
         input('Digite os dois últimos octetos: '))] = input('Nome da máquina: ')
    resp = input('Digite <S> para continuar: ').upper()

print("Exibindo ip's: ")
for ip in ips.keys():
    print(ip[0]+"."+ip[1])

print('Exibindo máquinas com o mesmo endereço: ')
pesquisa = input('Digite os dois últimos octetos: ')
for ip, nome in ips.items():
    print("Máquinas no mesmo endereço (Redes diferentes)")
    if(ip[1] == pesquisa):
        print(nome)

print("exibindo ad maquinas que compõe uma mesma rede: ")
rede = input("Digite os dois primeiros octetos: ")
for ip, nome in ips.items():
    if(ip[0] == rede):
        print(nome)