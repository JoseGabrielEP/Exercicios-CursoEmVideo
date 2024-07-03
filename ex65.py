#Crie um programa que leia vários números inteiros pelo teclado. 
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

valor = int(input('INSIRA UM NÚMERO: '))
opcao = input('Quer prossegui? [S/N]: ').upper().strip()[0]
lista = []
lista.append(valor)

while opcao in 'S':
    valor = int(input('INSIRA MAIS UM NÚMERO: '))
    lista.append(valor)
    opcao = input('Quer prossegui? [S/N]: ').upper().strip()[0]

print('-' * 45)
print('Processo Encerrado')
print('-' * 45)

media = sum(lista) / len(lista)
print(f'A média dos {len(lista)} valores foi {media:.2f}.')
lista.sort()
print(f'O maior valor citado foi {lista[len(lista) - 1]} e o menor foi {lista[0]}')