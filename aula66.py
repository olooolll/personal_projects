"""
Argumentos nomeados e não bineadis en funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor) 
"""


# Definição
def soma(x, y, z):
    print(f'{x=} y={y} {z=}', '|', 'x + y + z =', x + y + z)

soma(1, 2, 3) # agumento não nomeado
soma(3, 2, 1)
soma(y=2, z=3, x=1) # argumento nomeado
