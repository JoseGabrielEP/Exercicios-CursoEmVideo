#Faça um programa que leia um número qualquer e mostre o seu fatorial.

n = int(input('Dígite um número: '))
multiplicador = n - 1
original = n

while multiplicador > 0:
    n = n * (multiplicador)
    multiplicador = multiplicador - 1

print('-' * 30) 
print(f'O resultado fatorial de {original}! é {n}.')

