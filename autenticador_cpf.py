"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

import sys

while True:
        
    # Tratamento do input:
    cpf_input = input('Digite o CPF sem pontos: ') \
        .replace('.','') \
        .replace('-','')  # tiramos os '.' e '-' do input

    cpf_cortado = cpf_input[:9]

    entrada_repetida = cpf_input == cpf_input[0] * len(cpf_input)

    if entrada_repetida:
        print('Você enviou dados repetidos.')
        sys.exit()

    #-------------------------------------------------

    lista_cpf = []

    for numero in cpf_cortado:
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

    cpf_gerado = cpf_cortado + str(digito_1) + str(digito_2)
    
    if cpf_input == cpf_gerado:
        print('CPF válido')
    else:
        print('CPF inválido')