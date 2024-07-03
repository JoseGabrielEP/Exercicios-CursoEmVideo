#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#No final, mostre os 10 primeiros termos dessa progressão.
#AGORA UTILIZANDO WHILE

print('-----PROGRESSÃO ARITMÉTICA-----')
print('10 PRIMEIROS TERMOS')

p_termo = int(input('Insira o primeiro termo da P.A: '))
razao = int(input('Insira a Razão desta P.A: '))
contador = 1

print('INÍCIO')
print(p_termo)

while contador < 10:
    contador = contador + 1
    p_termo = p_termo + razao
    print(p_termo)

print('FIM')