"""
Exercícios com funcções

Crie uma função que multiplica todos os argumentos não nomeados recebidos

Retorn o total para uma variável e mostr o valo da variável.

Crie um função fala se um úmero é par ou ímpar. 

retorne se o número é par ou ímpar.
"""
import random

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    
    if total % 2 == 0:
        return f'O {total=} é par'
    
    return f'O {total=} é impar'

vars = multiplicar(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(vars)