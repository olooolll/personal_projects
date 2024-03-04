"""
CPF: 746.824.890-70

Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma contagem regressiva começando de 10

ex.:  (74682489070)
    10  9  8  7  6  5  4  3  2
CPF 7   4  6  8  2  4  8  9  0
    70  36 48 56 12 20 32 27 0
    
Somar todos os resultados:

70+36+48+56+12+20+32+27+0 = 301
Multiplicando o resultado anterior por 10

301 * 10 = 3010
Obter o resto da divisão da conto anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0

contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

"""
import re
import sys

primeiro_digito = 0
segundo_digito = 0
multiplo_1 = 10
multiplo_2 = 11

input_usr = input('Digite o seu CPF: ')

print()

re_input_cpf = re.sub(r'[^0-9]', '', input_usr)

repetido_input = re_input_cpf[0] * len(re_input_cpf)


if len(re_input_cpf) > 11:
    print(f'Este CPF {input_usr} tem números a mais')
    sys.exit()


elif repetido_input == re_input_cpf[0] * len(re_input_cpf):
    print('O seu CPF tem numeros repetidos')
elif len(re_input_cpf) == 11:
    for caracter_str in re_input_cpf:
        caracter_int = int(caracter_str)

        if multiplo_1 >= 2:        
            primeiro_digito += caracter_int * multiplo_1 
            multiplo_1 -= 1 

        if multiplo_2 >= 2:
            segundo_digito += caracter_int * multiplo_2
            multiplo_2 -= 1

    primeiro_digito = (primeiro_digito * 10) % 11
    primeiro_digito if primeiro_digito <= 9 else 0

    segundo_digito = (segundo_digito * 10) % 11
    segundo_digito if segundo_digito <= 9 else 0

    if primeiro_digito == int(re_input_cpf[-2]) and segundo_digito == int(re_input_cpf[-1]):
        print(f'O CPF {input_usr} é valido')
    else:
        print(f'O CPF {input_usr} é inválido')

else:
     print(f'Este CPF {input_usr} está faltando número(s)')
