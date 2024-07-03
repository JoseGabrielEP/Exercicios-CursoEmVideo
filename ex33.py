#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.



n1 = float(input('Insira um número qualquer: \n'))
n2 = float(input('Insira um número qualquer: \n'))
n3 = float(input('Insira um número qualquer: \n'))

lista = [n1,n2,n3]
lista.sort()
print(f'O maior valor da lista é {lista[2]} e o menor é {lista[0]}')