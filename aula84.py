# Lista - comprehension em python
# List - comprehension é uma forma rápida para criar listas a partir de iteráveis
# print(list(range(10)))

lista = []

for numero in range(10):
    lista.append(numero)
print(lista)

lista2 = [
    numero * 2 
    for numero in range(10)
    
]
print(lista2)