"""
Operações ternária (Condicional de uma linha)

<valor> if <condicao> else <outro valor>

"""

print('valor' if True else 'Outro valor', '\n')

print('valor' if False else 'Outro valor', '\n')

"""--------------------------------------------"""

condicao = 10 == 10
variavel = 'valor' if condicao else 'Outro Valor'

print(variavel, '\n')

"""--------------------------------------------"""

digito = 9

novo_digito = digito if  digito <= 9 else 0

print(novo_digito)

"""--------------------------------------------"""
