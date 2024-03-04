import random
import re
import sys

i_1 = 10
nove_digitos = ''
primeiro_digito = 0

for CPF in range(9):
    nove_digitos += str(random.randint(0, 9))
    
for caracter in nove_digitos:
    digito = int(caracter)
    
    if i_1 >= 2:
        digito = digito * i_1
        primeiro_digito += digito

        i_1 -= 1

primeiro_digito = (primeiro_digito * 10) % 11 
primeiro_digito if primeiro_digito <= 9 else 0





print(primeiro_digito)
# primeiro_digito = 0
# segundo_digito = 0
# multiplo_1 = 10
# multiplo_2 = 11

# input_usr = input('Digite o seu CPF: ')

# print()

# re_input_cpf = re.sub(r'[^0-9]', '', input_usr)

# repetido_input = re_input_cpf[0] * len(re_input_cpf)


# if len(re_input_cpf) > 11:
#     print(f'Este CPF {input_usr} tem números a mais')
#     sys.exit()


# elif repetido_input == re_input_cpf[0] * len(re_input_cpf):
#     print('O seu CPF tem numeros repetidos')
# elif len(re_input_cpf) == 11:
#     for caracter_str in re_input_cpf:
#         caracter_int = int(caracter_str)

#         if multiplo_1 >= 2:        
#             primeiro_digito += caracter_int * multiplo_1 
#             multiplo_1 -= 1 

#         if multiplo_2 >= 2:
#             segundo_digito += caracter_int * multiplo_2
#             multiplo_2 -= 1

#     primeiro_digito = (primeiro_digito * 10) % 11
#     primeiro_digito if primeiro_digito <= 9 else 0

#     segundo_digito = (segundo_digito * 10) % 11
#     segundo_digito if segundo_digito <= 9 else 0

#     if primeiro_digito == int(re_input_cpf[-2]) and segundo_digito == int(re_input_cpf[-1]):
#         print(f'O CPF {input_usr} é valido')
#     else:
#         print(f'O CPF {input_usr} é inválido')

# else:
#      print(f'Este CPF {input_usr} está faltando número(s)')
