#Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
#  No final, mostre a matriz na tela, com a formatação correta.
#Aprimore o desafio anterior, mostrando no final:                                                   
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna
#C) O maior valor da segunda linha.

linha0 = [[], [], []]
linha1 = [[], [], []]
linha2 = [[], [], []]
lista_pares = [0]

for x in range(0,3):
    coluna = int(input(f'Insira um número para [0,{x}]: '))
    linha0[x].append(coluna)
    if coluna % 2 == 0:
        lista_pares.append(coluna)
for y in range(0,3):
    coluna = int(input(f'Insira um número para [1,{y}]: '))
    linha1[y].append(coluna)
    if coluna % 2 == 0:
        lista_pares.append(coluna)
for z in range(0,3):
    coluna = int(input(f'Insira um número para [2,{z}]: '))
    linha2[z].append(coluna)
    if coluna % 2 == 0:
        lista_pares.append(coluna)

print('=-'*30)

print(linha0)
print(linha1)
print(linha2)

print('=-'*30)
print(f'A soma dos valores pares digitados é {sum(lista_pares)}.')
print(f'A soma dos valores da terceira coluna é {sum(linha0[2] + linha1[2] + linha2[2])}')
linha1.sort()
print(f'O maior valor da segunda linha é {linha1[2][0]}')

