#Escreva um programa em Python que leia um número inteiro qualquer 
#e peça para o usuário escolher qual será a base de conversão:
 #1 para binário, 2 para octal e 3 para hexadecimal.
n_user = int(input('Insira um número inteiro para conversão: \n'))
opção = int(input('''Escolha uma das opções:
1 - BINÁRIO
2 - OCTAL
3 - HEXADECIMAL 
Sua opção: ''' ))

if opção == 1:
    print(f'O número {n_user} em Binário é {bin(n_user)[2:]}.')
elif opção == 2:
    print(f'O número {n_user} em Octal é {oct(n_user)[2:]}.')
elif opção == 3:
    print(f'O número {n_user} em Hexadecimal é {hex(n_user)[2:]}')
else:
    print('Insira uma opção válida!')
print('---------FIM---------')