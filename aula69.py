"""
Escopo significa o local onde aquele código pode atingir.
Exite o escopo global e local

O escopo global é o escopo onde todo o código é alcançavel
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados

Não podemos acessao a nomes de escopos internos nos escopos externos. 

A palavra global faz uma variável do escopo externo ser a mesma no escopo interno

"""

x = 2

def escopo1():
    global x
    x = 10

    print(x)

def escopo2():
    x = 100
    
    def outra_funcao():
        y = 3
        print(x, y)
    outra_funcao()
    print(x)

print(x)

escopo1()

escopo2()