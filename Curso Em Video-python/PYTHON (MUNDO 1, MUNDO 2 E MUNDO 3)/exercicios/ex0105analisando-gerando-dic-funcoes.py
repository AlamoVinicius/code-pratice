""" Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes informações:
- a quantidade de notas
- A maior nota
- A menor nota
- a média da turma
- A situação (opcional)
Adiciona também as docstrings da função."""


def notas(*n, situacao=False):
    """
    ==> função para analisar a nota e situação de vários alunos.
    :param n: valores para analisar a situação (aceita vários números)
    :param situacao: analisa a situação como ruim, razoável ou boa,
    :return: retorna um dicionário com as informações.
    """
    dic = dict()
    dic['total'] = len(n)
    dic['maior'] = max(n)
    dic['menor'] = min(n)
    dic['media'] = sum(n)/len(n)
    if situacao:
        if dic['media'] <= 5:
            dic['situacao'] = 'RUIM'
        elif 5 < dic['media'] <= 7:
            dic['situacao'] = 'RAZOAVEL'
        elif dic['media'] > 7:
            dic['situacao'] = 'BOA'
    return dic


analise = notas(5.5, 2.5, 1.5, situacao=True)
print(analise)


