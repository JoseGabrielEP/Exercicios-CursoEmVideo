#Crie um programa que vai ler vários números e colocar em uma lista.                 
# Depois disso, mostre:                   
# A) Quantos números foram digitados.                                                                                                                    
# B) A lista de valores, ordenada de forma decrescente.   
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
n = int(input('Insira um número: '))
opcao = input('Quer continuar? [SIM/NÃO]: ').title().strip()[0]
lista.append(n)

while True:
    if opcao not in 'N':
        n = int(input('Insira outro número: '))
        lista.append(n)
        opcao = input('Quer continuar? [SIM/NÃO]: ').title().strip()[0]
    else:
        break

lista.sort(reverse=True)

print('=-'*15)
print(f'Foram digitados {len(lista)} números.')
print('=-'*15)
print(f'A lista de forma decrescente é {lista}')
print('=-'*15)

if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')