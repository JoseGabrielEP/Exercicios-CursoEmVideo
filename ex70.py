#Crie um programa que leia o nome e o preço de vários produtos.
#O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

print('=-' * 15)
print('MERCADÃO')
print('=-' * 15)

nome = input('Insira o nome do produto sendo comprado: ')
preco = float(input('Insira o preço do produto: R$'))
opcao = input('Quer continuar? [Sim/Não]: ').upper().strip()[0]
print('=-'*15)
tot_preco = 0
maior1000 = 0
nome_barato = nome
preco_barato = preco
while opcao not in 'N':
    nome = input('Insira o nome do produto sendo comprado: ')
    preco = float(input('Insira o preço do produto: $'))
    opcao = input('Quer continuar? [Sim/Não]: ').upper().strip()[0]
    tot_preco += preco
    print('=-'*15)
    if preco >= 1000:
        maior1000 += 1
    elif preco_barato > preco:
        preco_barato = preco
        nome_barato = nome
    

print('PROCESSO ENCERRADO.')
print(f'O total gasto na compra foi R${tot_preco}')
print('=-'*15)
print(f'Foram comprados {maior1000} produtos mais caros que R$1000')
print('=-'*15)
print(f'O produto mais barato é {nome_barato}, custando R${preco_barato}.')