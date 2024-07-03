#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. 
#No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

n1 = int(input('Digíte os números: '))
n2 = int(input('Digíte os números: '))
n3 = int(input('Digíte os números: '))
n4 = int(input('Digíte os números: '))

tupla = (n1,n2,n3,n4)
lista = []

for numero in tupla:
    par = numero % 2
    if par == 0:
        lista.append(numero)

print(f'''Estátisticas:
Aparições número 9: {tupla.count(9)}
Posição número 3: {tupla.index(3)}
Números Pares: {lista}''')