#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
#o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

p18 = 0
homem = 0
m20 = 0
opcao = ''
while True:
    if opcao in 'S':
        sexo = int(input('Insira o sexo da pessoa sendo cadastrada [1-F/2-M]: '))
        idade = int(input('Insira a idade da pessoa cadastrada: '))
        print('=-'*15)
        opcao = input('Quer continuar? [SIM/NÃO]: ').upper().strip()[0]
        if sexo == 2: #HOMEM
            homem += 1
            if idade >= 18:#Homem maior de 18
                p18 += 1
        elif sexo == 1:#mulher
            if idade == 18 or idade == 19: #menor de 20, porém maior de 18
                p18 += 1
            elif idade >= 20: #maior de 20
                p18 += 1
                m20 += 1
    elif opcao not in 'SN':
        opcao = input('Houve um erro de digitação, deseja continuar com o programa? [SIM/NÃO]: ').upper().strip()[0]
    elif opcao in 'N':
        break
    
print('=-' * 15)
print('Fim de processo')
print(F'''Estatistícas:
Pessoas com mais de 18 anos: {p18}
Homens: {homem}
Mulheras com mais de 20 anos: {m20}
---ENCERRADO---''')