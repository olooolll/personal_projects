"""

splite e join com list e str

split - divide uma string (lista)

join - une uma string

"""

frase = 'Olha só que, coisa interessante'

lista_palavras_cruas = frase.split(',')

lista_palavras = []
for i, frase in enumerate(lista_palavras_cruas):
    #print(lista_palavras[i].strip())
    #lista_palavras[i] = lista_palavras[i].strip()
    lista_palavras.append(lista_palavras_cruas[i].strip())

print(lista_palavras_cruas)
print(lista_palavras)

#frase_unidas = ''.join('abc')
frase_unidas = '-'.join(lista_palavras)
print('\n', frase_unidas)