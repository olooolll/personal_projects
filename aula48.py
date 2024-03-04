"""
Listas em Python    
Tipo list - mutável
Suporta Vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final da lista
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - Apaga um índice
    clear - Limpa a lista
    extend - estende a lista
    + - Contatena a lista

Creat Read Update Delete
Cria, Ler, Alterar, Apagar = lista[i] (CRUD)

"""
"""---------------------"""

#         0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Guilherme')
nome = lista.pop()
lista.append(1223)
numero = lista.pop()
del lista[-1]
print(lista, nome, numero)

"""---------------------"""

lista.insert(0, 5)
print(lista)

"""---------------------"""

lista.insert(0, 'Guilherme')
print(lista)

"""---------------------"""
print(len(lista))