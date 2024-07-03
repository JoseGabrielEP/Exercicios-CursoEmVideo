#Aprimore o desafio 93 para que ele funcione com vários jogadores,
#incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogador = dict()
time = list()

menu = input('Começar cadastro? [S/N]: ').upper().strip()[0]

while True:
    if menu in 'S':
        jogador['Nome'] = input('Insira o nome do jogador: ')
        jogador['Quantidade de Partidas'] = int(input('Insira a quantidade de partidas jogadas: '))
        jogador['Total de Gols'] = 0
        for x in range(0, jogador['Quantidade de Partidas']):
            gol = int(input(f'Insira a quantidade de gols feitos na {x + 1}ª partida: '))
            jogador[f'Gol na {x+1}ª partida'] = gol
            jogador['Total de Gols'] += gol
        time.append(jogador.copy())
        menu = input('Continuar cadastro? [S/N]: ').upper().strip()[0]
    elif menu in 'N':
        break
    else:
        menu = input('Não entendi. prosseguir com cadastro? [S/N]: ').upper().strip()[0]

print('=-'*15)
for x in range(0, len(time)):
    print(f'{x + 1}- {time[x]['Nome']}')

opcao = int(input('Insira o jogador que quer ler as estátisticas (0 para encerrar): '))
while True:
    if opcao > len(time):
        opcao = int(input('Número inválido. Insira outro jogador ou encerre (0 para encerrar): '))
    elif opcao != 0 :
        print('=-'*15)
        for k,v in time[opcao-1].items():
            print(f'{k} = {v}')
        print('=-'*15)
        opcao = int(input('Insira outro jogador ou encerre (0 para encerrar): '))
    elif opcao == 0:
        break
    

print('=-'*15)
print('PROGRAMA ENCERRADO')
print('=-'*15)