# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada


def contagem(i,f,r):
    print('=-'*25)
    for x in range(i,f,r):
        print(f'--> {x}', end='')
    print('--> FIM!')
    print('=-'*25)


contagem(1,11,1)
contagem(10, -2, -2)

print('Agora é a sua vez!')
opcao = int(input('[CONTAGEM NORMAL - 1/ INVERSA -2 / ENCERRAR O PROGRAMA - 3]: '))
while True:
    if opcao == 1:
        comeco = int(input('Insira o número que iniciará a contagem: '))
        fim = int(input('Insira o número que finalizará a contagem: '))
        ritmo = int(input('Insira o número que definirá o ritmo de contagem: '))
        while True:
            if ritmo > 0:
                contagem(comeco, fim, ritmo)
                opcao = int(input('[CONTAGEM NORMAL - 1/ INVERSA -2 / ENCERRAR O PROGRAMA - 3]: '))
                break
            elif ritmo < 0:
                ritmo = int(input('Insira o número que definirá o ritmo de contagem: '))
    elif opcao == 2:
        comeco = int(input('Insira o número que iniciará a contagem: '))
        fim = int(input('Insira o número que finalizará a contagem: '))
        while True:
            if comeco < fim:
                comeco = int(input('Insira o número que iniciará a contagem(DEVE SER MAIOR QUE O FIM): '))
                fim = int(input('Insira o número que finalizará a contagem(DEVE SER MENOR QUE O COMEÇO): '))
            elif comeco > fim: 
                ritmo = int(input('Insira o número que definirá o ritmo de contagem: '))
                break
        if ritmo < 0:
            contagem(comeco, fim, ritmo)
            opcao = int(input('[CONTAGEM NORMAL - 1/ INVERSA -2 / ENCERRAR O PROGRAMA - 3]: '))
        elif ritmo > 0:
            contagem(comeco, fim, -ritmo)
            opcao = int(input('[CONTAGEM NORMAL - 1/ INVERSA -2 / ENCERRAR O PROGRAMA - 3]: '))
    elif opcao == 3:
        break

print('=-'*25)
print('PROGRAMA ENCERRADO')