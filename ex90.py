# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = dict()

aluno['Nome'] = input('Insira o nome do aluno: ').title().strip()
aluno['Média'] = float(input('Insira a média do aluno (0 a 10): '))
    
if aluno['Média'] >= 7.0:
    aluno['Situação'] = 'APROVADO(A)'
else:
    aluno['Situação'] = 'REPROVADO(A)'

for k,v in aluno.items():
    print(f'{k} é {v}!')