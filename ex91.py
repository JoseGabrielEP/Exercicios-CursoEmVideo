#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#  Guarde esses resultados em um dicionário em Python.
#  No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter
from time import sleep

tabela = dict()
resultados = list()

while True:
    if len(tabela) < 4:
        dado = randint(1,6)
        if dado not in resultados:
            tabela[input('Insira seu nome: ')] = dado
            print(f'O resultado do dado foi {dado}.')
            resultados.append(dado)
    else:
        break

tabela_ordenada = sorted(tabela.items(), key= itemgetter(1), reverse= True)

print('A ordem dos resultados ficou:')
for y in range(0,4):
    print(f'{tabela_ordenada[y][0]} = {tabela_ordenada[y][1]}')
    sleep(1)

print(f'Parabéns {tabela_ordenada[0][0]}!!')