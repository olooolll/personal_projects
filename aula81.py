"""
Função lambda em python

A função lambda é a uma função como qualquer outra en python. 
Porém, são funções anônimas que contém apenas uma linha. 
Ou seha, tudo deve ser contido dentro de uma única expressão.

lista = [
    {'nome': 'Guilherme', 'sobrenome': 'araujo'}
    {'nome': 'Guilherme1', 'sobrenome': 'araujo1'}
    {'nome': 'Guilherme2', 'sobrenome': 'araujo2'}
    {'nome': 'Guilherme3', 'sobrenome': 'araujo3'}
    {'nome': 'Guilherme4', 'sobrenome': 'araujo4'}
    {'nome': 'Guilherme5', 'sobrenome': 'araujo5'}
    {'nome': 'Guilherme6', 'sobrenome': 'araujo6'}
    {'nome': 'Guilherme7', 'sobrenome': 'araujo7'}
    {'nome': 'Guilherme8', 'sobrenome': 'araujo8'}
]
"""
lista2 = [
    {'nome': 'Guilherme8', 'sobrenome': 'araujo8'},
    {'nome': 'Guilherme1', 'sobrenome': 'araujo1'},
    {'nome': 'Guilherme3', 'sobrenome': 'araujo3'},
    {'nome': 'Guilherme2', 'sobrenome': 'araujo2'},
    {'nome': 'Guilherme5', 'sobrenome': 'araujo5'},
    {'nome': 'Guilherme4', 'sobrenome': 'araujo4'},
    {'nome': 'Guilherme7', 'sobrenome': 'araujo7'},
    {'nome': 'Guilherme6', 'sobrenome': 'araujo6'},
    {'nome': 'Guilherme', 'sobrenome': 'araujo'},
]





lista = [4 , 32, 1, 34, 5, 6, 6, 21]

lista.sort()
print(lista)

print()

lista.sort(reverse=True)
print(lista)

print()
print()
print()


def ordena_nome(item):
    return item['nome']


lista2.sort(key=ordena_nome)

for item in lista2:
    print(item)
