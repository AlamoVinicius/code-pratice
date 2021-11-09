""" Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
o programa encerra quando ele disser que quer mostrar 0 termos"""
primeiro_termo = int(input("Digite o valor do primeiro termo da p.A: "))   # entrada do primeiro termo
razao = int(input("Digite o valor da razão da P.A: "))   # entrada da razão da p.a
termo = primeiro_termo    # váriavel que irá receber o valor do primeiro termo
controlador = 1           # controlador do meu loop
total = 0                 # váriavel de controle
mais = 10                 # váriavel de controle já começa com 10 para exibir os 10 primeiros termos
while mais != 0:          # enquanto mais for diferente de 0 o bloco de código abaixo acontece.
    total += mais         # total vai ser somado com o valor da váriavel 'mais'
    while controlador <= total:    # enquanto controlador for menor que total que já começa valendo 10 então loop 10x
        print(termo, end=' ')     # aqui eu exibo os 10 primeiros termos
        termo += razao           # lógica da p.a
        controlador += 1         # controlador recebe +1 para finalizar o loop
    print('pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? digite 0 para sair: '))   # váriavel de controle para
    # receber o total de quantos mais termos o usuário deseja exibir
print("Fim")









