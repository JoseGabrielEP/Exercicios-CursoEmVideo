#Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
#calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida

altura = float(input('Insira a sua altura: \n'))
peso = float(input('Insira o seu peso: \n'))

imc = peso / (altura ** 2)

#condicionais

if imc < 18.5:
    print(f'ABAIXO DO PESO, SEU IMC FOI DE {imc:.2f}!')
elif imc <= 25:
    print(f'PESO IDEAL, SEU IMC É DE {imc:.2f}!')
elif imc <= 30:
    print(f'VOCÊ ESTÁ EM SITUAÇÃO DE SOBREPESO, SEU IMC É DE {imc:.2f}!')
elif imc <= 40:
    print(f'SITUAÇÃO DE OBESIDADE, SEU IMC É DE {imc:.2f}!')
elif imc > 40:
    print(f'PROCURE UM MÉDICO, SITUAÇÃO DE OBESIDADE MÓRBIDA, SEU IMC É DE {imc:.2f}!')