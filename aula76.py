
# pessoas = dict(
#     nome='Guilherm',
#     sobrenome='Araujo'
# )

pessoas = {
    'Nome': 'Guilherme',
    'Sobrenome': 'Araujo',
    'Idade': 20,
    'Altura': 1.74,
    'Endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'fulano fulano', 'número': 321},
    ]
}

print(pessoas['Altura'])

print()

for chave in pessoas:

    print(chave, pessoas[chave])


"""--------------------------------------------"""

# Manipulando chaves e valores em dicionários
pessoa = {}



##
##

chave = 'nome'

pessoa[chave] = 'Guilherme Araujo'
pessoa['sobrenome'] = 'costa'

print(pessoa[chave])


pessoa[chave] = 'Julia'

del pessoa['sobrenome']
print(pessoa)

# (Erro) errado fazer isso
# if pessoa['sobrenome']:
#     print('Existe')

if pessoa.get('sobrnome') is None:
    print('Não existe')

else:
    print(pessoa['sobrenome'])