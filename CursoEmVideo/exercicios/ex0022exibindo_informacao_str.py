""" Crie um programa que leia o nome completo de uma pessoa e mostre:
- o nome com todas as letras maiusculas e minusculas.
- quantas letras ao todo (sem considerar espaços)
- quantas letras tem o primeiro nome."""


nome = str(input('Digite o seu nome: ')).strip()  # com strip() eu pulo os meus espaçõs antes e depoois da stringer
print(f'{nome.upper()} em maiusculo.')
print(f'{nome.lower()} em minusculo')
print(f'O nome completo tem {len(nome) - nome.count(" ")} letras')   # - nome.count('  ') elimino o espaço dentro da str
separacao = nome.split(' ')
print(f'O primeiro nome tem {len(separacao[0])} letras')