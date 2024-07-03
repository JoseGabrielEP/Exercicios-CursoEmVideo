#Faça um programa que leia nome e peso de várias pessoas,                   
# guardando tudo em uma lista. No final, mostre:                
# A) Quantas pessoas foram cadastradas.    
# B) Uma listagem com as pessoas mais pesadas.                                                                  
# C) Uma listagem com as pessoas mais leves

pessoas = list()
info = list()
pergunta = input('Quer começar o cadastro? [S/N]: ').strip().title()[0]

while pergunta not in 'N':
    print('=-'*15)
    info.append(input('Insira o Nome: '))
    info.append(float(input('Insira o peso: ')))[0:4]
    pessoas.append(info[:])
    info.clear()
    pergunta = input('Quer continuar o cadastro? [S/N]: ').strip().title()[0]

print('=-'*15)

print(f'Existem {len(pessoas)} pessoas na lista.')
print('')

mais_pesado = [['!!!!!!', -9999999999999999999999999999999999999]]

for item in pessoas:
    if item[1] > mais_pesado[0][1]:
        mais_pesado.clear()
        mais_pesado.append(item)
        
    elif item[1]== mais_pesado[0][1]:
        mais_pesado.insert(1, item[0])
        mais_pesado.pop()
        
print(f'O maior peso é de {item[1]}, e é de {mais_pesado}.')
mais_leve = [['----', 99999999999999999999999999999999999999999]] 

for item2 in pessoas:
    if item2[1] < mais_leve[0][1]:
        mais_leve.clear()
        mais_leve.append(item)
    
        
    elif item2[1] == mais_leve[0][1]:
        mais_leve.insert(1, item2[0])
        mais_leve.pop()

print(f'O menor peso é de {item2[1]}, e é de {mais_leve}.')


#corrigir corrigir corrigir