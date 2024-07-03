#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
#  o nome de um jogador e quantos gols ele marcou.
#  O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha():
    n = input('Diga o nome do jogador se souber: ').strip().title()
    g = str(input('Insira a quantidade de gols marcados pelo jogador:')).strip()
    if n == '':
        n = '<DESCONHECIDO>'
        if g == '':
            g = 0
            print(f'O jogador {n}, marcou {g} gols.')
        elif g.isnumeric():
            g = int(g)
            print(f'O jogador {n}, marcou {g} gols.')
        else:
            g = 0
            print(f'O jogador {n}, marcou {g} gols.')
    else:
        if g == '':
            g = 0
            print(f'O jogador {n}, marcou {g} gols.')
        elif g.isnumeric():
            g = int(g)
            print(f'O jogador {n}, marcou {g} gols.')
        else:
            g = 0
            print(f'O jogador {n}, marcou {g} gols.')


ficha()







    