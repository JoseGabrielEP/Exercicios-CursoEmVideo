#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
#  A primeira função vai sortear 5 números e vai colocá-los dentro da lista
#  e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint


numeros = list()

def sorteio():
    for x in range(0, 5):
       n = randint(0,10)
       numeros.append(n)


def somaPar(lst):
    pares = list()
    for i in lst:
        if i % 2 == 0:
            pares.append(i)
    print(f'Os números sortesados foram {lst}, e a soma dos pares foi {sum(pares)}.')

sorteio()
somaPar(numeros)
    