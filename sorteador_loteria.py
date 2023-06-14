import random
import os
from datetime import datetime

LOOP = True
TODAYS_DATE = datetime.today().strftime('%d/%m/%Y')
border = '-' * 50
header = f'{" Sorteador de números da MEGA ":$^50}'
welcome = f'Bem vindo, hoje é dia {TODAYS_DATE}.'


def cls():
    """ Clear the terminal."""    
    
    os.system('cls' if os.name == 'nt' else 'clear')  #clear multiplataform


def drawer():
    """return a function that generate random numbers and
       put in a set 

    Args:
        no args

    Returns:
        function: generator of random numbers list
    """
    

    def random_number_list_generator(x):
        """generate a set of random numbers

        Args:
            x (int): quantitiy of numbers to be sorted

        Returns:
            list: a list of x random and unrepeated numbers
        """
        RANGE_LOTERY_NUMBERS = 101
        drawn_numbers_set = set()  # Using set we ensure that there is not repeated numbers
    
        while len(drawn_numbers_set) != x:
            # We are using while loop instead for loop because we 
            # want set have exactly x numbers in
            drawn_numbers_set.add(random.randint(1 ,RANGE_LOTERY_NUMBERS))

        # For aestetic reasons, lets turn the set into a list. (I really prefer '[]' instead '{}').
        drawn_numbers_list = list(drawn_numbers_set)
        return drawn_numbers_list
        
    return random_number_list_generator


def drawer_ex(y, x):
    """execute drawer function

    Args:
        y (int): number of lists desired
        x (int): number of numbers to be sorted
    """
    for _ in range(y):
        drawed_list = drawer()
        print(drawed_list(x), '\n')


def try_int_or_exit(input_data):
    """process the user input, if user wants to leave, execute
       a function exit() to confirm, else, trys to convert str to int

    Args:
        input_data (str): user inputs str

    Return:
        int: input str converted to int
        or
        function: returns exit()
    """

    def exit():
        """Confirms if the user wants do leave.

        Returns:
            bool: Global LOOP variable to break while loop
        """
        global LOOP
        confirm = input(
            'Deseja realmente sair? Digite "sair" ou qualquer'\
                ' outra tecla para voltar: '
            )
    
        if confirm.lower() == 'sair':
            LOOP = False
            return LOOP
    try:
        int_entry = int(input_data)
        return int_entry
    except:
        if input_data == 's' or input_data == 'S':
            return exit()
        
        return 'Favor, digite apenas números ou [s].'
    


print(header, end=2*'\n')
print(welcome, '\n')

while LOOP:
    print(border)
    number_of_lists_to_be_generated = input(
        f'\nDigite quantos jogos você deseja fazer,'\
              'ou caso queira sair, digite "s": '
    )

    int_number_of_lists_to_be_generated = try_int_or_exit(
        number_of_lists_to_be_generated
        )
    
    if LOOP == False:  #Stop de program 
        break
    
    quantity_of_numbers_to_sorted = input(
        'Quantos números deseja sortear: '
    )
    print()
    int_quantity_of_numbers_to_sorted = try_int_or_exit(
        quantity_of_numbers_to_sorted
    )
    
    print('Os números sorteados são: \n')
    drawer_ex(
        int_number_of_lists_to_be_generated,
        int_quantity_of_numbers_to_sorted
        )