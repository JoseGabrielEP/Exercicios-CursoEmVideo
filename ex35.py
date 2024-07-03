# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.
from emoji import emojize

reta1 = float(input('Insira o valor de uma reta: \n'))
reta2 = float(input('Insira o valor de uma reta: \n'))
reta3 = float(input('Insira o valor de uma reta: \n'))

calculo1= reta1 + reta2 > reta3
calculo2 = reta1 + reta3 > reta2
calculo3 = reta3 + reta2 > reta1

if (calculo1 == True) and (calculo2 == True) and (calculo3 == True):
    print(emojize('\033[0;30;42m Um triângulo pode ser formado com as medidas dadas! :thumbs_up:'))
else:
    print(emojize('\033[0;30;41m Não é possível formar um triângulo com as medidas dadas! :thumbs_down:'))

print('---------------------------------------------------------')
 