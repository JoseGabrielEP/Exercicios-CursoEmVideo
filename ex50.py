#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado for ímpar, desconsidere-o.

lista = []

for x in range(0,7):
    n = int(input('Insira um valor inteiro: '))
    if (n % 2) == 0:
        lista.append(n)
soma = sum(lista)
print(f'A soma dos números pares que você inseriu é {soma}.')