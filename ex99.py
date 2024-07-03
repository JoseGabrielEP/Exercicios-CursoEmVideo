# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(lst):
    print('=-'*15)
    lst.sort()
    print(f'Foram informados {len(lst)} valores ao todo.')
    print(f'O maior valor é {lst[len(lst)-1]}')


quantidade = int(input('Quantos números você quer comparar? '))
lista = list()

for x in range(0, quantidade):
    n = int(input(f'Insira o {x+1}ª número para a comparação: '))
    lista.append(n)

maior(lista)