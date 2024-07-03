#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#O programa vai ler o nome do jogador e quantas partidas ele jogou.
#Depois vai ler a quantidade de gols feitos em cada partida.
#No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()

jogador['Nome'] = input('Insira o nome do jogador: ')
jogador['Quantidade de Partidas'] = int(input('Insira a quantidade de partidas jogadas: '))
jogador['Total de Gols'] = 0

for x in range(0, jogador['Quantidade de Partidas']):
    gol = int(input(f'Insira a quantidade de gols feitos na {x + 1}ª partida: '))
    jogador[f'Gol na {x+1}ª partida'] = gol
    jogador['Total de Gols'] += gol

print('=-'*15)

for k,v in jogador.items():
    print(f'{k} = {v}')

print('=-'*15)