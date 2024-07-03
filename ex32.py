#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('Insira um ano: \n'))
if ano % 4 != 0:
    print(f'O ano {ano} não é bissexto!')
else:
     print(f'O ano {ano} é bissexto!')