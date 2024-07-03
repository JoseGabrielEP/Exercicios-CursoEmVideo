# Faça um programa que calcule a soma entre todos os números que são múltiplos 
# de três e que se encontram no intervalo de 1 até 500.
soma = 0
cont = 0
for x in range(1,501,2):
    if (x % 3) == 0:
        cont = cont + 1
        soma = soma + x
print(f'A soma de todos os {cont} valores é {soma}')