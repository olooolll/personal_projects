"""
Faça um lista de comprar com listas
O usuário deve ter a possibilidade de inserir, apagar e listar valors de sua lista
Não permita erros de ídices inexistentes na lista
"""
import os

lista = []

while True:


    usr_inuput = input('Selecione um opção\n'
                    '[I]nserir [A]pagar [L]istar: ')


    if usr_inuput.lower() == 'i':
        os.system('clear')
        
        usr_inuput2 = lista.append(input('Produto: '))
        
        print(usr_inuput2, 'Adicionado a lista de produtos.')      
    
    elif usr_inuput.lower() == 'a':
        os.system('clear')

        usr_inuput2 = int(input('Digite o número do produto que quer remover: '))

        if int(usr_inuput2):
            if usr_inuput2 <= len(lista):
                lista.pop(usr_inuput2 - 1)

            
            else: 
                print(f'Não temos o produto N°{usr_inuput2}')

        else:
            os.system('clear')
            print('Apenas númros!!!')
            

    elif usr_inuput.lower() == 'l':
        os.system('clear')
        for numero, item in enumerate(lista, start=1):
            print(numero, item)
    else:
        os.system('clear')
        print('Opção invalida\n')
        