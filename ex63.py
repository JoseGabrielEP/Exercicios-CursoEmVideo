# Escreva um programa que leia um número
#N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
#0 – 1 – 1 – 2 – 3 – 5 – 8

print('---FIBONACCI---')

n = int(input('Quantos algarismos da sequência de FIBONACCI deseja ver: '))
termo = 0
termo2 = 1
contador = 3

print('INÍCIO')
print(termo)
print(termo2)

while contador <= n:
    termo3 = termo + termo2
    print(termo3)
    contador += 1 
    termo = termo2
    termo2 = termo3

print('FIM')
