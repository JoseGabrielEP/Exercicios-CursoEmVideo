# Crie um programa que faça o computador jogar Jokenpô com você.
from random import choice

jokenpo = ['Pedra', 'Papel', 'Tesoura']
escolha = input('''
Insira sua escolha entre:
Pedra
Papel
Tesoura
Sua Opção: ''').title().strip()

sorteio = choice(jokenpo)
print('-' * 30)

#condições

if sorteio == escolha:
    print('---EMPATE-JOGUE-NOVAMENTE---')
elif (sorteio == jokenpo[0]) and (escolha == 'Papel'):
    print('A máquina escolheu Pedra.')
    print('-' * 30)
    print('Você Ganhou!')
elif (sorteio == jokenpo[1]) and (escolha == 'Tesoura'):
    print('A máquina escolheu Papel.')
    print('-' * 30)
    print('Você Ganhou!')
elif (sorteio == jokenpo[2]) and (escolha == 'Pedra'):
    print('A máquina escolheu Tesoura.')
    print('-' * 30)
    print('Você Ganhou!')
elif (sorteio == jokenpo[2]) and (escolha == 'Papel'):
    print('A máquina escolheu Tesoura.')
    print('-' * 30)
    print('Você Perdeu!')
elif (sorteio == jokenpo[1]) and (escolha == 'Pedra'):
    print('A máquina escolheu Papel.')
    print('-' * 30)
    print('Você Perdeu!')
elif (sorteio == jokenpo[0]) and (escolha == 'Tesoura'):
    print('A máquina escolheu Pedra.')
    print('-' * 30)
    print('Você Perdeu!')
else:
    print('---VERIFIQUE SE DIGITOU DE FORMA ADEQUADA---')