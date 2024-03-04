"""
Introdução ás funções (def) em Python
Funções são trechos de código usados para replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""
# def Print():
#     print('Várias0')
#     print('Várias1')
#     print('Várias2')
#     print('Várias3')
#     print('Várias4')
#     print('Várias5')


# Print()

def imprimit(a, b, c):
    print(a, b, c)

imprimit(1, 2, 3)
imprimit(4, 5, 6)


def saudacao(nome='Sem nome'):
    print(f'olá, {nome}')

saudacao('Guilherme')
saudacao('Maria')
saudacao()