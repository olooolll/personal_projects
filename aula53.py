"""
enumerate - enumera iteráveis (índices)
""" 


lista = ['Maria', 'Helena', 'Guilherme']
lista.append('joão')

lista_enumerada = enumerate(lista)

for nome in lista_enumerada:
    print(nome)



for nome in enumerate(lista):
    print(nome)

"""------------------------------"""


#[(0, 'Maria'), (1, 'Helena'), (2, 'Guilherme'), (3, 'joão')]
lista_enumerada = list(enumerate(lista))

print(lista_enumerada)

"""------------------------------"""

for indice, nome in enumerate(lista):
    print(indice, nome)