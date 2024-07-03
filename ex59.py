#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

#VARIAVEIS

print('----------CALCULADORA----------')
print('') #ESPAÇO

n1= float(input('Insira um número para calcular: '))
n2= float(input('Insira um número para calcular: '))
comparacao = []

opcao = int(input('''Qual opção deseja?
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Insira sua opção: '''))

#LOOP

while opcao != 5:
    if opcao == 1:
        print('-' * 30)
        print(f'{n1} + {n2} = {n1 + n2}')
        print('-' * 40)
        opcao = int(input('''Qual opção deseja agora?
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Insira sua opção: '''))
    elif opcao == 2:
        print('-' * 30)
        print(f'{n1} x {n2} = {n1 * n2}')
        print('-' * 40)
        opcao = int(input('''Qual opção deseja agora?
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Insira sua opção: '''))
    elif opcao == 3:
        print('-' * 30)
        comparacao.append(n1)
        comparacao.append(n2)
        comparacao.sort()
        print(f'O maior número é {comparacao[1]}')
        print('-' * 30)
        opcao = int(input('''Qual opção deseja agora?
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Insira sua opção: '''))
        print(f'O maior número é {comparacao[1]}')
    elif opcao == 4:
        print('-' * 30)
        n1= float(input('Insira um número novo para calcular: '))
        n2= float(input('Insira um número novo para calcular: '))
        opcao = int(input('''Qual opção deseja agora?
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Insira sua opção: '''))
        print('-' * 30)
    else:
        print('Insira um número ADEQUADO')
        print('-' * 30)
        opcao = int(input('''Qual opção deseja agora?
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Insira sua opção: '''))
        
#CASO OPÇÃO 5

print('-----FIM DO PROCESSO-----')