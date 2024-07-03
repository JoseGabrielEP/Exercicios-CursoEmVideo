#Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
lista_par = []
lista_imp = []

n = int(input('Insira um número: '))
opcao = input('Deseja continuar? [S/N]: ').title().strip()[0]

while True:
    print('=-'*15)
    if opcao not in 'N':
        n = int(input('Insira um número: '))
        opcao = input('Deseja continuar? [S/N]: ').title().strip()[0]
        lista.append(n)
        if n % 2 == 0:
            lista_par.append(n)
        else:
            lista_imp.append(n)
    else:
        break

print(f'Lista Normal: {lista}')
print(f'Lista Par: {lista_par}')
print(f'Lista Ímpar: {lista_imp}')