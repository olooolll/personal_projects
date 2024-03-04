"""
Exercícios
Crie funções que duplicam, triplicam e quadriplicam o número recebido como parâmetro
"""
import random
"""
def multi(numero):
    def duplicam(numero):
        return numero * 2

    def triplicam(numero):
        return numero * 3
        
    def quadriplicam(numero):
        return numero * 4

    return numero, duplicam(numero), triplicam(numero), quadriplicam(numero)
"""
def criar_multiplicar(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicar(2)
triplicar = criar_multiplicar(3)
quadruplicar = criar_multiplicar(4)

print(duplicar(4))
print(triplicar(4))
print(quadruplicar(4))