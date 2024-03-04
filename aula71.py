"""

args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)

"""
# Lembre-te de desempacotamento

x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(x, y):
    return x + y


def soma2(*args):
    # args = list(args)
    numeros = 0
    for argumento in args:    
        numeros += argumento
    return numeros


soma_1 = soma2(1, 2, 3, 4, 5, 6)
print(soma_1)

soma_2 = soma2(1, 2, 6, 8, 4, 8, 156)
print(soma_2)

# soma_3 = soma2(numeros) Isso acontece um erro
numeros = 1, 2, 6, 8, 4, 8, 156
soma_3 = soma2(*numeros)
print(soma_3)


print(sum((1, 2, 6, 8, 4, 8, 156)))
print(sum(numeros))
