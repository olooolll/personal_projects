"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

s1 = criar_saudacao('Bom dia')
s2 = criar_saudacao('Boa noite')

for nome in ['Maria', 'joão', 'guilherme']:
    print(s1(nome))
    print(s2(nome))