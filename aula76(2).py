"""
Métodos úteis dos dicionários em python

len - quantas as chaves
keys - iterável com os valores
values - interável com os valores
items - iterável com chaves e valores
serdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a chave especifica (del)
popitem - apaga o ultimo item adicionada
update - atualiza um dicionário com outro


"""
import copy

d1 = {
    'Altura': 1.74,
    'Endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'fulano fulano', 'número': 321},
    ]
}


pessoas = {
    'Nome': 'Guilherme',
    'Sobrenome': 'Araujo',
    # 'idade': 20,
    'Altura': 1.74,
    'Endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'fulano fulano', 'número': 321},
    ]
}


# len - quantas as chaves
print('\nlen')
print(len(pessoas))

# keys - iterável com os valores
print('\nkeys')
print(pessoas.keys())

# values - interável com os valores
print('\nvalues')
print(list(pessoas.keys())[2])

# values - interável com os valores
print('\nvalues')
print(list(pessoas.values()))


for valor in pessoas.values():
    print(valor)


# items - iterável com chaves e valores
print('\nitems')
print(list(pessoas.items()))


# serdefault - adiciona valor se a chave não existe
print('\nserdefault')

pessoas.setdefault('idade', 0)
print(pessoas['idade'])

# copy - retorna uma cópia rasa (shallow copy)
print('\ncopy')

d2 = d1.copy()
d2 = copy.deepcopy(d1)

d2['Altura'] = 2.00

print(d1)
print(d2)

# get - obtém uma chave
print('\nget')
print(pessoas.get('Nome', 'Não existe'))

# pop - apaga um item com a chave especifica (del)
print('\npop')

nome = pessoas.pop('Nome')
aultima_chave = pessoas.popitem()
print(aultima_chave)
print(nome)

# update - atualiza um dicionário com outro

pessoas.update({
    'nomes': 'novo valor',
    'idades': 50
})

pessoas.update(tal='coisa', coisa='tal')

tupla = ('coisa', 'coisas'), 

lista = [123, 312],

pessoas.update(tupla)
pessoas.update(lista)
print(pessoas)