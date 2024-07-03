#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(i):
    idade = 2024 - i
    if idade > 17:
        return 'OBRIGATÓRIO'
    elif idade < 16:
        return 'NEGADO'
    else:
        return 'OPCIONAL'
    

ano = int(input('Insira o ano em que nasceu: '))
print(f'Você nasceu em {ano}, a sua situação eleitoral é {voto(ano)}')