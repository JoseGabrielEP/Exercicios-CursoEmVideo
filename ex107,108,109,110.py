#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
#  Faça também um programa que importe esse módulo e use algumas dessas funções.
from modulo111 import moedas
from modulo111 import dados

num = dados.leiaDinheiro()
descaum = int(input('De quando serão os aumentos e descontos? %'))
dob = moedas.dobro(num, format=True)
met = moedas.metade(num, format=True)
aum = moedas.aumento(num,descaum ,format=True)
des = moedas.desconto(num,descaum,  format=True)

print(f'O dobro de {num}R$ é {dob}.')
print(f'A metade de {num}R$ é {met}.')
print(f'Se for feito um aumento de {descaum}% o preço ficará {aum}.')
print(f'Se for feito um desconto de {descaum}% o preço ficará {des}.')

print('=-'*15)

moedas.resumo(num, descaum)
