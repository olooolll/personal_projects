"""
Cuidados com dados mutaveis

= - Copia o valor (imutáveis)
= - Aponta para o mesmo valor na memória (mutalvel)

"""

nome = 'Guilherme'
nome_variavel = nome
nome = 'araujo'
#print(nome)
#print(nome_variavel)

lista_a = ['Gulherme', 'Julia', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)