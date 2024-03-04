"""
Sets - Conjuntos em python (tipo set)
"""


#   Criando um set
#   ser(iterável) ou {1, 2, 3}
s1 = set('Guilherme')
s2 = {'Guilherme', 2, 3, 4}


#   Sets são eficientes para remover valores duplicados de iteráveis
#   Seus Balores serão sempre únicos;
#   Eles não tem ídenxes ;
#   Eles não garantem ordem ;
#   Eles são iteráveiss (for, in, not in)
s2 = {'Guilherme', 2, 3, 3, 3, 3, 3, 3, 4}

print(s2)

#   Métodos úteis :
#   add, update, clear, discard

s3 = set()
print(s3)
s3.add('Guilherme')
s3.add(1)
s3.update((('Olá, mundo', 1, 2, 3, 4,),))
print(s3)

s3.discard('Guilherme')
print(s3)

s3.clear()
print(s3)

#   Operadores úteis:
#   união | união (union) - Une
#   intersecção & (intersection) - Itens presente em abos
#   Diferença - intens presentes apenas no set da esquerda
#   Diferença simétrica ^ - Itens que não estão em ambos


s4 = {1, 2, 3}
s5 = {2, 3, 4}

s6 = s4 | s5 # União
s7 = s4 & s5 # Interseção
s8 = s4 - s5 # Intersecção do intem a direita s5
s9 = s5 - s4 # Intersecção do intem a direita s4
s10 = s5 ^ s4 # Difereça simetrica 

print(s6)
print(s7)
print(s8)
print(s9)
print(s10)