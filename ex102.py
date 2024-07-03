# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show,
# que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, opc = ''):
    if opc in 'N':
        for x in range(num, 1, -1):
            num *= x - 1
        return num
            
    
    elif opc in 'S':
        print('=-'*20)
        for x in range(num,1,-1):
            print(f'-> {num}', end='')
            num *= x - 1
        print('')
        print('=-'*20)
        return num
    

n = int(input('Insira um número para ver fatorial: '))
opcao = input('Deseja ver o cálculo? [N/S]: ').strip().upper()[0]


print(f'O resultado é {fatorial(n,opcao)}.')