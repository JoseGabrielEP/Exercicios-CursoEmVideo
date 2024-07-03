#Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
#  No final, mostre a matriz na tela, com a formatação correta.

linha0 = [[], [], []]
linha1 = [[], [], []]
linha2 = [[], [], []]

for x in range(0,3):
    coluna = int(input(f'Insira um número para [0,{x}]: '))
    linha0[x].append(coluna)
for y in range(0,3):
    coluna = int(input(f'Insira um número para [1,{y}]: '))
    linha1[y].append(coluna)
for z in range(0,3):
    coluna = int(input(f'Insira um número para [2,{z}]: '))
    linha2[z].append(coluna)

print('=-'*30)

print(linha0)
print(linha1)
print(linha2)