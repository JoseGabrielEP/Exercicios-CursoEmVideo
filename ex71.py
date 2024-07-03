#Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.


saque = int(input('Insira o valor que deseja sacar: R$'))
total = saque
ced50 = 50
totced50 = 0
ced20 = 20
totced20 = 0
ced10 = 10
totced10 = 0
ced1 = 1
totced1 = 0

if (total >= 50):
    while True:
        total -= ced50
        totced50 += 1
        if total < 50:
            break

if (total >= 20):
    while True:
        total -= ced20
        totced20 += 1
        if total < 20:
            break

if (total >= 10):
    while True:
        total -= ced10
        totced10 += 1
        if total < 10:
            break

if (total >= 1):
    while True:
        total -= ced1
        totced1 += 1
        if total < 1:
            break

print('=-'*15)
print(f'''Estatísticas:
{totced50} cédulas de 50.
{totced20} cédulas de 20.
{totced10} cédulas de 10.
{totced1} cédulas de 1.''')