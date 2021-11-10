from capitulo3_funcoes.identificadrdeFuncoes import *
minhalista = []
print('Preenchendo')
preencherinventario(minhalista)
print('Exibindo')
exibirinventario(minhalista)

print('pesquisando')
localizarpornome(minhalista)
print('Alterando')
depreciarpornome(minhalista, 20)

print('Excluindo')
print(excluirporserial(minhalista))
exibirinventario(minhalista)

print('Resumindo')
resumivalores(minhalista)