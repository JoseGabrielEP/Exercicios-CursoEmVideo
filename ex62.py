#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#No final, mostre os 10 primeiros termos dessa progressão.
#AGORA UTILIZANDO WHILE
#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
#O programa encerrará quando ele disser que quer mostrar 0 termos.

print('-----PROGRESSÃO-ARITMÉTICA-----') #TITULO

p_termo = int(input('Insira o primeiro termo da progressão aritmética: '))
razao = int(input('Insira a razão da progressão aritmética: '))
confirmacao = ''
print('Vizualizar os 10 primeiros termos [S/N]:  ')
pergunta = input('').upper().strip()[0]
confirmacao = pergunta

while confirmacao not in 'N':
    print(p_termo)
    for x in range(0,10):
        p_termo += razao
        print(p_termo)
    pergunta = input('Vizualizar mais 10 termos [S/N]:\n').upper().strip()[0]
    confirmacao = pergunta

print('-----FIM-DO-PROCESSO-----')

#CORRIGIR ATIVIDADE CORRIGIR ATIVIDADE CORRIGIR ATIVIDADE CORRIGIR ATIVIDADE
