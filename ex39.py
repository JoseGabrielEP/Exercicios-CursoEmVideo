#Faça um programa que leia o ano de nascimento de um jovem e informe,
#de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
#se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

nascimento = int(input('Insira o seu ano de nascimento: '))
idade = 2024 - nascimento
futuro_alistamento = 18 - idade
alistamento_passado = (idade - 18) 
if nascimento == 2006:
    print('Você tem ou fará 18 anos este ano, é seu ano de alistamento.')
elif nascimento < 2006:
    print(f'Você tem ou fará {idade} anos em 2024, sua fase de alistamento já passou à {alistamento_passado} ano(s).')
elif nascimento > 2024:
    print('ANO INVÁLIDO, REINICIE O PROCESSO!!!!')
else:
    print(f'Você tem ou fará {idade} anos em 2024, seu alistamento será daqui a {futuro_alistamento} ano(s).')