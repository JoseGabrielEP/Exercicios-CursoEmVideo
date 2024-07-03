#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []

for x in range(0,5):
    print('=-'*15)
    lista.append(int(input('Insira um número: ')))
print('=-'*15)
lista.sort()
print(lista)
print(f'O menor valor é {lista[0]} na posição 0, e o maior é {lista[4]} na posição 4')