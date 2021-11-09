"""Crie um código em python que teste se o site pudim está acessivel pelo computador usado."""
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except :
    print('falhou! Site não conectado. Verifique sua conexão ou url')
else:
    print('Site conectado com sucesso,')
