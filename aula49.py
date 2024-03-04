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
"""----------------------------"""

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_c = lista_a + lista_b
print(lista_c) 

"""----------------------------"""
lista_a.extend(lista_b)
print(lista_a)

