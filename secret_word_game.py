"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = "gaivota"
dica = "é um animal"
os.system('cls')
texto_dica = f'A dica é "{dica}" com {len(palavra_secreta)} letras. Boa sorte =)'
palavra = len(palavra_secreta) * '*'
repeticoes = 1 # Número de tentativas que a pessoa tentou.

print(f'{texto_dica:-^25}')


while True:

    letra_input = input('Digite uma letra: ')
    if len(letra_input) != 1:
        print('Digite apenas uma letra.')
        continue

    elif letra_input.isalpha() is False:
        print('Digite apenas letras.')
        continue

    if letra_input.isupper():
        print('Digite apenas letras minúsculas.')
        continue

    i = 0    
    if letra_input in palavra_secreta:
        while i < len(palavra_secreta):  
            index = palavra_secreta.find(letra_input)
            palavra = palavra[:index] + letra_input + palavra[index + 1:]
            
            # Agora vamos concatenar e contruindo a palavra letra a letra.
            if index <= i <len(palavra_secreta):  
                index = palavra_secreta.find(letra_input, i)
                if index != -1:
                    palavra = palavra[:index] + letra_input + palavra[index + 1:]

            i += 1
    
    print(palavra)

    if palavra == palavra_secreta:
        os.system('cls')
        parabens = f'Parabéns, você ganhou! A palavra era "{palavra_secreta}" '\
            f'e você adivinhou em {repeticoes} tentativas.'
        print('') # pulando linha
        print(f'{parabens:-^55}')

        # Zerando as variáveis.
        palavra_secreta = input('Digite a palavra secreta: ').lower()
        dica = input('Digite a dica: ')
        palavra = len(palavra_secreta) * '*'
        repeticoes = 1 # Número de tentativas que a pessoa fez.
        os.system('cls')
        texto_dica = f'A dica é "{dica}" com {len(palavra_secreta)} letras. Boa sorte =)'
        print(f'{texto_dica:-^25}')

    


# Solução do professor (muito mais simples)-------------------------

# import os

# palavra_secreta = 'perfume'
# letras_acertadas = ''
# numero_tentativas = 0

# while True:
#     letra_digitada = input('Digite uma letra: ')
#     numero_tentativas += 1

#     if len(letra_digitada) > 1:
#         print('Digite apenas uma letra.')
#         continue

#     if letra_digitada in palavra_secreta:
#         letras_acertadas += letra_digitada

#     palavra_formada = ''
#     for letra_secreta in palavra_secreta:
#         if letra_secreta in letras_acertadas:
#             palavra_formada += letra_secreta
#         else:
#             palavra_formada += '*'

#     print('Palavra formada:', palavra_formada)

#     if palavra_formada == palavra_secreta:
#         os.system('clear')
#         print('VOCÊ GANHOU!! PARABÉNS!')
#         print('A palavra era', palavra_secreta)
#         print('Tentativas:', numero_tentativas)
#         letras_acertadas = ''
#         numero_tentativas = 0