#Crie um programa que leia vários números inteiros pelo teclado. 
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final,
# mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = int(input('Insira um número [999 para parar]: '))
if n != 999:
    lista_n = []
    lista_n.append(n)

    while n != 999:
        n = int(input('Insira outro número número [999 para parar]: '))
        if n != 999:
            lista_n.append(n)
    print('-' * 30)
    print(f'O a soma dos {len(lista_n)} números é de {sum(lista_n)}!!!!')
print('---PROCESSO ENCERRADO---')
