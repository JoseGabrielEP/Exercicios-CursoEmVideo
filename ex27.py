#Faça um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Insira o seu nome completo: \n').strip().title()
divisão = nome.split()
print(f'O seu primeiro nome é {divisão[0]}, e seu último nome é {divisão[len(divisão)-1]}')