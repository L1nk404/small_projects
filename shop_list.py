'''
Faça uma lista de compras com listas.
O usuário deve ter a possibilidade de inserir, apagar e listar valores
da sua lista.
Não permita que o programa quebre com erros de índices inexistentes na
lista.
'''
import os
lista = []

while True:
        
    entrada = input('[i]nserir, [a]pagar, [l]istar, [L]impar: ')

    if entrada == 'i':  #Inserir itens
        while True:     
            novo_item = input('Digite o item ou pressione [v] para voltar: ')
            os.system('cls')  # Limpar o programa       
            print()

            if novo_item == 'v':  #Retorna a entrada
                os.system('cls')
                break

            lista.append(novo_item)  #Acrescenta um novo item    

            for indice, item in enumerate(lista):   
                print(indice, item)     


    elif entrada == 'a':  #apagar itens
        while True:
            for indice, item in enumerate(lista):
                print(indice, item)     

            indice_apagar = input('Digite o número do item que deseja apagar'\
                                ' ou pressione [v] para voltar: ')
            os.system('cls')
            if indice_apagar == 'v':
                os.system('cls')
                break               

            try:
                item_apagar_int = int(indice_apagar)
                del lista[item_apagar_int]
            except ValueError:
                os.system('cls')
                print('Por favor, digite apenas números inteiros.') 
            except IndexError:
                os.system('cls')
                print('Índice não encontrado.')
            except Exception:
                os.system('cls')
                print('Erro desconhecido.') 



    elif entrada == 'l':  #listar itens
        print(20*'-')        

        for indice, item in enumerate(lista):
                print(f'{indice: <4}{item}')    

        print(20*'-')

    elif entrada == 'L':  #Limpar a lista
        lista.clear()
        os.system('cls')
        continue

    else:  #No caso de um comando desconhecido
        os.system('cls')
        continue