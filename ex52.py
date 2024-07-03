#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input('Insira um número: '))
tot = 0
for x in range(1, n + 1):
    if n % x == 0:
        print("\033[34m", end= ' ')
        tot = tot + 1 
    else :
        print("\033[m", end= ' ')
    print(f'{x}', end= ' ')

if tot > 2:
    print(f'\nO número {n} não é primo, pois é divísivel {tot} vezes')
else:
    print(f'\nO número {n} é divísivel apenas {tot} vezes, sendo assim ele é primo, pois é divísivel apenas por 1 e ele mesmo.')