# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random

print('-='*15)
print('PAR OU ÍMPAR')
print('-='*15)

n_user = int(input('Insira um número: '))
opcao = int(input('[PAR = 1][ÍMPAR = 2] QUAL SUA OPÇÃO? escreva: '))
contagem = 0
contagem_par = 0
contagem_imp = 0

n_pc = random.randint(0, 10)

if (opcao == 1) or (opcao == 2):
    while True:
        print('-=' * 15)
        if ((n_user + n_pc) % 2 == 0 ) and opcao == 1: #VITÓRIA PAR
            print(f'A escolha do PC foi {n_pc}, que somado a sua escolha é PAR! VOCÊ VENCEU!')
            contagem += 1
            contagem_par += 1
            n_pc = random.randint(0, 10)
            n_user = int(input('Insira outro número: '))
            opcao = int(input('[PAR = 1][ÍMPAR = 2] QUAL SUA OPÇÃO? escreva: '))
        elif ((n_user + n_pc) % 2 != 0) and opcao == 2: #VITÓRIA ÍMPAR
            print(f'A escolha do PC foi {n_pc}, que somado a sua escolha é ÍMPAR! VOCÊ VENCEU!')
            contagem += 1
            contagem_imp += 1
            n_pc = random.randint(0, 10)
            n_user = int(input('Insira outro número: '))
            opcao = int(input('[PAR = 1][ÍMPAR = 2] QUAL SUA OPÇÃO? escreva: '))
        else: #DERROTA
            print(f'Você Perdeu! O pc escolheu o número {n_pc}.')
            break

else:
    print('Insira uma opção adequada.')

print('-=' * 15)
print('FIM DE JOGO')
print('-=' * 15)
print(f'''Estátisticas:
Vitórias: {contagem}
Vitórias ímpares: {contagem_imp}
Vitórias pares: {contagem_par}\n''')