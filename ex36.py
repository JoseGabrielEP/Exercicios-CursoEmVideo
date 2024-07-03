# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
from time import sleep

nome = input('Insira seu nome: \n').title()
casa_valor = float(input('Insira o valor para a compra do imóvel: R$'))
salario_comprador = (float(input('Insira o valor do seu salário: R$')) / 100) * 30
financiamento_tempo = int(input('Insira em quantos anos você pretende financiar o imóvel: \n')) * 12

valor_mensal = casa_valor / financiamento_tempo

#condições
if financiamento_tempo <= 180:
    print('-----CALCULANDO-----')
    sleep(2)
    if valor_mensal < salario_comprador:
        print(f'Parabéns {nome}, seu empréstimo será aprovado! O valor das parcelas será de R${valor_mensal:.2f}')
        print('-----Se direcione a uma AGÊNCIA DO BANCO-----')
    elif valor_mensal == salario_comprador:
        print(f'{nome}, você possui capital o suficiente para realizar o empréstimo, \n porém é um investimento de grande risco.')
    else:
        print(f'Infelizmente {nome}, seu empréstimo foi negado, deviso ao valor das parcelas de R${valor_mensal:.2f} ser maior que 30% de seu salário.')
        print('-----Em caso de dúvidas se direcione a uma AGÊNCIA DO BANCO-----')
else:
    sleep(1.5)
    print('Nosso prazo máximo de financiamento é de 15 anos. -----REINICIE O PROCESSO----- ')