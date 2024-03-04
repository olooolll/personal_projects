"""
Desempacontamento em chamadas de médodos e funções
"""

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'


p, b, c, *_, ap, u = lista

#print(p, u, ap)

print(*string, end='///\n')

print(*lista, sep='-*-')

print(*tupla)