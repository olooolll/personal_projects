"""
Escopo de funções em Python

Escopo signifíca o local onde aquele código pode atingir.
Existe o escopo é global e local
O escopo aonde todo o códfigo é alcançavel.
O escopo local é o escopo onde apenas nomes do mesm local podem ser alcançados.  

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