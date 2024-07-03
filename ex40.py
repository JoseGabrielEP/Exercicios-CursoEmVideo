#Crie um programa que leia duas notas de um aluno e calcule sua média,
#mostrando uma mensagem no final, de acordo com a média atingida:

#– Média abaixo de 5.0: REPROVADO

#– Média entre 5.0 e 6.9: RECUPERAÇÃO

#– Média 7.0 ou superior: APROVADO

n1 = float(input('Insira a nota de sua Avaliação 1: \n'))
n2 = float(input('Insira a nota de sua Avaliação 2: \n'))

if ((n1 or n2) < 10.1) and ((n1 or n2) > -0.1):
    média = (n1 + n2) / 2
    if média < 5.0:
        print(f'Sua média foi {média}, você foi REPROVADO!')
    elif (média < 7.0) and (média > 4.9):
        print(f'Sua média foi {média}, você foi para a RECUPERAÇÃO!')
    else:
        print(f'Sua média foi {média}, você foi APROVADO!')
        print('-----PARABÉNS-----')
else:
    print('INSIRA VALORES VÁLIDOS!')
    print('VALORES DE 0 A 10 APENAS.')