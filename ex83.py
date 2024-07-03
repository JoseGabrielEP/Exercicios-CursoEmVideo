#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

from time import sleep

expressao = input('Insira uma expressão matemática: ')
print('O sistema irá verificar se a expressão está com os parênteses fechados adequadamente.')

sleep(1.5)

cont_aberto = expressao.count('(')
cont_fechado = expressao.count(')')

if cont_aberto != cont_fechado:
    print('EXPRESSÃO INCORRETA.')
else:
    print('Expressão CORRETA.')