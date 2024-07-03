#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = input('Insira seu nome completo:\n')
coerencia = nome.lower()
teste = 'silva' in coerencia
if teste == True:
    print('Você tem "Silva" no seu nome!')
else:
    print('Você não tem "Silva" no seu nome!')