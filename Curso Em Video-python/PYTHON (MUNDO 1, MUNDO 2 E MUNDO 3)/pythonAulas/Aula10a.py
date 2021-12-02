""" testes com as estruturas de decisões  if, else ...etc """
r = ' '
while r == ' ':
    nome = input('nome: ').strip()
    if nome == 'Alamo':
        print('Uauuu!!! versão Brasileira Álamo kkkkkkkkk sues pais cagaram no seu nome em pqp! ')
    elif nome == 'Samuel':
        print('Meu fiquei até com sono Baiano é foda!')
    elif nome == 'Thiago':
        print('Sem comentarios, viciado em pornò de mulheres gravidas. fico com pena desse cara')
    elif nome == 'Lipe':
        print('Tirem esse cara da cidae de SP imediamente antes que o Pulmão dele para de uma vez kkkkkkk')
    elif nome == 'Edu':
        print('Vixi, Carioca boi de webnamoro, melhor nem comentar nada antes q eu tome uns tiros!')
    r = input('aperte espaço para inserir outro nome: ')


nota1 = float(input('The first note:'))
nota2 = float(input('The second note: '))
media = (nota1 + nota2)/2
print(f'Your grade is: {media:.1f}')
if media >= 8 :
    print("congratulations!!! your grade is above average;")
elif 5 <= media < 8:
    print('Not to bad! but you need to study more!')
else:
    print('You need to study a lot more Dude!!!!')
