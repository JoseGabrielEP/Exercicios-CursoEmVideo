#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais

lista = []
n = int(input('Insira um valor inteiro: \n'))
n2 = int(input('Insira um valor inteiro: \n'))

lista.append(n)
lista.append(n2)

if n != n2:
    lista.sort()
    print(f'O maior número é {lista[1]} e o menor é {lista[0]}')
else:
    print('Os dois números são iguais!')