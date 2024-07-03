#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('Insira um número inteiro: \n'))
cálculo = num % 2 
if cálculo == 0:
    print('O número inserido é par!')
else: 
    print('O número inserido é ímpar!')