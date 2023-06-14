# Exercício - sistema de perguntas e respostas

import os

def cls():
    """ Clear the terminal."""    
    
    os.system('cls' if os.name == 'nt' else 'clear')  #clear multiplataform

def question_generator():
    """Generate question 

    Returns:
        dict: return question data in dict type
    """
    
    NUM_OPTIONS = range(5)  # set the quantity of answer options
    question_data_dict = {}  # Question data will be stored here.
    answer_option_list = []  # Answer options will be stored here
    input_question = input('\nDigite a pergunta: ')  

    for answer_index in NUM_OPTIONS:   
        # Here the user can generate the answer options and add to answer_option_list
        answer_option = input(f'Digite uma opção. {answer_index}) ')
        answer_option_list.append(answer_option)

    while True:  # treating right_option input
        # index of correct answer 
        correct_answer_index = input('\nDigite o index da opção correta: ')

        try:
            int(correct_answer_index)  #converting for int for treat the input

            if int(correct_answer_index) in NUM_OPTIONS:
                break
            elif int(correct_answer_index) not in NUM_OPTIONS:
                print(
                    '\nVocê digitou um índice inexistente.',
                       sep = '', end = 2*'\n'
                       )
                continue

        except:
            print(
                '\nDigite apenas o número do índice.', 
                  sep = '', end = 2*'\n'
                  )
            continue
    
    cls()

    # Now we will fill question the question data in question dict.
    question_data_dict.setdefault('question', input_question)
    question_data_dict.setdefault('options', answer_option_list)
    question_data_dict.setdefault('right option', correct_answer_index)

    return question_data_dict


def run_question():
        """ This function is responsible for running the question and
            check the user's answer.
        """
        
        answer = input('Digite a opção correta: ')
        print()

        if answer == question['right option']:
            print('Parabéns! 😸', end=2*'\n')
            
            global number_of_correct_answers 
            number_of_correct_answers += 1

        else:
            print(
                 f"Errou ❌. \nA resposta correta é a alternativa " \
                    f"{question['right option']}", end=2*'\n'
                  )

while True:  # Main loop
    questions_lists = []  # store generated questions

    while True:  # Loop for treat user input
        number_of_questions = input('Quantas questões deseja incluir? ')
        # Allow user to choose the number of question they want

        try:
            number_of_questions_int = int(number_of_questions)
            break
        except TypeError:
            print('\nDigite apenas números inteiros', 
                '\n', sep='')
            continue
        except:
            print('\nErro desconhecido de entrada, tente novamente.',
                '\n', sep='')
            continue


    number_of_correct_answers = 0  
    grade = number_of_questions_int - number_of_correct_answers # shows the user's grade

    for i in range(number_of_questions_int):
        # Generates the number of questions asked

        question = question_generator()
        questions_lists.append(question)  # Save the question in a list

    for question in questions_lists:
        # Now we'll run the question for the user be able to respond
        print(question['question'], end='\n')

        for list_index, answer_option in enumerate(question['options']):
            # Shows the index and options for the user can remmember right_option index
            print(f'{list_index}) {answer_option}')

        run_question()


    # Final result :
    print('\n', 20*'-', '\n', sep='')
    print(f'Sua nota final é {number_of_correct_answers} de {number_of_questions_int}.\n')

    if number_of_correct_answers >= number_of_questions_int/2:
        print('Parabéns, você tirou uma nota acima da média. 🎉🎉\n')
    else:
        print('Você tirou uma nota abaixo da média. 😢😢\n')


    
    print('Deseja jogar novamente?\n')  #Ask to user if they want to play again.

    play_again = input('Digite "sim" para jogar novamente, ou apenas pressione Enter para sair: ').lower()

    if play_again == 'sim':
        cls()
        continue  # restart the game
    else:
        break  # Closes the program