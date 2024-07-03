#Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
#  No final, mostre:
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média

Tpessoas = list()
pessoa = dict()
tMulheres = list()
idadeM = 0
opcao = input('Quer começar o cadastro? [S/N]: ').strip().title()[0]
#CADASTRAMENTO
while True:
    if opcao in 'S':
        print('=-'*15)
        pessoa['Nome'] = input('Insira o Nome da pessoa sendo cadastrada: ')
        pessoa['Idade'] = int(input('Insira a idade da pessoa sendo cadastrada: '))
        pessoa['Sexo'] = input('Insira o sexo da pessoa sendo cadastrada [F/M]: ').upper().strip()[0]
        idade = pessoa['Idade']
        idadeM += idade
        Tpessoas.append(pessoa.copy())
        while True:
            if pessoa['Sexo'] in 'F':
                tMulheres.append(pessoa['Nome'])
                break
            elif pessoa['Sexo'] not in 'MF':
                pessoa['Sexo'] = input('Insira uma opção válida [F/M]: ').upper().strip()[0]
            elif pessoa['Sexo'] in 'M':
                break
        opcao = input('Quer continuar o cadastro? [S/N]: ').strip().title()[0]
    elif opcao in 'N': 
        break
    else:
        opcao = input('Não entendi. Quer continuar o cadastro? [S/N]: ').strip().title()[0]
    
idadeM = idadeM / len(Tpessoas)

#Exibição
exibicao = int(input('[1-Pessoas Cadastradas/2-Lista das Mulheres/3-Pessoas com idade acima da média/4-Encerrar]: '))
while True: 
    if exibicao == 1:
        for x in range(0, len(Tpessoas)):
            print(Tpessoas[x])
        exibicao = int(input('O que quer ver agora?\n[1-Pessoas Cadastradas/2-Lista das Mulheres/3-Pessoas com idade acima da média/4-Encerrar]: '))
    elif exibicao == 2:
        if len(tMulheres) != 0:
            for y in range(0, len(tMulheres)):
                print(tMulheres[y])
            exibicao = int(input('O que quer ver agora?\n[1-Pessoas Cadastradas/2-Lista das Mulheres/3-Pessoas com idade acima da média/4-Encerrar]: '))
        else:
            print('Não há mulheres cadastradas.')
            exibicao = int(input('O que quer ver agora?\n[1-Pessoas Cadastradas/2-Lista das Mulheres/3-Pessoas com idade acima da média/4-Encerrar]: '))
    elif exibicao == 3:
        print(f'A média de idade é {idadeM:.2f}.')
        for z in range(0, len(Tpessoas)):
            if Tpessoas[z]['Idade'] >= idadeM:
                print(Tpessoas[z])
        exibicao = int(input('O que quer ver agora?\n[1-Pessoas Cadastradas/2-Lista das Mulheres/3-Pessoas com idade acima da média/4-Encerrar]: '))
    elif exibicao == 4:
        break
    else:
        print('=-'*15)
        exibicao = int(input('Não Entendi. O que quer ver agora?\n[1-Pessoas Cadastradas/2-Lista das Mulheres/3-Pessoas com idade acima da média/4-Encerrar]: '))

print('=-'*15)
print('PROGRAMA ENCERRADO')
print('=-'*15)