"""
CPF digits alghoritm:
We first index the 9 firsrt index starting at 10
until 2.
Before that we multiply the number if his respective
index, them we sum all of the products.
We multipily the result of sum by 10 and take module
per 11.
If the results is minor than 9, than we take the value
for the first digt, else, it will be 0.
For the second one we repeat the process puting the 
first digit in calcule.

Example:
Took 746824890,

   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
=  70  36 48 56 12 20 32 27 0

for the sum: 70+36+48+56+12+20+32+27+0 = 301
=> 301 * 10 = 3010
=> 3010 % 7 = 7

so the first digit will be 7.

"""


import os
import random
import sys


def small_border():
    """create a small border
    """
    print(30*'-')


def cls():
    """ Clear the terminal."""    
    os.system('cls' if os.name == 'nt' else 'clear')  #clear multiplataform



def main_menu():
    """Main menu that allows the user to choose wich program they
       want to execute.    
    """
    MAIN_LOOP = True

    while MAIN_LOOP:

        cls()

        print(f'{" Bem vindo ":-^30}')  # Header
        entry_option = input(
            '[1] Gerador de CPF.\n' \
            '[2] Autenticador de CPF.\n' \
            '[s] Sair.\n' \
            'Qual programa deseja acessar: ' \
        )

        if entry_option == '1':
            return generator()

        elif entry_option == '2':
            return autenticator()

        elif entry_option == 's':
            confirm = input('Para confirmar digite "sair":')
            if confirm.lower() == 'sair':
                sys.exit()
            continue

        else:
            print('Entrada inválida, digite apenas as opções válidas. \n')
            continue



def test_int_or_back(input_data):
    """process the user input, if the user wants to leave, execute
    a function back() to confirm, else, return a bool true if 
    input_data is a digit

    Args:
        input_data (str): user inputs str

    Return:
        int: input str converted to int
        or
        function: returns exit()
    """
    is_digit = False 

    if input_data.isdigit():
        # we verify if input data is digit
        is_digit = True
        return is_digit
    
    if input_data.lower() == 'b':
        return main_menu()
    
    else:
        print('Favor, digite apenas números ou [b].')
        return is_digit


def digit_calculator(data_list):
    """Calculate a CPF' digit using CPF's algorithm

    Args:
        data_list (list): list containing the numbers
                          of cpf in reverse order

    Returns:
        int: return digit
    """
    sum_of_product = 0
    
    for i, number in enumerate(data_list, start =2): 
        #Starts in 2 because we want i in range 2,10
        product_i = i * number 
        sum_of_product += product_i
        digit = (sum_of_product * 10) % 11
        
        digit = digit if digit <= 9 else 0

    return digit



def generator():
    """Generate CPF numbers.

       Return:
            print CPF numbers.
    """
    cls()

    while True:
        range_of_cpf_to_be_generated = input(
            'Digite a quantidade desejada de CPF a gerar, ou [b] para voltar: '
        )
        is_digit = test_int_or_back(range_of_cpf_to_be_generated)

        if is_digit:  # If is digit we will convert to int
            int_range_of_cpf_to_be_generated = int(
                range_of_cpf_to_be_generated
            )

        for _ in range(int_range_of_cpf_to_be_generated):
            cpf_string = ''  #  We will use string to print CPF pattern more easily
            random_numbs_list = []  #Here we will put the numbers and make the calculation
            for j in range(9):
                random_number = random.randint(0,9)
                random_numbs_list.insert(0, random_number)
                cpf_string += str(random_number)

            digit_1 = digit_calculator(random_numbs_list)
            digit_2 = digit_calculator(random_numbs_list)


            print(f'{cpf_string}-{digit_1}{digit_2}')



def autenticator():
    """Run in a loop a CPF autenticator, until users wants to 
       going to back to main menu.
    """

    cls()
    while True:

        cpf_input = input('Digite o CPF a validar ou [b] para'\
                        ' voltar: ')\
            .replace('.','') \
            .replace('-','')  # we removed '.' and '-' from input
        cpf_len_9 = cpf_input[:9]  # We just want the first 9 digits

        is_digit_flag = test_int_or_back(cpf_input)

        if is_digit_flag:
            cpf_number_list = [
                int(number)
                for number in cpf_len_9[-1:-10:-1]
            ]

            digit_1 = digit_calculator(cpf_number_list)
            cpf_number_list.insert(0, digit_1)
            digit_2 = digit_calculator(cpf_number_list)
            cpf_number_list.insert(0, digit_2)

        
        correct_cpf = cpf_len_9 + str(digit_1) + str(digit_2)
               
        if cpf_input == cpf_input[0]*len(cpf_input):
            print('CPF inválido. (possui todos caracteres repetidos)\n')
            
        elif cpf_input == correct_cpf:
            print('CPF VÁLIDO!')
            small_border()
        else:
            print('CPF INVÁLIDO!')
            small_border()
 
######################################################################################

main_menu()