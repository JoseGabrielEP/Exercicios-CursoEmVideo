#Faça um programa que tenha uma função chamada escreva(),
#  que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. 

def escreva(msg):
    print('')
    print('=-' * ((len(msg)//2) + 1))
    print(msg)
    print('=-' * ((len(msg)//2) + 1))
    print('')

#programa principal
continuar = 'S'
while continuar not in 'N':
    if continuar == 'S':
        mensagem = input('Insira uma mensagem: ').capitalize().strip()
        escreva(mensagem)
        continuar = input('Quer continuar? [S/N]: ').strip().upper()[0]
    elif continuar not in 'NS':
        continuar = input('Não entendi. Quer continuar? [S/N]: ').strip().upper()[0]

escreva('Fim do Programa')