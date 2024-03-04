"""

lista de listas e seus índices

"""

salas = [
    #   0        1
    ['Maria', 'Helena'], #sala 0
    #   0
    ['Elaine',],  #sala 1
    #   0            1        2
    ['Guilherme', 'João', 'Eduarda', (0, 10, 20, 30, 40)], #sala 2

]


print(salas)

print(salas[0][1])
print(salas[2][2])

print(salas[2][3][2])

for i, sala in enumerate(salas):
    for aluno in sala:
        print(f'A sala do(a) {aluno} é {i}')