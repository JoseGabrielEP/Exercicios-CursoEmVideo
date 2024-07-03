#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

turma = list()
aluno_nota = list()
resposta = input('Começar cadastramento? [S/N]: ').strip().title()[0]
#CADASTRAMENTO
while True:
    if resposta in 'S':
        aluno = input('Insira o nome do aluno sendo avaliado: ').strip().title()
        nota1 = float(input('Insira a nota 1 do aluno: '))
        nota2 = float(input('Insira a nota 2 do aluno: '))
        if nota1 and nota2 <= 10 :
            aluno_nota.append(aluno)
            aluno_nota.append(nota1)
            aluno_nota.append(nota2)
            turma.append(aluno_nota[:])
            aluno_nota.clear()
            resposta = input('Quer continuar? [S/N]: ').strip().title()[0]
        else:
            print('Notas inseridas inválidas.')
            resposta = input('=-=-=-=-TENTE NOVAMENTE=-=-=-=-\n[S/N]: ').strip().title()[0]
    elif resposta in 'N':
        break
    else:
        resposta = input('Desculpa, não entendi. Quer continuar? [S/N]: ').strip().title()[0]

#EXIBIÇÃO
pergunta = int(input('Quer ver as notas individuais ou de todos alunos?\n[Individuais - 1 / Todos Alunos - 2 / encerrar - 3]: '))
opcao = 'S'
soma = list()
while True:
    if pergunta == 1:
        while True:
            if opcao in 'S':
                print('De quem deseja ver a média? ')
                for p in range(0, len(turma)):
                    print(f'{p + 1}- {turma[p][0]}')
                n_cadastro = (int(input('Insira o Número do aluno que deseja ver a média: ')) - 1)
                soma.append(turma[n_cadastro][1])
                soma.append(turma[n_cadastro][2])
                soma2 = sum(soma)
                print(f'''O aluno selecionado é {turma[n_cadastro][0]}.
    Suas notas foram:
    Nota 1 = {turma[n_cadastro][1]}
    Nota 2 = {turma [n_cadastro][2]}
    Média = {soma2/2}''')
                soma.clear()
                opcao = input('Quer ver mais alguma nota? [S/N]: ').upper().strip()[0]
            elif opcao in 'N':
                break
            else:
                opcao = input('Não entendi. Quer ver mais alguma nota? [S/N]: ').upper().strip()[0]
    elif pergunta == 2:
        for a in range(0, len(turma)):
            media = (turma[a][1] + turma[a][2]) / 2
            print(f'{turma[a][0]}- N1({turma[a][1]}), N2({turma[a][2]}), Média = {media}')
        print('=-'*15)
        pergunta = int(input('[Individuais - 1 / Todos Alunos - 2 / encerrar - 3]: '))
    elif pergunta == 3:
        break
    else:
        pergunta = int(input('Desculpa, não entendi. [Individuais - 1 / Todos Alunos - 2 / encerrar - 3]: '))

print('=-'*15)
print('PROCESSO ENCERRADO')