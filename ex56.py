#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre:
#a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.


#listas

mulheres_20 = []
idades = [] 
homem_velho = 0
nomemaisvelho = ''

#loop informações
for pessoas in range(0,4):
    print('-' * 30)
    nome = input(f'Insira o nome da {pessoas + 1}ª pessoa: ').capitalize()
    idade = int(input('Insira a idade da pessoa: '))
    sexo = int(input('''Insira o sexo da pessoa:
[M(1) ou F(2)]: ''' ))
    idades.append(idade)

    #condicionais internas do loop

    if (sexo == 2) and (idade < 20):            #caso mulher menor de 20 anos
        mulheres_20.append(nome)
    elif sexo == 1:                    #caso homem.
        if idade > homem_velho:        #mais velho
            homem_velho = idade
            nomemaisvelho = nome

        


    
#media de idades
media_idade = (idades[0] + idades[1] + idades[2] + idades[3]) // 4

#exibição resultado
print('-' * 30)
print(f'A média de idades é {media_idade} anos.')
print('-' * 30)
print(f'Há {len(mulheres_20)} mulheres menores de 20 anos.')
print('-' * 30)
print(f'O homem mais velho é {nomemaisvelho} e sua idade é {homem_velho} anos.')

