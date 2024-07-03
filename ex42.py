#Refaça o DESAFIO 35 dos triânguloswq2
#acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes
reta1 = float(input('Insira o valor de uma reta: \n'))
reta2 = float(input('Insira o valor de uma reta: \n'))
reta3 = float(input('Insira o valor de uma reta: \n'))

calculo1= reta1 + reta2 > reta3
calculo2 = reta1 + reta3 > reta2
calculo3 = reta3 + reta2 > reta1

if (calculo1 == True) and (calculo2 == True) and (calculo3 == True):
    print('Um triângulo pode ser formado com as medidas dadas!')
    if (reta1 == reta2 != reta3) or (reta2 == reta3 != reta1) or (reta3 == reta1 != reta2):
        print('É um triângulo ISÓSCELES.')
    elif (reta1 == reta3) and (reta3 == reta2) and (reta2 == reta1):
        print('É um triângulo EQUILÁTERO.')
    elif (reta1 != reta2) and (reta1 != reta3) and (reta2 != reta3):
        print('É um triângulo ESCALENO.')
else:
    print('Não é possível formar um triângulo com as medidas dadas!')