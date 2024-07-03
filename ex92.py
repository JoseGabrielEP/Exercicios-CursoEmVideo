#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
#Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

informações = dict()

informações['Nome'] = input('Insira seu nome: ')
informações['Nascimento'] = int(input('Insira seu ano de nascimento: '))
informações['CTPS'] = int(input('Insira o número de sua carteira de trabalho (0 se não possuir): '))

if informações['CTPS'] != 0:
    informações['Salário'] = float(input('Insira o seu Salário: '))
    informações['Ano Contribuição'] = int(input('Insira o ano em que começou a contribuir: '))
    idade = 2024 -informações['Nascimento']
    informações['Idade Aposentadoria'] = (2024 - informações['Ano Contribuição']) + 35 + idade

elif informações['CTPS'] == 0:
    informações['CTPS'] = 'Não possui Carteira de Trabalho.'

for k,v in informações.items():
    if k != 'Idade Aposentadoria':
        print(f'{k} = {v}')
    else:
        print(f'{k} = {v} anos.')