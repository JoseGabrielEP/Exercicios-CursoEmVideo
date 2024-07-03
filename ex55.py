#Faça um programa que leia o peso de cinco pessoas. 
#No final, mostre qual foi o maior e o menor peso lidos.

lista_pesos = []

for x in range(0,5):
    print('-'*30)
    peso = float(input(f'Insira o peso da {x + 1}ª pessoa: '))
    lista_pesos.append(peso)
lista_pesos.sort()
print(f'O maior peso foi de {lista_pesos[4]} e o menor foi {lista_pesos[0]}.')