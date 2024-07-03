#Crie um programa onde o usuário possa digitar sete valores numéricos 
#e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
#No final, mostre os valores pares e ímpares em ordem crescente.

num = [[],[]]
n = 0
for x in range(0,7):
    n = int(input('Insira um número: '))
    if n % 2 == 0:
        num[1].append(n)
    else:
        num[0].append(n)

num[1].sort()
num[0].sort()

print(f'A lista de pares é {num[1]}.')
print(f'A lista de ímpares é {num[0]}.')