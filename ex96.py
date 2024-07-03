#Faça um programa que tenha uma função chamada área(),
#  que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(l, c):
    area_c = l * c
    print(f'A área do terreno com largura de {l}m, e comprimento de {c}m, é\nde {area_c:.2f}m2.')
    print('=-'*20)

continuar = 'S'

while continuar not in 'N':
    if continuar in 'S':
        largura = float(input('Insira a largura do terreno: '))
        comprimento = float(input('Insira o comprimento do terreno: '))
        area(largura, comprimento)
        continuar = input('Quer continuar calculando áreas? [S/N]: ').upper().strip()[0]
    elif continuar not in 'NS':
        continuar = input('Não entendi. Quer continuar calculando áreas? [S/N]: ').upper().strip()[0]

print('=-'*20)
print('FIM DO PROGRAMA')