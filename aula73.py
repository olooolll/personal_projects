"""

higher Orfer Functions
Funções de primeira classe

"""

def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executar(funcao, *args):
    return funcao(*args)

v = executar(saudacao, 'bon dia', 'Guilherme')
print(v)

print(
    executar(saudacao, 'bon noite', 'Julia')
)