#Crie um programa que leia o ano de nascimento de sete pessoas. 
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
mais18 = []
menos18 = []
for x in range(0,7):
    ano = int(input('Insira o ano de nascimento: '))
    if ano <= 2006:
        mais18.append(ano)
    else:
        menos18.append(ano)
print('-' * 30)
print(f'No total tem-se {len(mais18)} maiores de idade, sendo seus anos de nascimento {mais18}.')
print('-' * 30)
print(f'E no total tem-se {len(menos18)} manores de idade, sendo seus anos de nascimento {menos18}.')
