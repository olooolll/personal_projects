#  Empacotamenteo e desempacotamento de dicícionarios

a, b = 1, 2
a, b = b, a

# print(a, b)

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'souza',
}

dados_pessoas = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoas, 'chave':1}

# print(pessoas_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword argumenst (Argumentos nomeados)
def mostro_argumentos_nomeados(*args, **kwargs):
    print('Não nomeados:', args)
    
    for chave, valor in kwargs.items():
        print(chave, valor)
    

# mostro_argumentos_nomeados(nome='Joana', qlq=123)
mostro_argumentos_nomeados(**pessoas_completa)

configurações = {
    'args1': 1,
    'args2': 2,
    'args3': 3,
    'args4': 4,
    'args5': 5,
    'args6': 6,
}

mostro_argumentos_nomeados(**configurações)
