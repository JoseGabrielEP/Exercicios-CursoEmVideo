# Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, 
# que é a condição de parada. No final, mostre quantos números foram digitados 
# e qual foi a soma entre elas (desconsiderando o flag).

n = int(input('Insira um número [999 para encerrar.]: '))
contador = 0
lista = []
lista.append(n)

if n != 999:
    while True:
        n = int(input('Insira mais um número [999 para encerrar.]: '))
        if n == 999:
            break
        else:
            lista.append(n)
            contador += 1

print('-=' * 30)
print('FIM DO PROCESSO')

soma = sum(lista)

print(f'A soma dos {contador} algarismos digitados é {soma}!')