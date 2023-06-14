import random
import sys

for _ in range(200):

    nove_digitos = ''

    # Vamos randomizar 9 dígitos de 1 a 9 e gerar nosso CPF com isso.
    for j in range(9):
        nove_digitos += str(random.randint(0, 9))

    lista_cpf = []

    for numero in nove_digitos:
        lista_cpf.insert(0, int(numero)) # Criamos a lista com os digitos de trás pra frente.

    soma = 0  # elemento neutro da soma

    # Agora faremos as operações definindo o primeiro índice i como 2 e indo até 10
    
    for i, numero_lista in enumerate(lista_cpf, start =2): 
        produto_i_numero_lista = i * numero_lista 
        soma += produto_i_numero_lista
        digito_1 = (soma * 10) % 11
        
    # Assim obtemos o primeiro dígito 
    digito_1 = digito_1 if digito_1 <= 9 else 0 

    # De forma análoga calcularemos agora o segundo dígito com a única diferença 
    # de que agora temos que incluir o primeiro dígito na operação.

    lista_cpf.insert(0, digito_1)  # incluímos o digito_1 no começo da lista.

    soma = 0  # zeramos a soma novamente.

    for i, numero_lista in enumerate(lista_cpf, start =2): 
        produto_i_numero_lista = i * numero_lista 
        soma += produto_i_numero_lista
        digito_2 = (soma * 10) % 11

    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado = nove_digitos + '-' + str(digito_1) + str(digito_2)

    print(cpf_gerado)