#Elabore um programa que calcule o valor a ser pago por um produto, 
#considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros

preco = float(input('Valor a ser pago no produto escolhido da loja: R$'))
pergunta = int(input('''
1– à vista dinheiro/cheque: 10% de desconto
2– à vista no cartão: 5% de desconto
3– em até 2x no cartão: preço formal 
4– 3x ou mais no cartão: 20% de juros
Opção: '''))
print('-' * 30)
op1 = preco - (preco / 100) * 10
op2 = preco - (preco / 100) * 5
op3 = preco 
op4 = preco + (preco / 100) * 20

#condições

if pergunta == 1:
    print(f'O preço final terá um desconto de 10%, sendo assim R${op1:.2f}.')
elif pergunta == 2:
    print(f'O preço final terá um desconto de 5%, sendo assim R${op2:.2f}.')
elif pergunta == 3:
    print(f'O produto poderá ser parcelado em até 2x à preço normal de R${op3:.2f}.')
elif pergunta == 4:
    print(f'O produto poderá ser parcelado em 3x ou mais com juros de 20%, sendo assim, o preço\nserá de R${op4:.2f}.')
    print('-' * 30)
    parcelas = int(input('INSIRA O NÚMERO DE PARCELAS: \n'))
    if (parcelas >= 3) and (parcelas < 13):
        print(f'O valor das parcelas será de R${op4 / parcelas :.2f}')
    else:
        print('As parcelas vão de 3 até 12, insira uma quantidade adequada de parcelas.')
else:
    print('--- INSIRA UM VALOR VÁLIDO ---')
