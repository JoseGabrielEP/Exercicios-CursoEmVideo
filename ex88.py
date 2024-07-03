#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
# cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

while True:
    quantidade = int(input('Insira quantos palpites você deseja que sejam formados (0 a 10): '))
    if quantidade in range(0,11):
        print('=-'*20)
        print(f'PALPITE PARA {quantidade} JOGO(s) DA MEGA SENA!')
        print('=-'*20)

        Tpalpites = list()
        nrepetido = list()

        for x in range(0, quantidade):
            palpite = list()
            while len(palpite) < 6:
                num = randint(1,60)
                if (num not in nrepetido) and (num not in palpite):
                    palpite.append(num)
                    nrepetido.append(num)
                    palpite.sort()
            Tpalpites.append(palpite[:])
            palpite.clear

        print('=-'*15)
        for y in range(0,quantidade):
            sleep(0.75)
            print(f'Jogo {y + 1}: {Tpalpites[y]}')

        print('BOA SORTE!')
        break
    else:
        print('=-'*15)
        print('Insira uma quantidade adequada.')
        print('=-'*15)
        