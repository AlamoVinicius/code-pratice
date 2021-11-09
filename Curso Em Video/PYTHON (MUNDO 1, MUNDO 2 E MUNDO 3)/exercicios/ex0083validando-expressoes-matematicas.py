""" Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá
 analisar se a expressão passada está com os parêntes abertos e fechados na ordem correta."""
expressao = input('digite a expressao: ')
pilha = []
for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()    # função pop() elimina o últiomo item por da lista por padrão.
        else:
            pilha.append(')')
            break
print(pilha)
if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('sua expressão é inválida!')


''' essa foi uma fórma interessante de realizar o exercício proposto, eu poderia tambem útilizar numero para
verificar ou qualquer outra coisa q eu achar necessário'''