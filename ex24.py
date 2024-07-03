# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
nome_cidade = input('Insira o nome de uma cidade: \n')
lista_partes_nome = nome_cidade.split()
minusculo = lista_partes_nome[0].lower()
if  minusculo != "santo":
    print('O nome desta cidade não começa com a palavra "Santo"')
else:
    print('O nome desta cidade começa com a palavra "Santo"')