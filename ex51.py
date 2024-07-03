#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#No final, mostre os 10 primeiros termos dessa progressão.

print('-' * 30)
print('10 PRIMEIROS TERMOS DE UMA P.A')
print('-' * 30) 

prim_t = int(input('Insira o primeiro termo de uma progressão aritmética: '))
razao = int(input('Insira a razão de uma progressão aritmética: '))

print('-' * 30)
print('Os 10 primeiros termos da progressão aritmética são:')
for x in range(prim_t, (razao * 10) + 1, razao):
    print(x)
print('---FIM---')