# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import choice

#Variáveis
lista = [1,2,3,4,5,6,7,8,9,10]
escolha_pc = choice(lista)
escolha_user = int(input('Insira um número de 1 a 10: '))
contagem = 1

#Em caso de erro
while escolha_user != escolha_pc:
    escolha_pc = choice(lista)
    escolha_user = int(input('Você errou, Insira um número de 1 a 10: '))
    contagem = contagem + 1

#ACERTO
print(f'VOCê ACERTOU!!! Você levou {contagem} tentativas para acertar o número {escolha_pc}!')