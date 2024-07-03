#Escreva um programa que faça o computador “pensar” em um número
# inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from emoji import emojize

numero_pc = randint(0,5)
numero_user = int(input('Insira um número de 0 a 5: \n'))
if numero_user == numero_pc:
    print(emojize('Parabéns você acertou o número :thumbs_up: '))
else:
    print(emojize('Você errou o número :thumbs_down:'))